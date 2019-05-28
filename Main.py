import tkinter
from direct import getSonglist
from edgarbpm import getBPM
from tkinter import Label
from tkinter import Listbox
from tkinter import Button
from tkinter import messagebox

filename = ''
tempo = 0
tempoMarking = ''

def CurSelet(event):
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    global filename 
    filename = "./songs/"
    filename = filename + picked

def getSongBPM():
    global filename
    global tempo, tempoMarking
    tempo, tempoMarking, terms = getBPM(filename)
    message = "The song tempo is:\t" 
    message = message + str(tempo)
    message = message +  "\nThe tempo marking is:\t"
    message = message  + str(tempoMarking)
    message = message + "\nThis means "
    message = message + str(terms)
    message = message + " in English"
    messagebox.showinfo("Song Tempo", message)

def main():
    window = tkinter.Tk()
    window.title("BEE PEE EEM")
    Label(window, text='BPM & tempo marking Identifier', bg='red').pack(fill=tkinter.X)
    Label(window, text='Song Bank', bg='yellow').pack(fill=tkinter.X)
    lbox1 = Listbox(window, selectmode='SINGLE')
    lbox1.bind('<<ListboxSelect>>',CurSelet)
    songList = getSonglist()
    count = 1
    for song in songList:
        lbox1.insert(count, song)
        count = count + 1
    lbox1.pack()
    Button(window, text='Determine BPM', bg='pink', command=getSongBPM).pack(fill=tkinter.X)
    Label(window, text='Paolo ni Edgar 553').pack(fill=tkinter.X)
    window.mainloop()

if __name__ == '__main__':
    main()