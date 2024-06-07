from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        if not file:
            return "No file uploaded", 400

        # Đọc dữ liệu từ file CSV
        data = pd.read_csv(file)

        # Chuyển đổi dữ liệu ban đầu thành JSON để hiển thị trên trang web
        raw_data = data.head(20).to_dict(orient='records')  # Hiển thị 20 dòng đầu tiên để tránh quá tải trang

        # Kiểm tra các cột bắt buộc
        required_columns = ['Product Category', 'Product Name', 'Region', 'Payment Method', 'Date', 'Units Sold', 'Unit Price', 'Total Revenue']
        if not all(column in data.columns for column in required_columns):
            return f"Missing columns in CSV. Required columns: {required_columns}", 400

        data.dropna(inplace=True)

        # Mã hóa các biến phân loại
        label_encoders = {}
        categorical_features = ['Product Category', 'Product Name', 'Region', 'Payment Method']
        for feature in categorical_features:
            le = LabelEncoder()
            data[feature] = le.fit_transform(data[feature])
            label_encoders[feature] = le

        # Tạo thêm các biến mới từ cột 'Date'
        data['Date'] = pd.to_datetime(data['Date'])
        data['Year'] = data['Date'].dt.year
        data['Month'] = data['Date'].dt.month
        data['Day'] = data['Date'].dt.day

        # Chọn các features và label
        features = ['Product Category', 'Product Name', 'Units Sold', 'Unit Price', 'Region', 'Payment Method', 'Year', 'Month', 'Day']
        label = 'Total Revenue'
        X = data[features]
        y = data[label]

        # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Xây dựng và huấn luyện mô hình
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Dự đoán trên tập kiểm tra
        y_pred = model.predict(X_test)
        
        # Đánh giá mô hình
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Tính toán các giá trị tổng doanh thu
        total_actual_revenue = y_test.sum()
        total_predicted_revenue = y_pred.sum()
        revenue_change = total_predicted_revenue - total_actual_revenue
        change_percentage = (revenue_change / total_actual_revenue) * 100

        # Kết hợp dự đoán và giá trị thực tế với ngày tương ứng
        X_test['Actual Revenue'] = y_test
        X_test['Predicted Revenue'] = y_pred
        X_test['Date'] = pd.to_datetime(X_test[['Year', 'Month', 'Day']])

        # Tính tổng doanh thu thực tế và dự đoán theo ngày
        daily_revenue = X_test.groupby('Date').agg({'Actual Revenue': 'sum', 'Predicted Revenue': 'sum'}).reset_index()

        # Tính tổng doanh thu thực tế và dự đoán theo khu vực
        region_revenue = X_test.groupby('Region').agg({'Actual Revenue': 'sum', 'Predicted Revenue': 'sum'}).reset_index()
        region_revenue['Region Name'] = region_revenue['Region'].map(lambda x: label_encoders['Region'].inverse_transform([x])[0])

        # Tính tổng doanh thu thực tế và dự đoán theo danh mục sản phẩm
        category_revenue = X_test.groupby('Product Category').agg({'Actual Revenue': 'sum', 'Predicted Revenue': 'sum'}).reset_index()
        category_revenue['Category Name'] = category_revenue['Product Category'].map(lambda x: label_encoders['Product Category'].inverse_transform([x])[0])

        # Vẽ đồ thị so sánh doanh thu thực tế và dự đoán theo ngày
        plt.figure(figsize=(14, 8))
        plt.plot(daily_revenue['Date'], daily_revenue['Actual Revenue'], label='Actual Revenue')
        plt.plot(daily_revenue['Date'], daily_revenue['Predicted Revenue'], label='Predicted Revenue')
        plt.xlabel('Date')
        plt.ylabel('Revenue')
        plt.title('Actual vs Predicted Revenue by Date')
        plt.legend()
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        # Vẽ đồ thị so sánh doanh thu thực tế và dự đoán theo khu vực
        plt.figure(figsize=(14, 8))
        plt.bar(region_revenue['Region Name'], region_revenue['Actual Revenue'], width=0.4, label='Actual Revenue', align='center')
        plt.bar(region_revenue['Region Name'], region_revenue['Predicted Revenue'], width=0.4, label='Predicted Revenue', align='edge')
        plt.xlabel('Region')
        plt.ylabel('Revenue')
        plt.title('Actual vs Predicted Revenue by Region')
        plt.legend()
        plt.xticks(rotation=45)
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        region_plot_url = base64.b64encode(img.getvalue()).decode()

        # Vẽ đồ thị so sánh doanh thu thực tế và dự đoán theo danh mục sản phẩm
        plt.figure(figsize=(14, 8))
        plt.bar(category_revenue['Category Name'], category_revenue['Actual Revenue'], width=0.4, label='Actual Revenue', align='center')
        plt.bar(category_revenue['Category Name'], category_revenue['Predicted Revenue'], width
=0.4, label='Predicted Revenue', align='edge')
        plt.xlabel('Product Category')
        plt.ylabel('Revenue')
        plt.title('Actual vs Predicted Revenue by Product Category')
        plt.legend()
        plt.xticks(rotation=45)
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        category_plot_url = base64.b64encode(img.getvalue()).decode()


        # Tạo DataFrame chứa dữ liệu dự đoán
        predicted_data = X_test.copy()
        predicted_data['Actual Revenue'] = y_test
        predicted_data['Predicted Revenue'] = y_pred

        # Xuất ra tệp CSV
        predicted_data.to_csv('predicted_data.csv', index=False)

        # Trả về tệp CSV đã tạo cho người dùng để tải xuống
        predicted_data_link = '/export_predictions'

        return render_template('index.html', 
                               mae=mae, mse=mse, r2=r2, plot_url=plot_url, 
                               region_plot_url=region_plot_url, 
                               category_plot_url=category_plot_url, 
                               region_revenue=region_revenue.to_dict(orient='records'), 
                               category_revenue=category_revenue.to_dict(orient='records'), 
                               raw_data=raw_data, 
                               total_actual_revenue=total_actual_revenue,
                               total_predicted_revenue=total_predicted_revenue,
                               revenue_change=revenue_change,
                               change_percentage=change_percentage,
                               predicted_data_link=predicted_data_link)
    except Exception as e:
        return str(e), 500

@app.route('/export_predictions', methods=['GET'])
def export_predictions():
    try:
        # Trả về tệp CSV đã tạo cho người dùng để tải xuống
        return send_file('predicted_data.csv', as_attachment=True, download_name='predicted_data.csv')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
