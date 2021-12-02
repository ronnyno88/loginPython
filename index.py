#importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk

#criar janela
window = Tk()
window.title("Ronny RN")
window.geometry("600x300")
window.configure(background="white")
window.resizable(width=False, height=False)


#logo
logo = PhotoImage(file="Icons/logo.png")

#widget
Leftframe = Frame(window, width=200, height=300, bg="gray", relief="raise")
Leftframe.pack(side=LEFT)

Rigthframe = Frame(window, width=398, height=300, bg="gray", relief="raise")
Rigthframe.pack(side=RIGHT)

#inserindo logo
logoLabel = Label(Leftframe, image=logo, bg="gray")
logoLabel.place(x=50, y=100)

#inserindo acesso
userLabel = Label(Rigthframe, text="Usuário", font=("Century Gothic", 20), bg="gray", fg="black")
userLabel.place(x=28, y=40)

userText = ttk.Entry(Rigthframe, width=30)
userText.place(x=130, y=50)

passLabel = Label(Rigthframe, text="Senha", font=("Century Gothic", 20), bg="gray", fg="black")
passLabel.place(x=28, y=87)

passText = ttk.Entry(Rigthframe, width=30)
passText.place(x=130, y=100)

#inserindo botões
loginButton = ttk.Button(text="LOGIN", width=30)
loginButton.place(x=330, y=150)

registerButton = ttk.Button(text="REGISTRAR", width=30)
registerButton.place(x=330, y=200)

window.mainloop()