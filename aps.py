


import random


'''
Calcula o totiente do numero primo
'''
def totient(number): 
    if(prime(number)):
        return number-1
    else:
        return False

    
'''
Verifica se um numero gerado é primo
'''

def prime(n): 
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True



'''
Gera um numero aleatório E, sasfazendo as condições
'''
def generate_E(num): 
    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e

        
'''
Gera um numero primo aleatório
'''
def generate_prime(): 
    while True: 
        x=random.randrange(1,100) 
        if(prime(x)==True):
            return x
'''
Função modular entre dois números
'''
def mod(a,b): 
    if(a<b):
        return a
    else:
        c=a%b
        return c

    
    
'''
Cifra um texto
'''
def cipher(words,e,n): 
    tam = len(words)
    i = 0
    lista = []
    while(i < tam):
        letter = words[i]
        k = ord(letter)
        k = k**e
        d = mod(k,n)
        lista.append(d)
        i += 1
    return lista

'''
Descriptografa um texto criptografado
'''
def descifra(cifra,n,d):
    lista = []
    i = 0
    tamanho = len(cifra)
    
    while i < tamanho:
        result = cifra[i]**d
        texto = mod(result,n)
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return lista


'''
Calcula a chave privada
'''
def calculate_private_key(toti,e):
    d = 0
    while(mod(d*e,toti)!=1):
        d += 1
    return d




## MAIN
if __name__=='__main__':
    text = input("Insert message: ")
    p = generate_prime() 
    q = generate_prime() 
    n = p*q 
    y = totient(p) 
    x = totient(q) 
    totient_de_N = x*y 
    e = generate_E(totient_de_N) 
    public_key = (n, e)

    print('Your public key:', public_key)
    text_cipher = cipher(text,e,n)
    print('Your encrypted message:', text_cipher)
    d = calculate_private_key(totient_de_N,e)
    print('Your private key is:', d)
    original_text = descifra(text_cipher,n,d)
    print('your original message:', original_text)