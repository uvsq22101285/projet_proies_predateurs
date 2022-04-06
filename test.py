'''TEST IMAGE'''
from tkinter import *  
from PIL import ImageTk,Image  

root = Tk()  
root.title('PythonGuides')
root.geometry('500x500')

canvas = Canvas(root, width = 500, height = 500)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open('terrain.png'))  
canvas.create_image(10,10,anchor=NW, image=img) 
root.mainloop() 