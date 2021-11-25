from os import path
from PIL import ImageEnhance

#ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

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

def pixels_to_ascii(image, ASCII_chars): # new
    pixels = image.getdata()
    characters = ''.join(ASCII_chars[pixel // (255 // len(ASCII_chars) + 1)] for pixel in pixels)
    return characters

def do_ascii_art(image, coeff, ASCII_chars, width, height): # new
    ASCII_img_in_arr =  pixels_to_ascii(grayify(resize_image_user_tools(contrast(image, coeff), width, height)), ASCII_chars)
    pixel_count = len(ASCII_img_in_arr)
    ascii_image = '\n'.join(ASCII_img_in_arr[i:(i + width)] for i in range(0, pixel_count, width))
    return ascii_image

def modify_image_to_P_mode(image):
    P_image = image.convert("P")
    return P_image

def contrast(image, coeff):
    return ImageEnhance.Contrast(image).enhance(coeff)