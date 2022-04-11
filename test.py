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

canvas = Canvas(root, width = 640, height = 640,bg='black')
img = PhotoImage(file ="carré_sol.png")
img2 = PhotoImage(file ="rabbit.png")
img3 = PhotoImage(file ="fox.png")
img4 = PhotoImage(file="tomato.png")
img5 = PhotoImage(file="migrant.png")
img6 = PhotoImage(file="police-officer-head.png")
img7 = PhotoImage(file="water-flask.png")
img8 = PhotoImage(file="rolling-bomb.png")

for x in range(20):
    for y in range(20):
        canvas.create_image(x*64,y*64,image=img,anchor=NW)

canvas.create_image(64,0, image=img3, anchor=NW)
canvas.create_image(0,0,image=img2, anchor=NW)
canvas.create_image(0,64,image=img4, anchor=NW)
canvas.create_image(64,64,image=img5, anchor=NW)
canvas.create_image(64,128,image=img6, anchor=NW)
canvas.create_image(128,128,image=img7, anchor=NW)
canvas.create_image(128,64,image=img8, anchor=NW)


canvas.grid()

root.mainloop()
