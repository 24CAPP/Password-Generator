import random

minuscole = "abcdefghilmnopqrstuvzwyjkx"
maiuscole = "ABCDEFGHILMNOPQRSTUVZWYJKX"
numeri = "0123456789"
simboli = "[]{}()*.:,;-_/!$%&=?^" #ecludere quelli non accettati dal sistema

combinazione = maiuscole + minuscole + numeri + simboli 
lunghezza = 16

password = "".join(random.sample(combinazione,lunghezza))

print(password)