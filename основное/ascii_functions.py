from os import path
from PIL import ImageEnhance

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image_accurate(image, new_width): # аккуратное изменение размеров
    width, height = image.size # size - кортеж из двух элементов, содержащий ширину и высоту в пикселях.
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    # Image.resize(size, resample=None, box=None, reducing_gap=None)
    # Returns a resized copy of this image.
    return(resized_image)

def resize_image_user_tools(image, width, height): # ресайзит по желанию пользователя
    resized_image = image.resize((width, height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    # image.getdata(band=None)
    # getdata() возвращает содержимое этого изображения как объект последовательности, содержащий значения пикселей.
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return(characters)

def contrast(image, coeff):
    return ImageEnhance.Contrast(image).enhance(coeff)

def do_ascii_art(image, coeff, width, height):
    new_image_data =  pixels_to_ascii(grayify(resize_image_user_tools(contrast(image, coeff), width, height)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+width)] for i in range(0, pixel_count, width))
    return ascii_image