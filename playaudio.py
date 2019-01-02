from tkinter import*
from tkinter import filedialog
import winsound

root = Tk()
def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    global data
    data= (filename)

def playAudio(data):
    winsound.PlaySound(data, winsound.SND_FILENAME)

browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

playbutton= Button(root, text= "Play", command=lambda: playAudio(data))
playbutton.pack()

pathlabel = Label(root)
pathlabel.pack()
root.mainloop()