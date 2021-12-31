from PIL import Image, ImageDraw


def load_image(filename):
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)  # кисть для рисования; не нужна если использовать putpixel
    pixels = image.load()  # загрузка пикселей; <class 'PixelAccess'>
    return image, draw, pixels


# оттенки серого
def grayscale_pure(filename):
    image, draw, pixels = load_image(filename)
    width = image.size[0]  # ширина
    height = image.size[1]  # высота

    for i in range(width):
        for j in range(height):
            R, G, B = pixels[i, j]  # R,G,B = image.getpixel((i, j)) # через getpixel почему-то медленнее
            # S = (R + G + B) // 3 # другая (более грубая) формула  grayscale
            S = round(0.2989 * R + 0.587 * G + 0.114 * B)
            # draw.point((i, j), (S, S, S))
            image.putpixel((i, j), (S, S, S))  # так быстрее чем через draw

    del draw
    return image
