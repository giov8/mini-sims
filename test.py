from tkinter import *
from tkinter import messagebox 

root = Tk() 
root.geometry("300x200") 

w = Label(root, text ='GeeksForGeeks', font = "50") 
w.pack() 

mensagem = "Este emprego está disponível. Deseja aceitar o emprego?"
resposta = messagebox.askquestion("Oferta de emprego", message=mensagem)

if resposta == "yes":
    messagebox.showinfo("Oferta de emprego", "Parabéns, você está empregado")

else:
    print("ESCOLHEU NÃO")
    messagebox.showerror("Oferta de emprego", "Não há mais empregos disponíveis")
root.mainloop()