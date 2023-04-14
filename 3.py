from tkinter import *
import pygame
import os

root = Tk()
root.title('MUsic Player')
root.geometry("500x300")

pygame.mixer.init()

songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next.png')
rewind_btn_image = PhotoImage(file='rewind.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0)
rewind_btn = Button(control_frame, image=rewind_btn_image, borderwidth=0)

play_btn.grid(row = 0, column = 0, padx = 2, pady = 3)
pause_btn.grid(row = 0, column = 1, padx = 7, pady = 10)
next_btn.grid(row = 0, column = 2, padx = 7, pady = 10)
rewind_btn.grid(row = 0, column = 3, padx = 7, pady = 10)



root.mainloop()
