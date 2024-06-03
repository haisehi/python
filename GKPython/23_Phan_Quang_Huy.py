from abc import ABC, abstractmethod

# Tạo một lớp trừu tượng (abstract) Sach
class Sach(ABC):
    def __init__(self, MaSach, TieuDe, TacGia, NamXuatBan):
        self.MaSach = MaSach
        self.TieuDe = TieuDe
        self.TacGia = TacGia
        self.NamXuatBan = NamXuatBan

    @abstractmethod
    def thanhTien(self):
        pass

    def __str__(self):
        return f"MaSach: {self.MaSach}, TieuDe: {self.TieuDe}, TacGia: {self.TacGia}, NamXuatBan: {self.NamXuatBan}"

# Tạo lớp SachGiaoKhoa kế thừa từ lớp Sach

class SachGiaoKhoa(Sach):
    def __init__(self, MaSach, TieuDe, TacGia, NamXuatBan, SoTrang, PhuThu):
        super().__init__(MaSach, TieuDe, TacGia, NamXuatBan)
        self.SoTrang = SoTrang
        self.PhuThu = PhuThu

    def thanhTien(self):
        gia_ban = (self.SoTrang * 200) + self.PhuThu
        return gia_ban

    def __str__(self):
        return super().__str__() + f", SoTrang: {self.SoTrang}, PhuThu: {self.PhuThu}"


# Tạo lớp SachTieuThuyet kể thưà từ lớp Sach
class SachTieuThuyet(Sach):
    def __init__(self, MaSach, TieuDe, TacGia, NamXuatBan, SoTrang, TheLoai, Rating):
        super().__init__(MaSach, TieuDe, TacGia, NamXuatBan)
        self.SoTrang = SoTrang
        self.TheLoai = TheLoai
        self.Rating = Rating

    def thanhTien(self):
        gia_ban = (self.SoTrang * 500) + (0.01 * self.Rating * (self.SoTrang * 500))
        return gia_ban

    def __str__(self):
        return super().__str__() + f", SoTrang: {self.SoTrang}, TheLoai: {self.TheLoai}, Rating: {self.Rating}"

# Tạo lớp Quan LyQuanSach để quản lý danh sách các sách
class QuanLyQuanSach:
    def __init__(self):
        self.danh_sach_sach = []

    def themSach(self, sach):
        self.danh_sach_sach.append(sach)

    def hienThiSach(self):
        for sach in self.danh_sach_sach:
            print(sach)

    def tongGiaSach(self):
        tong_gia = sum(sach.thanhTien() for sach in self.danh_sach_sach)
        return tong_gia


# tạo đối tượng quản lý sách
quan_ly_sach = QuanLyQuanSach()

sach_giao_khoa = SachGiaoKhoa("GK001", "Toan 10", "Nguyen Van A", 2022, 300, 10000)
sach_tieu_thuyet = SachTieuThuyet("TT001", "Harry Potter", "J.K. Rowling", 2005, 500, "Fantasy", 4)

quan_ly_sach.themSach(sach_giao_khoa)
quan_ly_sach.themSach(sach_tieu_thuyet)
quan_ly_sach.hienThiSach()
quan_ly_sach.tongGiaSach()



while True:
    print("\nMenu:")
    print("1. Thêm sách vào danh sách")
    print("2. Hiển thị thông tin của tất cả sách trong danh sách")
    print("3. Tổng giá của tất cả sách ")
    print("4. Thoát")

    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == "1":
        loai_sach = input("Chọn loại sách (GK: Giáo khoa, TT: Tiểu thuyết): ")
        if loai_sach.upper() == "GK":
            ma_sach = input("Nhập mã sách: ")
            tieu_de = input("Nhập tiêu đề sách: ")
            tac_gia = input("Nhập tác giả: ")
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            so_trang = int(input("Nhập số trang: "))
            phu_thu = int(input("Nhập phụ thu: "))
            sach = SachGiaoKhoa(ma_sach, tieu_de, tac_gia, nam_xuat_ban, so_trang, phu_thu)
        elif loai_sach.upper() == "TT":
            ma_sach = input("Nhập mã sách: ")
            tieu_de = input("Nhập tiêu đề sách: ")
            tac_gia = input("Nhập tác giả: ")
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            so_trang = int(input("Nhập số trang: "))
            the_loai = input("Nhập thể loại: ")
            rating = int(input("Nhập rating (từ 1 đến 5): "))
            sach = SachTieuThuyet(ma_sach, tieu_de, tac_gia, nam_xuat_ban, so_trang, the_loai, rating)
        else:
            print("Lựa chọn không hợp lệ!")
            continue
        quan_ly_sach.themSach(sach)
        print("Sách đã được thêm thành công!")
    elif lua_chon == "2":
        quan_ly_sach.hienThiSach()
    elif lua_chon == "3":
        print(f"Tổng giá của tất cả sách là: {quan_ly_sach.tongGiaSach()} VND")
    elif lua_chon == "4":
        break
    else:
        print("Lựa chọn không hợp lệ!")
