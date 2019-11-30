# Python3 code to find sequences of one upper 
# case letter followed by lower case letters

#import re 
import string
# Function to add more values for String
def fStringAdd (str, word):
    return str[:len(str)] + word + str[len(str):]
def fStringRead (str):
    return str[:len(str)]

# Function to catch the string and put on a array.
def PutArray(text, z): #the parameter must be a string
    a = str(string.ascii_lowercase) #Alfabeto minusculo
    b = str(string.ascii_uppercase) #Alfabeto maiusculo
    li = [] #Array principal para adição de nomes
    nUltCount = 0
    for x in range (z, len(text)):
        if text[x] in b:
            li.append(text[x])
            nUltCount = len(li)-1
            d = x
            input(fStringRead(li[nUltCount]))
            if text[x] == fStringRead(li[nUltCount]): #irá adicionar as letras minusculas apenas se a ultima letra adicionada na str for maiuscula
                for k in range (x+1, len(text)): #laço que da continuidade da posição da str
                    nUltCount = len(li)-1
                    if text[k] != fStringRead(li[nUltCount]):
                            if text[k] in b:
                                li[nUltCount] = fStringAdd(li[nUltCount], text[k])
                                nUltCount = len(li)-1
                    for minu in range (len(a)): #laço para montar a palavra adicionando as letras minusculas
                            if text[k] == a[minu]:
                                li[nUltCount] = fStringAdd(li[nUltCount], text[k])
                                nUltCount = len(li)-1
                            if text[k] == " ":
                                li[nUltCount] = fStringAdd(li[nUltCount], text[k]) #Adicionar espaço
                                nUltCount = len(li)-1
                                break #saindo do comando quando encontrar espaço
                            if text[k] == "," or text[k] == "–": #Ao chegar aqui significa que chegou ao final de um nome.
                                zzz = k
                                break 
                    if text[k] == "," or text[k] == "–":
                        print(z)
                        print(li)
                        break
                if text[k] == "," or text[k] == "–":
                    break
            print(x)
    
    return li, zzz










          
  
# Driver Function

liz   = []
text  = "Francisco Abel Alves Mota, Genilda da Silva "
count = 0
while count != len(text)-1:
    funct = []
    funct.append(PutArray(text, count))
    liz.append(funct[0][0])
    print(liz)
    count = funct[0][1]
    print("Este é o contador", count)


