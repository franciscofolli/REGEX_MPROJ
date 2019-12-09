# Python3 code to find sequences of one upper 
# case letter followed by lower case letters


#import re 
import string

# Function to add more values for String
def fStringAdd(str, word):
    return str[:len(str)] + word + str[len(str):]
def fStringRead(str):
    return str[:len(str)]

def fTratNome (cEsc): #Irá manter apenas os dois nomes de acordo com texto da mari
    stringss = cEsc
    #input(cEsc)
    if "faz " in stringss: #Condições que irá apagar tudo até chegar na palavra "Faz "
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
    else:
        try:
            setr = stringss.replace(stringss[:stringss.index(" que ")], "")
        except ValueError:
            return cEsc
        
        
    #Em seguida apagar os fazem
    #setr = setr.replace("faz ", "")
    #setr = setr.replace("fazem o ", "")

    if "faz " in setr: #Condições que irá apagar tudo até chegar na palavra "Faz "
        setr = setr.replace("faz ", "")
    elif "faz a " in setr:
        setr = setr.replace("faz a ", "")
    elif "faz as " in setr:
        setr = setr.replace("faz as ", "")
    elif "faz à " in setr:
        setr = setr.replace("faz à ", "")
    elif "faz às " in setr:
        setr = setr.replace("faz às ", "")
    elif "faz o " in setr:
        setr = setr.replace("faz o ", "")
    elif "faz os " in setr:
        setr = setr.replace("faz os ", "")
    elif "fazem " in setr:
        setr = setr.replace("fazem ", "")
    elif "fazem o " in setr:
        setr = setr.replace("fazem o ", "")
    elif "fazem os " in setr:
        setr = setr.replace("fazem os ", "")
    elif "fazem a " in setr:
        setr = setr.replace("fazem a ", "")
    elif "fazem as " in setr:
        setr = setr.replace("fazem as ", "")
    elif "fazem à " in setr:
        setr = setr.replace("fazem a ", "")
    elif "fazem às " in setr:
        setr = setr.replace("fazem as ", "")
    else:
        setr = setr.replace(" que ", "")
        
    #input(setr)
    try:
        setr = setr.replace(setr[setr.index("–"):len(setr)], "")
    except ValueError:
        try:
            setr = setr.replace(setr[setr.index("no valor de "):len(setr)], "")
        except ValueError:
            return cEsc
        
    
    #quebrado nomes de comprador e vendedor em array
    if "com o" in setr:
        setr = setr.split("com o")
    elif " à " in setr:
        setr = setr.split(" à ")
    elif " a " in setr:
        setr = setr.split(" a ")
    elif " ao " in setr:
        setr = setr.split(" ao ")
        
    if "no valor de " in setr[1]:
        setr[1] = setr[1].replace(setr[1][setr[1].index("no valor de "):len(setr[1])], "")
    
    #setr[1] = setr[1].replace(setr[1][setr[1].index("–"):len(setr[1])], "")
    return setr #Retorna array com um nome em cada posição.


          #\
  
# Driver Function
text = [] #Lista com apenas Escrituras
AN = [] #Lista de códigos --> será processado outro dia.
#liz   = [] #lista que trará nomes para serem tratados
aFinalResult = [[],[],[]] #Lista que irá conter todos os nomes
text1  = """"""
text1  = text1.split("\n") # irá dividir todo o texto e transformar a string em lista
opo = int() #Contador auxiliar para deletar as posições e não prejudicar o programa.
cod = [] #Codigo da Escritura
for i in range (len(text1)-1,-1,-1): #Laço para retirar todas as posições desnecessárias
    if text1[i] == '' or text1[i] == 'Descrição': #Deleta posições vazias ou com a palavra Descrição
        del(text1[i])
        opo = i
    elif 'Data - ' in text1[i]: #Deleta todas as Datas
        del(text1[i])
        opo = i
    opo -= 1    
    if "Escritura" in text1[opo]: #Condição que irá adicionar apenas as Escrituras (que tem os nomes) na variável [text]
        text.append(text1[opo])
del(i)
for i in range (len(text1)-1,-1,-1):
    if "Escritura" in text1[i]:
        del(text1[i])

oCodEsc = open('Códigos.txt', 'w') #Cria TXT
#oCodEsc = open('Códigos.txt', 'r')
oCodEsc.write(f'{text1}')
oCodEsc.close()
input("codigos colocados em TXT")
input("Deu certo")

del(oCodEsc)
del(text1) #Deleta variável que pega texto incial
#deleta variável contadora do for
del(opo) #deleta contador auxiliar
input('array de Escrituras e Códigos separadas')


del(cod) #Deleta os Codigos de Escritura


for p in range (len(text)): #Loop para apagar tudo que estiver dentro de colchetes
    try:
        text[p] = text[p].replace(text[p][text[p].index("["):text[p].index("]")+2], "")
    except ValueError:
        continue
del(p)

input('pressione o enter para começar a processar os dados')

#oVend = open('Vendedor.txt', 'w') #Cria TXT
#oComp = open('Comprador.txt', 'w')

aVend = []
aComp = []
aNTrat = []
for puu in range (len(text)): #Começa a processar e separar nomes 
    aNomes = fTratNome(text[puu]) 
    if type(aNomes) == str:
        aNTrat.append(aNomes)
    else:
        aVend.append(aNomes[0])
        aComp.append(aNomes[1])

#Cria TXT Vendedores
oVendArq = open('Vendedores.txt', 'w') 
oVendArq.write(f'{aVend}')
oVendArq.close()

#Cria TXT Compradores
oCompArq = open('Compradores.txt', 'w') 
oCompArq.write(f'{aComp}')
oCompArq.close()

#Cria TXT de Não tratados
oNTratArq = open('Não tratados.txt', 'w')
oNTratArq.write(f'{aNTrat}')
oNTratArq.close()





