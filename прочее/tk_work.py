from tkinter import *
from tkinter import ttk
from PIL import Image
from ascii_functions import *

new_width=50

path = 'mun.jpg' #input("Enter avalid pathname to an image: \n")
try:
    image = Image.open(path)
except:
    print(path, "is not a valid pathname to an image.")


coeff = 1.5 #int(float(input('Введите коэффициент контрастности: \n')))
resized_image = resize_image_user_tools(contrast(image, coeff), new_width, new_width-10)
resized_image_size_x, resized_image_size_y = resized_image.size
new_image_data = pixels_to_ascii(grayify(resized_image))

pixel_count = len(new_image_data)
ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

root = Tk()

size_canvas_x = 1500
size_canvas_y = 1000

root.title("ASCII Art")
#root.resizable(0, 0) # размеры менять нельзя

canvas = Canvas(root, width=size_canvas_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()

style = ttk.Style()
style.configure('Style.TButton', font='TkFixedFont')

label = ttk.Label(text=ascii_image, style='Style.TButton')
label.place(x = 0, y = 0)
print(size_canvas_x)
print(resized_image_size_x)
print(size_canvas_y)
print(resized_image_size_y)
print((size_canvas_y - resized_image_size_y)/2)

root.mainloop()