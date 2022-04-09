'''TEST IMAGE'''
from tkinter import *  
from PIL import ImageTk,Image
''''''''''
im = Image.open("carré_sol.png")
print(im.size)
new_size = im.resize((32,32))
new_size.show()
'''''''''
root = Tk()
root.title('PythonGuides')
root.geometry('500x500')

canvas = Canvas(root, width = 640, height = 640,bg='green')
sol = PhotoImage(file ="carré_sol.png")
rabbit = PhotoImage(file ="rabbit.png")
fox = PhotoImage(file ="fox.png")
for x in range(20):
    for y in range(20):
        canvas.create_image(x*64,y*64,image=img,anchor=NW)

canvas.create_image(64,0, image=img3, anchor=NW)
canvas.create_image(0,0,image=img2, anchor=NW)

canvas.grid()

root.mainloop()
