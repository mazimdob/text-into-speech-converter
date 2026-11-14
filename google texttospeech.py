from tkinter import *
import gtts
from tkinter import messagebox
root=Tk()
root.title("google text to speech")
root.geometry("600x400")
root.configure(bg="light green")

def convert_text_to_speech():
        text1=E1.get()
        audiofile=gtts.gTTS(text=text1,lang="en",slow=False)
        audiofile.save("output.mp3")
        messagebox.showinfo("succes","mp3 file is saved")




l1 = Label(root, text="Text to speech",width=20, height=3,font=("Airal",30))
l1.place(x=150, y=30)

E1 = Entry(root, width=40, font=("Arial", 14))
E1.place(x=170, y=200)
b1 = Button(root, text="Submit",width=15, height=1,font=("Arial", 14),command=convert_text_to_speech)
b1.place(x=250, y=300)





root.mainloop()
