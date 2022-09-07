from PIL import ImageEnhance


def resize_image_accurate(image, new_width):  # аккуратное изменение р-ров
    width, height = image.size  # size - ширина + высота (в пикселях)
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)


def resize_image_user_tools(image, width, height):  # resize пользователя
    resized_image = image.resize((width, height))
    return(resized_image)


def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)


def pixels_to_ascii(image, ASCII_chars):
    pixels = image.getdata()
    ascii_len = len(ASCII_chars)
    chars = ''.join(ASCII_chars[p // (255 // ascii_len + 1)] for p in pixels)
    return chars


def do_ascii_art(image, coeff, ASCII_chars, width, height):
    contrasted_im = contrast(image, coeff)
    resized_im = resize_image_user_tools(contrasted_im, width, height)
    ASCII_im = pixels_to_ascii(grayify(resized_im), ASCII_chars)
    pix_count = len(ASCII_im)
    w = width
    return '\n'.join(ASCII_im[i:(i + w)] for i in range(0, pix_count, w))


def modify_image_to_P_mode(image):
    P_image = image.convert("P")
    return P_image


def contrast(image, coeff):
    return ImageEnhance.Contrast(image).enhance(coeff)
