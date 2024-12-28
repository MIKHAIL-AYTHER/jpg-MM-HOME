from PIL import Image
from PIL import ImageFilter


with Image.open('img.png') as image_original:
    image_original.show()

    image_gray = image_original.convert("L")
    image_gray.save("img_anetoklaznyl.png")

    image_blure = image_original.filter(ImageFilter.BLURE)
    image_blure.save('img_blure.jpg')

    image_rotate = image_original.transpose(Image.ROTATE_180)
    image_rotate.save("img_rotate.jpg")
