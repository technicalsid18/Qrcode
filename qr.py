import qrcode
from tkinter import *

cp = Tk()
cp.title("SIDDHANT QR GENERATOR")
cp.geometry('500x500')
cp.config(bg='#d43334')

def generate():
    img = qrcode.make(msg.get())
    type(img)
    img.save(f'{save_name.get()}.png')
    Label(cp, text='File Saved!', bg='#d43334' , fg='black', font=('Arial', 8)).pack()

frame = Frame(cp, bg='#d43334')
frame.pack(expand=True)

# ENTER THE TEXT OR URL

Label(frame, text='Enter the Text or URL : ', font=('Arial Black', 16),
      bg='#d43334').grid(row=0, column=0, sticky='w')

msg = Entry(frame)
msg.grid(row=0, column=1)

#ENTER THE FILE NAME
Label(frame, text='File Name(Save As) : ', font=('Arial Black', 16),
      bg='#d43334').grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

# BUTTONS TO SAVE QRCODE

btn = Button(cp, text='Save QR code', command=generate, bd='5', width=15)
btn.pack()

cp.mainloop()