from tkinter import *
import random

root = Tk()
root.title("Palabras aleatorias")
root.geometry("400x400")

listword = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]

print(listword)

def random_code():
    random_code = random.randint(0,51)
    print(random_code)
    random_word = listword[random_code]
    
    print("Código Generado:  " + random_word)
        
btn1 = Button(root,text="Generar Código", command = random_code)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()