import tkinter as tk
import random

# Genera Password (escludere i simboli non ammessi)
def genera_password():
    minuscole = "abcdefghilmnopqrstuvzwyjkx"
    maiuscole = "ABCDEFGHILMNOPQRSTUVZWYJKX"
    numeri = "0123456789"
    simboli = "[]{}()*.:,;-_/!$%&=?^"

    combinazione = maiuscole + minuscole + numeri + simboli
    lunghezza = 20

    password = "".join(random.sample(combinazione, lunghezza))
    
    # Password generata
    casella_password.delete(1.0, tk.END)
    casella_password.insert(tk.END, password)

# Finestra principale
finestra = tk.Tk()
finestra.title("Generatore di Password")

# Casella password
casella_password = tk.Text(finestra, height=1, width=30)
casella_password.pack(pady=10)

# Bottone
bottone_genera = tk.Button(finestra, text="Genera Password", command=genera_password)
bottone_genera.pack()

# Esecuzione della finestra
finestra.mainloop()
