'''
name: josh tytler

date: 4/9/20
'''

#---Libraries----------- 
from tkinter import * 

#---Lists and Class---------------
class intro_greetingGUI:
    
    def __init__(self, parent):
        labell = Label(parent, text = "Plese enter name here:")
        labell.pack()
        e1 = Entry(parent)
        e1.pack(pady = 10)

        b1 = Button(parent, text = "Continue")
        b1.pack()
        root.geometry("200x200")

    def
#---main loop-----------
if __name__=="__main__":
    root = Tk()
    entry_ex = intro_greetingGUI(root)
    root.mainloop()
    


