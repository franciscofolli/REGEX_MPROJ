# Python3 code to find sequences of one upper 
# case letter followed by lower case letters

#import re 
import string
# Function to add more values for String
def fStringAdd(str, word):
    return str[:len(str)] + word + str[len(str):]
def fStringRead(str):
    return str[:len(str)]

# Function to catch the string and put on a array.
def PutArray(text, z): #the parameter must be a string
    a = str(string.ascii_lowercase) #Alfabeto minusculo
    b = str(string.ascii_uppercase) #Alfabeto maiusculo
    a = fStringAdd(a, "ãáàâçéèêíìîóòôõúùû")
    b = fStringAdd(b, "ÃÁÀÂÇÉÈÊÍÌÎÓÒÔÕÚÙÛ")
    #print(a)
    #print(b)
    li = [] #Array principal para adição de nomes
    nUltCount = 0
    for x in range (z, len(text)):
        if text[x] in b:
            li.append(text[x])
            nUltCount = len(li)-1
            d = x
            #print(li)
            #print("Esta é a ultima letra do texto ", fStringRead(li[nUltCount]))
            #print("text[x] ",text[x])
            if fStringRead(li[nUltCount]) in b: #irá adicionar as letras minusculas apenas se a ultima letra adicionada na str for maiuscula
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
                            if text[k] == "–": #Ao chegar aqui significa que chegou ao final de um nome.
                                zzz = k
                                break 
                    if text[k] == "–":
                        #print("esta é a variavel z ", z)
                        #print("este é o array da função ", li)
                        #print("este será o retorno ", zzz)
                        break
                if text[k] == "," or text[k] == "–":
                    break
            #print("variavel x ", x)
            zzz = x
    
    return li, zzz

def fTratNome (array): #Irá manter apenas os dois nomes de acordo com texto da mari
    stringss = array
    if "faz " in stringss:
        setr = stringss.replace(stringss[:stringss.index("faz ")], "")
    elif "faz a " in stringss:
        setr = stringss.replace(stringss[:stringss.index("faz a ")], "")
    elif "faz as " in stringss:
        setr = stringss.replace(stringss[:stringss.index("faz as ")], "")
    elif "faz à " in stringss:
        setr = stringss.replace(stringss[:stringss.index("faz à ")], "")
    elif "faz às " in stringss:
        setr = stringss.replace(stringss[:stringss.index("faz às ")], "")
    elif "faz o " in stringss:
        setr = stringss.replace(stringss[:stringss.index("faz o ")], "")
    elif "faz os " in stringss:
        setr = stringss.replace(stringss[:stringss.index("faz os ")], "")
    elif "fazem " in stringss:
        setr = stringss.replace(stringss[:stringss.index("fazem ")], "")
    elif "fazem o " in stringss:
        setr = stringss.replace(stringss[:stringss.index("fazem o ")], "")
    elif "fazem os " in stringss:
        setr = stringss.replace(stringss[:stringss.index("fazem os ")], "")
    elif "fazem a " in stringss:
        setr = stringss.replace(stringss[:stringss.index("fazem a ")], "")
    elif "fazem as " in stringss:
        setr = stringss.replace(stringss[:stringss.index("fazem as ")], "")
    elif "fazem à " in stringss:
        setr = stringss.replace(stringss[:stringss.index("fazem a ")], "")
    elif "fazem às " in stringss:
        setr = stringss.replace(stringss[:stringss.index("fazem as ")], "")

    setr = setr.replace("faz ", "")
    setr = setr.replace("fazem o ", "")
    if " ao " in setr:
        setr = setr.split(" ao ")
    elif " a " in setr:
        setr = setr.split(" a ")
    elif " à " in setr:
        setr = setr.split(" à ")
    if "no valor de  réis" in setr[1]:
        setr[1] = setr[1].replace("no valor de  réis", "")

    return setr


          #\
  
# Driver Function
text = [] #Lista com apenas Escrituras
AN = [] #Lista de códigos --> será processado outro dia.
liz   = [] #lista que trará nomes para serem tratados
aFinalResult = [[],[]] #Lista que irá conter todos os nomes
text1  = """AN, 1ON, 50, p. 15v; AGCRJ, Códice 42-3-56, p. 128
Data - 1670
Descrição
Escritura de venda de chãos que faz Antonio Álvares a Domingos Rodrigues Durões, no valor de 36 réis – com três braças de testada, sitos na rua de Mateus de Freitas, partindo de uma banda com casas de Ana Pinta, sogra dele vendedor e da outra com chãos de Antonio Ferreira da Silva, havidos por legítima de seu [sogro] Antonio Fernandes [Lugo].



AN, 1ON, 50, p. 65; AGCRJ, Códice 42-3-56, p. 136
Data - 1670
Descrição
Escritura de doação de chãos para instituição de patrimônio que fazem o Doutor Francisco da Fonseca [Diniz, médico do presídio do Rio de Janeiro desde 1663 - ABN, 39, p. 102, por alcunha "o Gadelha"] e sua mulher Isabel Rangel [de Macedo] ao Licenciado Jorge de Oliveira – com três braças de testada e 12 de quintal, sitos na rua de Aleixo Manoel, o velho, caminho da pabuna, partindo de uma banda com casas do doador e da outra com chãos de quem de direito, [comprados de Eusébio Dias Cardoso e sua mulher Francisca da Costa Homem em 21/11/1653 – 1º Ofício?]

"""
text1  = text1.split("\n") # irá dividir todo o texto e transformar a string em lista
for i in range (len(text1)-1,-1,-1): #Laço para retirar todas as posições desnecessárias
    if text1[i] == '' or text1[i] == 'Descrição':
        del(text1[i])
        opo = i
    opo -= 1    
    if "Escritura" in text1[opo]: #Condição que irá adicionar as Escrituras (que tem os nomes) na variável [text]
        text.append(text1[opo])
        
for p in range (len(text)):
    try:
        text[p] = text[p].replace(text[p][text[p].index("["):text[p].index("]")], "")
    except ValueError:
        continue


count = 0
for i in range (len(text)):
    while count != len(text[i])-1:
        funct = []
        funct.append(PutArray(text[i], count))
        liz.append(funct[0][0][0])
        count = funct[0][1]
        if text[i][count] == "," or text[i][count] == "–":
            break
    count = 0
input(liz)
for u in range (len(liz)):
    aFinalResult[0].append(fTratNome(liz[u])[0])
    aFinalResult[1].append(fTratNome(liz[u])[1])
print(aFinalResult)




