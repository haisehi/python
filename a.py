from PIL import Image
img = Image.open(r"D:\code\python\project_phan_loai_ban_tay\train1-dataset-image\2786.png")
angle = 328
rotate_img= img.rotate(angle, expand = True)
rotate_img.show()