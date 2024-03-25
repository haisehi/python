from PIL import Image
img = Image.open(r"C:\Users\Quang Huy\Downloads\ML\New folder\3040.png")
angle = 20
rotate_img= img.rotate(angle, expand = True)
rotate_img.show()