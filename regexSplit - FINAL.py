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



AN, 1ON, 50, p. 69v
Data - 1670
Descrição
Escritura de doação de uma morada de casas para instituição de patrimônio que fazem Antonio Rodrigues e sua mulher Catarina Martins(?) a seu filho Sebastião Ribeiro – de pedra e cal, coberta de telhas, com sala, câmara, cozinha e quintal, sita na rua que chamam detrás do Carmo, partindo de uma banda com casas de ... Barroso(?) e da outra com casas da cunhada (ou do cunhado) do Capitão Francisco Munhoz

AN, 1ON, 50, p. 79v; AGCRJ, Códice 42-3-56, p. 138
Data - 1670
Descrição
Escritura de doação de chãos que faz Angela da Assunção à sua afilhada e sobrinha Margarida – com 2,5 braças de testada, sitos na rua do tabelião Antonio de Andrade, partindo de uma banda com casas dela doadora e da outra com casas de Inês Peçanha, viúva de Jacinto Barbosa

AN, 1ON, 51, p. 34; AGCRJ, Códice 42-3-56, p. 143
Data - 1670
Descrição
Escritura de venda de uma morada de casas que fazem Domingos Rodrigues Durão e sua mulher Catarina Martins ao Capitão André Ferreira da Silva, no valor de 50 réis - térrea, de pedra e cal, sita na travessa adiante da rua dos Pescadores que vai sair à rua direita que vai para São Bento, que foi de Maria da Cunha, partindo de uma banda com casas dos herdeiros de [João] Velho Prego e da outra com casas do comprador.


AN, 1ON, 51, p. 38v; AGCRJ, Códice 42-3-56, p. 145
Data - 1670
Descrição
Escritura de venda de uma morada de casas que faz Catarina Ferreira a Leonardo Dorneles de Vasconcelos, no valor de 93 réis - com sala e câmara, corredor, cozinha, poço e quintal, coberta de telhas, sita na rua que chamam de São Francisco, feita em chãos comprados a Leonor da Fonseca, viúva de João de Freitas [de Araújo] [em 25/10/1662 – 1º Ofício].

AN, 1ON, 51, p. 42; AGCRJ, Códice 42-3-56, p. 146
Data - 1670
Descrição
Escritura de venda de uma morada de casas que faz Manoel Rodrigues Ribeiro ao Capitão Feliciano da Silva, no valor de 215 réis - térrea, com sala e câmara, sita na rua de Gaspar de Carvalho, partindo de uma banda com Baltazar Rangel e da outra com os herdeiros de Manoel Meira Peixoto.

AN, 1ON, 51, p. 67; AGCRJ, Códice 42-3-56, p. 148
Data - 1670
Descrição
Escritura de venda de chãos que fazem Antonio Vieira Branco e sua mulher Maria Fernandes e Domingos de Oliveira e sua mulher Maria Ribeiro a João da Cruz, no valor de 8.5 réis – com seis braças de testada, sitos em Nossa Senhora da Ajuda, defronte da casa do ermitão de Nossa Senhora do Desterro, sendo 3 pertencentes ao primeiro casal, herdadas de seu neto João, filho de Antonio Ribeiro e Assença Cordeiro, e outras 3 herdadas pela esposa do segundo casal do dito Antonio Ribeiro



AN, 1ON, 51, p. 77v; AGCRJ, Códice 42-3-56, p. 149
Data - 1670
Descrição
Escritura de venda de chãos que faz o Sargento-mor Francisco de Macedo Freire a Francisco de Macedo Viegas, no valor de 60 réis – com sete braças de testada e 9 de fundos, sitos na rua do Açougue Velho, que partem fronteiros com as casas do Sargento-mor Martim Correia Vasqueanes e de outra banda com Manoel Afonso [Cruz] e com quem de direito.



AN, 1ON, 51, p. 86v; AGCRJ, Códice 42-3-56, p. 150
Data - 1670
Descrição
Escritura de venda de uma morada de casas que faz o Capitão Miguel de Azedias Machado a Francisco de Macedo Viegas, no valor de 280 réis - de sobrado, sita na rua do Açougue Velho, partindo de uma banda com André Velho da Fonseca e da outra com Eliseu de Macedo e com quem de direito.



AN, 1ON, 51, p. 87v; AGCRJ, Códice 42-3-56, p. 150
Data - 1670
Descrição
Escritura de venda de chãos que faz Salvador Lopes a Antonio Duarte Filgueira, no valor de 21 réis – com 3,5 braças de testada, sitos na rua de São Francisco e rua da Cadeia, partindo de uma banda com Catarina Ferreira e da outra com João Lopes, irmão do vendedor, havidos por partilha de bens de sua mãe Bárbara de Faria.

AN, 1ON, 51, p. 94
Data - 1670
Descrição
Escritura de venda de uma morada de casas que faz Manoel Martins a Pedro Duarte, no valor de 130 réis  - sita na rua de Domingos Coelho Valadares, o cirurgião, partindo de uma banda com os padres de São Bento e fazem canto para o campo e com quem de direito.



AN, 1ON, 51, p. 107; AGCRJ, Códice 42-3-56, p. 156
Data - 1670
Descrição
Escritura de venda de uns chãos e paredes que fazem João Martins, calafate, e sua mulher Maria da Silva ao Sargento-mor Martim Correia Vasques, no valor de 450 réis - chãos e casa térrea em que vivem, e umas paredes de pedra e cal que o vendedor havia levantado, sitos na rua Direita, da banda do mar, partindo de uma banda com o Capitão Pedro Godinho Rosado e da outra com Matias Gonçalves, a saber, da banda do dito Matias Gonçalves a metade de toda a parede da rua até o mar, com toda a altura do sobrado tirando o pedaço do eirado, e da banda do Capitão Pedro Godinho Rosado a metade da dita parede da rua até o cais, até a altura do sobrado e o cais que está na dita fronteira e portões começados a se levantar sobre ele....

AN, 1ON, 51, p. 112v; AGCRJ, Códice 42-3-56, p. 157
Data - 1670
Descrição
Escritura de venda de uma morada de casas que fazem Pedro Pinto [da Fonseca] e sua mulher Ana Soares a Carlos Antonio, condestável-mor da artilharia, no valor de 150 réis - térrea, de taipa de mão, coberta de telhas, com sala, câmara, corredor e quintal, sita em três braças de chãos à face da rua que foi de Manoel Ribeiro, e com o quintal que tiver, partindo de uma banda com casas de Cristóvão de Lima e da outra com casas de Francisco Rabelo e com quem de direito, comprada a Paula da Silveira.

AN, 1ON, 51, p. 110v
Data - 1670
Descrição
Escritura de distrato de venda de uma morada de casas a retro aberto que fazem Egas Muniz Teles e Miguel de Freitas Ribeiro, no valor de 487 réis – sobre uma morada de casas sita na rua defronte do Capitão João Dias Rangel, que Miguel de Freitas tinha vendido a retro a Egas Muniz Teles em preço de 487$000 [escritura do 3º Ofício]



AN, 1ON, 51, p. 116v; AGCRJ, Códice 42-3-56, p. 158
Data - 1670
Descrição
Escritura de doação de parte de uma morada de casas que faz Beatriz Álvares, mulher de Pedro de Albernaz Correia, ao reverendo padre Manoel Correia Pestana - sita na rua do Padre Pedro Homem indo para São Francisco, partindo de uma banda com o Alferes Jorge Fernandes Cardoso e com quem mais deva partir, comprada pelo Padre Manoel da Fonseca Passos a mando do seu marido



AN, 1ON, 51, p. 147v; AGCRJ, Códice 42-3-56, p. 164
Data - 1671
Descrição
Escritura de quitação de venda de uma tenda de ferreiro que faz João Reimão a Bartolomeu Duarte, no valor de 18 réis

AN, 1ON, 51, p. 151; AGCRJ, Códice 42-3-56, p. 166
Data - 1671
Descrição
Escritura de venda de parte de uma morada de casas que faz Francisco da Costa da Fonseca a seu irmão Marcos da Costa da Fonseca [Castelo Branco], no valor de 60 réis - térrea, sita na rua do Gadelha, partindo com casas de Pantaleão Duarte e com quem de direito.



AN, 1ON, 51, p. 153v; AGCRJ, Códice 42-3-56, p. 167
Data - 1671
Descrição
Escritura de venda de uma morada de casas que fazem Gonçalo de Pontes de Labrit e sua mulher Dona Leonor [Faleira] a Manoel Francisco, no valor de 50 réis - térrea, sita na rua dos Pescadores, partindo de uma banda com casas de Francisco Machado Homem e da outra com chãos de Antonio Nunes de Menezes, havida por partilha dos bens de seu pai Gonçalo de Pontes de Labrit e sua mãe Margarida de Albuquerque.

AN, 1ON, 51, p. 154v; AGCRJ, Códice 42-3-56, p. 167
Data - 1671
Descrição
Escritura de venda de uma morada de casas a retro aberto que fazem Francisco Dias Medonho e sua mulher Isabel Soares de Mendonça ao reverendo padre Simão Camelo [de Lemos], no valor de 200 réis - térrea, de pedra e cal, sita na rua de Miguel de Freitas, partindo de uma banda com casas de Salvador ... [Luiz?] e da outra com casas de ....



AN, 1ON, 51, p. 160v; AGCRJ, Códice 42-3-56, p. 168
Data - 1671
Descrição
Escritura de venda de uma morada de casas a retro aberto que fazem Francisco Rabelo e sua mulher Beatriz de Oliveira ao reverendo padre Vicente de Leão, clérigo de São Pedro, no valor de 100 réis - térrea, de taipa de mão, com o seu quintal, sita na rua da Cadeia, partindo de uma banda com o dito Francisco Rabelo e da outra com Pedro Pinto [da Fonseca], comprada a Maria Vaz e Juliana (ou Juliano) Ramires.

AN, 1ON, 51, p. 155v; AGCRJ, Códice 42-3-56, p. 167
Data - 1671
Descrição
Escritura de doação de uma morada de casas que faz o reverendo padre João da Fonseca, sacerdote do hábito de São Pedro, à Santa Casa da Misericórdia – de sobrado, com seu quintal, sita no bairro da Santa Casa da Misericórdia, partindo de uma banda com casas do Padre Brás Garcez e da outra com o muro da parte do mar, havida por compra do Capitão Gonçalo Teixeira Tibau

AN, 1ON, 51, p. 161v; AGCRJ, Códice 42-3-56, p. 168
Data - 1671
Descrição
Escritura de venda de uma morada de casas que fazem o Capitão Manoel Caldeira Soares e sua mulher Bárbara Pinta de Castilho a Belchior Rodrigues Ribeiro, morador na Guaxindiba, no valor de 180 réis - térrea, sita na rua da Cadeia que vai para São Francisco, partindo de uma banda com o Padre Vicente de Leão e da outra com quem de direito.
Observações
Preço: 180$000 [ou 130$000]


AN, 1ON, 51, p. 171v
Data - 1671
Descrição
Escritura de dinheiro a razão de juros com hipoteca de uma morada de casas que faz André Fernandes a Francisco Alvares, tutor do órfão Eugênio, seu enteado e filho de Bento Ferreira e de Maria Álvares, no valor de 187.041 réis – sita na rua Direita, para a banda de Santo Antonio, que parte com casas do mesmo dito órfão e são da banda do mar.

AN, 1ON, 51, p. 185; AGCRJ, Códice 42-3-56, p. 171
Data - 1671
Descrição
Escritura de venda de uma morada de casas que fazem o Provedor e mais Irmãos da Santa Casa da Misericórdia a Sebastião Álvares da Silva, no valor de 125 réis - sita no bairro da Misericórdia, ao pé da fortaleza de Santiago...
Observações
Preço: 125$000(?)



AN, 1ON, 51, p. 186
Data - 1671
Descrição
Escritura de dinheiro a razão de juros com hipoteca de uma morada de casas que faz o Capitão Francisco de Gouveia ao Juízo dos Órfãos, no valor de 130 réis – de sobrado, de taipa de pilão, sita na rua do meirinho do mar [que chamam de Diogo de Montarroio], onde de presente vive, e uma sorte de terras em ...



AN, 1ON, 51, p. 189; AGCRJ, Códice 42-3-56, p. 171
Data - 1671
Descrição
Escritura de venda de uma morada de casas que fazem Manoel Pereira de Távora e sua mulher Maria da Assunção a Bento Ribeiro, no valor de 320 réis - térrea, de pedra e cal, com sala, câmara, varanda e quintal, com uma parede de cada banda do quintal, sita na rua do Gadelha, partindo de uma banda com casas de Leonor de Montarroio e da outra com os herdeiros do Doutor Lopo da Costa e com quem de direito.



AN, 1ON, 51, p. 194v; AGCRJ, Códice 42-3-56, p. 172
Data - 1671
Descrição
Escritura de venda de chãos que faz João de Ataíde Freire a Antonio Cardoso de Azevedo - na rua do General Salvador Correia de Sá e Benevides, partindo de uma banda com Antonio Duarte Velho e da outra com Francisco da Costa, o cego



AN, 1ON, 52, p. 39v
Data - 1672
Descrição
Escritura de venda de uma morada de casas que faz o reverendo padre João do Rosário, religioso de São Francisco da Penitência(?), como procurador de Manoel de Gonzaga Negrão e de João Caldeira Soares, cunhado e irmão do Capitão Manoel Caldeira Soares, residentes em Lisboa, a Bárbara Pinta, viúva do Capitão Manoel Caldeira Soares, no valor de 550 réis - térrea, de pedra e cal, sita na rua Direita, no canto da rua que fica de frente da quitanda, partindo com casas de Manoel Lopes(?) de Morais(?)...

AN, 1ON, 52, p. 46v
Data - 1672
Descrição
Escritura de venda de chãos que fazem Antonio Rodrigues e sua mulher Isabel Rodrigues a João da Cruz, no valor de 3.6 réis – com quatro braças de testada, sitos no bairro de Nossa Senhora da Ajuda, partindo de uma banda com chãos do comprador, havidos por dote de Isabel Ribeira [3º Ofício].

AN, 1ON, 52, p. 48v
Data - 1672
Descrição
Escritura de venda de uma morada de casas que fazem João Gonçalves de Sá e sua mulher Bárbara Vaz ao Padre Vicente de Leão, no valor de 260 réis - térrea, de pedra e barro, coberta de telhas, com seu quintal, partindo de uma banda com casas de Felipe Rodrigues e de outra com casas de Nicolau Soares, comprada a Assenço Lopes e a José Simões, seu genro [3º Ofício].

AN, 1ON, 52, p. 52
Data - 1672
Descrição
Escritura de venda de chãos que faz Margarida Gomes, viúva de Manoel Coelho de Souza, a Manoel de Barros de Freitas, no valor de 80 réis – com 4,5 braças de testada, sitos na rua que chamam do Rabelo [bar]beiro, travessa da cadeia, partindo de uma banda com casas de Inês Henriques, mãe da vendedora, e de outra com casas de sobrado dos órfãos de Domingos Martins, havidos por dote que lhe fez seu pai



AN, 1ON, 52, p. 55
Data - 1672
Descrição
Escritura de dinheiro a razão de juros com hipoteca de duas moradas de casas que faz Luiz da Costa Moreira, devedor, ao Juízo dos Órfãos, tendo como fiador Domingos Francisco, no valor de 140 réis – de sobrado, de pedra e cal, sita na rua defronte da quitanda, que parte de uma banda com casas de Pedro de [Bacilon] e da outra com João Tomás Brum. O fiador hipoteca uma morada de casas sita na rua que chamam de Antonio Vaz Viçoso, que parte de uma banda com casas de Pedro(?) ... e da outra com quem de direito for.


AN, 1ON, 52, p. 63
Data - 1672
Descrição
Escritura de venda de duas moradas de casas que faz Margarida Pinta, viúva de Inácio de Figueiredo, a seus filhos órfãos, no valor de 1100 réis - de sobrado, altos e baixos, contíguas umas às outras, de frente à igreja de São José, compradas ambas ao Prelado Administrador Doutor Manoel de Souza de Almada



AN, 1ON, 52, p. 71
Data - 1672
Descrição
Escritura de dinheiro a juros com hipoteca de uma morada de casas e de um partido de canas que faz Roque Pinto, [ourives], devedor, ao Juízo dos Órfãos, tendo como fiador Antonio da Silveira Fialho, no valor de 101 réis – sita na rua de Antonio Vaz Viçoso, que parte de uma banda com casas de Antonio Gomes e da outra com casas de Gaspar de Amorim(?). O fiador hipoteca um partido de canas que possui no engenho de Antonio Zuzarte, com oito peças do gentio de guiné.

AN, 1ON, apud 6LTMSBRJ; Cortines Laxe, p. 267; VF, IV, 167
Data - 1672
Descrição
Escritura de troca que entre si fazem o Doutor Clemente Martins de Matos e os reverendos padres de São Bento desta cidade - O Doutor Clemente Martins de Matos troca uma data de terras sita em Nuam (Inoã), junto a Maricá, comprada a Teotônio da Silva, por uma morada de casas térrea, de pedra e cal, de propriedade do Mosteiro, sita na rua que vem de São Francisco para a Cadeia

AN, 1ON, 52, p. 25v; AGCRJ, Códice 42-3-57, p. 264
Data - 1672
Descrição
Escritura de venda de uma morada de casas que fazem Francisco Coelho da Silva e sua mulher Bárbara Pereira a Francisco Dias Medonho, no valor de 300 réis - térrea, de pedra e cal, com sala, câmara, varanda e quintal, sita na rua que chamam de Miguel de Freitas, partindo de uma banda com casas do Capitão João Dias Rangel e da outra com casa onde mora o comprador, havida por partilha dos bens de sua mãe e sogra Isabel Rodrigues
Observações
Estas casas são revendidas em 17/1/1674 por Francisco Dias Medonho a Rodrigo de Castro Pinto por 260$000 (AN, 1ON, 53).



AN, 1ON, 52, p. 27
Data - 1672
Descrição
Escritura de dinheiro a juros com hipoteca de moradas de casas que faz Francisco Dias Medonho, devedor, ao Juízo dos Órfãos, tendo como fiador o Capitão Jerônimo Malheiros(?) de Souza, no valor de 309 Réis – O devedor hipoteca quatro moradas térreas, místicas, duas acabadas de todo, sitas na rua de Miguel de Freitas, começando da morada de casas do Capitão João Dias Rangel até entestar com as casas de Brás Luiz [Sucussarará?]. O fiador hipoteca uma morada sita no canto defronte das casas que foram do vigário João Manoel

AN, 1ON, 52, p. 141
Data - 1672
Descrição
Escritura de dinheiro a razão de juros com hipoteca de escravos e de uma morada de casas que faz o Licenciado Antonio da Silva ao Juízo de Órfãos tendo como fiador Manoel Fernandes Vareiro – O devedor hipoteca escravos e o fiador hipoteca uma morada de casas térrea, de pedra e cal, sita na rua que chamam de Miguel de Freitas, que parte de uma banda com casas de João Dias Rangel e da outra com casas de João de Araújo(?)

AN, 1ON, 52, p. 98v; AGCRJ, Códice 42-3-57, p. 274
Data - 1672
Descrição
Escritura de composição e nova obrigação que fazem o Capitão Cláudio Antonio Besançon e o Capitão Inácio da Silveira Vilalobos – a respeito de uma morada de casas de sobrado, de pedra e cal, sita defronte da igreja de Nossa Senhora do Monte do Carmo, que faz canto por uma banda e pela outra parte com casas do Licenciado João Dias da Costa, cuja casa o capitão Cláudio Antonio vendera ao capitão Inácio por 4.000 cruzados

AN, 1ON, 52, p. 100v; AGCRJ, Códice 42-3-57, p. 274
Data - 1672
Descrição
Escritura de venda de uma morada de casas que faz o Padre Vicente de Leão a Manoel da Costa, no valor de 160 réis – térrea, de pedra e barro e adobes, sita na rua que vai para São Francisco, que parte por uma banda com casas que foram do Padre Vigário João de Bastos e pela outra com chãos que foram de Simão de Souza, comprada a Lourenço Dias, já defunto, em 165...

AN, 1ON, 52, p. 81; AGCRJ, Códice 42-3-57, p. 271
Data - 1673
Descrição
Escritura de venda de uma morada de casas que fazem o Alferes Nicolau Soares e sua mulher Dona Bárbara Barreta ao Alferes Lucas do Couto, no valor de 120 réis - térrea, de taipa de pilão, coberta de telhas, sita na rua que chamam do açougue velho, partindo de uma banda com chãos de André Velho e da outra com casas do Alferes Eliseu de Macedo, comprada a Bento Barbosa de Sá em 23/8/1671.



AN, 1ON, 52, p. 45v; AGCRJ, Códice 42-3-57, p. 267
Data - 1673
Descrição
Escritura de dinheiro a razão de juros com hipoteca de duas moradas de casas que faz Aleixo Vaz, senhor de engenho, devedor, ao Juízo dos Órfãos, com dinheiro dos órfãos de Antonio do Vale, tendo como fiador Bento Pereira Bacelar, no valor de 150 réis – o devedor hipoteca duas moradas de casas de sobrado, sitas na rua detrás do Carmo, que partem de uma banda com casas de Antonio Teixeira e da outra com casas de Domingos Barroso.



AN, 1ON, 52, p. 47v
Data - 1673
Descrição
Escritura de dinheiro a razão de juros com hipoteca de um partido de canas e de uma morada de casas que faz o Capitão Francisco Martins Soares [homem de negócio], com dinheiro dos órfãos de Inácio de Figueiredo, tendo como fiador Matias Gonçalves, cavaleiro da Ordem de Cristo, no valor de 120 réis – sito no engenho do Capitão Tomé de Souza, com 16 peças do gentio de guiné. O fiador hipoteca uma morada de casas de dois sobrados, de pedra e cal, sita na rua Direita, que por uma banda faz canto e da outra parte com casas de Antonio Gomes.

AN, 1ON, 52, p. 53; AGCRJ, Códice 42-3-57, p. 268
Data - 1673
Descrição
Escritura de venda de chãos que fazem Bernardinho (ou Bernardigno, como ele assina) de Magalhães e sua mulher Domingas Gomes de Figueiredo, moradores no rio de Iriri, a João da Cruz, que tem uma chácara ao Desterro, no valor de 2.5 réis – Com 2,5 braças de testada, sitos indo de Nossa Senhora da Ajuda para o Desterro, com fundos para o campo de Nossa Senhora da Ajuda, partindo de uma banda com chãos de Margarida da Conceição, irmã da dita Domingas, e da outra com casas do comprador, herdados da legítima de seu pai e sogro Lourenço Gonçalves, quando neles ainda havia uma casa térrea que depois caiu.



AN, 1ON, 52, p. 54v; AGCRJ, Códice 42-3-57, p. 268
Data - 1673
Descrição
Escritura de venda de uma morada de casas que fazem o Capitão-mor José Varela e sua mulher Dona Ana Ribeira, moradores no Outeiro da Conceição, a Mamede Álvares, no valor de 19 réis - térrea, com sala e câmara à face da rua e uma câmara da banda de dentro, com sua varanda para a banda do quintal, toda com parede de taipa de pilão, sita no alto do Colégio indo para a fortaleza de São Sebastião, partindo de uma banda com casas de Maria da Silveira e da outra faz canto, e pelos fundos do quintal que vai à face da rua parte com casas do Alferes João de Mariz.

AN, 1ON, 52, p. 64v
Data - 1673
Descrição
Escritura de dinheiro a razão de juros com hipoteca de um partido de canas e de uma morada de casas que faz Agostinho de Paredes, devedor, ao Juízo de Órfãos, tendo como fiador o Capitão Jorge Fernandes Cardoso, no valor de 71 réis – O devedor hipoteca um partido de canas que possui no engenho de seu irmão Luiz de Paredes, em Sapopemba, com 12 peças do gentio de guiné. O fiador hipoteca uma morada de casas térrea, sita na travessa do Padre Pedro Homem.

AN, 1ON, 52, p. ?; AGCRJ, Códice 42-3-57, p. 261; FF, HCRJ, I, 322, nota 3
Data - 1673
Descrição
Escritura de venda de uma morada de casas que fazem Antonio de Sampaio de Almeida e sua mulher a João Soares Pereira - de sobrado, com paredes de pedra e cal, sita na travessa desta cidade que chamam de Gadelha, que de uma banda parte com casas do Capitão Francisco Barreto de Faria e da outra faz canto na travessa que chamam do dito Francisco Barreto, e cujas portas e lojas nesta dita travessa, com o seu quintal até entestar com a casa dos herdeiros do Capitão-mor Gaspar Carrilho, comprada ao Padre Paulo da Costa, como procurador de Dona Isabel de Mariz, em maio de 1670 [1º Ofício]



AN, 1ON, 53, p. 3
Data - 1673
Descrição
Escritura de fiança que fazem ao Senado da Câmara o Alferes Francisco Godinho Correia, eleito para tesoureiro dos efeitos do donativo, tendo como fiadores Manoel Cardoso Leitão, Baltazar Rangel de Souza e o Capitão Sebastião Coelho Damim – Manoel Cardoso Leitão hipoteca uma morada de casas térrea, de pedra e cal, e parede e chãos de outras contíguas, em que de presente vive. O fiador Baltazar Rangel de Souza hipoteca uma morada de casas térrea, em que de presente vive, sita na rua que chamam dos Tabeliães, e um partido de canas no engenho de Agostinho Pimenta, e outro partido sito em terras próprias, onde chamam a Pedra, com 30 peças do gentio de guiné. O Capitão Sebastião Coelho Damim ... (escritura danificada)

AGCRJ, Códice 42-3-57, p. 270
Data - 1673
Descrição
Escritura de obrigação e contrato que faz Dona Úrsula da Silveira com os mestres Luiz Teixeira e Antonio Fernandes Trigueiro – para conserto de uma morada de casas de sobrado, sita na rua que chamam da Portuguesa
Observações
Data: 1673.

AN, 1ON, 44, p. 219
Data - 1662-08-07
Descrição
Escritura de venda de chãos que fazem Antonio Coelho de Oliveira e sua mulher Cordula Gomes de Oliveira a Isabel Pedrosa [de Gouveia], viúva do Capitão Gaspar Dias de Figueiredo, no valor de 30 réis – com 2,5 braças de testada, sitos na rua de Miguel de Freitas, partindo de uma banda com chãos de Isabel Pedrosa e da outra com quem de direito, comprados a Antonio Martins Ribeiro.

AN, 1ON, 44, p. 222v
Data - 1662
Descrição
Escritura de dote de casamento que faz o Capitão Feliciano Coelho Cão e sua mulher Dona Luiza de Souza Leite a seu genro Manoel Teles de Menezes e sua filha Dona Mariana de Souza – Dentre os bens estão peças de guiné, uma morada de casas térrea, sita no bairro de Nossa Senhora da Ajuda, e terras sitas nos Coqueiros

AN, 1ON, 44, p. 257v
Data - 1662
Descrição
Escritura de venda de chãos que faz Leonor da Fonseca, viúva de João de Freitas de Araújo, a Catarina Ferreira – com três braças de testada, sitos na rua que vai [para São Francisco], partindo de uma banda com chãos de ... e da outra com três braças dela dita vendedora


AN, 1ON, 45, p. 28; AGCRJ, Códice 42-3-56, p. 5
Data - 1662
Descrição
Escritura de ratificação e declaração de venda de uma morada de casas que faz o General Salvador Correia de Sá e Benevides ao Capitão João Batista [Jordão] – de sobrado, sita na rua Direita, no canto do Carmo

AGCRJ, Códice 42-3-56, p. 3
Data - 1662
Descrição
Escritura de doação de uma morada de casas para instituição de patrimônio que fazem o Capitão Antonio de Sampaio e sua mulher Francisca de Almeida ao Licenciado Inácio Varela, para que se ordene - térrea, de taipa de pilão, sita na travessa do Sargento ....

VF, II, 157
Data - 1662
Descrição
Carta de sesmaria de chãos concedida a Jerônimo de Souza Brito - chãos no morro do Castelo, junto ao antigo forte de São Januário. Haverá contenda judicial sobre isso mais tarde, no período joanino, quando Luiz Antonio de Faria Lobato pede que seja mantido na posse da chácara que comprara no morro do Castelo. Título de sesmaria era legítimo, mas as terras passaram depois para a Coroa, razão pela qual o pedido foi indeferido
Observações
Data: 1662.

AN, 1ON, 45, p. 47; AGCRJ, Códice 42-3-56, p. 8
Data - 1663-01-22
Descrição
Escritura de venda de uma morada de casas que fazem Manoel Barbosa e sua mulher Maria de Amorim ao Alferes Antonio Borges, no valor de 28 réis - térrea, de taipa de pilão e de mão, coberta de telhas, sita no bairro da Misericórdia, partindo de uma banda com casas de Ventura de ... e da outra com chãos de Lauriano de Souza.
Preço
28 Réis
Código

AN, 1ON, 45, p. 47; AGCRJ, Códice 42-3-56, p. 8
Data - 1663
Descrição
Escritura de venda de uma morada de casas que fazem Manoel Barbosa e sua mulher Maria de Amorim ao Alferes Antonio Borges, no valor de 28 réis - térrea, de taipa de pilão e de mão, coberta de telhas, sita no bairro da Misericórdia, partindo de uma banda com casas de Ventura de ... e da outra com chãos de Lauriano de Souza.
Preço
28 Réis
Código

AN, 1ON, 45, p. 48; AGCRJ, Códice 42-3-56, p. 8
Data - 1663
Descrição
Escritura de venda de chãos que fazem Manoel Afonso e sua mulher Clara Barbosa ao Padre Reitor do Colégio da Companhia de Jesus – com 3,5 braças de testada, sitos defronte da porta de carro dos reverendos padres da Companhia, no alto da cidade, na ladeira que vai da Misericórdia, partindo de uma banda com José da Maia e da outra com quem de direito, havidos por partilha dos bens de seu pai Diogo Afonso.
Preço
Código


AN, 1ON, 45, p. 50
Data - 1663
Descrição
Escritura de obrigação de legítimas que faz Manoel de Espinha Ribeiro ao Juízo dos Órfãos - Manoel de Espinha Ribeiro diz que estava entregue das legítimas dos órfãos Inácia Ferreira e Amador de Lemos [Ferreira], filhos do defunto Manoel Rodrigues Ferreira [com Inácia Cardosa], seu antecessor, e que os estava sustentando, importando cada uma das duas legítimas em 598$636, totalizando 1:197$272, em que entravam 600$000 de uma morada de casas sita na travessa defronte da quitanda. Por esta escritura toma este dinheiro emprestado com obrigação de pagá-lo aos órfãos no futuro

AN, 1ON, 45, p. 54; AGCRJ, Códice 42-3-56, p. 10
Data - 1663
Descrição
Escritura de doação de uma morada de casas para instituição de patrimônio que faz Catarina Gomes ao Padre Vigário da Vila de São Paulo Domingos Gomes Albernaz - térrea, de taipa de mão, coberta de telhas, em que de presente vive, com quatro braças de testada e 10 de comprido, sita em Vila Verde, na rua que vai de Gaspar Carneiro (Carvalho?) para o campo, avaliada em 250$000 e que rende 16$000 ao ano

AN, 1ON, 45, p. 70; AGCRJ, Códice 42-3-56, p. 15; VF, V, 57
Data - 1663
Descrição
Escritura de aforamento de uma morada de casas que faz a Santa Casa da Misericórdia, por seu provedor Martim Correia Vasqueanes e mais irmãos, a André Mendes da Silva - térrea, de pedra e cal, sita [na travessa do Azeite de Peixe], no canto da igreja da Candelária, defronte de Manoel Rodrigues Cruz, partindo de uma banda com casas da Santa Casa da Misericórdia, e quintal até a parede da igreja de Nossa Senhora da Candelária, havida por doação feita por Gonçalo Gonçalves

AN, 1ON, 45, p. 71v; AGCRJ, Códice 42-3-56
Data - 1663
Descrição
Escritura de venda de uma morada de casas que fazem o Capitão Lourenço de Figueiredo e sua mulher Maria da Conceição a Brás Dias, no valor de 21 réis - sita no alto da cidade, partindo de uma banda com casas de Crispim da Cunha e da outra com casas de Joana Sardinha(?), arrematada em praça pública

AN, 1ON, 45, p. 73v; AGCRJ, Códice 42-3-56
Data - 1663
Descrição
Escritura de venda de uma morada de casas que fazem André Tavares e seu filho Francisco Tavares a João Fernandes, no valor de 280 réis - de sobrado, de cal e barro, sita na rua que vai para a [porta da cidade], partindo de uma banda com casas de Francisco Correia e da outra com o dito André Tavares.

AN, 1ON, 45, p. 92
Data - 1663
Descrição
Escritura de dinheiro a juros com hipoteca de uma morada de casas que faz o Juiz dos Órfãos, Capitão Francisco Teles Barreto, a Manoel da Silva Borges, devedor, no valor de 85 réis – térrea, de pedra e cal, em que vive, no canto da rua do Governador, na travessa

AN, 1ON, 45
Data - 1663-04-23
Descrição
Escritura de venda de uma morada de casas que faz Clara Filgueira, viúva de André Álvares [Gaio], a Catarina Correia, no valor de 27 réis - térrea, sita na rua dos Pescadores, partindo de uma banda com casas de ... Correia e da outra com casas do Capitão-mor Francisco Lidrales(?).


AN, 1ON, 45, p. 131
Data - 1663
Descrição
Escritura de venda de chãos que faz o Padre Domingos Gomes de Albernaz, vigário da vila de São Paulo, por seu procurador, Licenciado Antonio Gomes Mealha, a Manoel da Silva Borges, no valor de 165 réis – com 11 braças de testada, sitos na rua dos Quartéis, defronte das casas dos herdeiros de Mateus de Freitas, que fazem canto onde está o Paço, com todo o seu comprimento e quintais, até entestar com as casas da Misericórdia ou com quem de direito.
Observações
165$000 (15$000 por braça)

AN, 1ON, 45, p. 102; AGCRJ, Códice 42-3-56, p. 21
Data - 1663-05-07
Descrição
Escritura de dote e casamento que fazem Maria Jácome de Melo, viúva de Francisco Ferreira Travassos, seu pai Capitão João Pimenta de Carvalho, e seu filho Francisco Machado de Aguiar, a Gregório Nazianzeno da Fonseca, que vai casar com sua filha, neta e irmã Maria Machada de Melo - 5,5 braças de chãos de testada com seu quintal ... dos padres de São Bento, partindo com casas de Cristóvão de Melo à ponte (fonte?) de São Bento
Observações
Rheingantz diz que Gregório Nazianzeno da Fonseca casou com Maria Pimenta de Carvalho, filha de Francisco Ferreira Travassos e de Maria Jácome de Melo, por volta de 1667 - Rheingantz, II, 151

AGCRJ, Códice 42-3-56, p. 29
Data - 1663
Descrição
Escritura de venda de uma morada de casas que fazem Francisco de Espinosa e sua mulher Tomásia de Lima a Mônica Correia, no valor de 30 réis - térrea, de taipa de pilão, sita no Alto do Colégio, havida por herança de sua mãe e sogra Margarida de Lima [filha de Pero da Costa, o velho].
Observações
30$000 (pagos pela cessão de uma escrava de guiné). Esta escritura está acoplada a outra de venda de benfeitorias de terras na Lagoa por parte de Mônica Correia


AN, 1ON, 45, p. 143v; AGCRJ, Códice 42-3-56, p. 35
Data - 1663
Descrição
Escritura de venda de chãos que faz Bartolomeu Pinto ao Capitão Domingos Árias de Aguirre – com 15 palmos de testada, sitos detrás das casas do vendedor, na rua que ... de Gaspar Dias Mesquita, partindo de ....


AN, 1ON, 45, p. 147v; AGCRJ, Códice 42-3-56, p. 38
Data - 1663
Descrição
Escritura de venda de chãos que fazem Mateus Luiz e sua mulher Maria Raposo a Antonio Pereira, no valor de 50 réis - sitos defronte do Paço do Sargento-mor, partindo de uma banda com casas de Antonio ... e da outra com Antonio(a) da Silva.

AN, 1ON, 45, p. 170v; (AGCRJ, Códice 42-3-56, p. 43
Data - 1664
Descrição
Escritura de venda de chãos que faz Antonio Fernandes Lugo a Manoel de Carvalho Soares – sitos na rua em que ele mora, a entestar com casas do comprador, com quintal até entestar com casas dos herdeiros do Capitão Mateus de Freitas.

AN, 1ON, 45, p. 174v; AGCRJ, Códice 42-3-56, p. 44
Data - 1664
Descrição
Escritura de venda de chãos que fazem Bento da Rocha Gondim e sua mulher Maria de Muros a Vicente Álvares, no valor de 250 réis – com três braças de testada, sitos na banda da praia, com comprimento até o mar, partindo de uma banda com o comprador e da outra com outras três braças de chãos de ... marido e mulher, foreiros ao Senado da Câmara em 7$200 por ano. Já havia algo nesses chãos


AN, 1ON, 45, p. 182v
Data - 1664
Descrição
Escritura de venda de chãos que faz Pascoal Leitão a Miguel do Couto de Azevedo, no valor de 7 réis  – com três braças de testada e 11 de quintal, sitos na rua que vai [para São Francisco], que partem de uma banda com umas casas que se estão fazendo de Margarida Moura(?) e da outra com chãos dele vendedor.
Observações
A escritura de outorga desta venda, feita por Catarina Ribeira, viúva de Pascoal Leitão, só é realizada em 5/4/1692 (AN, 1ON, 59, p. 10v; AGCRJ, Códice 42-4-88, p. 833)


AN, 1ON, 45, p. 189; AGCRJ, Códice 42-3-56, p. 46
Data - 1664
Descrição
Escritura de dote e casamento que fazem Gaspar Fernandes e sua mulher Generosa Salgada à sua filha Luzia de Magalhães e seu genro João Gonçalves Cerqueira - uma morada de casas térrea, de taipa de mão, coberta de telhas, pegada com as dos dotadores na Prainha, com 12 braças de quintal...

AN, 1ON, 45, p. 189v; AGCRJ, Códice 42-3-56, p. 47
Data - 1664
Descrição
Escritura de venda de chãos que fazem Bento da Rocha Gondim e sua mulher Maria de Muros a Domingos Rodrigues de Lisboa, no valor de 175 réis  – com três braças de testada, sitos na rua Direita, com comprimento até o mar, foreiros ao Senado da Câmara, com foro de 7$200 por ano.

AN, 1ON, 46, p. 3v
Data - 1664
Descrição
Escritura de obrigação que faz ... Cordeiro, como procurador de seu filho Matias Cordeiro, ao Juízo dos Órfãos – Diz que seu filho fora condenado para degredo em Angola ... seu constituinte precisa de 100$000 ... não os tem ... empresta dinheiro e dá em garantia uma morada de casas térrea, de pedra e barro, sita ao pé da ladeira do Colégio ...

AN, 1ON, 46, p. 11v; AGCRJ, Códice 42-3-56, p. 50
Data - 1664
Descrição
Escritura de doação de uma morada de casas para instituição de patrimônio que fazem Francisco Cordeiro e sua mulher Margarida da Silva a Gregório Pereira, para ordenar-se - térrea, de taipa de mão, coberta de telhas, sita na rua que vai da porta da cidade à Santa Misericórdia, partindo de uma banda com chãos do Capitão Marcos de Azeredo Coutinho e da outra com chãos dos herdeiros de Brás de Souza, avaliada em 50$000


AN, 1ON, 46, p. 22v; AGCRJ, Códice 42-3-56, p. 51
Data - 1664
Descrição
Escritura de venda de chãos que faz Diogo Aranha a Manoel da Silva Borges, no valor de 25 réis – sitos na rua dos Quartéis, partindo de uma banda com casas dos reverendos padres do Carmo e da outra com casas do Padre Antonio Correia.

AN, 1ON, 46, p. 29
Data - 1664
Descrição
Escritura de dinheiro a juros com hipoteca de uma morada de casas que faz Antonio Duarte [Velho], credor, a Antonio Gonçalves, devedor, no valor de 2000 cruzados – de sobrado, de pedra e cal, onde vive

AN, 1ON, 46; AGCRJ, Códice 42-3-56, p. 52
Data - 1664
Descrição
Escritura de venda de chãos que faz Manoel de Souza a Isabel Fernandes, viúva de Manoel Lopes, no valor de 35 réis – com três braças de testada e 10 ou 12 de quintal, sitos na rua nova detrás que vai para São Bento, partindo de uma banda com casas de Manoel Rodrigues Salvado e da outra com chãos de Dom Luiz Quixada, chãos comprados ao Capitão Miguel de Abreu Soares por escritura de 25/6/1664.


AN, 1ON, 46, p. 32
Data - 1664
Descrição
Escritura de dote de casamento que fazem Antonio Gonçalves Madeira e sua mulher Simoa Antunes a Antonio Duarte [Velho] e sua filha Antonia de Abreu, no valor de 1000 cruzados – Dotam o casal em 1.000 cruzados, valor da morada de casas de sobrado, de pedra e cal, em que vivem eles dotadores


AN, 1ON, 46, p. 36v; AGCRJ, Códice 42-3-56, p. 53
Data - 1664
Descrição
Escritura de venda de uma morada de casas que faz o Capitão Manoel de Gouveia, como administrador dos bens de suas filhas, a seu irmão Francisco de Gouveia, no valor de 450 réis - de sobrado, de taipa de pilão, sita na rua que chamam de Diogo de Montarroio, defronte do meirinho do mar Francisco de [Araújo], partindo de uma banda com casas de Pantaleão Duarte e da outra com Inês Nogueira.


AN, 1ON, 46, p. 37v; AGCRJ, Códice 42-3-56, p. 53
Data - 1664
Descrição
Escritura de venda de uma morada de casas que fazem Jerônimo Rodrigues e sua mulher Bárbara de Morais a Assenço de Siqueira, no valor de 43 réis - térrea, de pedra e cal, coberta de telhas, sita na rua que vai para São Francisco, partindo de uma banda com chãos de Nicolau Tavares e da outra com casas de Francisco de Lemos.


AN, 1ON, 46, p. 42
Data - 1664-11-07
Descrição
Escritura de dote de casamento que fazem Diogo Soares de Albergaria e José Soares de Albergaria, filhos do defunto José Soares, a sua irmã Lauriana (ou Cecília) de Menezes, para casar com Baltazar de Brito – metade de sua legítima, da parte que tem em uma morada de casas de sobrado, sita na rua dos Pescadores

AN, 1ON, 46, p. 78; AGCRJ, Códice 42-3-56, p. 67
Data - 1665
Descrição
Escritura de venda de duas moradas de casas a retroaberto que faz Maria Savalos, viúva de Jerônimo Camelo de Sampaio, a Gonçalo Ferreira Fortuna, no valor de 151 réis - térreas, de taipa de pilão e parte de pedra e cal, com seu quintal e uma cozinha de pedra e barro, cobertas de telhas, sitas defronte da cadeia, partindo de uma banda com casas de Pedro de Sá e da outra com casas de Francisco de Espinosa [uma delas comprada a André Dias Tenreiro e sua mulher Isabel de Lima em 4/4/1650 – 1º Ofício].
Preço
151 Réis
Código
AN, 1ON, 46, p. 78; AGCRJ, Códice 42-3-56, p. 67

AN, 1ON, 47, p. 21v
Data - 1665
Descrição
Escritura de venda de uma morada de casas que faz o Ajudante Manoel Afonso Cruz a Marcos Gonçalves, no valor de 55 réis - térrea, de taipa de mão, coberta de telhas, com seu quintal, feita em 2,5 braças de testada e 10 braças de fundo, sita na rua do Açougue Velho, partindo de uma banda com casas do vendedor e da outra com Domingos José.

AN, 1ON, 47, p. 7
Data - 1665
Descrição
Escritura de venda de chãos que fazem o Ajudante Manoel de Faria Peçanha(?) e sua mulher a Antonio Rodrigues Pereira – sitos no bairro da Misericórdia, que partem com umas casinhas ..., comprados ao Padre Assenço Gago da Câmara ...

AN, 1ON, 47, p. ?
Data - 1665
Descrição
Escritura de venda de chãos que fazem Bento de Sampaio e sua mulher Maria Ferreira a Afonso Lopes, no valor de 15 réis – com três braças de testada, sitos na rua ... das casas de Inácio Castanheira, partindo de uma banda com outra três braças (vendidas a?) Manoel Álvares e da outra com quem de direito, as quais duas três braças houveram de troca e compra do Sargento-mor Manoel Correia Vasqueanes.

AN, 1ON, 47, p. 85v
Data - 1665
Descrição
Escritura de venda de uma morada de casas que fazem Domingos Rodrigues de Lisboa e sua mulher Joana de Araújo a Rodrigo de Castro, no valor de 350 réis - térrea, de pedra e cal, coberta de telhas, com seus quintais, sita na rua de [Diogo de] Montarroio, partindo de uma banda com casas dos herdeiros do Capitão João do Souro e da outra com casas dos Padres do Carmo, havida de dote de casamento.

AN, 1ON, 47, p. 89v
Data - 1665-06-01
Descrição
Escritura de dinheiro a razão de juros com hipoteca de três moradas de casas que faz Pedro Pinto da Fonseca no Juízo dos Órfãos desta cidade, tendo como fiador Domingos Martins de Azevedo – Para garantia do empréstimo, o devedor hipoteca três moradas de casas térreas, sitas defronte da Cadeia, e vão correndo do canto pela travessa [da Cadeia] adiante
Observações
Data: 1-5/6/1665.


AN, 1ON, 47, p. 92
Data - 1665
Descrição
Escritura de troca de duas moradas de casas que fazem o reverendo padre Francisco da Silva Cabral e os reverendos padres da Companhia – O Padre Francisco da Silva Cabral trespassa uma morada térrea, de taipa de pilão, sita na ladeira do Colégio, defronte do ...., que parte de uma banda com casas dos herdeiros do defunto .... e da outra com chãos dos padres da Companhia, e o Reitor do Colégio, Padre Francisco de Avelar, dá em troca de outra morada térrea, de pedra e cal, coberta de telha sita no desembarcadouro dos ditos Padres na Misericórdia, que faz canto de uma banda e parte da outra banda com quem de direito for

AN, 1ON, 47
Data - 1665
Descrição
Escritura de venda de uma morada de casas que fazem Antonio Lopes e sua mulher a João Barbosa, no valor de 22 réis - térrea, de taipa de pilão, coberta de telhas, sita no bairro da Misericórdia, partindo de uma banda com casas de Domingos Gomes ... e da outra faz canto, havida por legítima.
Observações
Data: ?/7/1665

AN, 1ON, 47, p. 37v
Data - 1665
Descrição
Escritura de venda da quarta parte de uma morada de casas que fazem Francisco Machado de Aguiar e sua mulher Margarida Ferreira de Melo ao Capitão Francisco Teles Barreto, no valor de 150 réis - de sobrado, com altos e baixos, de pedra e cal, coberta de telhas, sita no canto onde foi o paço do Sargento-mor, havida por pagamento que a ele fizera seu irmão Manoel ... Machado.

AN, 1ON, 47, p. 44
Data - 1665
Descrição
Escritura de venda de uma morada de casas que faz o reverendo padre Vicente de Leão a Francisco Álvares, no valor de 200 réis - térrea, de pedra e cal, sita na rua que vai para São Francisco, partindo de uma banda com casas de Simão de Souza e da outra com casas de João de Castilho Pinto, comprada aos herdeiros de Lourenço Dias em 16/5/1659.

AN, 1ON, 47, p. 51
Data - 1665
Descrição
Escritura de dote de casamento que faz o Capitão João Batista Jordão a João de Campos de Matos, para casar-se com sua filha Isabel de Amaral – Dentre outros bens, uma morada de casas de sobrado, sita na rua Direita, no canto de Nossa Senhora do Carmo, comprada ao General Salvador Correia de Sá [em 28/11/1662 – 1º Ofício]
Preço

AN, 1ON, 47, p. 55v
Data - 1665
Descrição
Escritura de venda de uma morada de casas a retro aberto que fazem Luiz Gomes Sardinha e sua mulher Assença de Andrade ao Capitão Feliciano da Silva, no valor de 201 réis – Dizem que devem 134$330 ao Capitão Feliciano da Silva. Em pagamento vendem a retro aberto a ele dito Feliciano uma morada de casas térrea, de pedra e cal, com uma parede da banda do quintal de pedra e barro, sita na rua do Licenciado Domingos Coelho, partindo de uma banda com Eusébio Dias Cardoso e da outra com Leonor Morgada e Marcos Chofre(?).


AN, 1ON, 47, p. 80v
Data - 1666
Descrição
Escritura de dote que faz Dona Helena do [Souto Maior], viúva do Capitão Inácio de Andrade [Machado], à sua neta Helena do Zouro, filha de sua filha [Antonia] de Andrade e do Sargento-mor João Rodrigues Pestana – Diz que, para ajudar sua neta a tomar estado, doa uma morada de casas de sobrado, altos e baixos, sita na rua Direita desta cidade, onde vive Manoel Rodrigues Ribeiro, que parte de uma banda com casas de Domingos Ribeiro, defunto, e da outra com casas de Juliana Ramires, que está empenhada ao dito Manoel Rodrigues Ribeiro ...
Observações
Data: ?/1/1666.


AN, 1ON, 47, p. ?
AN, 1ON, 47, p. 105
Data - 1666
Descrição
Escritura de dinheiro a juros com hipoteca de uma morada de casas que faz Antonio de Leão, devedor, a Domingos Francisco, no valor de 25 réis – em que mora, sita na travessa da Candelária.

Data - 1666
Descrição
Escritura de venda de um engenho, com pagamento parcial de uma morada de casas, que faz o Capitão Bento Pinheiro de Lemos ao Capitão Francisco de Moura Fogaça, no valor de 12000 cruzados – de fazer açúcar, de invocação São Bento, sito em Mutuá.
Observações
12.000 cruzados. Pagos em parte por uma morada de casas sita na rua Direita, defronte da igreja de São José, partindo de uma banda com casas do Reverendo Prelado Doutor Manoel de Souza de Almada e da outra com casas dos reverendos padres da Companhia, avaliada em 600$000. Escritura não teve efeito

AN, 1ON, 47, p. 109v
Data - 1666
Descrição
Escritura de venda de duas moradas de casas a retro aberto que faz Diogo Mendes Coluna, por si e como procurador de seu irmão Francisco da Costa ..., a Manoel Soares Rubina e Manoel Rodrigues Cruz, no valor de 220 réis  – de taipa de pilão, de sobrado, altos e baixos, cobertas de telhas, sitas na rua Direita desta cidade, defronte da igreja da Cruz.

AN, 1ON, 47, p. 147v
Data - 1666
Descrição
Escritura de venda de uma morada de casas que faz Manoel Vieira da Costa a Domingos Francisco, no valor de 60 réis – térrea, de taipa de mão, coberta de telha, erguida em 5 braças de chãos de testada e 11 (ou 20) de fundos, sita defronte do cruzeiro de São Francisco, que por uma banda faz canto e pela outra parte com chãos dele vendedor.

AN, 1ON, 47, p. 159v
Data - 1666
Descrição
Escritura de venda de uma morada de casas que fazem Antonio Lopes Dias e sua mulher Angela Pacheca a João Barbosa, no valor de 22 réis – térrea, de taipa de pilão, coberta de telha, sita no bairro da Misericórdia, que parte por uma banda com casas de Domingos Gomes e da outra faz canto, havida pela vendedora por sua legítima, por falecimento de sua mãe Maria ...
Observações
Data: ?/7/1666.

AN, 1ON, 47, p. 165v
Data - 1666
Descrição
Escritura de dinheiro a juros com hipoteca de uma morada de casas que faz Dona Isabel Cabral ao Juízo dos Órfãos, no valor de 140 réis – de sobrado, sita na rua que chamam do Gadelha, que parte de uma banda com casas de Diogo Mendes Coluna e da outra com casas do General Salvador Correia de Sá e Benevides.
Observações
Data: 9-13/7/1666.


AN, 1ON, 47, p. 180v
Data - 1666
Descrição
Escritura de venda de chãos que fazem Domingos ... e sua mulher .... a Manoel Cardoso Leitão, no valor de 20 réis  – com cinco braças de testada, sitos na rua de Gaspar de Carvalho, que partem de uma banda com casas de Francisco de Souza(?) Coutinho e da outra com casas de Manoel Cardoso Leitão, genro do dito Gaspar de Carvalho, ... por escritura de patrimônio que dos ditos chãos lhe fizeram Gaspar de Carvalho e sua mulher Maria de Mendonça em 22/4/1651 [1º Ofício].
Observações
Data: 9-13/9/1666.


AN, 1ON, 47, p. 184v
Data - 1666
Descrição
Escritura de venda de uma morada de casas que fazem Manoel Fernandes Miranda, mercador, e sua mulher Beatriz da Paz a Fernão Vaz Pereira [homem de negócio], no valor de 400 réis – térrea, de pedra e cal, sita na praça desta cidade, da banda da praia, foreira à Câmara em 2$660 anuais, comprada a Francisco Fernandes de Mesquita, como procurador bastante de seu irmão Gaspar Dias de Mesquita em 11/5/1652 [2º Ofício].
Preço
400 Réis
Código

AN, 1ON, 48, p. 1
Data - 1668
Descrição
Escritura de dote de casamento que fazem o Capitão Antonio Pereira Lobo e sua mulher Dona Ana da Silva a Julião Rangel da Silva, filho do Capitão João Correia da Silva, para casar-se com sua sobrinha Dona Isabel de Vasconcelos, filha de seu irmão e cunhado Capitão Manoel Pereira Lobo, que Deus tem, e de sua mulher Dona Ana Maria – dentre outros bens, seis braças de chãos sitos na rua dos Pescadores, para neles fazerem casas de canto ... do dito canto, indo para a Prainha, herdados de seu pai e sogro Sebastião Lobo Pereira e por compra que fizeram a seu irmão e cunhado Manoel Pereira Lobo

AN, 1ON, 48, p. 23
Data - 1668
Descrição
Escritura de doação de uma morada de casas para instituição de patrimônio que faz Luíza Pedrosa a seu filho João Pereira, no valor de 150 réis - térrea, coberta de telha, com três braças de chãos de testada e 12 de fundos, com fronteira de parede de adobes e a parede do meio e as outras das ilhargas de parede de pau-a-pique feitas ao moderno ... e alicerces de pedra e barro, onde ela atualmente vive, sita na rua que chamam de Inácio Castanheira, partindo de uma banda com Antonio Freitas(?) e da outra com chãos de um parente(?) de Antonio Barbosa Calheiros, comprada ao dito Antonio Barbosa Calheiros,.



AN, 1ON, 48, p. 28v; AGCRJ, Códice 42-3-56, p. 77
Data - 1668
Descrição
Escritura de venda de uma morada de casas que faz Domingos Dias a Miguel Carrasco, no valor de 130 réis - térrea, de taipa de mão, coberta de telhas, que está em um dos cantos que estão defronte de outras de sobrado, de pedra e cal, que chamam de Helena do Souto, partindo de uma banda com casas de Guiomar Gondim, a castelhana, e da outra com a rua que vai para o campo chamada de Pedro da Costa, comprada a Jorge de Souza, o moço.

AN, 1ON, 48, p. 34v; AGCRJ, Códice 42-3-56, p. 78
Data - 1668
Descrição
Escritura de venda de chãos que fazem o Capitão Manoel do Rego da Silva e sua mulher Isabel Viçosa a Domingos de Oliveira, carpinteiro, no valor de 72 réis – com 6,5 braças de testada, sitos por detrás de cinco moradas de casas que foram de Antonio Vaz Viçoso, que Deus tem ..., com 16,5 de sertão, partindo com .... e nos fundos com a parede das casas de Domingos Garcia, ferreiro, que partem com a parede das casas de Antonio Vaz Viçoso, o moço, chãos havidos por folha de partilha do dito seu pai e sogro Antonio Vaz Viçoso.

AN, 1ON, 48, p. 54; AGCRJ, Códice 42-3-56, p. 79
Data - 1668
Descrição
Escritura de venda de uma morada de casas que fazem João de Abreu de Oliveira e sua mulher Felipa Soares a João da Costa, oficial de calafate, no valor de 70 réis - térrea, de taipa de mão, coberta de telhas, sita na rua nova de detrás da rua de São Bento, partindo de uma banda com ... dos vendedores e da outra com chãos dos herdeiros de João Velho Prego, comprada a seu sogro e pai, Capitão Miguel de Abreu Soares.

AN, 1ON, 48, p. 65v
Data - 1668
Descrição
Escritura de dote de casamento que faz Ana Pinta, viúva de Antonio Fernandes Lugo, a seu genro Antonio Álvares e sua filha Maria Cardosa – além de outros bens, doa três braças de chãos de testada, sitos na rua em que ela doadora vive, que partem com outros chãos do dito seu genro e filha por uma banda, e pela outra com casas de mim tabelião, que lhe couberam na meação dos bens de seu marido

AN, 1ON, 48, p. 82; AGCRJ, Códice 42-3-56, p. 83
Data - 1668
Descrição
Escritura de venda de uma morada de casas que fazem Domingos Rodrigues de Lisboa e sua mulher Joana de Araújo a Antonio Bogado de Mendanha Souto Maior, no valor de 600 réis - de sobrado, de pedra e cal, coberta de telhas, com seu quintal cercado de parede de pedra e cal, sita na rua que chamam de Gregório Mendes, partindo de uma banda com casas do Capitão Manoel de Gouveia e da outra com casas de Cristóvão Osório Dantas, obtida por dote de casamento de seu sogro e pai Francisco de Araújo, meirinho do mar, em janeiro de 1665.

AN, 1ON, 48, p. 85v; AGCRJ, Códice 42-3-56, p. 84
Data - 1668
Descrição
Escritura de venda e trespasso de uma morada de casas que fazem o Capitão Francisco Teles Barreto, juiz dos órfãos, e sua mulher Dona Inês [de Andrade] ao Licenciado Domingos Coelho Valadares, no valor de 215 réis - térrea, de pedra e cal, coberta de telhas, sita na rua que chamam de Maria de Araújo, partindo com casas de Roque Fernandes Barrocas de uma banda e com casas de Bernardo de Araújo Calheiros de outra, e pelos quintais com casas do comprador, comprada a André da Rosa e sua mulher Isabel Pina em 20/10/1668.
Observações
Preço: o mesmo da compra de 20/10: 215$000



AN, 1ON, 48, p. 89; AGCRJ, Códice 42-3-56, p. 85
Data - 1668
Descrição
Escritura de venda de uma morada de casas que fazem Manoel Rodrigues Arronches e sua mulher Catarina Soares a Domingos Rodrigues de Lisboa, no valor de 600 réis - térrea, de pedra e cal, sita na rua Direita que vai para São Bento, partindo de uma banda com casas de sobrado do Capitão Domingos Árias [de Aguirre] e da outra com chãos de Domingos Rodrigues Resende, com quintal até o mar e parede separando-a dos confrontantes laterais, havida por compra de Francisco Gomes Guedes.



AN, 1ON, 48, p. 120; AGCRJ, Códice 42-3-56, p. 93
Data - 1669
Descrição
Escritura de venda de chãos que faz Antonia Tavares de Oliveira, viúva do Sargento-mor João Velho Prego, a Domingos Rodrigues Resende, no valor de 60 réis – com seis braças de testada e 10 de quintal, sitos por detrás das casas de Maria da Cunha, sua mãe, já defunta, fazendo canto com a travessa que vai para a rua onde esteve o açougue de Mariano de Linhares, partindo pela outra banda com chãos do Capitão Francisco de Lemos Peixoto, chãos havidos por dote de casamento em 25/11/1642.


AN, 1ON, 48, p. 158; AGCRJ, Códice 42-3-56, p. 98
Data - 1669
Descrição
Escritura de venda de uma morada de casas que faz João de Azevedo a Catarina Simões, no valor de 130 réis- térrea, de taipa de mão, sita na rua que chamam de Diogo de Ávila, partindo de uma banda com casas e chão de Manoel Martins e da outra com chãos e casas da Santa Casa da Misericórdia.



AN, 1ON, 48, p. 164; AGCRJ, Códice 42-3-56, p. 98
Data - 1669
Descrição
Escritura de venda de uma morada de casas que fazem Gonçalo Correia Pinto e sua mulher Isabel da Cruz a Pero Gomes de Sepúlveda, no valor de 100 réis - térrea, de taipa de pilão, coberta de telhas, com câmara e quintal, sita na rua de Nossa Senhora do Parto, partindo de uma banda com casas de sua sogra Maria Leitoa e da outra com casas da Misericórdia que foram de Grácia Nunes, com quintal até entestar com a fortaleza de São Sebastião.

AN, 1ON, 48, p. 169; AGCRJ, Códice 42-3-56, p. 100
Data - 1669
Descrição
Escritura de venda de parte de uma morada de casas que faz Sebastião Álvares Senra a Francisco Dias [Medonho?], no valor de 150 réis - com salas, duas câmaras no mesmo andar, uma varanda e seu corredor, sita na rua de Domingos de Freitas, partindo de uma banda com casas da sogra de Miguel de Freitas e da outra com ...



AN, 1ON, 48, p. 171v
Data - 1669
Descrição
Escritura de doação de uma morada de casas para instituição de patrimônio que fazem Matias Gonçalves, cavaleiro do hábito de Cristo, e sua mulher Bárbara da Cunha a seu filho Manoel Gonçalves – uma morada de casas de dois sobrados, de pedra e cal, coberta de telha, sita na rua Direita, com sua sala, corredor e câmaras, que parte de uma banda com Antonio Gomes e da outra com Maria da Cunha, já viúva


>>>>>>>>>>>>>>>>>>>>>>>>>Data – 1669<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Descrição
Escritura de dote de casamento que faz Isabel da Fonseca, viúva de Francisco Freire da Fonseca, ao Capitão Manoel Cardoso Castelo, casado com sua filha Isabel da Fonseca - uma morada de casas térrea, de pedra e cal, coberta de telhas, com sala, câmara e seu corredor, com quintal murado de pedra e cal, sita na rua que foi de João Pereira [Bacelar], partindo de uma banda com casas de Matias Gonçalves e da outra com casas dos reverendos padres da Companhia em que ora vive Sebastião Martins, cirurgião do presídio, havida por morte de seu marido



AN, 1ON, 48, p. 182
Data - 1669
Descrição
Escritura de venda de uma morada de casas que fazem o Capitão Manoel Cardoso Castelo e sua mulher Isabel Freire da Fonseca a Valério Negrão, no valor de 220 réis – térrea, de pedra e cal, coberta de telha, com sala, câmara e seu corredor, sita na rua de João Pereira Bacelar, havida por dote de casamento de sua mãe e sogra Isabel da Fonseca.



AN, 1ON, 48, p. 189; AGCRJ, Códice 42-3-56, p.103
Data - 1669
Descrição
Escritura de venda de uma morada de casas que faz o Capitão André Ferreira, como procurador de Duarte Ferreira e de sua mulher Maria Álvares Pinta, a Manoel Soares, no valor de 32 réis - de adobes, coberta de telhas, com sala, câmara, corredor e quintal, sita na rua de Domingos Rodrigues quando vão por baixo de São Francisco, partindo de uma banda com casas de Maria Rodrigues e da outra com chãos do comprador.

AN, 1ON, 48, p. 192
Data - 1669
Descrição
Escritura de venda da parede de uma morada de casas que faz Diogo de Sá da Rocha a Jerônimo de Matos de Castilho, no valor de 12 réis – de sobrado, de pedra e cal, sita na rua que vai para São Bento(?).



AN, 1ON, 49, p. 25; AGCRJ, Códice 42-3-56, p. 114
Data - 1669
Descrição
Escritura de venda de uma morada de casas que faz Dona Brites de Lemos, viúva do Governador Agostinho Barbalho Bezerra, ao Capitão João Fernandes Pedra, no valor de 1425.52 réis - de dois sobrados, de pedra e cal, sita na rua que chamam do Gadelha, partindo de uma banda com casas onde ora vive o Capitão Manoel de Gouveia e da outra com os terreiros que são de Manoel da Silva.

AN, 1ON, 49, p. 34v; AGCRJ, Códice 42-3-56, p. 118
Data - 1669
Descrição
Escritura de venda de uma morada de casas que faz Domingos Garcia a Domingos Fernandes Coelho, no valor de 120 réis - de taipa de mão, coberta de telhas, com sala, câmara, corredor e quintal, partindo de uma banda com casas de Gonçalo Gonçalves e da outra com casas de Manoel Machado, arrematada em praça pública..
Preço
120 Réis
Código



AN, 1ON, 49, p. 57v; AGCRJ, Códice 42-3-56, p. 121
Data - 1669
Descrição
Escritura de venda de chãos que faz Ana Pinta, viúva de Antonio Fernandes Lugo, a Antonio Ferreira Rios, no valor de 24 réis – com seis braças de testada, sitos na rua que chamam de Gaspar de Carvalho, que começam a medir depois de 5 braças que pertencem aos herdeiros de Antonio Gonçalves ..., comprados à mãe da vendedora, Isabel de Souza, e partem da outra banda, depois de medidas as 6 braças, com chãos de sua filha e genro Antonio Álvares e Maria dos Reis.

AN, 1ON, 50, p. 2; AGCRJ, Códice 42-3-56, p. 126
Data - 1670
Descrição
Escritura de venda de metade de uma morada de casas que faz Tomé de Souza a Luiz Nogueira, no valor de 55 réis - térrea, coberta de telhas, sita na travessa de Matias Gonçalves, o ferreiro da praia, partindo de uma banda com Domingos de Araújo e da outra com a rua que vai para São Bento, até entestar com umas casas de sobrado de Antonio de Faria.


AN, 1ON, 50, p. 3; AGCRJ, Códice 42-3-56, p. 126
Data - 1670
Descrição
Escritura de venda de chãos que fazem Dom Luiz [Reinoso] Queixada e sua mulher Maria [Peixota] a Manoel Rodrigues Salvado – com três braças de testada, sitos na rua dos Pescadores, partindo de uma banda com chãos de José da Costa e da outra com casas de Dom José Rendon [y Quevedo, cunhado dos vendedores].

AN, 1ON, 50, p. 5v
Data - 1670
Descrição
Escritura de pagamento e quitação que faz Antonio Maciel Tourinho a sua irmã Vitória Maciel – sobre uma morada de casas sita na rua Direita, junto às casas de Juliana ..., em que a dita sua irmã ...

AN, 1ON, 50, p. 13
Data - 1670
Descrição
Escritura de venda de uma morada de casas a retro aberto que faz João ... a Francisco Rabelo, barbeiro, no valor de 45 réis – térrea, coberta de telha, com sala, câmara e quintal, sem localização.



AN, 1ON, 50, p. 14; AGCRJ, Códice 42-3-56, p. 127
Data - 1670
Descrição
Escritura de venda de uma morada de casas que faz o Licenciado Padre Sebastião Caldeira a Mateus de Moura Fogaça, no valor de 300 réis - de pedra e cal, cobertas de telha, com sala, câmara, corredor e varanda e quintal cercado de muro de pedra e barro, na rua de São José, partindo de uma banda com casas de Dona Inês da Costa, irmã do vendedor, e da outra com casas de Diogo Fagundes, cunhado do vendedor. Venda inclui obrigação de capela de missas.
Observações
O pagamento é feito com compensação de pagamentos anteriores, informando-se que fora feito um pagamento por Dona Úrsula da Costa, irmã dele vendedor e mulher que foi do Capitão Mateus de Moura Fogaça, procedido da compra que fez o Capitão Mateus de Moura Fogaça, já defunto seu marido, ao Capitão João de Moura Fogaça, já defunto, pai do dito comprador, do engenho que possuía na Pabuna, da qual quantia davam o Padre Sebastião Caldeira e sua irmã Dona Úrsula da Costa quitação ao comprador
AN, 1ON, 41; AGCRJ, Códice 42-3-57, p. 310
Data - 1653
Descrição
Escritura de venda de um lanço de casas que fazem Pedro Gomes Sepúlveda e sua mulher Domingas Carvalha a Lourenço Dias, no valor de 250 réis – [duas moradas] térreas, cobertas de telhas, de pedra e cal, com todas as câmaras, varanda e quintal, [sitas na rua de Manoel Ribeiro acima, indo para Santo Antonio à mão esquerda], partindo de uma banda com casas do Padre João de Bastos e da outra com Simão de Souza, compradas a Baltazar Leitão [em 11/3/1636 – 1º Ofício].
 
In: MMoraes, Crgeral, p. 203-206
Data - 1653
Descrição
Escritura de medição judicial de chãos doados por Frei Crispim da Cunha ao Convento de Nossa Senhora do Carmo - 60 braças em quadra, em que mais tarde seria construída a "cerca" do Convento da Ajuda
Observações
Em 5/6/1653, quando foi medido judicialmente, começava "do sítio das casas que foram de Sebastião Baldez, donde se meteu um marco de pedra de cantaria, que tem um C. e um R., e do dito marco se começou a medir a testada, até entestar com a Lagoa, onde se meteu outro marco com as mesmas letras; e daí se fez a quadra, e se foram medindo as 60 braças, e no cabo delas, se veio buscar o travessão do primeiro marco, e se foram medindo outras 60 braças, pela fralda do outeiro acima....". Terreno foi vendido pelos carmelitas em 3/9/1750

AN, 1ON, 41, p. 122; AGCRJ, Códice 42-3-57, p. 317
Data - 1653
Descrição
Escritura de venda de uma morada de casas que faz Úrsula de Magalhães, viúva do Capitão Antonio Gonçalves, a Gaspar de Azevedo, no valor de 55 réis - térrea, de taipa de mão, coberta de telhas, com sala, câmara e quintal, sita em Vila Verde, partindo com Gaspar de Azevedo de uma banda e com o muro dos Padres de São Bento da outra.

AN, 1ON, 41, p. 122v ; AGCRJ, Códice 42-3-57, p. 318
Data - 1653
Descrição
Testamento de Gabriel Gomes, lançado na nota deste ofício de notas por mandado de justiça – Diz que é casado com Grácia Maciel, da qual não teve filho. Declara que tem um partido de canas em Serapoy. Declara que tem seis braças de chãos na rua que vai para Nossa Senhora da Conceição com 14 de quintal. Declara que tem 7 peças do gentio de guiné

AN, 1ON, 41, p. 140; AGCRJ, Códice 42-3-57, p. 320
Data - 1653
Descrição
Escritura de distrato de uns chãos que faz Manoel Garcez e Gralha com Manoel Ribeiro Caldeira – sobre uns chãos sitos no caminho que vai dar na praia da Carioca, que começam onde acaba a data dos Alvarengas. Por esta escritura dá de volta ao dito Manoel Ribeiro Caldeira o valor de 18$000, pelos quais havia comprado os chãos
Preço
Código

AN, 1ON, 41, p. 141v; AGCRJ, Códice 42-3-57, p. 320
Data - 1653
Descrição
Escritura de venda de umas moradas de casas que fazem Sebastião Pinto e sua mulher Madanela Sardinha a Manoel Soares Rubina, no valor de 273 réis - dois lanços de casas térreas, sitas na rua dos Pescadores, partindo de uma banda com casas de Francisco Dias Frade e da outra com casas de Francisco Pinto Pereira, havidas de seu sogro e pai Manoel André [um Manoel André testemunha para os beneditinos em 1611, confirmando serem eles possuidores das terras da Prainha - SNigra, CAMSBRJ, p. 26*).


AN, 1ON, 41, p. 144v
Data - 1653
Descrição
Escritura de venda de uma morada de casas que fazem Antonio da Silva Lobo e sua mulher Inês da Luz da Conceição a Domingas da Silveira, no valor de 300 réis - térrea, de pedra e cal, sita na rua da Candelária, partindo de uma banda com Domingos Grácia e da outra com Domingos da Silveira. Vendem também mais três braças de chãos de testada (acho que na mesma rua), que partem com Jerônimo Luz Teixeira. Vendem também quatro ilhas que estão entre Paquetá e Tomé Soares que se chamam Jerobaíba(?).

AN, 1ON, 41, p. 147v
Data - 1653
Descrição
Escritura de venda de um lanço de casas que faz José Nogueira Passos, como procurador(?) dos reverendos padres de Santo Antonio, a .... , no valor de 140 réis - térreas, de taipa de pilão, cobertas de telhas, sitas na rua que vai para Santo Antonio, partindo de uma banda com casas de Pascoal Sardinha e da outra com casas de Maria Ribeiro, deixadas de esmola por André Simões aos padres de Santo Antonio após a sua morte, de quem o dito José Nogueira as havia comprado.

AN, 1ON, 41, p. 148; AGCRJ, Códice 42-3-57, p. 321
Data - 1653
Descrição
Escritura de venda de um lanço de casas de sobrado que fazem Domingos Pimentel de Abreu e sua mulher Sebastiana Martins ao Capitão Antonio Juzarte de Almeida, no valor de 500 réis – de sobrado, de pedra e cal e de taipa de pilão, sitas na rua de Duarte Correia, partindo de uma banda com o Capitão Manoel Caldeira Soares e da outra com casas térreas de Antonio Rodrigues, havidas por dote de casamento.

AN, 1ON, 41, p. 157; AGCRJ, Códice 42-3-57, p. 320
Data - 1653
Descrição
Escritura de doação de uma morada de casas para instituição de patrimônio que faz o Capitão Clemente Nogueira da Silva a José Vieira de Melo, para tomar ordens sacras - térrea, de pedra e cal, sita defronte do mar, na rua que vai direito para a Misericórdia, partindo de uma banda com casas de sobrado dele doador, em que de presente vive, construída em 24 palmos de chãos, com sala e, para dentro, uma câmara e despensa e quintal que lhe toca até o trasto da calçada que vai para o Colégio, e com a testada até o mar
Observações
Um Clemente Nogueira da Silva foi nomeado capitão do forte de S. João em 26/8/1635 - ABN, 39, p. 15

AN, 1ON, 41, p. 162v ; AGCRJ, Códice 42-3-57, p. 324
Data - 1653
Descrição
Escritura de empenho de uma morada de casas que faz Inocêncio Correia a Miguel Pedroso – de taipa de ..., sita na rua que vai para Nossa Senhora da Conceição [depois dos Pescadores], que parte com André Alves e Francisco Gomes Sardinha, pela quantia de 60$000

AN, 1ON, 41, p. 166; (AGCRJ, Códice 42-3-57, p. 325
Data - 1653
Descrição
Escritura de venda de chãos que fazem José de Frias e sua mulher Assença de Andrade, moradores na rua de Pedro da Costa, a Sebastião de Oliveira, no valor de 60 réis – com seis braças de testada, sitos na rua que vai para a Misericórdia, que começam da porta da cidade para a banda da cidade, havidos por compra de André Tavares.
Observações
60$000, pagos em um moleque do gentio de guiné (42$000) e o restante em dinheiro. Informação de 20/10/1653: "Declaro que os bens que possuo de raiz são os seguintes: duas moradas de casas de sobrado na rua Direita, de pedra e cal, em que vivo, livres e isentas, que partem com as casas dos herdeiros de Simão Rodrigues do Prado, já defunto, e pelo quintal com casas dos padres da Companhia e de Gregório Gonçalves [A segunda casa, ao que parece, parte pelo quintal com casas de Domingos de Araújo, falecido em 28/2/1652, fundador da capela de São Domingos, na banda dalém [Pizarro, III, pp. 158, 269].... Declaro que tenho na rua do Capitão Mateus de Freitas uma morada de casas terreiras, de taipa de mão, que partem de uma banda com casas de Gregório Lopes e da outra banda com casas de D. José Teruin .. E declaro que comprei a Manoel Rodrigues Cardoso, no fundo do quintal destas ditas casas, três braças de chão de toda a largura das casas do dito Manoel Rodrigues Cardoso, como consta da escritura que me fez..... Declaro que tenho 4 braças de chãos na rua do Padre Pedro Homem Albernaz, que chegam à rua de Brás Pa. (Pereira?), e partem de uma banda com casas do Padre Francisco Gomes [da Rocha] e da outra com chãos dos herdeiros de Álvaro Pires, como consta da escritura.... Declaro que tenho um lanço de casas de pedra e cal repartido em 3 moradas no canto da rua dos Pescadores, partindo com casas de Sebastião Pinto ..." (Testamento de Francisco Dias Frade, de 20/10/1653, Apud SILVA-NIGRA, Clemente Maria da. Construtores e artistas do Mosteiro de São Bento do Rio de Janeiro. Salvador: Tip. Beneditina, 1950, p. 245*).


AN, 1ON, 41, p. 177; AGCRJ, Códice 42-3-57, p. 327
Data - 1653
Descrição
Escritura de venda que faz João Dias da Costa [filho de Francisco Dias Frade], como procurador de Diogo Vaz de Escobar, a Manoel Soares, no valor de 180 réis - dois lanços de casas térreas, de taipa de mão, cobertas de telhas, sitas na rua dos Pescadores, partindo de uma banda com casas de Manoel Soares e da outra com casas de Simão ...

AN, 1ON, 41, p. 178; AGCRJ, Códice 42-3-57, p. 320
Data - 1653
Descrição
Escritura de venda de uma morada de casas a retro aberto que faz Inocêncio Correia a Antonio Furtado, no valor de 144 réis - de taipa de mão, com sua sala e câmara, e seu quintal, sita na várzea desta cidade, [na rua dos Pescadores] partindo com casas de Constantino Cardoso e de Gonçalo de Ponte [Gonçalo de Pontes de Labrit?].

AN, 1ON, 41, p. 185; AGCRJ, Códice 42-3-57, p. 320
Data – 1653
Descrição
Escritura de venda de chãos que fazem Eusébio Dias Cardoso e sua mulher Francisca da Costa [Homem] ao Doutor Francisco da Fonseca Diniz, no valor de 80 réis – com três braças de testada, com casa já começada a construir, sitos na rua do Padre Pedro Homem Albernaz, partindo de uma banda com os filhos de Diogo Mendes Coluna e da outra com Maria de Araújo, havidos por dote.

AN, 1ON, 41 ; AGCRJ, Códice 42-3-57, p. 330
Data - 1653-12-02
Descrição
Escritura de recompra de uma morada de casas vendida a retro aberto que fazem Matias Gonçalves e sua mulher Bárbara da Cunha a Francisco Lopes, no valor de 430 réis - térrea, coberta de telhas, com sala, câmara, varanda e seu quintal, sita na travessa e rua da Candelária, partindo de uma banda com Sebastião Gomes e da outra com Manoel Dias
Preço
430 Réis
Código

AN, 1ON, 41, p. 193 ; AGCRJ, Códice 42-3-57, p. 330
Data - 1653
Descrição
Escritura de venda de chãos que faz o Capitão João Gomes Sardinha, capitão-mor do distrito de Casserebu, por si e como procurador de sua mulher Margarida Antunes, ao Capitão Antonio Correia, no valor de 60 réis – com seis braças de testada e 14 de quintal, que partem de uma banda com casas de Antonio Correia e da outra com casas dos herdeiros de Manoel Ribeiro, comprados a Manoel da Costa.


AN, 1ON, 41, p. 200v; AGCRJ, Códice 42-3-57, p. 331
Data - 1654
Descrição
Escritura de doação de dois lanços de casas para instituição de patrimônio que fazem Sebastião Gonçalves e sua mulher Margarida da Silva a Francisco Pereira da Silva, a fim de se ordenar de ordens sacras, no valor de 160 réis - de taipa de mão, cobertas de telhas, com suas câmaras, varandas e quintais, sitas no bairro da Misericórdia, da porta da cidade para dentro, partindo de uma banda com Marcos de Azeredo e da outra com Mateus Antunes.

AN, 1ON, 41, p. 209v; AGCRJ, Códice 42-3-57, p. 329
Data - 1654
Descrição
Escritura de venda de uma morada de casas que faz Heitor de Barros Pereira ao Capitão Gaspar de Mariz de Almeida, no valor de 120 réis - de sobrado, danificada, sita no bairro da Santa Misericórdia, herdada de seu pai.

AN, 1ON, 41, p. 212v
Data - 1654
Descrição
Escritura de concerto e composição que faz Bento Garcez [de Araújo], como procurador de sua mãe Maria da Silveira, [segunda mulher e] viúva de Bento Garcez, o velho, com Antonio Pereira [Sarmento] e sua mulher Antonia da Costa [filha do primeiro casamento de Bento Garcez, o velho] – O casal diz que por falecimento de seu sogro e pai [em 17/11/1651 – Rheingantz, II, p. 224] pretendiam herdar seu quinhão de herança. Por esta escritura, ficam com seis braças de chãos sitos na rua de Inocêncio Correia [depois dos Pescadores], com 10 braças de quintal, que foram avaliados em 35$000, os quais chãos partem de uma banda com três braças que são de uma órfã de João de Souza por nome Joana de Souza ... em casa de Domingos da Silveira, e da outra com chãos de Dona Luiza, moradora em São Paulo


AMSBRJ, Seção 2, Nº 78; AMSBRJ, Estados do Mosteiro, Vol. 1, Parte 1, p. 47
Data - 1654
Descrição
Mosteiro de São Bento herda por cabeça de seu religioso Frei Mauro de Assunção, filho de Francisco Dias Frade, três moradas de casas térreas, sem quintal, sitas na rua da Candelária [que em 1766 eram duas terreiras com seus sótão e uma de sobrado], que principiam no canto da rua da Candelária com a dos Pescadores, avaliadas em 600$000 e rendem a cada ano 46$000. Herda também uma morada de casas térrea à rua da Alfândega, indo para o campo à mão direita. Herda também quatro braças de chãos na rua de Santa Rita, indo para o Parto à mão esquerda, fazendo fundos para a rua Nova das Flores (chegam até aí), avaliados em 10$000

AN, 1ON, 41, p. 218
Data - 1654
Descrição
Escritura de concerto e composição que fazem Manoel Garcez e sua mulher Leonor Bentes com Bento Garcez [de Araújo], como procurador de sua mãe Maria da Silveira, viúva de Bento Garcez, o velho – Por esta escritura, o casal herda os bens que lhe cabiam por morte de Bento Garcez, dentre os quais estavam 6 braças de chãos de testada por 10 de quintal, sitos na rua de Inácio Duarte de Leão, que foi Juiz dos Órfãos, que partem de uma banda com chãos de uma órfã filha de João de Souza, por nome Joana de Souza, e da outra com chãos de Dona Luiza, moradora em São Paulo

AN, 1ON, 42, p. 32v; AGCRJ, Códice 42-3-57, p. 227
Data - 1654
Descrição
Escritura de venda de uma morada de casas que faz Lourenço Dias ao Padre Vicente de Leão, no valor de 250 réis - térrea, de pedra e barro e adobes, sita na rua que vai para São Francisco, partindo de uma banda com casas de Simão de Souza e da outra com casas de Mariana de Souza, comprada a Pero Gomes, o surdo, e sua mulher Maria Caldeira.

AN, 1ON, 42, p. 35; AGCRJ, Códice 42-3-57, p. 228
Data - 1654
Descrição
Escritura de venda de chãos que faz André Velho de Araújo ao Capitão Mateus de Moura Fogaça, no valor de 160 réis – com três braças de testada e 11 de quintal, sitos na rua Direita, partindo de uma e de outra banda com Jerônimo Camelo de Sampaio, e o quintal entestando com o quintal de Ana Barbosa, comprados a Álvaro Barreto.

AN, 1ON, 42, p. 94
Data - 1654
Descrição
Escritura de venda de uma morada de casas que fazem Manoel da Mota e sua mulher Úrsula Ribeira, e Manoel Pereira e sua mulher Grácia de Siqueira, aos reverendos padres da Companhia, no valor de 2000 cruzados - de sobrado, de pedra e cal, com seus altos e baixos, com quintal cercado de muro de pedra e cal, sita na rua do Padre Manoel de Araújo, havidos por partilha dos bens de seu pai e sogro Gaspar Gonçalves e de sua mulher .... Ribeira, partindo de uma banda com casas térreas de Gonçalo Ferreira, caldeireiro,e da outra com casas de Pero Mendes, caldeireiro.

AN, 1ON, 42, p. 101; AGCRJ, Códice 42-3-57, p. 201
Data - 1654
Descrição
Escritura de dote de casamento que fazem Domingos Rodrigues Resende e sua mulher Mécia Bareina (ou Barreira) a Vicente Álvares, por se casar com sua filha Joana Rodrigues – além de outros bens, doam uns chãos na praia, que partem de uma banda com Matias Gonçalves e da outra com os filhos de Jorge de Souza, foreiros à Câmara

AN, 1ON, 42, p. 119; AGCRJ, Códice 42-3-57, p. 207
Data - 1654
Descrição
Escritura de venda de chãos que faz Isabel Martins, viúva de Domingos Rodrigues Lamego, a Lourenço Gonçalves, no valor de 5 réis – com cinco braças de testada e o sertão que lhe pertencer, conforme as cartas de sesmaria, os quais herdara de seu pai Bastião Gil, sitos na várzea de Santo Antonio e Nossa Senhora da Ajuda, partindo de uma banda com chãos de Domingas Pereira, viúva, e da outra com chãos do Capitão Belchior da Fonseca, chãos havidos por troca de outros chãos de três braças sitos no bairro da Misericórdia, feita com João Gomes Sardinha e sua mulher Maria Freire [conforme escritura do tabelião Antonio Pimenta de Abreu].

AGCRJ, Códice 2-4-9, p. 38; ADF, 2, 267-268
Data - 1654
Descrição
Escritura de dinheiro a juros com hipoteca de metade de uma morada de casas que faz Bartolomeu de Amorim Calheiros, como testamenteiro de Gaspar Fernandes Clemente, a Manoel de Barros, com dinheiro da terça de Frei Gaspar, noviço do Convento de Nossa Senhora do Carmo, no valor de 110 réis - Diz o testamenteiro que o dito defunto deixara um negro e terras para seu filho, que só deviam lhe ser entregues quando oficiasse missa. Os bens foram vendidos para, com isso, obter dinheiro que pudesse por a render. Por esta escritura empresta dinheiro a Manoel de Barros, com obrigação deste último devolvê-lo ao frei quando oficiar missa. Para garantia, Manoel hipoteca metade de uma morada de casas de sobrado sita na rua de Mateus de Freitas.
Observações
110$000 (ou 1:010$000 - as duas cifras aparecem na escritura, mas deve ser a primeira). Juro de 8% ao ano. Obs.: Escritura confusa. Diz também que metade deveria ser dada aos frades do Carmo e metade aos de São Francisco, para missas a favor de sua alma

AN, 1ON, 42, p. 120, p. 149v; AGCRJ, Códice 42-3-57, p. 208, 218
Data - 1654
Descrição
Escritura de dote de casamento que faz Beatriz da Silva, viúva de Antonio Vaz Viçoso, a Eliseu de Macedo por casamento com sua filha Joana Viçosa (ou da Silva) - uma morada de casas térrea, de pedra e cal, sala, câmara, varanda e quintal murado de pedra e cal, sita por detrás da igreja da Candelária, no cabo da rua que foi antigamente de Antonio Martins da Palma, que Deus haja, que é a casa do canto onde ela doadora mora de presente, partindo de uma banda com casas do Capitão Luiz Pinheiro [Montarroio] e com quem de direito mais haja de partir. Doa também seis braças de chãos na mesma rua, que partem com chãos de seu genro Manoel de Barcelos [Domingues]. Doa também meia légua de terras de testada com uma de sertão, sitas no Campo Grande, começando a medir onde acabar Bartolomeu Machado com a sua data

AN, 1ON, 42, p. 123; AGCRJ, Códice 42-3-57, p. 209
Data - 1654
Descrição
Escritura de venda de um lanço de casas que fazem Jerônimo Fernandes e sua mulher Isabel Vaz a Domingos Carvalho, no valor de 90 réis – térreas, de taipa de mão, cobertas de telha, com sala, câmara, quintal e sua cozinha, sitas na rua de Manoel Ribeiro, partindo de uma banda com casas de Pero Pacheco [Cabral] e da outra com casas de Paula da Silveira, compradas a João de Leão.

AN, 1ON, 42, p. 128; AGCRJ, Códice 42-3-57, p. 210; AMSBRJ, Estados do Mosteiro, Vol. 1, Parte 1, p. 45
Data - 1654
Descrição
Escritura de venda de quatro lanços de casas que fazem Manoel Soares Rubina e sua mulher Inocência Cardosa aos reverendos padres de São Bento, no valor de 450 réis – todas térreas, dois desses lanços comprados a Sebastião Pinto e sua mulher Madanela Sardinha [em 14/7/1653 – 1º Ofício] e os outros dois a João Dias da Costa, como procurador bastante de Diogo Vaz de Escobar e de sua mulher Antonia de Aguiar (documento muito danificado).
Observações
No AMSBRJ há uma escritura com data de 20/3/1655 pela qual Manoel Soares Rubina vendeu ao Mosteiro de São Bento umas casas térreas e de taipa, sitas na rua dos Pescadores, indo da praia para o campo à mão esquerda, em substituição às quais o Mosteiro levantou posteriormente quatro moradas térreas e duas de sobrado, já existentes em 1766 (AMSBRJ, Seção 2, Nº 78; LTMSBRJ)

AN, 1ON, 42, p. 135v; AGCRJ, Códice 42-3-55, p. 211
Data - 1654
Descrição
Escritura de venda de chãos que faz Aleixo Manoel a João do Souro de Oliveira, no valor de 24 réis – sitos na várzea desta cidade, [na rua de Aleixo Manoel?], no cabo do seu quintal, que parte com João do Souro e com Francisco de Araújo, meirinho [do mar], e da outra parte com Cosme da Guarda, ... da mesma largura das casas do dito João do Souro, e para dentro o que se achar.

AN, 1ON, 42, p. 142; AGCRJ, Códice 42-3-57, p. 215
Data - 1654
Descrição
Escritura de venda de um lanço de casas que faz Gonçalo de Araújo a Pantaleão Duarte Velho, no valor de 200 réis - térreas, sitas na rua de Aleixo Manoel, em três braças de testada e 12,5 de quintal, de pedra e cal, partindo de uma banda com casas do comprador e da outra com casas de Bento Pinheiro, comprada a Diogo de Montarroio e que lhe couberam por partilha dos bens de sua mulher Mécia de Barcelos.

AN, 1ON, 42, p. 145; AGCRJ, Códice 42-3-57, p. 217
Data - 1654
Descrição
Escritura de venda de chãos que fazem Felipe Vaz Morgado e sua mulher Ana Rodrigues a Mateus de Freitas, o moço, no valor de 67 réis – com quatro braças de testada, sitos na rua dos Quartéis, por detrás dos quintais de Mateus de Freitas, o velho, na rua de Jorge Pinto..., havidos por sentença judicial contra Mateus de Freitas, o velho.

ACMRJ, Freguesia da Sé, 4LO
Data - 1654
Descrição
Verba testamentária de Bárbara Barreta, viúva de ... - Deixa em capela aos Religiosos de Nossa Senhora do Carmo a morada de casas de sobrado em que vivia, com obrigação de uma missa todos os sábados "enquanto o mundo durar"
Preço
Código

AN, 1ON, 42, p. 155v; AGCRJ, Códice 42-3-57, p. 220
Data - 1654
Descrição
Escritura de venda de dois lanços de casas que fazem Manoel da Luz e sua mulher Bárbara da Fonseca, e Tomás Cordeiro de Peralta e sua mulher Inês da Luz, ao Capitão Francisco de Oliveira, no valor de 2500 cruzados - uma casa de sobrado com uma casa térrea no quintal, de pedra e cal, altos e baixos, sitas na rua do Vila Verde, havidas por falecimento de seu pai e sogra e sogro.

AMSBRJ, Seção 6.2, Documento 182
Data - 1655
Descrição
Escritura de venda de uma morada de casas que faz Antonia Rodrigues ao Mosteiro de São Bento - de sobrado, sita na rua Direita

ACMRJ, Freguesia da Sé, 4LO
Data - 1655
Descrição
Verba testamentária de Grácia Muniz, viúva de ... - Deixa a morada de casas em que vive à Santa Casa da Misericórdia, com obrigação de missas
Observações
A Santa Casa da Misericórdia toma posse dessa casa em 7/6/1655. Ficava na rua de Inácio da Castanheira e foi vendida ao Sargento Leonardo Dorneles [de Vasconcelos] em 23/8/1680 por 50$000, que ficaram a juros nas mãos do comprador (SCMRJ, Quinto Livro do Tombo, p. 3v).

IHGB: Lata 57, Pasta 3
Data - 1655
Descrição
Escritura de doação de uma capela e igreja que faz Maria de Mendonça, viúva de Miguel Carvalho [Cardoso], ao reverendo padre Frei Mauricio da Piedade - capela de Nossa Senhora da Conceição, sita no outeiro chamado da Conceição, fora da cidade, para a banda do poente, em terras parte do Conselho e parte suas, da qual ela é padroeira, para que o dito doado e seus sucessores fundem um convento de religiosos carmelitas recoletos (Escritura original do 1º Ofício)

AGCRJ, Códice 42-3-57, p. 211
Data - 1655
Descrição
Escritura de doação de uma igreja e chãos que faz Maria de Mendonça, viúva de Miguel Carvalho [Cardoso], a Confraria de Nossa Senhora da Conceição – chãos começando do meio da dita igreja para a banda da varanda da casa onde ela doadora se recolhe, com 20 palmos de chão em redondo para o adro. Com condição que os mordomos farão uma tribuna para ela em sua vida se gozar dela, bens que lhe ficaram por morte de seu marido

AMSBRJ, Seção 3, Nº 1025
Data - 1655
Descrição
Escritura de dívida e obrigação que fazem o Capitão Manoel Barbosa Simões e sua mulher Dona Maria de Araújo aos reverendos padres da Companhia - Diz o Capitão que ele devia 2.000 cruzados ao defunto Vicente de Aristondo. Como os padres da Companhia são agora os seus herdeiros, celebra esta escritura, transferindo a dívida para os mesmos. Em garantia de pagamento, arreta uma morada de casas de sobrado sita na rua Direita, da banda do mar, em que de presente mora, com declaração que ele dito Capitão Manoel Barbosa Simões morará na dita casa pagando de aluguel delas 64$000 anuais (Escritura do 3º Ofício)

AMSBRJ, Estados do Mosteiro, Vol. 1, Parte 1, p. 47
Data - 1655
Descrição
Testamento de Diogo Dias – Mosteiro herda uma morada de casas de pedra e cal, com obrigação de uma missa por semana, que rende 20$000 a cada ano

ACMRJ, Freguesia da Sé, 4LO
Data - 1655
Descrição
Verba testamentária de Andreza de Souza, viúva de Baltazar da Costa - Deixa à sua sobrinha Maria de Souza, filha de seu irmão João de Souza, três braças de chãos que tem na Prainha, junto às que vendeu a seu genro Francisco de Oliveira, com o comprimento que tiverem de rua a rua

AMSBRJ, Estados do Mosteiro, Vol. 1, Parte 1, p. 47
Data - 1655
Descrição
Mosteiro de São Bento herda de Lourença da Costa duas moradas de casas de taipa de mão, cobertas de telhas, com seus quintais, que rendem cada ano 19$200

AGCRJ, Códice 40-3-71, p. 66
Data - 1656
Descrição
Escritura de dote de casamento que fazem Antonio Rodrigues Trigueiro e sua mulher Margarida de Aguiar à sua filha Úrsula de Aguiar para se casar com Manoel Gomes Pereira – Doam 500 braças de terras de testada com meia légua de sertão, sitas onde chamam o Taipu, ... com outras deles dotadores ... fazem sua testada onde acabam as duas léguas dos índios da Aldeia de São Lourenço, partindo de uma banda com eles ditos dotadores e da outra .... outeiros ... pai do dito dotado .. como constará da carta de sesmaria... Doam também uma morada de casas térrea, de taipa de pilão, coberta de telha, mística com outra em que eles dotadores vivem de presente, sita defronte de Nossa Senhora do Parto, que é a que fica da banda de São Francisco. Dão também um negro do gentio de guiné por nome Alexandre e uma negra do mesmo gentio por nome Andreza e lhe dão mais pelo tempo em diante 150$000, ou em açúcar ou em dinheiro, e mais outros bens móveis (vestidos, panos, cobertor, jóias, etc.)

SCMRJ, Quinto Livro do Tombo, p. 3v
Data - 1656-07-27
Descrição
Testamento de Maria de Veras – Lega à Santa Casa da Misericórdia metade de uma morada de casas sita na rua por detrás de Nossa Senhora do Carmo e uma sorte de terras em Guaratiba, com encargo de uma capela de missas


2LTMSBRJ, p. 90, nota 2; CAMSBRJ, p. 48
Data - 1656
Descrição
Escritura de aforamento de chãos que fazem os reverendos padres de São Bento à Companhia Geral de Comércio, no valor de 12 réis - chãos junto à ribeira de São Bento, no princípio da antiga ladeira até o mar, para os seus armazéns e casas de negócio. Foro anual: 12$000. Este terreno foi doado à Coroa em 26/4/1696


AMSBRJ, Estados do Mosteiro, Vol. 1, Parte 1, p. 47
Data - 1656
Descrição
Escritura de arrendamento de uma morada de casas que fazem os religiosos de São Bento à Companhia Geral – sita nas terras do Mosteiro pegado à ponte, com 12 anos de arrendamento, para no cabo delas lhe pagarmos as benfeitorias, abatendo-nos 100$000 do em que se avaliaram, as quais rendem a cada ano 12$000

ACMRJ, Freguesia da Sé, 4LO
Data - 1657
Descrição
Verba testamentária de Bento de Oliveira - Deixa a seu filho Manoel da Costa(?), para ordenar-se de clérigo, a casa em que vive, que herdara de sua irmã Vicência Tavares(?) com uma pensão de missas

AMSBRJ, Seção 13.2, Nº 962
Data - 1657
Descrição
Testamento de Catarina Gomes - natural do Rio de Janeiro, filha legítima de Luiz Lopes e de Maria Freire ou Freitas, já defuntos, casada com Antonio Lopes [Mealhas], irmã de Domingos Gomes e de Juliana Freire, cunhada de Inês Mexias. Informa ter 2 filhos homens (Jerônimo Lopes e Antonio Gomes), duas filhas mulheres ([Úrsula?] e Inês Lopes) e um genro por nome Gabriel da Rocha [Freire, casado com Inês], com quem divide a propriedade de uma caravela. Possui uma morada de casas de taipa de mão, em que vive [que deve ser em Vila Verde, conforme informado na escritura de 25/1/1663] e que, junto à ela, possui três braças de chãos, que deixa para sua neta. Informa também que os chãos que estão no fundo do seu quintal, com três braças de testada pela rua de Manoel Álvares Carapau, pertencem ao dote de sua filha Inês

ACMRJ, Freguesia da Sé, 4LO
Data - 1657
Descrição
Verba testamentária de Margarida de Lima - Deixa em capela a seu filho Padre Inácio Ferreira uma morada de casas de taipa de mão. Deixa também a esse seu filho, para seu patrimônio, uma morada de casas sita na rua da Candelária. Deixa a casa em que vivia à sua filha Tomásia de Medina. Declarou que na sua fazenda havia uma ermida de Nossa Senhora da Guia, que deixa ao dito seu filho padre.

AMSBRJ, Estados do Mosteiro, Vol. 1, Parte 1, fp. 71-72
Data - 1658
Descrição
Escritura de venda de uma morada de casas que faz Catarina de Almeida aos religiosos de São Bento, no valor de 300 réis – térrea, de pedra e cal, sita na rua Direita.

AMSBRJ, Seção 2, Nº 78
Data - 1658
Descrição
Escritura de venda de chãos que fazem Sebastião Pinto e sua mulher Madalena Sardinha ao Mosteiro de São Bento, no valor de 18 réis – com duas braças de testada, [sitos na rua do Carmo?], contíguos à casa que Catarina de Almeida vendeu ao Mosteiro, no fundo dela.


2LTMSBRJ, pp. 250-251; AGCRJ, Códice 42-3-57, p. 157; AMSBRJ, Seção 2, Documento 78; Estados do Mosteiro, Vol. 1, Parte 1, fp. 71-72
Data - 1658
Descrição
Escritura de venda de chãos que fazem o Capitão José de Barcelos Machado e sua mulher Bárbara de Madureira aos reverendos padres de São Bento, no valor de 64 réis – com 4,5 braças de testada e 12 de quintal, sitos na Varge desta cidade, partindo de uma banda com casas do Capitão Cosme da Guarda Maciel e da outra com a rua do Capitão Frutuoso Pinheiro de Lemos, herdados por morte de seu pai e mãe.
Observações
64$000, pagos em oito capelas de missas pelas almas de seu pai e sua mãe. Atenção: Informação posterior dá conta que o Mosteiro comprara três braças de chãos a José de Barcelos na rua Nova das Flores (6LTMSBRJ, p. 252). Capitão José de Barcelos Machado falece por volta de 1674 (AN, 1ON, 53, p. 162; Rheingantz, II, 503). Há também informação de 1810 que o Mosteiro possuía 4 braças de chãos na rua dos Ourives, entre Ouvidor e Cano, "que deitam os fundos até a rua Nova das Flores ou rua Nova do Ouvidor" (6LTMSBRJ, p. 288) - Classificado errado

AN, 1ON, 38, p. ?
Data - 1658
Descrição
Escritura de débito e obrigação que faz o Capitão Gonçalo de Muros aos reverendos padres da Companhia de Jesus – Diz o capitão que ele devia ao Colégio da Companhia 1:975$000. Por garantia, hipoteca(?) uma morada de casas de sobrado, de pedra e cal, altos e baixos, sita na rua Direita, da banda da praia, que parte de uma banda com casas de Domingos Árias de Aguirre e da outra com casas de Bento da Rocha Gondim ...

ACMRJ, Freguesia da Sé, 4LO
Data - 1658
Descrição
Verba testamentária de Domingas de Mariz, mulher de Assenço Pereira - Deixa à sua sobrinha Isabel de Mariz, filha de seu irmão ... , uns chãos no bairro de Nossa Senhora da Ajuda

AGCRJ, Códice 42-3-57, p. 239
Data - 1658
Descrição
Escritura de dote de casamento que faz Apolônia Gonçalves a José do Couto, marido de sua filha Paulina de Oliveira – umas terras sitas no rio de Aguapeiaçu, cinco braças de chãos sitos na rua de Gaspar de Carvalho, duas peças do gentio da terra, um macho e uma fêmea, e um sítio que tinha no dito rio, em que vivia

AGCRJ, Códice 42-3-57, p. 210 - AGCRJ, Códice 42-3-57, p. 240
Data - 1658
Descrição
Escritura de venda de uma morada de casas que faz Domingos Fernandes Nunes a João ... – térrea, de taipa de mão, coberta de telhas, sita no bairro de Nossa Senhora, quando vão para a Carioca

AGCRJ, Códice 42-3-57, p. 243
Data - 1658
Descrição
Escritura de venda de açúcares brancos e mascavados com hipoteca de uma morada de casas que faz Antonio de Macedo a Antonio Pereira – térrea, de pedra e cal, sita na várzea desta cidade, na travessa do ferreiro da praia

AGCRJ, Códice 42-3-57, p. 244
Data - 1658
Descrição
Escritura de venda de uma morada de casas que fazem Jorge de Souza Coutinho e sua mulher Dona Isabel de Aguiar ao Padre Francisco do Amaral, no valor de 170 réis – térrea, de taipa de mão, coberta de telhas, já velha e muito antiga, feita em cinco braças de chãos de testada, sita na rua travessa que vem do mar e praia para o sertão, na rua onde mora o provedor de Sua Majestade Pero de Souza Pereira, que mora em casa do General Salvador Correia de Sá e Benevides, partindo de uma banda com casas térreas dos padres da Companhia, que agora de novo fizeram, e da outra com casas de pedra e cal de sobrado de João Godinho, correndo o quintal de 12 braças até entestar com chãos e quintal de João [de Azevedo] Roxas, herdada de seu pai e sogro Diogo de Souza Coutinho e Dona Antonia de Sampaio.

AGCRJ, Códice 42-3-57, p. 210, 247
Data - 1658
Descrição
Escritura de venda de uma morada de casas que fazem Manoel Jorge da Silva e Manoel Rodrigues Ribeiro, como testamenteiros de Domingos Manoel, marido de Emerenciana da Costa, a João Ferreira – de sobrado, de pedra e cal, sita na rua de Pedro da Costa.


AGCRJ, Códice 42-3-57, p. 210
Data - 1658
Descrição
Escritura de débito com hipoteca de uma morada de casas que fazem Francisco da Rocha e João Luiz Mafra, no valor de 100 réis – térrea, de pedra e cal, sita no bairro de São Bento, junto à casa em que ora vive Miguel Tomé Pinheiro.

AMSBRJ, Estados do Mosteiro, Vol. 1, Parte 1, fp. 71-72
Data - 1658
Descrição
Escritura de venda de uma morada de casas, com chãos anexos(?), que faz ... aos religiosos de São Bento, no valor de 70 réis – térrea, de madeira e barro, nova, rebocada de cal.

ACMRJ, Freguesia da Sé, 4LO
Data - 1659
Descrição
Verba testamentária de Pero Pacheco [Cabral] - Deixa à Santa Casa da Misericórdia metade de uma morada de casas térrea, de pedra e cal, com condição que morará nela a sua mulher enquanto viver.
Observações
A Santa Casa recebe essa casa logo a seguir; estava localizada na travessa da Cadeia (SCMRJ, Quinto Livro do Tombo, p. 3v). A viúva de Pedro Pacheco, falecida em 1687, deixará a outra metade da morada à Santa Casa. Ver 11/9/1687


Data - 1659
Descrição
Escritura de venda de uma morada de casas que faz o Capitão Gonçalo de Muros ao governador da praça do Rio de Janeiro Tomé Correia de Alvarenga, no valor de 1300 réis – de sobrado, de pedra e cal, sita na rua Direita, da banda da praia, que por uma parte faz canto e fica fronteira, e da banda da rua com casas de canto que são da Misericórdia e pela outra banda parte com outras casas também de pedra e cal, sobradadas, dele dito Capitão Gonçalo de Muros, a qual casa aqui vendida houve por compra feita a Manoel Soares Rubina, com fundos ate o mar. Vende também a meia parede que já está feita, que parte com ele vendedor.
Preço
1300 Réis
>>>>>>>>>>>>>>>>>>>>>Código <<<<<<<<<<
Observações
AGCRJ, Códice 42-3-57, p. 258 ; José Antonio Caldas. Notícia geral de toda esta capitania da Bahia desde o seu descobrimento até o prezente anno de 1759. In Revista do Instituto Histórico e Geográfico da Bahia, Nº 57, 1931, p. 156. Também citada esta transação em (Catálogo dos Capitães-mores ...., RIHGB, Tomo 2, 1840, p. 53).

AMSBRJ, Seção 2, Nº 78
Data - 1659
Descrição
Escritura de doação de chãos que faz Antonia da Silva, mulher de Pedro Félix Napolitano, ao Mosteiro de São Bento - com 5 braças na rua de Santa Rita, indo para o Parto à mão direita [que ainda não estavam construídas em 1766]

AGCRJ, Códice 42-3-57, p. 250
Data - 1659
Descrição
Escritura de venda de uma morada de casas que faz o Capitão Pedro de Souza Pereira a Jerônimo Camelo de Sampaio, no valor de 300 réis – térrea, de taipa de pilão, coberta de telha, sita na rua Direita, defronte da cadeia, arrematada em praça pública por uma dívida que estava lhe devendo Jerônimo Camelo de Sampaio da quantia de 300$000. Agora vende ao dito Jerônimo pelo mesmo preço

AGCRJ, Códice 42-3-57, p. 252
Data - 1659
Descrição
Escritura de doação de uns chãos que faz Matias de Mendonça a Gaspar de Carvalho – sitos na várzea desta cidade

AGCRJ, Códice 42-3-57, p. 259
Data - 1659
Descrição
Escritura de venda de uma morada de casas que faz Lucrécia Viegas, dona viúva, a seu filho Francisco de Macedo Viegas, no valor de 200 réis – térrea, de pedra e cal, coberta de telha, sita na ... que chamam [do ferreiro da praia] Matias Gonçalves, que parte por uma banda com casas do dito Matias Gonçalves e com Antonio [Gomes] alfaiate, e da outra com outra morada de casas dela vendedora, correndo o quintal até entestar com uma parede do vigário geral Manoel de Araújo.

AGCRJ, Códice 42-3-57, p. 260
Data - 1659
Descrição
Escritura de venda de uma morada de casas que fazem Fernão Gomes de Freitas e sua mulher Maria Godinha a Margarida Pinheira, dona viúva, no valor de 500 réis – de sobrado, sita na rua Direita, freguesia de Nossa Senhora da Candelária, partindo de uma banda com casas de Antonio da Veiga e da outra com casas de Domingas de Oliveira, dona viúva, arrematada em praça pública.
Observações
Data: 1659.

AN, 1ON, 44, p. 18v
Data - 1661
Descrição
Escritura de venda de uma morada de casas que faz André Tavares a Francisco Cordeiro e sua mulher Margarida da Silva, no valor de 270 réis - de sobrado, de pedra e cal, sita junto à porta da cidade que vai para a Misericórdia, partindo de uma banda com o vendedor e da outra com casas que estão por acabar dele dito vendedor ou de quem de direito for.
Observações
Data: ?/5/1661.

AN, 1ON, 44, p. 26
Data - 1661
Descrição
Escritura de dote de casamento que fazem Assenço Lopes e sua mulher Bárbara da ... a Mateus Cordeiro casando com sua filha Maria Lopes – três braças de chãos de testada, e o comprimento para trás, que o dito seu genro tinha por lhes haver dado à dita sua filha Maria Lopes, mulher do dito Mateus Cordeiro, seu tio Inácio da Castanheira e sua mulher primeira ...

AN, 1ON, 44, p. 33
Data - 1661
Descrição
Escritura de dote de casamento que fazem André Álvares Gaio e sua mulher Clara Filgueira a Luiz Mendes [sapateiro], casando com sua enteada Joana Filgueira, filha de Antonio Gonçalves - uma morada de casas térrea, sita na rua de João de Azevedo ..., no canto da dita rua, partindo da outra banda com casas dele doador. Estas últimas ele também as doa, e parte da outra banda com casas de Manoel Borges, ferreiro. Sem valor declarado

AN, 1ON, 44, p. 196v
Data - 1661
Descrição
Treslado do testamento de Catarina de Medeiros, viúva de Antonio P..., falecida em 15/6/1662 – Diz ter tido os seguintes filhos: Licenciado Francisco Álvares Góis e Antonio da Guerra, já defuntos, mas que deixaram filhos, que hoje são vivos os seguintes: Margarida Gomes e Antonio Fernandes, filhos do Licenciado Francisco Álvares Góis, e Catarina Mendes, Antonio da Guerra, Paula Gonçalves e Isabel da Guerra(?), filhos de Antonio da Guerra. Declara que possuía duas moradas de casas térreas, de taipa de mão, cobertas de telhas, uma delas sita no canto, na rua Direita, com 3,5 braças de testada e 12 de comprido, e a outra na travessa da Candelária, com três braças de testada e 6 de sertão, até entestar com a parede de pedra de ... Rodrigues de Lisboa, partindo de uma banda com Belchior Gonçalves e da outra ficam ... Declara que tem uma sorte de terras no rio de Guapiaçu. Declara que tem quatro peças do gentio de guiné, duas mulatinhas que deixa forras, um mulatinho que vendeu ao Capitão Pedro ...


AN, 1ON, 44, p. 59
Data - 1661
Descrição
Escritura de venda de terras que faz o reverendo padre Pedro Homem Albernaz a Sebastião Fernandes, sapateiro – sitas por detrás do outeiro de Nossa Senhora da Conceição, que partem de uma banda com terras do Capitão Francisco Munhoz Correia e João de Azevedo e da outra com terras de Antonio Pereira (ou Ferreira) ...

AGCRJ, Códice 39-3-71; VF, II, 452-453
Data - 1661
Descrição
Escritura de permuta de imóveis que fazem Salvador Correia de Sá e Benevides e sua mulher Dona Catarina de Vasconcelos de Velasco com os oficiais da Câmara desta cidade - Como a Câmara despendia 150$000 anuais com a aposentadoria dos governadores, Salvador Benevides fez a seguinte proposta, que foi aceita pelo corregedor da Comarca Doutor Sebastião Cardoso de Sampaio: "o general larga três moradas de casas contínuas e místicas, com porta por dentro, que estão na rua Direita desta cidade, defronte da casa da Alfândega, que fazem canto e têm para a dita rua Direita duas salas com seis janelas rasgadas, com sacadas e grades de ferro, e pela travessa [hoje rua da Alfândega] com sete janelas, até entestar com outras casas que o dito general deu à Santa Casa da Misericórdia, cortando pela parte detrás com paredes e quintal de Baltazar de Amorim Calheiros". O Conselho, por sua vez, largava uma morada de casas de sua propriedade na rua que vulgarmente chamam do Gadelha, que parte de uma banda com casas de Agostinho Barbalho Bezerra e da outra com casas de Leonardo de Souza. Além disso, a Câmara cedia a Salvador um total de 84$400 de foros, que eram pagos pelas seguintes casas sitas à rua Direita: "as de Francisco da Silveira [VF lê Inácio da Silva], que estão no canto defronte do Mosteiro do Carmo, em 10$500; as de João Dias, que se seguem a elas, em 10$500; as de Ana Pereira, viúva de Marcos Duarte, que vão seguindo as acima, em ... mil e quinhentos réis; e outras que se seguem do padre vigário da Sé, o licenciado Manoel da Nóbrega, em 7$500; e em três outras que se seguem, a saber, as de João Godinho, pedreiro, em 9$800 (em outra escritura, corrigem este valor para 8$750); as de Marcos da Costa Manoel, boticário, que partem com casas do Colégio, em 12$000; e uns chãos e casas do Capitão Francisco Monteiro Mendes, que partem com o dito boticário até o canto da igreja da Cruz, em 19$000; e nas do provedor da Fazenda Real Pedro de Souza Pereira, que partem com as casas da Alfândega e da outra parte com casas de Maria de Araújo, dona viúva do Capitão Manoel Barbosa Simões, 6$600, os quais foros fazem quantia dos ditos oitenta mil e quatrocentos réis"
Observações
Cedia também os foros onde estavam edificadas as casas do Provedor da Fazenda Real, Pedro de Souza Pereira, e que partem com as casas da Alfândega de um lado, e do outro com as propriedades de Dona Maria de Araújo, viúva do Capitão Manoel Barbosa Simões, e bem assim um pedaço de chão que serviu de corpo da guarda. No ato da assinatura do contrato recebeu mais Salvador a quantia de 300$000" (AGCRJ, Códice 16-2-21, fp. 30-32; VF, II, 467-468). VF informa também (p. 468) que tal convênio não teve confirmação régia, pois Salvador, voltando logo depois para Portugal, caiu em desgraça por ter tomado o partido do rei Afonso VI frente às lutas com os partidários de seu irmão, o futuro Pedro II (VF, II, 467; VF, V, 180)

AN, 1ON, 44, p. 85
Data - 1661
Descrição
Escritura de venda de chãos que fazem Miguel do Couto [de Azevedo] e sua mulher Maria de Aguiar a Francisco Ferreira, no valor de 10 réis – com três braças de testada, sitos no caminho que vai para a Prainha, onde chamam Vila Verde, partindo de uma banda com Clemente da Rocha e da outra com Antonio de Mendonça, com 20 braças de quintal, chãos havidos por dote de sua sogra Luzia Ferreira e por escritura de compra que seu pai Diogo de Aguiar fez a Pedro G... Álvares.

FF, HCRJ, p. 327
Data - 1661
Descrição
Escritura de venda de chãos que fazem Antonio Vieira e sua mulher a ... - "sitos na travessa de Lucas do Couto por onde vai um cano real". FF diz que esta escritura, cujo texto não é apresentado, ensina "que estes chãos foram obtidos por sesmaria por Álvaro Pires, cujo herdeiro foi seu filho [Antônio] Pires Fróis, de que os herdaram Antonio Vieira e sua mulher"
Observações
Data: 1661 (ou 1681).

AN, 1ON, 44
Data - 1662
Descrição
Escritura de venda de uma morada de casas que faz Pedro Gomes Salgado a Salvador Luiz, oficial de pedreiro, no valor de 67 réis - térrea, de taipa de mão, com quatro braças de testada, sita na rua de Miguel de Freitas, partindo de uma banda com casas que foram de Ana Fernandes e da outra com casas da dita Ana Fernandes.

SCMRJ, Quinto Livro do Tombo, p. 5v
Data - 1662
Descrição
Santa Casa da Misericórdia recebe a doação que lhe havia sido feita por Pedro de Siqueira e sua mulher Estácia de Távora, com obrigação de capelas de missas – os bens constavam de 800 braças de terras e 6 braças de chãos sitas no alto desta cidade, além de oito escravos. A Santa Casa vendeu os bens e recebeu 268$600 de rendimento, além de 170$000 pela venda de três negros

AN, 1ON, 44
Data - 1662
Descrição
Escritura de venda de duas moradas de casas a retro aberto que faz o reverendo vigário geral Francisco da Silveira Vilalobos ao Capitão Mateus de Moura Fogaça e sua mulher Dona Úrsula da Costa, no valor de 2000 cruzados - de sobrado, de pedra e cal, altos e baixos, com todas as suas lógeas, sitas na rua Direita, defronte da igreja de São José.
Observações
Prazo: 3 anos. Em maio de 1663, o Padre Francisco da Silveira Vilalobos fez outra escritura com o Ilustríssimo Prelado e Administrador do Rio de Janeiro, Doutor Manoel de Souza Almada, da mesma morada, "onde ora vive o Reverendo Senhor Prelado", dizendo que tinha sido anteriormente vendida ao Capitão Mateus de Moura Fogaça por 2.000 cruzados, a serem pagos em açúcares, venda que foi desfeita por falta de pagamento no prazo combinado. Mesmo assim é dado novo prazo ao Capitão Mateus de Moura Fogaça para fazer o pagamento; não o fazendo, a venda será concretizada com o Prelado (AGCRJ, Códice 42-3-56, p. 24). Em junho de 1663, o Padre trespassou essa casa pelo mesmo preço ao Capitão Mateus de Moura Fogaça (AN, 1ON, 44, p. 145v). Em 1/1/1666, Frei Francisco de Jesus Vilalobos, [que teve grande desentendimento com o Prelado Administrador, Manoel de Souza de Almada, e agora no Mosteiro de S. Bento?], e "antes vigário geral do Rio de Janeiro", faz testamento onde diz que "morei em casas do Capitão Mateus de Moura Fogaça dois anos pouco mais ou menos, e a esta conta lhe hei dado dinheiro todas as vezes que me pedia, e ao Licenciado João de Moura, seu filho, por ordem sua dei duas caixas de açúcar.... (CAMSBRJ, p. 259*)

AN, 1ON, 44, p. 173v
Data - 1662
Descrição
Escritura de dinheiro a ganho com hipoteca de uma morada de casas que faz João da Fonseca Coutinho ao Juízo dos Órfãos, no valor de 238 réis – de sobrado, de pedra e cal, em que vive, sita na rua de Gregório Mendes.


AN, 1ON, 44, p. 161v
Data - 1662
Descrição
Escritura de venda de uma morada de casas que faz o Capitão Luiz Machado Homem, como testamenteiro de sua tia Úrsula Varela, a Domingos Rodrigues de Carvalho, no valor de 100 réis - térrea, sita na rua dos Quartéis, partindo de uma banda com casas do Capitão Alexandre de Castro e da outra com casas onde vive Antonio Dias.

AN, 1ON, 44, p. 162v
Data - 1662
Descrição
Escritura de venda de uma morada de casas que fazem o Capitão Domingos Árias de Aguirre e sua mulher Dona Inês [Rabela] ao Capitão Francisco Teles Barreto, no valor de 1100 réis - de sobrado, nova, de pedra e cal, em três braças de testada, sita na rua Direita, da banda da praia, partindo de uma banda com casas do Reverendo Vigário Geral Francisco da Silveira Vilalobos e da outra com casas do Capitão Gonçalo de Muros, com todo o seu comprimento até à praia, foreira à Câmara em fatoesim

AN, 1ON, 44, p. 168v
Data - 1662
Descrição
Escritura de venda de uma morada de casas que fazem o Capitão Hipólito Lopes Cerqueira e sua mulher Joana de Moura ao Alferes Manoel Afonso [Cruz], no valor de 53 réis - térrea, coberta de telhas, sita na rua do Açougue Velho, defronte das casas que foram de Mestre João, partindo de uma banda com casas do Alferes Manoel Afonso [Cruz] e da outra com chãos que foram do Capitão Hipólito Lopes Cerqueira e ora são do Capitão Francisco de Macedo Freire, havida por dote de seu sogro João de Freitas de Araújo e sua mulher Leonor da Fonseca.

AN, 1ON, 44, p. 175
Data - 1662
Descrição
Escritura de venda de uma morada de casas que fazem Francisco de Mendonça Gávea(Gouveia?) e sua mulher Paula da Fonseca a Gonçalo Ribeiro Barbosa, no valor de 36 réis - térrea, de taipa de pilão, sita na cidade velha, no alto desta, partindo de uma banda com Antonio dos Banhos e da outra com chãos de Lucas do Couto, comprada a Francisco do ... , já defunto [3º Ofício].
Observações
Um Gonçalo Ribeiro Barbosa, filho de Gonçalo Ribeiro de Basto, pede provisão da propriedade do ofício de escrivão da correição e ouvidoria geral da cidade de S. Sebastião do Rio de Janeiro em 1643 - ABN, 39, p. 28]. Gonçalo Ribeiro de Basto era moço da Câmara de Sua Majestade em 15/5/1650 (AHU-CA, docs 789 e seguintes).

AN, 1ON, 44, p. 203v
Data - 1662
Descrição
Escritura de dote de casamento que fazem Diogo da Fonseca e sua mulher Maria do Amaral ao Sargento-mor Diogo Cardoso de Mesquita [cavaleiro da Ordem de São Bento de Avís, capitão da fortaleza de Santa Cruz em 1663 - ABN, 39, 110], para se casar com sua filha Dona Ana do Amaral - uma casa de sobrado, de pedra e cal, sita na rua Direita, da banda da praia, partindo de uma banda com casas de João Godinho e da outra com casas dos herdeiros de Marcos Duarte, com todo o comprimento até o mar, foreira à Câmara, que vale 3.000 cruzados. Doam também um partido de canas em terras próprias, em Irajá, com obrigação de lenhas ao engenho do Capitão ... Juzarte, ficando o partido entre as terras do dito engenho e a testada ... do mar, com 108 braças de testada e 1300 de sertão. Doam também uma sorte de terras em Inhaúma, com 750 braças de largo e sertão de meia légua(?), que partem com terras que foram de Pedro de Siqueira e João Botelho. Doam também 16 peças do gentio de guiné e outros bens

AN, 1ON, 44, p. 210
Data - 1662-07-13
Descrição
Escritura de venda de uma morada de casas e uns chãos que fazem o Capitão Mateus de Freitas da Costa e sua mulher Feliciana de Azevedo ao Alferes João Godinho Leite, no valor de 361 réis - de sobrado, de pedra e cal, sita na travessa de Diogo Correia de Faria, no canto da rua dos Quartéis, partindo de uma banda com casas de Diogo Correia de Faria e da outra com Marta de Oliveira, sua irmã. Os chãos têm quatro braças de testada e partem de uma banda com Diogo Correia e da outra com Antonio Fernandes, por alcunha o caruru.

AN, 1ON, 44, p. 218
Data - 1662
Descrição
Escritura de venda de um sítio de terra e chãos que faz o Sargento-mor Martim Correia Vasques, capitão do presídio desta cidade, por si e como procurador bastante de seu irmão Tomé Correia de Alvarenga, governador que foi desta praça, a Dona Vitória de Sá, no valor de 200 réis – sito no alto desta cidade, na conformidade que foi do General Salvador Correia de Sá e Benevides, primeiro possuidor que foi do dito sítio e chãos, e depois coube ao dito Governador Tomé Correia de Alvarenga.
ABN, 82, 1962, pp. 127-129
Data - 1577
Descrição
Escritura de arrendamento de terras que faz o Colégio de Jesus a Gaspar Sardinha, para fazer um trapiche - Sardinha já havia arrendado ao Colégio, "nas terras que o Colejo tem do Eyoassu pera a tapera de Inhaúma, ao pé da serra, pera a banda da cidade" 240 braças em quadra, "e pela serra ser boa e muito conveniente para fazer um trapiche de açúcar, o dito Gaspar Sardinha pediu aos ditos Padres que no dito sítio lhes aforassem, por tempo de dezoito anos, 600 braças de terra de comprido, começando do princípio de uma roça que agora tem Rui Dias Machado e seu genro, entrando toda na conta, correndo para a banda do oeste pela fralda da serra até se encher a quantia dita, e de largo 500 braças, que começarão do cabo da roça que agora tem plantado de novo Rodrigo Velho, entrando toda a roça plantada nessa conta e daí para a dita serra se encherão as ditas 500 braças ... junto com a água que corre nessas terras...". Padres concordam e fazem um contrato em que Gaspar Sardinha teria que montar o trapiche em 2 anos e pagaria 2,5% de todo o açúcar produzido e o dízimo das mais novidades da terra; não fazendo o engenho pagará mais.... e Gaspar não impedirá os outros arrendatários, se eles lá quiserem ficar....". Gaspar já havia feito alguns melhoramentos na terra e é o primeiro que faz trapiche nas terras dos jesuítas, por isso eles fazem um arrendamento abaixo do custo. Aforamento por 18 anos (Carta d’arrendamento que fêz o Colégio a Gaspar Sardinha pera fazer hum trapiche nas terras do dito Colégio.
Esta escritura não teve efeito, mas uma outra certamente foi feita, pois em 3/4/1579 Gaspar Sardinha traspassa seu trapiche e benfeitorias a Paulo Dias Novaes e a João Guterres Valeiro.

ABN, 82, 1962, pp. 130-131
Data - 1579
Descrição
Escritura de trespasso de aforamento de um trapiche e benfeitorias que faz João Guterres [Valeiro], em seu nome e no nome do Governador de Angola Paulo Dias de Novais, aos reverendos padres da Companhia - João Guterres informa que, em nome do Governador de Angola e em seu próprio nome, havia comprado a Gaspar Sardinha "o trapiche com todas as benfeitorias [que] nele tinha nas terras do dito Colégio, de que dera parte e quinhão ao Senhor Capitão Salvador Correia de Sá, a qual companhia ora desfizera e tomara o dito engenho todo sobre o dito Senhor Governador Paulo Dias de Novais, e a quinta parte para ele dito João Guterres Valeiro, por virtude da qual traspassação do dito engenho ele dito João Guterres per si e todos seus bens móveis e de raiz, havidos e por haver, se obrigou por esta escritura a cumprir e manter o aforamento e arrendamento e obrigação que foi feita ao dito Gaspar Sardinha de quem ele houve o dito engenho, o qual aforamento e arrendamento começou a correr do princípio do mês de janeiro de 1577, de maneira que correrão os dezoito anos conteúdos na dita escritura do dito Gaspar Sardinha de janeiro a janeiro, até se acabarem os dezoito anos conteúdos na dita escritura, e o dito João Guterres Valeiro se obrigou por esta escritura sua pessoa e bens, como dito é, a pagar de renda das ditas terras as ditas duas arrobas e meia de açúcar, que é de cada cem arrobas duas e meia, de foro, e lhe pagará mais de dízimo de todo o açúcar que se fizer no dito engenho, pouco ou muito, e por as mais novidades e frutos das ditas terras, lhe pagará por cada uma de cento e dez arrobas de açúcar por todo o dízimo que dever, que faça muito quer pouco, se dará do dito dízimo as ditas cento e dez arrobas cada ano, conforme no açúcar que o dito engenho der, isto com condição que eles ditos Padres o desobrigarão de o pagar a outrem. Padres informam que faziam a dita avença do dito dízimo por ser o primeiro engenho que nas ditas terras se fêz (Escritura de trespassação do trepiche ao Governador d’Angola e aforramento dos dízimos.

ABN, 82, 1962, pp. 190-192
Data – 1580
Descrição
Escritura de troca de terras que faz o Colégio de Jesus com Cristóvão de Barros e sua mulher, Dona Isabel de Lima - Padre Anchieta, representando o colégio, diz que este tinha umas datas de terras "onde diz que se chama o Rio do Macucu, e correm sobre a banda de Magé, e porque a terra do dito Colégio parte com terras de Cristóvão de Barros, .. havia por bem de se largar ao dito Cristóvão de Barros uma légua de terra, a qual começava de um rio que se chama Magé-Mirim para a parte do engenho do dito Cristóvão de Barros, ficando Magé-Mirim por marca ao dito rio da parte onde este (está?) correndo ao Noroeste e quarta de Norte [em nota diz-se que "é correndo para a parte da Piedade"], conforme a medição que é feita por parte do dito colégio até o lugar e marca da dita medição ... e daí do dito marco se fará quadra da dita légua ao Noroeste com quarta de Leste [nota: "é correndo do Magé para o sertão para o fim da quarta légua] correndo do noroeste para sudeste, que desta maneira traspassava a dita légua de terra .. por outra légua de terra em quadra no Rio de Macacu [nota: "é a da Água"], que parte a dita légua com terras do dito colégio, se começará a medir desta légua de terra se medindo até onde se acabar a medição do dito colégio e começará a largura da dita légua de terra do Rio Macacu para a quarta de leste, que é para a banda daquele marco ... e desta maneira houveram a troca por boa ... (Consêrto das terras de Magé entre Christóvão de Bairros e o Collégio e troca de huma légoa por outra no Macucu.

AMSBRJ, Seção 6.2, Documento 174
Data - 1582
Descrição
Escritura de venda de terras que fazem Jerônimo Barroso e sua mulher Maria Barbosa a Jorge Ferreira, o moço, no valor de 11 réis. Dizem que tinham meia légua de terra de comprido no rio de Aguassu, por ele acima, e 700 braças craveiras de largo, ficando o dito rio no meio, a saber, 350 braças de uma banda e de outra, com o dito rio de Aguaçu no meio, e a meia légua de comprido pelo dito rio acima, a qual terra começará a medir onde acabar de medir Marquesa Ferreira a sua primeira légua para diante, e donde ... acabar a dita meia légua acima começará de medir a dita Marquesa Ferreira outra légua que no dito rio tem, e a dita meia légua, com a dita largura dos ditos 750 braças fica no meio entre as ditas duas léguas, terras que lhes foram dadas de sesmaria ... a sua carta declara (Escritura do 1º Ofício). 

ABN, 82, 1962, pp. 145-147
Data - 1584
Descrição
Escritura de venda de terras que faz Brás Yunes [Eanes] a Domingos Machado, no valor de 4 réis. – com 500 braças de terra de largo e 600 de comprido, obtidas por carta de sesmaria, sitas no termo desta cidade, "além de Ynhaúma, na cabeceira das terras de Simão Barriga e partindo com o dito Simão Barriga pelo caminho que ia para aldeia do Pindelo [na carta de sesmaria diz "que vai para a aldeia de Pindobuçú] ou cortando direito pelo rumo da agulha e pelas cabeceiras das que aí já tinha antes dele pedir ao longo do mar, e disse que ia o dito caminho pelo meio da dita terra, e disse e declarou ele dito Brás Zeanis que os padres da Companhia de Jesus lhe tinham tomado um pedaço da dita terra, que dito é, o tinham demarcado, e que sobre isso Simão Barriga, procurador dele vendedor, trazia demanda com os ditos Padres, e que somente ele vendia ao dito comprador Domingos Machado a terra que estava ao presente desembaraçada e livre, pouca ou muita, e que sendo caso que ele vendedor houvesse sentença da dita terra e tornasse a haver o dito pedaço de terra que dito é, que lhe os ditos Padres tinham tomado, que por esta escritura se obrigava ... a lhe dar a dita terra e a lhe entregar toda, assim e da maneira e por encher que na sua carta de sesmaria mais largamente era declarado ... e vende com tal condição que o dito comprador será obrigado a tapar a dita terra entre ele e Simão Barriga com tapagem alta e forte, de maneira que o gado do dito comprador não faça nojo nem dano ao dito Simão Barriga ...". (Carta da terra que vemdeo Braz Yunes a Domingos Machado. Colégio mede e toma posse dessas terras em 10/9/1595.

ABN, 82, 1962, pp. 121-123
Data - 1586
Descrição
Escritura de venda de terras que fazem Domingos Machado e sua mulher Ana Rodrigues aos padres da Companhia, no alor de 9 réis – com 500 braças de largo e 600 de comprido, situadas em Inhaúma, nas cabeceiras de Simão Barriga, compradas a Brás Eanes em 13/2/1584, que as havia recebido de sesmaria.
Escritura das terras que o Collégio comprou a Domingos Machado, que estão nas Inhaumas, a uma légoa.
AGCRJ, Códice 40-3-71, p. 37v
Data - 1587
Descrição
Escritura de venda de terras que fazem Liodoro Ebanos e sua mulher Isabel Velha a Francisco de Braga, no valor de 12 réis – com meia légua em quadra, sitas da banda do Cabo Frio, que partem com Diogo de Braga, que Deus haja.

ABN, 82, 1962, pp. 156-157; 167-168
Data - 1589
Descrição
Escritura de doação de terras que faz Marquesa Ferreira aos padres da Companhia - Diz que fizera seu testamento e nele dissera que deixava ao Colégio desta Cidade a metade das terras que tinha em Guaratiba e Guarapirangua, para a parte de São Vicente. Por esta escritura faz a doação em vida, dizendo que seu marido [Cristóvão Monteiro] e ela e filho [Eliseu Monteiro] (já mortos) sempre tiveram vontade de lhas dar. Faz isso agora (Carta das terras de Guaratiba que deu Marquesa Ferreira que deus haja.

ABN, 82, 1962, pp. 155-156
Data - 1590
Descrição
Escritura de doação e troca de terras que fazem José Adorno e sua mulher Catarina Monteira com os padres da Companhia de Jesus - Escritura feita na Vila do Porto de Santos. José Adorno e sua mulher dizem que tinham umas terras no Rio de Janeiro, que herdaram por legítima herança de Marquesa Ferreira, mãe da dita Catarina Monteira e sogra dele, sitas onde se chama Guaratiba, das quais terras metade já era dos padres da Companhia de Jesus por doação feita pela dita Marquesa Ferreira em sua vida. A outra metade pertencia aos herdeiros. Por esta escritura doam aos padres da Companhia a outra metade. Em troca, os Padres trespassam aos doadores umas terras que tinham na Bertioga e 40 braças de chãos no arrabalde da Vila de Santos (Carta de troca das terras de Guaratiba que forão de José Fadorno (sic) com as da Bertioga.

AMSBRJ, Seção 6.2, Documentos 85, 150
Data - 1591
Descrição
Escritura de doação de terras que faz Jorge Ferreira, o velho, aos Religiosos de São Bento - uma ilha que está dentro do rio de Guaguaçu e 300 braças de terra ao longo do rio, as quais começarão a medir donde acabou Manoel Cisne, meirinho da igreja, e que assim e da maneira que se medir Manoel Cisne se medirão as 300 braças, assim ao longo do rio como para o sertão, com informação de que a ilha é uma ponta cercada de mangues, tudo herdado de sua filha Marquesa Ferreira (Escritura do 2º Ofício). Mosteiro toma posse dessas terras em 29/11/1591

VF, II, 108-109
Data - 1591
Descrição
Escritura de venda de terras que fazem os herdeiros de Cristóvão Monteiro aos Religiosos de São Bento - A sesmaria de meia légua de testada por costa, onde acaba o salgado, e duas léguas para o sertão correndo o rio acima com 750 braças para uma e outra banda do rio Iguaçu ficando este no meio (não fica claro se também foram compradas as terras de Manoel Gonçalves, que estavam nas cabeceiras das de Cristóvão Monteiro, mas tudo indica que sim pois as terras originais de Cristóvão Monteiro eram menores - AHU, RJ-Avulsos, Caixa 146 N° 17 confirma que beneditinos compraram as terras de Cristóvão Monteiro e de Manoel Gonçalves Sapateiro). (ABN, 82, 1962, p. 156, nota 21). Essas terras foram confirmadas pelo Governador Geral D. Francisco de Souza em 25/4/1602, que mandou que elas fossem medidas. Foram medidas em 1603, começando a medição na terra firme onde acabasse o salgado. Dessas terras venderam os beneditinos, antes de 1682, a Diogo Mendes Coluna, trezentas braças de largo e oitocentas de comprido, correndo do rio Morobaí (que é o rio do Pilar) para a barra do Iguaçu (em 1765 essas terras ainda estavam nas mãos dos herdeiros de Coluna). Em 7/6/1666 trocou também o mosteiro com Fernão Cabral de Melo mil braças de comprido e trezentas e cinquenta de largo, correndo pela margem do rio, e confrontando com terras do engenho do dito Cabral até a Tipueira, recebendo em troca outra sorte de terras de cento e oitenta braças de largo e mil e quinhentas de comprido em parte mais remota de sua propriedade. "Em 6/4/1799 escreveu o Conde de Resende uma carta ao Senado da Câmara pedindo informações sobre bens das comunidades religiosas ... A Câmara [enviou resposta]: No Iguaçu: possui o Mosteiro uma fazenda com meia légua de testada, começando no salgado, de uma e outra banda do rio chamado Iguaçu ficando este em meio, com 750 braças para cada lado, com duas léguas de comprido para o sertão, as quais foram doadas em sesmaria a Cristóvão Monteiro e o Mosteiro depois as houve por compra ...."
As questões referentes a estas terras dos beneditinos e seus confrontantes estão em AHU, RJ-Avulsos, Caixa 146, N° 17.

AMSBRJ, Seção 6.2, Documento 85
Data - 1593
Descrição
Escritura de venda de terras que fazem Jerônimo Monteiro e sua mulher aos Religiosos de São Bento, no valor de 44 réis, pagos metade em gado e metade em dinheiro. 
1.000 braças ao longo do rio de Goauaçu de comprido e 1.500 de largo, sendo 750 de cada banda do rio, terras que receberam de doação de Marquesa Ferreira por verba de seu testamento. Preço: 44$000, pagos metade em gado e metade em dinheiro. Como desta venda ficaram faltando 400 braças, o Mosteiro entrou na justiça e as recebe em 1597

ABN, Vol. 57, 1939, pp. 300-302; ADF, III, pp. 251-53; AGCRJ, Códice 2,4,9, p. 70, p. 72
Data - 1594
Descrição
Escritura de medição e partilha de terras entre o Colégio de Jesus, o Mosteiro de Nossa Senhora do Carmo e Manoel dos Rios - Recebem, meio a meio, as terras que pertenciam a Aires Fernandes Vitória. Em 15/3/1594 o Padre Luiz da Grã, procurador do Colégio de Jesus, pede que se parta a metade das terras que o Colégio herdara e que mandasse requerer aos Padres do Carmo e a Manoel dos Rios, como herdeiros confrontadores das ditas terras, e a Duarte Nunes e a Aleixo Manoel, como procuradores e partidores, para que viessem estar às partilhas e medição da dita terra. Escrivão vai no mesmo dia à Praia de Nossa Senhora do Ó e requer a Manoel dos Rios e a Duarte Nunes para estarem presentes à medição e partilhas. Vai também à casa de Aleixo Manoel e ao "Mosteiro da Casa de Nossa Senhora do Ó". A medição e partilha é feita em 16-17/3/1594 com a colocação de marcos que vão até um morro no sertão, rumo noroeste. Partidores Duarte Nunes e Aleixo Manoel aprovam. Ficaram então os padres da Companhia "para a banda do loloeste e os reverendos padres do Carmo e Manoel dos Rios para a banda do leste, para a banda do engenho de Magé, até entestarem com o rio de Iriri, e os reverendos padres de Jesus até entestarem com os marcos e medição de João Carrasco e seus herdeiros". Depois vão todos às casas de Aires Fernandes "que estão junto de Magé, entre o rio de Iririmirim (ou Cririmirim) e o rio de Iriri, por onde acabam 350 braças de terra de João Carrasco, onde está um marco de pedra, onde estava uma roça plantada de novo dos Padres do Carmo, o qual marco fica a loeste da dita roça, para a banda do Cresnimirim (ou Iririmirim). Começam a medir dali pelo rumo lesnordeste, correndo a costa do mar. Medem 950 braças até a boca do rio de Iriri, onde fica uma cruz junto a um mangue, onde acabou a medição do primeiro dia. No dia seguinte medem mais 450 braças, passando pelas casas dos escravos de Aires Fernandes. Então põem a agulha rumo do sertão a noroeste, "que é pelo meio das ditas 950 braças", o qual vai para a serra por um morro grande, para o que foi citado Aleixo Manoel, como procurador dos Padres de Nossa Senhora do Carmo. Manoel dos Rios também esteve presente, como hereo que era das ditas terras (AGCRJ, Códice 2-4-9, p. 78). Em 8/5/1595, carmelitas compram aos jesuítas por 60$000 umas terras em Magé (na realidade, Suruí), que o Colégio havia herdado por falecimento de Aires Fernandes Vitória. As terras partiam de uma banda com os próprios padres do Carmo e da outra com os herdeiros de João Carrasco, e tinham 475 braças por costa do mar e 1.500 para o sertão.


ABN, Vol. 57, 1939, pp. 300-302
Data - 1595
Descrição
Escritura de venda de terras que faz o Colégio de Jesus aos Religiosos de Nossa Senhora do Carmo, no valor de 60 réis - umas terras em Magé (Suruí), que o Colégio havia herdado por falecimento de Aires Fernandes Vitória. As terras partiam de uma banda com os próprios padres do Carmo e tinham 475 braças por costa do mar e 1500 para o sertão.

2LTMSBRJ, p. xvii
Data - 1596
Descrição
Escritura de consolidação da doação da capela de Nossa Senhora da Conceição e dos bens da irmandade de Nossa Senhora da Conceição que fazem Aleixo Manoel, o velho, e sua mulher Francisca da Costa, ao Mosteiro de São Bento – bens que compreendem meia légua de terras de testada e légua e meia de sertão, sitas à margem do rio Saracuruna, e dez vacas parideiras com suas crias. Essas terras corriam de uma banda com as do então falecido Manuel de Albernaz e, da outra, com terras de Domingos Machado e sua mulher Ana Rodrigues, que também doaram aos beneditinos, por escritura da mesma data, mais légua e meia de testada.
Observação: Nesse mesmo dia Manuel de Brito e sua mulher Dona Maria de Oliveira doam aos beneditinos a sua sesmaria.

AGCRJ, Códice 2-4-9, p. 26
Data - 1598
Descrição
Escritura de venda de terras que faz Aleixo da Costa a Manoel dos Rios, no valor de 8 réis – com 200 braças de testada e "mil duzentas e tantas de sertão", sitas no Rio Soroy, herdadas da legítima de sua mãe Felipa de Andrade. As terras eram parte da sesmaria de 1.000 braças de largo e 1.500 de sertão que seu pai Manoel da Costa, o velho, havia recebido em 19/11/1567. Informa-se que as terras ficavam nas cabeceiras das de Aires Fernandes, no rio de Iriri. Preço: 7$000. (Escritura do 1° Ofício). Em 15/4/1615, o mesmo Aleixo da Costa e sua mulher Susana Rodrigues vendem 800 braças de testada com uma légua de sertão, a Manoel dos Rios. Diz-se que ficavam "onde chamam Magé, no rio de Iriri, nas cabeceiras das terras que foram de Aires Fernandes, herdadas por falecimento de seu pai e mãe". Preço: 20$000 (Escritura do 1° Ofício). Em 9/12/1621 há um "Registro de uma escritura de venda de terras que fazem Pero de Campos Tourinho e sua mulher Margarida Furtada a Manoel dos Rios" - Trata-se de um pedaço de terra que Nicolau Baldim tinha das terras de 1 légua em quadra que Manoel da Costa recebera em Suruí. Ficavam (ao que parece) nas cabeceiras das terras que eram dos Padres do Carmo (e antes de Aires Fernandes). Nicolau Baldim herdara essa terra por parte de sua primeira mulher, Felipa de Andrade, filha do dito Manoel da Costa, de quem ficara viúvo. Casando segunda vez com Ana de Góis, que também faleceu sem filhos, metade das terras originalmente de Felipa de Andrade, couberam aos pais de Ana de Góis, os ditos Pero de Campos Tourinho e Margarida Furtada. É essa parte que foi então vendida por esta escritura, por preço de 8$000. Estas terras passarão depois ao Convento do Carmo.

ABN, 82, 1962, pp. 177-180
Data - 1602
Descrição
Escritura de aforamento de terras em perpétuo fatiosim que faz o Colégio de Jesus com Estevão Gomes e sua mulher Isabel Lopes - com meia légua em quadra, começando a medir "do fim do rumo das terras do dito Colégio que começam em Inhaúma. E se começará a medir a dita meia légua no fim das ditas terras, tornando do dito marco e fim da medição para trás pelo mesmo rumo de Inhaúma que vai correndo ao sudoeste, e há de tornar contra ao nordeste, medindo meia légua e no fim dela lhe botará o travessão em todo o que houver dentro na dita meia légua, a qual confronta de uma banda com o dito Colégio e da outra com o Capitão Gonçalo Correia de Sá e seu irmão Martim Correia de Sá....". Foro: 4,5% do açúcar moído, sendo duas partes de branco e uma de mascavado, tanto dos seus açúcares como das partes que no dito engenho fizer. E dos méis pagará também 4,5% anualmente. Obs.: É estabelecido prazo de 2 anos para ter o engenho moente e corrente, senão sofrerá penalidades. Poderá arrendar ou vender o engenho contanto que seja para pessoas de posse, para que o engenho vá por diante e não por diminuição. Estevão Gomes também se compromete a fazer "caminho por Inhaúma mais e melhor estiver donde na Peaçaba há de fazer huma caza para recolhimento dos açúcares e fábrica do engenho....". Esta escritura não teve efeito ("Escretura da terra que se deu a Estevão Gomes com huma água pera engenho. Não teve efeito.

ABN, 82, 1962, pp. 273-281
Data - 1602
Descrição
Escritura de aforamento em fateosim perpétuo que faz o Colégio de Jesus com Álvaro Fernandes Teixeira, cidadão desta cidade - "a água [rio] de Yebiracica [ou Birassica, ou Ubiracica] com seiscentas braças de terra que se começarão a medir pelo rio abaixo, rumo direito do pé da serra, e de largo em quadra outras seiscentas .. e pela serra acima a mesma largura até o fim da serra e medição dos referidos padres, a qual água e terra estão no termo e limite desta cidade...”. Aforamento é feito para que o dito Álvaro Fernandes Teixeira ali faça um engenho, com obrigação de tê-lo moente e corrente, feito na dita terra e água, em dois anos. Foro: 4% dos açúcares do engenho, a razão de 2 partes do branco e 1 do mascavado. Com declaração que não meterá nenhum lavrador nas ditas terras sem consentimento do Colégio, à exceção de seu irmão André Afonso e seu genro Fernão de Guirre (Aguirre). Com declaração de que fará cercas para que o gado do colégio não invada suas terras. Com obrigação de fazer no dito engenho ao dito Colégio cada ano 50 tarefas de cana, sem obrigação mais que o dito Colégio a cortar e por em parte que o carro a possa ir trazer.... Com declaração de que o dito Colégio dará ao dito Alvaro Fernandes Teixeira a piaçaba velha de São Cristóvão para serviço do dito engenho, onde fará uma casa para os açúcares e serviço do engenho.... E se vender terras pagarão a quarentena ao Colégio...." (Escritura do 2° Ofício) (In Aforamento em fatiosim que fizerão a Álv.° Frz. Teix.ra de M.ª légoa de terras e hua ágoa em Yebiracica pera engenho. In ABN, 82, 1962, pp. 181-183). Auto de medição das terras aforadas a Álvaro Fernandes Teixeira foi feito em 13/5/1602: "Fomos à água de Yubiracica abaixo, onde Álvaro Teixeira Fernandes há de fazer o engenho, e começamos a medir pelo rio abaixo, pelo caminho do norte e a quarta de nordeste, por onde fomos, até acabar de medir seiscentas braças que se acabaram ao pé de uma árvore que se chama urucurana, e da dita árvore, acabadas as ditas seiscentas braças, medimos trezentas braças pelo caminho de oeste e quarta de sueste que se acabaram na metade de uma roça de Luiz de Faria, onde se pôs um marco de pedra, e dali atravessamos para a serra fazendo o caminho do sul e quarta de sudoeste até sair ao caminho de carro com oitenta braças, e dali tornamos à árvore urucurana, onde se acabaram as primeiras seiscentas braças, e dela começaram outras duzentas pelo caminho de loeste e quarta de noroeste, nas quais acabamos de medir ao pé de uma árvore por nome andára-açu, donde se atravessou para a serra pelo caminho do sul e quarta de sudoeste, que se acabaram de medir as ditas seiscentas brács que se arrendaram a Álvaro Fernandes Teixeira ...." (Tombo dos Jesuítas, pp. 278-279). Em outro documento, de 30/4/1624, fala-se que as terras aforadas a Álvaro Fernandes Teixeira em 22/4/1602, que aí fizera o Engenho de Nossa Senhora de Guadalupe, eram no porto que chamam Maracom-a-Pobaga [à margem: Serra do Maracanã]. Este aforamento estava, em 1609, nas mãos de Duarte de Albuquerque de Melo, terceiro possuidor das ditas terras, que recebeu outras terras anexas à dada anterior. Em 1624 os Padres tinham um litígio com Baltazar Borges, que era o proprietário vizinho de suas terras. Em 1626, já tendo morrido Borges, faz-se a demarcação entre as duas terras, que já havia sido acordada antes. A medição começa em Maracanapoan [à margem: Serra de Maracanapoan], passa por Urucurana, pela fronteira com canaviais de Manoel do Couto e Manoel Veloso de Espinha (Escritura de composição entre o Coll.° e Baltazar Borges, na era de 1624).

AMSBRJ, Seção 6.2, Documentos 7, 41
Data - 1602
Descrição
Escritura de venda de terras que fazem Estevão de Araújo e sua mulher Catarina de Betancor, moradores na rua de Santo Antonio, aos Religiosos de São Bento, no valor de 4 réis – com 700 braças de largo e 1.000 braças de comprido ao longo do rio de Aguaçu, ficando o dito rio em meio, as quais se hão de começar a medir aonde acabar a primeira légua de Cristóvão Monteiro, defunto, que ora é dos ditos Padres, e daí por diante se encherão do comprimento das ditas 1.000 braças, partindo de uma banda com a terra que ora é dos ditos Padres e da outra com terra que diz Manoel Gomes que é sua, e da banda do nascimento do rio parte com o dito Manoel Gomes, terra que houveram por compra. Preço: 40$000 (Escritura do 1º Ofício)

AMSBRJ, Seção 6.2, Documentos 85, 171
Data - 1602
Descrição
Escritura de venda de terras que fazem Álvaro Fernandes Teixeira e sua mulher Maria de Azevedo ao Mosteiro de São Bento, no valor de 20 réis – com 200 braças de testada pelo rio de Aguaçu, que é no limite desta cidade, as quais 200 braças são de largo, ao longo do dito rio, e 700 de comprimento, partindo de uma banda com terras dos ditos reverendos padres e da outra com terras de Manoel Ribeiro e da outra com terras de Jerônimo Monteiro, compradas a Jerônimo Monteiro. Preço: 20$000 (Escritura do 1º Ofício).
Escritura feita nas pousadas dos vendedores, na praia de Nossa Senhora do Monte do Carmo.

AMSBRJRJ, Seção 6.2, Documentos 41, 85
Data - 1603
Descrição
Escritura de venda de terras que fazem Jerônimo Monteiro e sua mulher Maria de Faria (ou de Frias) ao Mosteiro de São Bento, no valor de 15 cruzados – com 100 braças de testada, sitas no rio de Guaguaçu, partindo de uma e de outra banda com terras dos reverendos padres. (Escritura do 2º Ofício). 
Os vendedores afirmam que já tinham doado 50 braças a seu cunhado Diogo Rodrigues.

AMSBRJRJ, Seção 6.2, Nº 75
Data - 1603
Descrição
Escritura de venda de terras que faz Diogo de Montarroio aos reverendos padres de São Bento – com 500 braças de testada, sitas junto à lagoa de Jundiá-Babu, nas cabeceiras e no mesmo rumo das terras compradas a Estevão de Araújo, terras compradas a Tomé de Alvarenga e a Manoel de Pontes.


AN, TCSRJ, 180-183
Data - 1603
Descrição
Escritura de doação de terras para instituição de patrimônio que faz Gonçalo de Aguiar ao Padre Martim Fernandes – Diz o Padre Martim Fernandes, vigário da Sé, que Gonçalo de Aguiar lhe deu 6.000 braças na fralda do outeiro de Gori-Sinonga ou Jorissinon [Gericinó], "duas léguas de terra na redondeza dele, em quatro meias ao pé do dito outeiro, para seu patrimônio, e porque agora algumas pessoas querem dar à carta de sesmaria ... de Gonçalo de Aguiar diferentes sentidos", tendo ele vigário tomado posse judicial da terra, pede reconfirmação, "começando a medir da outra banda da água do engenho de Manoel Gomes e Diogo de Montarroio e Diarroio(sic), com as águas que nas ditas terras se acharem. Recebe o que pede.

FF, p. 55, nota
Data - 1605
Descrição
Escritura de venda de terras que fazem Álvaro Gomes Osório e sua mulher Vitória de Mariz a Baltazar da Costa - as terras que se acharem da outra banda do rio de Suruí, com a largura que se achar que tiverem, com 500 braças, que se entenderá por um rumo direto para o sertão, começando-se a medir a terra do porto de Belchior Rodrigues, havidas por compra, com o dito engenho, de Antonio Cardoso de Barros, filho de Cristóvão de Barros. Preço: 30$000 (AGCRJ, Códice 2-4-9, p. 93). Obs.: Felisbelo Freire informa que "o engenho de Magé [de Cristóvão de Barros] passou ao filho de Cristóvão - Antonio Cardoso de Barros, que o vendeu a Aleixo (sic) Gomes Osório, que em 12 de abril de 1609 (sic) vendeu a Baltazar da Costa as terras pertencentes ao engenho e que ficavam de uma outra banda do rio Merery (sic)".

AMSBRJRJ , 6.2, Documento 85
Data - 1606
Descrição
Escritura de venda de terras que fazem Estevão de Araújo e sua mulher Catarina de Bitancur aos Religiosos de São Bento, no valor de 6 réis – com 50 braças de testada, sitas ao longo do rio de Guaguaçu, ficando ele em meio, onde os Padres acabaram de medir a sua data, e para cada banda 750 braças, o que faz 1.500 braças de largura, ficando o rio em meio, terras que haviam comprado a Francisco Carrasco e sua mulher Andreza Ramalha. (Escritura do 1º Ofício).


ABN, 82, 1962, pp. 273-276
Data -1609
Descrição
Escritura de acrescentamento de terras e diminuição de pensão que fazem os padres da Companhia, através do Padre Manoel de Lima, Visitador Geral, a Duarte de Albuquerque de Melo - Através desta escritura os padres acrescentam "às terras do Engenho de Nossa Senhora de Guadalupe, que primeiro foi de Álvaro Fernandes Teixeira e que ora é de Duarte de Albuquerque de Melo [terceiro possuidor dele], a terra que se achar do marco da primeira demarcação que se fez ao dito engenho à ponta da banda do Norte de uma água, de uma água que está além do arrozal que foi do Colégio, que demora mais ou menos do outeiro dos padres ao Nordeste e daí correndo rumo de loeste até o cume da serra, e assim mais lhe dava toda a terra que se achar ter o Colégio da casa de André Álvares para o engenho, e dará de lá rumo direito ao cume da serra que parte com Domingos Martins da terra que tem aforado ao Colégio. Satisfaz-se assim algumas dúvidas da primeira escritura. Foro também é reduzido, em relação à primeira escritura, passando a ser de 4% da metade de todo o açúcar macho que no dito engenho fizer. Nova escritura retira também de Duarte de Albuquerque a obrigação que o engenho tinha de 50 tarefas. Por esta escritura o Colégio pode agora dar 70 tarefas de canas plantadas nas terras do dito Colégio para serem moídas no engenho, obrigando-se também o Colégio a fornecer metade das lenhas, contidas nessas 70 tarefas 20 tarefas de cana de Domingos Martins (Escritura do 2° Ofício) (Apud ABN, 82, 1962, pp. 279-281). Obs.: Em 30/4/1624, o Colégio faz composição com Baltazar Borges, que foi o sucessor de Duarte de Albuquerque no aforamento. Pela escritura de composição, Baltazar Borges diz que aceita que na escritura de aforamento de Duarte de Albuquerque de Melo "aonde se diz que lhe dá do marco da primeira demarcação e medição até a ponta do outeiro grande, que está da parte do norte até além do arrozal que foi do dito Colégio, por este marco quer e é contente e se entenda aquele onde se acabaram as seiscentas braças que se começaram a medir junta com um engenho que Álvaro Fernandes fez nas ditas terras que se chama Nossa Senhora de Aguadelupe, pelo rio abaixo, pelo rumo do norte e quarta de nordeste, conforme a medição que se fez.... e bem assim é contente que pela ponta do dito oiteiro se entenda o cume dele, que é dos dois que tem o modo de sela o que fica da parte e banda do norte. Em contrapartida, por esta composição, Baltazar larga ao Colégio o domínio útil de um pedaço de terra plantada de cana que fazia parte da primeira data de Álvaro Fernandes Teixeira, que parte com o asseiro das canas e terra que Catarina de Faria tem junto ao canavial que o dito Baltazar vendeu ao dito Colégio por algum tempo por seiscentos mil réis, que terá cerca de 2 tarefas de cana. Colégio também larga a Baltazar Borges a terra e cana que se divide pelos asseiros dos canaviais que possui Manoel do Couto e Manoel Veloso, e daí correndo ao rumo do dito outeiro, como dito é, rumo direito, o qual pedaço de terra, exceto a da restinga, poderá levar duas ou três tarefas de cana .... (Escritura do 1° Ofício).


P. Freire, p. 59. Em nota, diz que a fonte é o Livro de Notas do 1° cartório do Rio, hoje do Tabelião Castro, de 1605-1609
Data - 1609
Descrição
Diogo de Amorim Soares vende o engenho que tinha na Lagoa a Sebastião Fagundes "da mesma maneira porque Sua Majestade lhe vendera".

6LTMSBRJ, p. 225
Data - 1609
Descrição
Escritura de doação de bens que fazem Baltazar Borges e sua mulher aos Religiosos de São Bento - umas terras, campos, dois currais de gado vacum e cavalar com 33 escravos. Sem localização.

AN, 1º Ofício de Notas, 26A, p. 17
Data - 1610
Descrição
Escritura de trespasse e composição que fazem o Provedor Diogo de Mariz e sua mulher Paula Rangel com Francisco Velho e sua mulher Luzia Martins - Provedor diz que ele e sua mulher possuíam na banda d’além, onde está o seu engenho, 200 braças de terra que pertenciam agora a Francisco Velho e à sua mulher por herança de sua filha, já defunta. Por esta escritura se ajustam, ficando as duzentas braças de volta a ele Provedor e sua mulher, os quais, em compensação, dão a Francisco Velho e sua mulher outras duzentas braças de testada ao longo do mar e uma légua de sertão, que confrontam com a data do sogro deste último João de São João, com as condições da escritura feita entre partes João de São João, Clara Martins, Sebastião Gomes e ele dito Diogo de Mariz. Fica acordado que Francisco Velho deixará os bois e cavalos do engenho pastarem nas ditas terras. Francisco Velho poderá plantar nas ditas terras até 50 tarefas de cana. O aforamento é por tempo de 9 anos depois de formado o canavial, pagando Francisco Velho 10$000 até que todas as tarefas forem plantadas e, depois disso, ficarão livres as terras do pagamento do foro ....

AN, 1º Ofício de Notas, 26A, p. 23
Data - 1610
Descrição
Escritura de venda de um partido de canas que fazem Afonso Gonçalves e sua mulher Maria Gonçalves a Pero da Silveira e sua mulher Leonor d’Orta, no valor de 70 réis – com benfeitorias de casas, roças, arrozais e tudo o mais que possuem, sito nas terras do Capitão Gonçalo Correia de Sá, em seu engenho da Tijuca.
Os vendedores recebem 10$000 de imediato e o restante virá em duas pagas, a saber: no primeiro corte que os compradores fizerem dos ditos canaviais lhe pagarão 30$000 em açúcar ou em dinheiro e os outros 30$000 quando fizerem a escritura definitiva. Gonçalo Correia de Sá, presente, desobriga o casal e seu filho João Gonçalves da obrigação que tinham assumido e transfere-a para Pero da Silveira e sua mulher. Por esta última assina seu pai Manoel Dias Leitão.

AN, 1º Ofício de Notas, 26A, p. 35v
Data - 1610
Descrição
Escritura de débito que faz Álvaro Fernandes Teixeira a Antonio Franco - Diz Álvaro que ele devia a Antonio Franco 428$530 em dinheiro de contado ou em açúcares brancos e mascavados. Por esta escritura se compromete a fazer o primeiro pagamento em agosto de 1610, com oito caixões de açúcares, quatro brancos e quatro mascavados, postos nesta cidade encaixados, e o mais restante de toda a quantia lhe acabará de pagar no mês de agosto de 1611, o qual dinheiro o dito Álvaro Fernandes Teixeira lhe paga a ele Antonio Franco para Baltazar Borges, por razão de comprar um engenho a Duarte de Albuquerque de Melo, que era o principal devedor da dita dívida, para o que o dito Antonio deu por quite ao dito Duarte de Albuquerque da dita quantia de hoje para todo sempre. E por Baltazar Borges foi dito que já que Álvaro Fernandes Teixeira lhe pagava esta dívida por ele a Antonio Franco se obrigava a tirar paz e a salvo da dita quantia.

AN, 1º Ofício de Notas, 26A, p. 43
Data -1610
Descrição
Escritura de venda de um engenho que fazem Álvaro Fernandes Teixeira e sua mulher Maria de Azevedo a Estevão Gomes, 2625 cruzados, a serem pagos em 4 anos. Trata-se de um engenho trapiche da invocação de Nossa Senhora das Neves, sito no lugar chamado Liriosoca (ou Lixiosoca), termo desta cidade, com as seguintes confrontações: parte da banda do nascente com o mar salgado e da banda do nordeste com terras dele dito comprador, e da outra banda com o rio de Meriti e da outra banda com terras dele dito comprador e com as mais terras com quem direitamente devam partir. O engenho tem quatro caldeiras [uma desarmada velha] e as outras três armadas, três tachos velhos, três [escumadeiras], três pombas, uma repuxadeira e uma batedeira ... de cobre, a casa de purgar... a olaria com seu forno e com todas as casas que se [acharem no] dito engenho, com toda a mais fábrica dele... com todos os bois mansos que se acharem tirados quatro que daí se hão de tirar e para encherem número de setenta bois... com dez peças de escravos de Guiné... com as obrigações dos partidos [das Escrituras] que tinha feito (uma de 25 tarefas de cana a Duarte Rabelo e outra de 12 tarefas a Fernão de Oliveira) .....", comprado a Baltazar Borges.

AN, 1º Ofício de Notas, 26A, p. 62
Data - 1610
Descrição
Escritura de partido que fazem Baltazar Borges e sua mulher Prudência Veloso a Francisco de Pina e sua mulher Francisca do Amaral - Baltazar Borges era dono de engenho situado nas terras de Birasica. Por esta escritura faz a obrigação de 20 tarefas de vinte e quatro carros cada, bem cheios, com obrigação também de dar a metade da lenha necessária à moagem da cana, em lugar em que se possa facilmente mandar buscar. Obrigação por tempo de três nove anos. Demais obrigações são as costumeiras. As terras alocadas a Pina começavam "indo pelo caminho desta cidade para o engenho, onde começou de roçar e hoje é roça e capoeiras, o padre Manoel da Costa já defunto e Manoel Fernandes Cavaco, correndo pelo dito caminho que [vai] para o engenho, tudo o que constar que roçou o dito padre e Manoel Fernandes e seu cunhado Francisco Viegas e toda a largura que há ao [longo] do dito caminho, irá correndo rumo direito por [uma] e por outra banda até o cume da serra [e ficando] para alguma das ilhargas algum mato que fosse roçado pelos ditos padre e Manoel Fernandes e Francisco [Viegas] o davam também ao dito Francisco de Pina, para [nelas haver] de fazer canas ou suas roçarias ... e sendo caso que [Baltazar] da Costa não fosse fazer cana no dito [engenho] deles ditos Baltazar Borges e sua mulher como [assim achavam] que fosse, davam ao dito Francisco de Pina [mais ...] tarefas de obrigação com as mesmas [condições ...] e assim mais toda a terra para [nela plantar] com os mais e fazer seus [mantimentos que] houver pelo dito caminho..... Tijuca e engenho até a [capoeira] que foi de [Fernão de Guaia] já defunto e para o cume da serra tudo o que houver".
Escritura não teve efeito, sendo substituída por outra de 18/8/1610

AN, 1º Ofício de Notas, 26A, p. 54v
Data - 1610
Descrição
Escritura de obrigação que fazem João Gomes da Silva, por si e como procurador de seu sogro Diogo de Mariz e de sua sogra Paula Rangel, e sua mulher Maria de Mariz com Antonio de Mariz e sua mulher Simoa Damini – Dizem que são possuidores do engenho de Nossa Senhora das Neves, sito na banda d’além. Por esta escritura Antonio de Mariz e sua mulher, que têm um partido nas terras do dito engenho, herdado por falecimento de seus pais, se obrigam a dar ao dito engenho, do ano de 1612 em diante, vinte tarefas de cana todos os anos, cortada no canavial, e a lenha necessária, posta em parte que os carros possam comodamente tomar, feitas nas ditas suas terras ou nas do engenho.

AN, 1º Ofício de Notas, 26A, p. 60v; AN, TCSRJ, Introdução, p. xvi
Data - 1610
Descrição
Escritura de venda de terras que fazem Frutuoso da Fonseca e sua mulher Isabel Furtada a Estevão Gomes, no valor de 32 réis - com 200 braças de testada e 600 de sertão, sitas nas vertentes desta cidade, ao longo do rio de Meriti e Upecouna.

AN, 1º Ofício de Notas, 26A, p. 67
Data - 1610
Descrição
Escritura de dote de terras que faz Gabriel Delgado a Antonio Fernandes, para casar com sua sobrinha Maria Batista, órfã de Agostinho Batista, com licença do Juiz dos Órfãos Luiz Cabral de Távora - as terras que a dita órfã herdara de seu pai e mãe, as quais estão na banda d’além, em Guarapetinga, junto do engenho de Gonçalo Gonçalves [caput diz Piratininga]. Doa também chãos na cidade.


AN, 1º Ofício de Notas, 26A, p. 100; AN, TCSRJ, Introdução, p. xvii
Data - 1610
Descrição
Escritura de dote de casamento que fazem Lázaro Fernandes e sua mulher Potência Brás a Pero Bentes de Souza, por casar-se com Francisca Rodrigues, filha do primeiro casamento da doadora com Pero Gonçalves - além de chãos na cidade, 200 braças de terras sitas ao longo do mar e meia légua de sertão, sitas na data de Curuará, junto ao cunhado do dito Pero Bentes de Souza, havidas por carta de sesmaria que lhes ficou de seu antecessor [Pero Gonçalves], e se entenderá onde Manoel de Abreu acabar, ao longo do mar, vindo medindo para a parte de Curuará. Doam também vinte e cinco tarefas de canas, pouco mais ou menos, com obrigação feita por escritura assinada com Manoel Gomes e seu genro Diogo de Montarroio, senhorios do engenho por nome São Diogo [sito em Gericinó]. A doação do partido é apenas pelo tempo da escritura já celebrada com os senhorios, de dois nove anos.

AN, 1º Ofício de Notas, 26A, p. 129
Data - 1610
Descrição
Escritura de partido de trinta tarefas de canas que fazem Baltazar Borges e sua mulher Prudência Veloso, donos do engenho de Nossa Senhora do Guadalupe, que está nas terras de Ubiracica, com Francisco de Pina e sua mulher [Francisca do Amaral] - Estes últimos se obrigam a fazer nas terras do engenho trinta tarefas de canas de açúcar em cada safra do ano. Demais condições são as habituais. Senhorio ficará com metade do açúcar. Obrigação é por três nove anos. Proprietários do engenho dão licença para que a cana seja plantada "em uma sorte de terra em que [ora] estavam que foi de Manoel Fernandes Cavaco que [foi] deles senhorios a qual terra começava, vindo do caminho da cidade para este engenho que [corre] com André Afonso, correndo a serra e [indo] pelo caminho do dito engenho até onde [os têm] eles ditos Francisco de Pina e sua mulher um [canavial] e no cabo dele correrá rumo direito entre eles e André Afonso a um bananal que está ao pé da serra que é do dito André Afonso e daí rumo direito até o cume da serra..." Francisco de Pina se obrigava a fazer os caminhos "para os (carros de boi) poderem ir tomar aos canaviais (as canas)".

AN, 1º Ofício de Notas, 26A, p. 12v; D. Leite de Macedo, Introdução, AN, TCSRJ, p. xii
Data - 1610
Descrição
Escritura de dote de casamento que fazem Belchior da Ponte [Maciel] e sua mulher Inês Gonçalves (ou Fernandes - Rheingantz, I, 91) em favor de João Pereira, para se casar com sua filha Margarida Cardoso - Dentre os bens que lhe deixam estão sete escravos do gentio de Guiné, as casas em que [eles] ditos doadores ora moram e 40 tarefas de partidos de canas de açúcar no engenho de Estevão Gomes, obrigando-se o dito João Pereira a plantar neste ano vinte tarefas e no ano que vem outra folha de outras vinte tarefas. Plantará também uma roça de mantimentos das que têm os ditos dotadores, com vinte mil covas de mandioca, a qual roça está no Guaguaçu no outeiro, e por conseguinte outra tanta terra no dito Guaguaçu das que eles ditos dotadores possuem, [a mesma quantidade que] deram a Belchior de Andrade, seu primeiro genro.

AN, 1º Ofício de Notas, 26A, p. 3
Data - 1610
Descrição
Escritura de partido que fazem João Gomes da Silva, por si e como procurador de seu sogro Diogo de Mariz e de sua sogra Paula Rangel, e sua mulher Maria de Mariz com Francisco de Lemos de Azevedo [e sua mulher Branca do Porto], João Barbosa Calheiros [e sua mulher Antonia de Oliveira] e Gaspar Rangel [e sua mulher Isabel Baldez] - São donos do engenho de Nossa Senhora das Neves, na banda d’além, na terra do Guaguaral. Por esta escritura informa-se que Manoel dos Rios tinha um partido nessas terras, que dera de dote a seu genro Sebastião Lobo, o qual, por sua vez, vendera-o a Francisco de Lemos de Azevedo. Também tinham partido nas terras os outros dois, João Barbosa Calheiros e Gaspar Rangel. Como as escrituras de todos tinham nulidades, resolvem se concertar por esta da seguinte forma: o dito João Gomes da Silva e sua mulher, por si e como procuradores de seus sogros e pais, obrigam-se a moer no dito engenho a Francisco de Lemos de Azevedo trinta tarefas de cana a cada ano, redondas, do seu partido, cortadas no canavial e onde as mandava buscar o senhor de engenho com seus bois e carros, carregando-as o dito lavrador Francisco de Lemos, e não lhas moendo lhe pagará as que ficarem por moer ou como as mais renderem naquele ano, e ele dito lavrador se obriga a lhe dar as ditas trinta tarefas de cana e duas partes da lenha para se moer, e faltando com algumas tarefas das trinta que tem de obrigação, lhas pagará ao senhor de engenho como renderem as mais daquele ano, e as lenhas as fará onde lhe for nomeado e as porá em parte donde os carros com comodidade as possam ir buscar. Esta escritura começará a valer de 1612 em diante e o trato valerá por três nove anos, no cabo dos quais os resíduos das benfeitorias que sobrarem ficarão ao engenho. O mesmo trato é feito com João Barbosa Calheiros e sua mulher Antonia de Oliveira, relativo a vinte e cinco tarefas de cana cada ano, e a Gaspar Rangel e sua mulher Isabel Baldez, relativo também a vinte e cinco tarefas a cada ano. Todos poderão plantar roçarias e canaviais para sustento dos ditos partidos e de sua gente. Com condição que, querendo eles vender os ditos partidos, poderão fazê-lo, e querendo o senhor de engenho vender suas terras, também poderá fazê-lo.

AN, 1º Ofício de Notas, 26A, p. 5
Data - 1610
Descrição
Escritura de obrigação que fazem João Gomes da Silva, por si e como procurador de seu sogro Diogo de Mariz e de sua sogra Paula Rangel, e sua mulher Maria de Mariz com Francisco de Mariz e sua mulher Ângela dos Banhos - Francisco de Mariz diz que possui na banda d’além, no sítio do engenho de Nossa Senhora das Neves, 200 braças que havia herdado de seu pai. Como fora para o Espírito Santo, e não sabendo onde ficariam essas terras deixara ordem a seu irmão Diogo de Mariz para que comprasse um partido que Amaro de Barros tinha nas ditas terras, o qual lhe comprou. Como a escritura de partido estava nula, faz esta, que segue as mesmas condições da escritura de Francisco de Lemos e outros, relativa a vinte e cinco tarefas. Por esta escritura, Francisco de Mariz permite também que os gados do engenho possam pastar em suas terras, podendo, por outro lado, tirar madeiras e trazer bois e cavalos nas terras do engenho.

ABN, 82, 1962, pp. 254-255
Data - 1611
Descrição
Escritura de troca de terras e chãos que faz o Colégio de Jesus com Fernão Baldez e sua mulher Ana Dias - Colégio troca parte da sesmaria de Macacu "começando da boca do rio de Tambeí até o rio de Cacerebu e indo por ele arriba té chegar o rio de Iguá e pelo dito rio de Igoá arriba até chegar ao cabo das terras que os ditos padres têm daquela banda .. e daí por ela torna até chegar ao rio de Tambeí", por chãos que pertenceram à antiga sesmaria de Aires Fernandes, que ficavam na "Várgea de Nossa Senhora do Ó desta cidade, os quais estam na Rua Direita que vai da Misericórdia ao longo da Praya pera a dita Senhora, que está na do canto a canto das casas de Gaspar Rangel, seu genro, e as casas dos ditos reverendos padres, tudo o que se achar, com o quintal que se achar para dentro..." (Escretura de trespaçasão de terras e chãos que fês Fernão Baldes e sua mulher ao Collégio.

AN, 1º Ofício de Notas, 28, p. 19; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de venda de terras que fazem os padres da Companhia de Jesus a Jacques Motete, pagamento em 500 alqueires de farinha. Tratam-se de terras com 400 braças de testada e 1.000 de sertão, sitas no rio de Casarabu, começando-se a medir onde acabam as 300 braças de Francisco da Costa, pelas mesmas confrontações e rumos de Vicente Gonçalves, serralheiro, partindo com Gaspar Rangel, com condição de o comprador ser obrigado a dar serventia para as terras das cabeceiras. Preço: 600 alqueires de farinha. Com declaração de que será obrigado a dar serventia, porto e caminho às terras que ficarem nas cabeceiras das ditas terras, e que havendo mais terra até a casa de Gaspar Rangel ele Jacques Motete a pagará e havendo menos o Colégio lhe tornará.

AN, 1º Ofício de Notas, 28, p. 18; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de venda de terras que fazem os padres da Companhia de Jesus a Alexandre Lopes, no valor de 40 réis – com 500 braças de testada e 1.000 de sertão, sitas no Agoapyacu, pegado com Miguel Grasia, no porto das pedras, com as mesmas confrontações de Miguel Grasia, começando-se a medir a testada do dito porto das pedras, e obrigação de dar serventia, porto e caminho para as terras das cabeceiras.

AN, 1º Ofício de Notas, 28; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de dote de casamento que fazem Miguel Árias Maldonado e sua mulher Maria de Medeiros a Francisco Cabral de Távora com sua filha Maria Maldonada - além de chãos e casas na cidade, doam toda a fazenda, canaviais e mais benfeitorias que têm na Tijuca ..., diversos escravos, e uma dada de terras na Goxandiba e Angra dos Reis.
AN, 1º Ofício de Notas, 28, p. 38v; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de venda de um partido de canas que faz Antonio Bandeira a Francisco de Mariz, no valor de 270 réis - com obrigação de 25 tarefas anuais, sito no engenho de mão de que é senhor Álvaro Gomes Osório, em Magé. Vende também as benfeitorias (roças, mandiocal, casas, bananais, junta de bois com seu carro, uma roda de mandioca).

AN, 1º Ofício de Notas, 28, p. 37v; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de venda de terras que fazem os reverendos padres de São Bento a Antonio João, flamengo, e sua mulher Felipa Ramalho, no valor de 50 réis - uma ponta de terra sita na boca do rio de Saracuruna, havida por herança de Brites da Costa.

AN, 1º Ofício de Notas, 27, p. 33v, p. 16; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de venda de terras que fazem os padres da Companhia de Jesus a Gaspar Rangel, no valor de 70 réis - com 500 braças de testada e 1.500 de sertão, sitas no Casarabu, "indo pela barra do mar arriba, começando na primeira ponta donde ora tem começado a roçar, pelos rumos e confrontações que as de Jacques Motete".

AN, 1º Ofício de Notas, 28, p. 29; AGCRJ, Códice 42-3-55, p. 15
Data - 1612
Descrição
Escritura de doação de terras que fazem Domingos Nunes Sardinha e sua mulher Maria da Cunha à sua ermida de Nossa Senhora das Neves – com 500 braças em quadra, sitas em Jaguaré.

AN, 1º Ofício de Notas, 27, p. 53; AGCRJ, Códice 42-3-55, p. 20
Data - 1612
Descrição
Escritura de quitação de um partido de cana que faz Nicolau Barreto a João Gomes da Silva - com casas e benfeitorias, sito no engenho de Álvaro Gomes Osório em Magé.

AN, 1º Ofício de Notas, 27, p. 70; AGCRJ, Códice 42-3-55, p. 21
Data - 1612
Descrição
Escritura de venda de terras que fazem Fernão de Sauzedo Coronel e sua mulher Margarida Fernandes a Miguel Gomes Bravo, no valor de 9 réis  – com 150 braças em quadra, sitas em Mereti, partindo de uma banda com Diogo de Medina e da outra com o comprador.

CAMSBRJRJ, p. 46
Data - 1612
Descrição
Escritura de doação de terras que fazem Belchior Tavares e sua mulher Margarida de Figueiredo aos Religiosos de São Bento – com duas léguas em quadra, sitas onde chamam Jerepetiba ou Inaiatiba, correndo os campos e matos de Juiari para Tamanduá, e olha para o Guandu, recebidas pelos vendedores, juntamente com Pedro Luiz Ferreira, por carta de sesmaria de 9/9/1591. Mosteiro toma posse dessas terras em 13/5/1612.

AN, 1º Ofício de Notas, 27, p. 10v; AGCRJ, Códice 42-3-55, p. 13; Rheingantz, I, 226
Data - 1612
Descrição
Escritura de venda de terras que fazem Roque Barreto [ex-capitão de São Vicente] e sua mulher [Ana Moreira(sic), filha de Jorge Ferreira, também ex-capitão de São Vicente] a seu irmão Nicolau Barreto – com 300 braças de testada, sitas em seu engenho de Nossa Senhora das Neves.

AN, 1º Ofício de Notas, 27, p. 14v; AGCRJ, Códice 42-3-55, p. 14
Data - 1612
Descrição
Escritura de doação de um partido de canas que faz Álvaro Barreto e sua mulher Luiza Reis a seus filhos Diogo Rodrigues e Maria Barreto – partido comprado a Antonio de Mariz.


AN, 1º Ofício de Notas, 28, p. 9; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de obrigação e concerto entre Francisco do Rego e Bento Garcez - recebendo este "de amor em graça", por 9 anos, um canavial que Francisco do Rego tinha em suas terras e no seu porto junto do mar, nas suas terras da costa de Pernoagua, termo desta cidade.

AN, 1º Ofício de Notas, 28, p. 10; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de venda de um partido de canas que fazem Francisco Pais Ferreira e sua mulher Maria da Cunha a Mateus Jaques - partido de 20 tarefas, sito no engenho de Nossa Senhora da Vitória, no termo desta cidade onde chamam Pabuna.

AN, 1º Ofício de Notas, 28, p. 12; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de obrigação que fazem Francisco Pais Ferreira e sua mulher Maria da Cunha com Domingos de Aguiar – para moer suas canas no engenho de Nossa Senhora da Vitória. Escritura não teve efeito.

AN, 1º Ofício de Notas, 28, p. 13v; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de obrigação de um partido de canas que fazem Francisco Pais Ferreira e sua mulher Maria da Cunha a João Rodrigues Faleiro e sua mulher Margarida da Costa – sito no engenho de Nossa Senhora da Vitória, no termo desta cidade onde chamam Pabuna. Não teve efeito.

AN, 1º Ofício de Notas, 28, p. 15; AGCRJ, Códice 42-3-55
Data – 1612
Descrição
Escritura de obrigação de um partido de canas que fazem Francisco Pais Ferreira e sua mulher Maria da Cunha a Brás Pereira e sua mulher Francisca Gata - partido de 20 tarefas, no engenho de Nossa Senhora da Vitória, no termo desta cidade onde chamam Pabuna. A escritura não teve efeito.

AN, 1º Ofício de Notas, 28, p. 16; AGCRJ, Códice 42-3-55
Data - 1612
Descrição
Escritura de obrigação de um partido de canas que fazem Francisco Pais Ferreira e sua mulher Maria da Cunha a Francisco [Rheingantz diz ser Antonio] Bogado e sua mulher Leocádia Fagundes - partido de 20 tarefas, no engenho de Nossa Senhora da Vitória, no termo desta cidade onde chamam Pabuna.

AN, 1º Ofício de Notas, 28
Data - 1613
Descrição
Escritura de concerto feita entre Sebastião Fagundes, senhor do engenho de Nossa Senhora da Encarnação do Rosário, sito na Lagoa, termo desta cidade, e Mateus Antonio, mestre de açúcar. Combinam o pagamento deste último "e sendo caso que ele dito senhorio do engenho tenha e haja o engenho de Martim de Sá, sito na dita alagoa, por este tempo ao diante lhe pagará por cada tarefa das canas da obrigação do dito engenho 1$000".

AN, 1º Ofício de Notas, 28, p. 62; AGCRJ, Códice 42-3-55, p. 29
Data – 1613
Descrição
Escritura de dote e casamento que fazem Francisco da Costa, torneiro, e sua mulher Felipa Nunes a Pedro Rodrigues Funchal e sua mulher Marta de Miranda – Além de casas urbanas, doam também 500 alqueires de farinha de guerra e umas casas de engenho de que já estava de posse.

AN, 1º Ofício de Notas, 28, p. 64; AGCRJ, Códice 42-3-55, p. 29
Data – 1613
Descrição
Escritura de venda de terras que fazem Miguel Gomes Bravo e sua mulher Isabel Pedrosa [de Gouveia] a Manoel da Ponte - sitas no rio de Meriti, compradas a uma sua tia. (Escritura parece não ter tido efeito).

AN, 1º Ofício de Notas, 28, p. 64v; AGCRJ, Códice 42-3-55, p. 29
Data - 1613
Descrição
Escritura de venda de terras que fazem Sebastião Lobo Pereira, juiz ordinário, e sua mulher Isabel dos Rios, a Miguel Aires Maldonado, no valor de 70 réis – com 1.000 braças em quadra, sitas no rio de Guaxindiba, acima da data de Diogo Teixeira [de Carvalho], havidas por dote de seu sogro Manoel dos Rios, pai da vendedora, as quais o dito Manoel dos Rios havia comprado a Antonio Gomes Vitória, e que haviam sido antes de seu sogro Gastão Franco, que Deus tem.
Observação: A escritura contém um termo de consentimento de Álvaro Fernandes Teixeira e sua mulher Maria de Azevedo, que desistem da contenda que tinham com Antonio Gomes Vitória sobre essas terras.

AN, 1º Ofício de Notas, 28, p. 69; AGCRJ, Códice 42-3-55, p. 30
Data - 1613
Descrição
Escritura de aforamento de terras e obrigação que fazem Bartolomeu Fernandes e sua mulher Maria Ferreira de Bulhões com Antonio Bandeira Rocha e sua mulher Dorotéia da Silva - Antonio Bandeira e sua mulher informam que querem fazer um engenho de três paus nas suas terras de Guaguaçu, em uma tapera e ilha por nome Jaguaripe, mas que só podem fazê-lo com a ajuda de 200 braças de terras pertencentes a Bartolomeu Fernandes e sua mulher. Por esta escritura este último casal afora as ditas 200 braças por 3 nove anos, com foro anual de 2% do açúcar que fizerem no dito engenho depois de dizimado. Ao mesmo tempo, Bartolomeu e sua mulher fazem contrato com Antonio Bandeira pelo qual se obrigam a dar 15 tarefas anuais de cana ao dito engenho. Na mesma escritura, Antonio Fernandes Atão também se obriga a dar as 15 tarefas (não sei se são as mesmas de Bartolomeu) ao engenho, por tempo de 3 nove anos.

AN, 1º Ofício de Notas, 28, p. 98; AGCRJ, Códice 42-3-55, p. 33; AMSBRJ, Seção 6.2, Documento 64
Data - 1613
Descrição
Escritura de venda de duas sortes de terras que fazem Tomé de Alvarenga e sua mulher Maria de Mariz aos Religiosos de São Bento, no valor de 110 réis - sitas no Rio de Guaguaçu, uma de 600 braças de comprido e 750 de largo, que é onde está Nuno Vaz e Saavedra e seu genro, que houveram por título de compra dos Padres de São Bento e a outra logo pegado à primeira, para a banda do sertão, que tem 1.200 braças de comprido e 750 de largo, a qual possuíam por carta de sesmaria do Governador Salvador de Sá [de 20/6/1570, doada a Tomé de Alvarenga].
Observações: no caput do documento do Mosteiro está escrito: "no rio de Iguaçu, onde chamam a Tipuera ou Guatinguá, que correndo pelas costas de outra do Mosteiro que ficam pela margem do rio e foram da sesmaria de Cristóvão Monteiro".

AN, 1º Ofício de Notas, 28, p. 73; AGCRJ, Códice 42-3-55, p. 30
Data – 1613
Descrição
Escritura de venda de terras que faz Manoel Antunes, capitão da vila de Angra dos Reis, por si e como procurador de sua mulher Clara de Oliveira, a Pedro Luiz Ferreira, no valor de 50 réis - uma dada de terra sita na Guaratiba, que começa a medir do rio de Curumaí para o nordeste até dar no morro de Sernãobetiba, que está na praia que vai da Teiuqua, e para o sertão 1 légua, além de 7 vacas parideiras.

6LTMSBRJ, p. 225
Data - 1613
Descrição
Escritura de venda de terras que faz Maria Soares aos Religiosos de São Bento - terras que foram de Domingos Nunes.

6LTMSBRJ, p. 225
Data – 1613
Descrição
Escritura de doação de terras que faz ... aos Religiosos de São Bento - sitas na Barra de Maricá com currais de gado.

6LTMSBRJ, p. 238
Data - 1615
Descrição
Escritura de venda de terras que fazem Manoel Pontes e sua mulher Joana Lopes aos religiosos de São Bento - com 300 braças de largo e 750 de comprido, sitas na Tipueira, terras que foram de Tomé de Alvarenga, ficando assim com toda a extensão original da sesmaria de Alvarenga, que era de 1500 braças em quadra. Preço: 10 novilhos.
Observações: Nas costas dessa data o Mosteiro comprou de André Afonso, em 8/9/1646, 1.000 braças de testada e 1500 de sertão, no Iguaçu onde chamam Baby, nas cabeceiras de Duarte Martins Mourão (Essas terras estavam tomadas por invasores em 1765, apesar da posse que foi tomada pelo Mosteiro). Preço: 10 novilhos.

AN, 1º Ofício de Notas, 28; Códice 42-4-88, p. 754; AGCRJ, Códice 42-4-89, p. 919
Data -1615
Descrição
Escritura de aforamento de terras que faz o Padre Fernão Cardim, reitor do Colégio de Jesus, ao Licenciado Manoel Dias - "uma terra que o dito Colégio tem desde o marco de Domingos Correia, que é da parte do caminho que vai desta cidade para a casa do dito Domingos Correia, do caminho para cima, rumo direito à serra, até entestar com terras de Baltazar Borges, para nelas fazer uma, duas ou mais moendas de fazer açúcar de três paus. Aforamento por 3 anos. Valor: 2% de todo o açúcar em cada ano.

AN, 1º Ofício de Notas, Livro 29; AGCRJ, Códice 42-4-88, p. 753; AGCRJ, Códice 42-4-89, p. 917
Data - 1615
Descrição
Escritura de venda de terras que faz Cecília Gaga a Simão Leitão - terras que possui por carta de sesmaria, que ficaram por morte de seu marido Francisco Dias Pinto, e que tinham sido antes do pai dele Diogo Fernandes Pinto, que as obtivera por carta de sesmaria. A doação original era de 2 léguas de costa na Guaratiba por 3 de sertão, tendo em meio a barra chamada da Guaratiba. Por esta escritura vende a parte que herdou de seu marido.

AGCRJ, Códice 42-4-88, p. 753; AGCRJ, Códice 42-4-89, p. 918
Data – 1615
Descrição
Escritura de venda do direito que têm sobre terras que fazem Bento Dias e sua mulher Margarida de Atouguia a Simão Leitão - sitas na Guaratiba, as quais foram dadas por sesmaria a seu sogro Diogo Fernandes Pinto, pai de Inês Pinta, com quem o vendedor foi casado em primeiras núpcias. Vendem também a parte que coube a sua segunda mulher, Margarida de Atouguia, que a houvera por morte de seu primeiro marido Baltazar Pinto, também filho do dito Diogo Fernandes Pinto.

AGCRJ, Códice 42-4-89, p. 917
Data - 1615
Descrição
Escritura de venda de um partido de canas que faz Francisca do Amaral ao Licenciado Manoel Dias, no valor de 150 réis – sito nas terras do engenho de Baltazar Borges, de invocação Nossa Senhora de Guadalupe, aonde chamam Maracanapoão.

ABN, Vol. 57, 1939, pp. 242-244
Data - 1616
Descrição
Escritura de doação de terras que fazem Pedro Luiz Ferreira e sua mulher Bárbara de Brito aos reverendos padres do Carmo - sitas em Soruhy, a saber entre o Rio de Soruhy até confrontar com os reverendos padres (Carmelitas), e todo o mais sertão que se achar...", terras que estavam arrendadas a Gaspar Rodrigues por dois nove anos, e que são agora doadas em troca de várias obrigações religiosas (missas, sepulturas, etc.) (Treslado da doassão q’ nos fez [Pedro] Luiz Fr.ª e sua Mulher Barbora de Brito de huas terras no Rio de Suruhy. 1616. In ABN, Vol. 57, 1939, pp.229-232; AGCRJ, Códice 2-4-9, p. 87v).
Os padres tomam posse dessas terras em 17/10/1616, numa olaria que estava nas ditas terras. (Auto de Posse.... Idem, pp. 232-233). As terras haviam sido aforadas pelo casal a Gaspar Rodrigues em 30/1/1614 e tinham "duzentas e tantas braças de costa as quais começão a medir do dito Rio do cabo dele para a banda da fazenda dos Padres do Carmo e para o sertão são oitocentas braças" (Tombo dos Carmelitas, pp. 391-392). Em 1634 Carmelitas já tinham um engenho nessas terras de Suruí. Por documento de litígio entre essas terras e as de Prudêncio Ramalho fica-se sabendo um pouco das obrigações a que estavam sujeitos os "lavradores" das terras de outrem. Como na nova demarcação, viu-se que duas tarefas de cana de Prudêncio estavam plantadas nas terras dos padres, Prudêncio aceitou, no que dizia respeito, a essas duas tarefas, as obrigações de lavrador: ".... eles partes se convieram ... em que as ditas duas tarefas de canas fossem obrigatórias ao engenho dos ditos reverendos padres ficando ele dito Prudêncio Ramalho lavrador do dito engenho com obrigação de dar toda lenha para moerem as ditas duas tarefas de cana debaixo da obrigação de lavrador, a qual obrigação das ditas duas tarefas de cana dará ele lavrador ao engenho enquanto a terra der a dita cana e a tiver, e for capaz de dar...." (Treslado da Escritura de compozição amigavelmente feita emtre os Reverendos P. P. do Carmo e Prudêncio Ramalho no Rio de Sorohy - 1634.

Eduardo Marques Peixoto, Apontamentos sobre a freguesia de Guaratiba. RIHGB, Tomo 67, Parte II, 1905, p. 244
Data - 1616
Descrição
Escritura de venda de terras que fazem Manoel Veloso [de Espinha] e sua mulher Isabel de Betancor e Jerônimo Veloso [Cubas] e sua mulher Beatriz Álvares [Gaga], filhos e noras de Manoel Veloso de Espinha, aos reverendos padres da Companhia, no valor de 60 réis – com 500 braças de testada e 1.500 de sertão, sitas em Guaratiba [à margem: Onde está o curral de Igoáa. Posse], começando de um monte que está defronte do curral que o dito Colégio tem em Santa Cruz, o qual monte fica do curral para a banda desta cidade obra de mil braças, .. e deste dito monte começamos a medir as ditas quinhentas braças, pondo-se corda da ilharga da medição que está feita nas terras do dito Colégio, e daí caminharam para a banda desta cidade, medindo-se as quinhentas braças de testada pelo rumo de leste e quarta de nordeste, que é o rumo por onde se mediu a testada do dito Colégio, e onde acabar se porá um marco de pedra, e daí para o sertão se medirão as 1.500 braças pelo rumo de norte a quarta de noroeste até entestar no rio Guandu, e sendo mais terras das ditas 1.500 braças até entestar no dito rio, lhe pagará o dito Colégio e respeito das outras, e da parte do norte e do sul e do leste partem com terras deles vendedores, e da outra parte com as do dito Colégio, as quais terras herdaram de seu pai e sogro, que as havia recebido por carta de sesmaria. Preço: 60$000 (Escretura de venda das terras de Goaratiba que fizerão Manoel Veloso e Jerônimo Velloso aos reverendos padres dêste Coll.°. In ABN, 82, 1962, pp. 258-261). Há informação de que esta escritura está também em: José Paulo Figueiroa Nabuco de Araújo. O tombo, ou cópia fiel da medição, e demarcação da fazenda nacional de Santa Cruz, segundo foi havida e possuida pelos padres da Companhia de Jesuz, por cuja extincção passou à nação. Rio de Janeiro: Na Typographia de Lessa e Pereira, 1829, 196 p. Essas terras, sitas no "termo de São Vicente", são medidas em 19/8/1617 (Tombo dos Jesuítas, pp. 260-261). Peixoto diz que o campo do Colégio citado acima era conhecido pelo nome de "curral falso".

AGCRJ, Códice 42-3-55, p. 38; IHGB, Lata 57, Pasta 3
Data - 1616
Descrição
Escritura de doação de terras e mais benfeitorias que fazem Francisco Dias Machado e sua mulher Isabel Esteves à sua ermida por nome São Francisco [de Cruará?], que tinham feito com licença do senhor administrador nas suas terras de Suruí.

AGCRJ, Códice 42-3-55, p. 37
Data - 1616
Descrição
Escritura de distrato de venda de um engenho que fazem Felipe Ferreira [de Abreu] e Sebastião de Sampaio – de invocação Santo Antonio, sito no lugar chamado a Pedra, que o segundo vendera ao primeiro.

AGCRJ, Códice 42-3-55, p. 41
Data - 1616
Descrição
Escritura de arrendamento de terras e de um engenho de fazer açúcar que faz Pero de Espinha a Sebastião Coelho Damim, tendo como fiador Gaspar Rodrigues - com 250 braças de testada, com todos os seus pertences.

AGCRJ, Códice 42-3-55
Data - 1617
Descrição
Escritura de venda de um partido de canas que fazem André Gavião [Coutinho] [juiz dos órfãos em 1624 - Tombo dos Jesuítas, p. 276] e sua mulher Catarina de Sampaio a Felipe Ferreira de Abreu - sem localização.

AGCRJ, Códice 42-3-55, p. 43
Data - 1617
Descrição
Escritura de partido e obrigação que fazem os padres da Companhia com Catarina de Faria, viúva de Domingos Martins - sem localização.

AGCRJ, Códice 42-3-55, p. 44
Data - 1617
Descrição
Escritura de aforamento de terras que fazem Fernão Baldez e sua mulher Ana Dias a Bastião de Oliveira e sua mulher Catarina Ferreira - sitas em Macacu, compradas aos padres da Companhia.

AGCRJ, Códice 42-3-55, p. 44
Data - 1617
Descrição
Escritura de venda de terras que fazem Fernão Baldez e sua mulher Ana Dias a Nuno Fernandes de Aguiar – com 400 braças de testada e 700 de sertão, sitas no rio de Suruí.

AGCRJ, Códice 42-3-55, p. 46
Data - 1617
Descrição
Escritura de venda de terras que fazem Manoel Fernandes Ozouro e sua mulher Isabel Martins a Antonio Martins da Palma - sem localização.

AGCRJ, Códice 42-3-55, p. 47
Data - 1617
Descrição
Escritura de partido e obrigação que faz Pero da Silva a Felipe Fernandes e a Lourenço Gomes – sobre arrendamento de canaviais.

AGCRJ, Códice 42-3-55, p. 48
Data - 1617
Descrição
Escritura de venda de terras que fazem Felipe Fernandes e sua mulher Clara Martins a .... - sitas no porto de Guarapitanga.

AGCRJ, Códice 42-3-55, p. 49
Data - 1617
Descrição
Escritura de venda de um partido de canas que faz Baltazar Leitão a Paulo da Cunha - com todas as suas casas, partido que foi de Manuel Quinteiro de Souza, no valor de 30 réis. 

AGCRJ, Códice 42-3-55, p. 49
Data - 1617
Descrição
Escritura de obrigação e declaração que faz Isabel Cardosa, [viúva(?) de Jerônimo Dias – Rheingantz, II, p. 444], a Diogo Lopes Ramos, seu genro, [casado com sua filha Francisca Cardosa] – com 300 braças de testada, sitas no rio de Macacu, no Morro Bom, [onde tem engenho].

6LTMSBRJ, p. 225
Data - 1620
Descrição
Escritura de doação de terras que fazem Diogo de Brito Lacerda e sua mulher Dona Tomásia de Vasconcelos aos Religiosos de São Bento – com 1.300 ou 1.500 braças de comprido e mil de largo ao longo da Gávea, junto ao ribeiro da Tijuca. Doam também uma ilha na barra do rio Inhomirim (morro de São Gregório) e outra que é a primeira que encontram os navegantes quando saem pela barra da cidade do Rio de Janeiro; a ilha fora da barra e as terras ao longo da Gávea estavam apossadas por terceiros em 1772.

Félix Ferreira, A Santa Casa ..., p. 145
Data
1620
Descrição
Através de seu testamento, Gonçalo de Aguiar faz doação ao padre Manoel da Nóbrega de uma morada de casas sita em Iguaçu (Guaguaçu?), de paredes de taipa de pilão, por acabar, para sobrado.

AN, 3º Ofício de Notas, 158, p. 2; AGCRJ, Códice 42-3-57, p. 282
Data - 1621
Descrição
Escritura de venda de um partido e obrigação que faz Diogo de Sá da Rocha a Diogo Nunes de Montarroio, no valor de 130 réis (“pagos em açúcar que fizer no dito canavial”) – sito junto do engenho de Meriquipari, com obrigação de fazer 60 tarefas de canas de 10 carros cada uma, por tempo de dois nove anos.

AN, 3º Ofício de Notas, 158, p. 6v; AGCRJ, Códice 42-3-57, p. 283
Data - 1621
Descrição
Escritura de venda de um sitio que faz Mateus de Azevedo a Alexandre Lopes – um pedaço de terra de 20 braças, sito em Aguapeiaçu, indo pelo rio acima à mão esquerda, onde morava Afonso Pereira, havido por dote de casamento de seu sogro João Sailhes. Preço: 350 alqueires de farinha de guerra, pagos à vista. Com declaração de que a terra aqui vendida constitui um quarto das que seu sogro comprou aos reverendos padres da Companhia.

AN, 3º Ofício de Notas, 158, p. 14v; AGCRJ, Códice 42-3-57, p. 284
Data - 1621
Descrição
Escritura de venda e troca de um partido de canas que fazem Felipe Ferreira de Abreu e sua mulher Maria de Arão a Aleixo Manoel, o moço – sito no engenho de Antonio Tavares, havido por título de compra feita a Antonio Fernandes, o empurra. Vende este partido em troca de outro partido que Aleixo Manoel possuía no sítio de ..., onde o dito Felipe Ferreira de Abreu tem um engenho, o qual partido houve de compra de Francisco da Costa Homem.

AN, 3º Ofício de Notas, 158, p. 30v; AGCRJ, Códice 42-3-57, p. 285
Data - 1621
Descrição
Escritura de venda de um pedaço de terras que fazem Baltazar Rodrigues(?) Calheiros(?) e sua mulher Beatriz Cardosa a Manoel Caldeira – sitas em Piracanopã, distrito desta cidade, junto às terras de Ma..., as quais houve por arrematação.

AN, 3º Ofício de Notas, 158, p. 45v; AGCRJ, Códice 42-3-57, p. 287
Data - 1621
Descrição
Escritura de venda de uma ilha que fazem Manoel Leitão e sua mulher Antonia de Aguiar a Baltazar da Costa (ou de Borba) – com seus canaviais, que foi de Gaspar da Costa.

AN, 3º Ofício de Notas, 158, p. 65; AGCRJ, Códice 42-3-57, p. 282; AGCRJ, Códice 42-3-57, p. 288
Data - 1621
Descrição
Escritura de doação de uma data de terras que fazem João Oliveira Pinto e sua mulher Violante Lopes a Domingos de Muros - Dizem que tinham meia légua de largo e uma de comprido, sitas na barra de Mutuapira. Por esta escritura doam 500 braças dessas terras, nas cabeceiras dela, com toda a largura que tiver, que é nas cabeceiras de ... Fernandes.

AN, 3º Ofício de Notas, 158, p. 66v; AGCRJ, Códice 42-3-57, p. 288
Data - 1621
Descrição
Escritura de arrendamento de terras que fazem Henrique Antunes e sua mulher Catarina Rodrigues a Domingos de Muros, no valor de 3 réis – com 200 braças de largo e 500 de sertão, sitas em Macucu, "as quais duzentas braças serão onde quiser o dito Domingos de Muros".

AN, 3º Ofício de Notas, 158, p. 80; AGCRJ, Códice 42-3-57, p. 289
Data- 1621
Descrição
Escritura de amigável composição que fazem o reverendo padre Pablo Sanches e Francisco Ramires - A respeito de alguns escravos de um engenho que o padre possuía de arrendamento, que foi de Bartolomeu Vaz, cujo contrato trespassara a Francisco Ramires

AN, 3º Ofício de Notas, 158, p. 81; AGCRJ, Códice 42-3-57, p. 291
Data – 1621
Descrição
Escritura de venda de um engenho que faz Antonio Tavares, por si e como administrador dos bens de seus filhos Antonio Tavares e M... Tavares, a Manoel Pinto – Manoel Pinto diz que por ordem do Ouvidor Geral Licenciado Amãosio Rebelo Velho se mandou por em pregão, a instância de Isabel Araújo, viúva do Licenciado Rui Vaz, o engenho dele dito Antonio Tavares, por nome Santo Antonio, com suas terras e 15 bois e pertenças, por quem mais desse. Manoel Pinto lançou três mil e duzentos .... cruzados. Manoel Pinto se compromete a pagar dívidas de Antonio Tavares ... e mais ... suas terras que têm por título dos padres da Companhia, em que têm o dito engenho.

AN, 3º Ofício de Notas, 158, p. 104; AGCRJ, Códice 42-3-57, p. 292; AMSBRJ, Seção 6.2, Documento 56
Data - 1621
Descrição
Escritura de venda de terras que faz Francisco Carrasco a Sebastião de Sampaio, no valor de 13 réis – com 150 braças de testada e 750 de sertão, sitas no rio de Guaguaçu, partindo de uma banda com terras de Bartolomeu Fernandes e da outra com terras de Jerônimo Monteiro, havidas por dote de casamento de Jerônimo Monteiro. 

ABN, Vol. 57, 1939, pp. 250-253
Data - 1624
Descrição
Escritura de amigável composição que fazem Manoel Veloso de Espinha e sua mulher Isabel de Bitancor com Jerônimo Veloso Cubas e sua mulher Beatríz Álvares Gaga, herdeiros de Manoel Veloso de Espinha - Manoel e Jerônimo dizem que dentre os bens que herdaram de seus pais estava uma sorte de terras sitas na Guaratiba, que se compunha de 3 léguas por costa e 6 para o sertão, que partem e começam por costa onde os reverendos padres da Companhia acabam e têm marco, terras que concordararam partilhar da seguinte forma: Jerônimo Veloso Cubas ficará "correndo deste dito marco dos padres, que é de uma ilha onde chamam Guaraqueçaba, até o rio de Tamandoati por costa, com todo o sertão que a dita terra tem da banda do dito rio para cá, com todas as voltas até acima a um morro que fica sobre o rio, e o dito morro correrá a rumo direito para o sertão, e toda a mais terra que no dito rio fica para a banda da barra da Guaratiba ficará a ele dito Manoel Veloso" (Escritura do 2° Ofício) (In Tombo dos Carmelitas, ABN, Vol. 57, pp. 254-256; Eduardo Marques Peixoto, Apontamentos sobre a freguesia de Guaratiba. RIHGB, Tomo 67, Parte II, 1905, pp. 243-262). Obs.: As terras que ficaram para Jerônimo Veloso Cubas e sua mulher Beatriz Álvares [Gaga] são por eles doadas aos carmelitas em 29/6/1629 (doação da capela de Nossa Senhora do Desterro de Guaratiba), assim como de todos os bens móveis e de raiz, escravos e criações. Em troca exigem grande número de missas e outras obrigações religiosas (In ABN, Vol. 57, 1939, p.200-202). A doação foi retificada por Beatriz em 1632, após a morte de Jerônimo. Em 1660 essa Beatriz Álvares ainda vivia nessas terras, casada agora com o Capitão Sebastião Mendes da Silveira; moravam eles como inquilinos dos padres e possuíam um engenho nessas terras. Como estavam muito velhos, queriam morar mais próximos da cidade, e resolvem pedir aos padres que tomem posse total das terras de Guaratiba e deixem-nos ficar, enquanto vivos, como administradores do Engenho de Santo André, que está no rio de Iriri, e que tinha sido comprado pelos padres de André Tavares [em 1/2/1643]. Padres concordam, mas reservam a olaria que está no dito engenho para si e seu convento e dão outras informações sobre relação cidade-campo: "... E declararam os ditos religiosos que o dito Sebastião Mendes Silveira será obrigado a lhes moer a cana que plantarem nas ditas terras Engenho e as não poderão moer no outro engenho senão do dito que administra o dito Sebastião Mendes Silveira e sua Mulher, com declaração que o açúcar que das ditas canas se fizer levarão aos ditos Religiosos as duas partes, assim do branco como de mascavado, e o engenho levará só uma parte das ditas três partes, não obstante ser uso levar a metade aos mais, e poderão os ditos Religiosos trazer nos pastos do dito engenho de Santo André seus bois para a fábrica da olaria ... e assim mais poderão tirar dos matos dos ditos engenhos algumas madeiras que lhe forem necessárias para as obras do seu convento e casas deles...." (Treslado de Escritura de Retificação, posse, concerto e troca feita entre os Reuerendos Padres de Nossa Senhora do Carmo e Sebastião Mendes da Sylveira - 1660.

AGCRJ, Códice 40-3-71, p. 17
Data - 1624
Descrição
Escritura de venda de terras que faz Miguel Carvalho, o velho, como procurador de João de Oliveira, a Miguel Carvalho, o moço, no valor de 30 réis – com meia légua em quadra, ou o que na verdade se achar, sitas no termo desta cidade, em Ipiíba, na banda d’além, herdadas por falecimento de seus pais Simão de Oliveira e Augustinha Dias. (Escritura original do 1º ou 2º Ofícios)

ABN, 82, 1962, pp. 188-189
Data - 1624
Descrição
Escritura de venda de terras que fazem o reverendo padre Inácio de Siqueira, superior da Aldeia de São Barnabé, e os índios de Cipotiba ao reverendo padre Francisco Carneiro, reitor do Colégio de Jesus, no valor de 40 réis – Dizem o padre Inácio e os índios principais e cabeças da dita aldeia, a saber, Fernando Merim, Silvestre, Baltazar, Lobato, Joanni, Jerônimo, Miguel, André, Gonçalo e Antonio que eles vendem um pedaço de campo com todas as suas águas e capões que se acharem nele, o qual começa do rio Cipotiba, que está junto à Tapera Velha, e daí correndo pelo rio acima e para a banda do mar, e daí para baixo, correndo pelo mesmo rio até uma ponta que está em o mesmo rio Cipetiba, em o caminho que vai para o Iguape, e daí atravessando por uns capões que estão ao socairo do mesmo caminho direito, a um pau que chamam Junhuíba, em o qual pau lá fica a mesma marca do Colégio, e o travessão do mesmo campo para a banda de Serpentiba, pelo caminho de Cabo Frio, até chegar ao rumo verdadeiro das roças dos Carijós, tudo o que for campo. Escritura de venda de terras que fazem o reverendo padre Inácio de Siqueira, superior da Aldeia de São Barnabé, e os índios de Cipotiba ao reverendo padre Francisco Carneiro, reitor do Colégio de Jesus – Dizem o padre Inácio e os índios principais e cabeças da dita aldeia, a saber, Fernando Merim, Silvestre, Baltazar, Lobato, Joanni, Jerônimo, Miguel, André, Gonçalo e Antonio que eles vendem um pedaço de campo com todas as suas águas e capões que se acharem nele, o qual começa do rio Cipotiba, que está junto à Tapera Velha, e daí correndo pelo rio acima e para a banda do mar, e daí para baixo, correndo pelo mesmo rio até uma ponta que está em o mesmo rio Cipetiba, em o caminho que vai para o Iguape, e daí atravessando por uns capões que estão ao socairo do mesmo caminho direito, a um pau que chamam Junhuíba, em o qual pau lá fica a mesma marca do Colégio, e o travessão do mesmo campo para a banda de Serpentiba, pelo caminho de Cabo Frio, até chegar ao rumo verdadeiro das roças dos Carijós, tudo o que for campo. Escritura de venda de terras que fazem o reverendo padre Inácio de Siqueira, superior da Aldeia de São Barnabé, e os índios de Cipotiba ao reverendo padre Francisco Carneiro, reitor do Colégio de Jesus – Dizem o padre Inácio e os índios principais e cabeças da dita aldeia, a saber, Fernando Merim, Silvestre, Baltazar, Lobato, Joanni, Jerônimo, Miguel, André, Gonçalo e Antonio que eles vendem um pedaço de campo com todas as suas águas e capões que se acharem nele, o qual começa do rio Cipotiba, que está junto à Tapera Velha, e daí correndo pelo rio acima e para a banda do mar, e daí para baixo, correndo pelo mesmo rio até uma ponta que está em o mesmo rio Cipetiba, em o caminho que vai para o Iguape, e daí atravessando por uns capões que estão ao socairo do mesmo caminho direito, a um pau que chamam Junhuíba, em o qual pau lá fica a mesma marca do Colégio, e o travessão do mesmo campo para a banda de Serpentiba, pelo caminho de Cabo Frio, até chegar ao rumo verdadeiro das roças dos Carijós, tudo o que for campo. Plena e geral quitação.

AGCRJ, Códice 2-4-9, p. 76
Data - 1626
Descrição
Escritura de venda de terras que fazem Miguel Gomes Bravo e sua mulher Isabel Pedrosa [de Gouveia] aos reverendos padres do Carmo, no valor de 320 réis - sitas "no distrito de Magé, em Iriri", místicas com as terras que os reverendos padres do Carmo haviam herdado de Aires Fernandes e de sua mulher Maria de Sá. Vendem também 237,5 braças "que se acabam no rio de Iriri", com sertão de 2.000 braças, que Luiz de Madureira herdara de sua mulher Maria de Sá e as vendera a Manoel (sic). Vendem também outra sorte de terras nas cabeceiras das terras que possuem os reverendos padres do Carmo, que ficaram de Aires Fernandes e sua mulher Maria de Sá, que são 800 braças de testada e 1 légua de sertão, que consta de uma escritura que Manoel dos Rios comprou a Aleixo da Costa [herdeiro de Manoel da Costa], e assim mais pelas mesmas cabeceiras outras 200 braças de testada com o próprio sertão de 800 braças, entendendo-se esta testada na data que eles vendedores possuíam, que foi de Luiz de Madureira. E vendem outra sorte de terras nas mesmas confrontações, que Pero de Campos Tourinho vendeu a Manoel dos Rios, a qual herdara de Nicolau Baldim. Área total das terras aqui vendidas: 237,5 braças de testada e 5.000 de sertão.

AGCRJ, Códice 42-4-69; Códice 40-3-71, p. 40
Data - 1626
Descrição
Escritura de venda de terras que faz Cosma Gomes, dona viúva de Francisco de Braga, a Diogo Martins Mourão, no valor de 27.92 réis - Diz que possui uma sorte de terras sitas aonde chamam Irii, na banda d’além desta cidade, que partem de uma banda com terras que foram de Diogo de Braga e da outra com terras de Duarte Martins Mourão, já defunto, herdadas por falecimento de seu marido. Por esta escritura vende metade das ditas terras, começando de uma tapera dela vendedora que está no alto de um outeiro, correndo para a lagoa de Piratininga. Vende também uma outra data de terra, que herdou por falecimento de seu primeiro marido Miguel Gonçalves, sita onde chamam Pondetiba (Piritiba em outro documento), que parte com a data que foi de Francisco Fernandes, já defunto, nas cabeceiras da data do dito Francisco Fernandes.

ADF, 1, 1894, p. 87; 5LTMSBRJ, p. 143
Data - 1627
Descrição
Escritura de doação de terras que fazem Diogo Martins Mourão e sua mulher aos Religiosos de São Bento – com uma légua em quadra, sitas em Jatoucaia [ou Taocaia, Itaocaia, ou Itaocara], caminho de Maricá, com a obrigação de uma missa perpétua todas as quartas feiras pela alma de Duarte Mourão e Apolônia Furtado.

Apud Rudge, As sesmarias de Jacarepaguá, pp. 35-36
Data - 1628
Descrição
Escritura de dote de casamento que fazem o Capitão Gonçalo Correia de Sá e sua mulher Dona Esperança Correia de Sá a Dom Luiz de Cespedes Xeria, para casar com sua filha Dona Vitória Correia de Sá - Doam um engenho e moenda d’água de fazer açúcar, da invocação de São Gonçalo, moente e corrente, com sua casa do dito engenho, casas da caldeira e de purgar, aposentos de vivenda, com capela e igreja com ornamentos que de presente tem, o qual engenho está situado aonde chamam o Camorim, termo desta cidade. Doam também 40 peças, entre de Guiné e da terra, 2 caldeiras de cobre do dito engenho e mais cobres que para ele forem necessários, com declaração de que nas 40 peças doadas entram dois negros do gentio de Guiné, um ferreiro e outro oleiro, e assim mais entrarão na dita conta três moços, um carpinteiro e dois serradores, do gentio da terra. Doam também meia légua de terras, começando onde acaba o caminho para o engenho, e assim mais lhes dão os canaviais que estão plantados na terra do dito engenho, exceto os que estão dados de partido a Antônio da Costa, e dos ditos canaviais reservam eles dotadores para si 20 tarefas de cana que o dito engenho será obrigado a moer cada ano para sempre, sem o senhor do engenho partir nem levar coisa alguma de todo o açúcar que renderem as ditas 20 tarefas que assim reservam, as quais gozarão eles ditos dotadores e um por falecimento do outro, e as poderão vender, dar e doar como lhes aprouver, como coisa sua que é. Doam, finalmente, mais uma légua de terra na restinga da praia, correndo do pé da serra de Guaratiba para a Tijuca. Com declaração final que a pessoa que possuir o dito engenho será sempre obrigada a reparar e ornar a dita capela e igreja de São Gonçalo, ficando a isto hipotecado o dito engenho e fazenda, que passam com este encargo. (Escritura do 3º Ofício).

AGCRJ, Códice 42-4-69; Códice 40-3-71, p. 42v
Data - 1629
Descrição
Escritura de venda de terras que faz Marcela Gomes, viúva de Garcia de Ávila, o moço, [filho de Garcia de Ávila, o velho, da Bahia] a Diogo Martins Mourão, no valor de 8 réis – Diz que possui uma sorte de terras onde chamam Lery, na banda d’além desta cidade, em um outeiro que está entre a lagoa de Piratininga, indo para a dita lagoa, que lhe ficaram por morte de seu pai, na qual terra está ainda hoje a tapera que foi do dito seu pai e sua mãe Cosma Gomes. Declara que sua mãe havia vendido a metade das ditas terras a Diogo Martins Mourão [em 18/9/1626]. Por esta escritura vende agora a outra metade.
A escritura contém uma declaração de que ela Marcela tem uma filha casada na Bahia, com nome Maria de Ávila, filha de seu marido Garcia de Ávila, o moço, e neta de Garcia de Ávila, o velho, e que sendo caso que em algum tempo se decida que ela tem parte nestas terras por herança, ela vendedora irá lhe recompensar com bens deixados na cidade da Bahia, nas fazendas do dito seu marido defunto.

IHGB: Lata 57, Pasta 3
Data - 1629
Descrição
Escritura de doação e hipoteca de terras que fazem Jerônimo Veloso Cubas e Beatriz Álvares Gaga a Nossa Senhora do Desterro - terras na Guaratiba (que depois pertenceram ao Convento do Carmo).

AGCRJ, Códice 42-4-69; Códice 40-3-71, p. 44
Data - 1630
Descrição
Escritura de retificação de venda de terras que faz Paulo da Cruz, como procurador e genro de sua sogra Cosma Gomes, casado com sua filha Luiza Teixeira – Diz que sua sogra havia vendido a Diogo Martins Mourão umas terras na banda d’além, onde chamam Rerehy. Por esta escritura ratifica a venda anterior [realizada em 18/9/1626].

AMSBRJ, Seção 6.2, Documento 104
Data - 1631
Descrição
Escritura de venda de terras que fazem Antonio Muniz Barreto, cidadão desta cidade, e sua mulher Dona Antonia [de Mariz] a Gaspar Cardoso, no valor de 25 réis - Dizem que possuem uma data de terras de meia légua em quadra no rio de Guaguaçu, que houveram de herança de seu pai e sogro Antonio de Mariz [filho de Antonio de Mariz Coutinho, que a recebera de sesmaria em 21/2/1578]. Por esta escritura vendem metade dessas terras, que se localizam onde chamam Mamembaia e Guarabaia, partindo com a data que foi de Pero Rodrigues, com obrigação dele Gaspar Cardoso abrir o rio das ditas terras e fazê-lo navegável de canoas grandes para a serventia das ditas terras. A parte aqui vendida é a que está no princípío das ditas terras. (Escritura do 2º Ofício).
Observações: Nestas terras Gaspar vai erguer um engenho. Por sua morte e de sua mulher Felipa Peres o engenho irá a praça pública e será arrematado, em 24/2/1652, por Fernão Cabral de Melo. Passará depois a Pedro de Moransi.

AN, 1º Ofício de Notas, 31, p. 16; AGCRJ, Códice 42-3-55, p. 56
Data - 1632
Descrição
Escritura de distrato, contrato e obrigação que fazem Gervásio Leitão e sua mulher Bárbara Lopes com João do Couto de Carnide e sua mulher Córdula Gomes [filha de Miguel Gomes Bravo e Isabel Pedrosa de Gouveia] – João do Couto e sua mulher dizem que tinham vendido a Gervásio Leitão um partido de canas em seu engenho, sito na banda d’além, por 150$000. Por esta escritura, Gervásio Leitão e sua mulher Bárbara Lopes vendem o dito partido, com as benfeitorias de um partido novo que fez, a João do Couto de Carnide e sua mulher por 280$000 (280 réis). 

AN, 1º Ofício de Notas, 31, p. 26v; AGCRJ, Códice 42-3-55, p. 57
Data - 1632
Descrição
Escritura de venda de terras que fazem Félix de Gusmão e o Capitão Diogo Teixeira de Carvalho, como procuradores de Dona Clemência Coutinha, a Diogo Álvares, no valor de 550 réis – com 500 braças de testada e uma légua de sertão, sitas em Guaxindiba, partindo com terras do vendedor e de Dona Brites.

AN, 1º Ofício de Notas, 31, p. 27; AGCRJ, Códice 42-3-55, p. 57
Data - 1632
Descrição
Escritura de venda de terras que fazem Manoel Velho e sua mulher Maria de Azeredo a João Álvares Pereira, no valor de 70 réis – com uma légua de testada (ou em quadra), sitas em Marapicu, começando a medir nas cabeceiras dos padres da Companhia, e daí vindo acabar em uma légua de terra que o comprador comprou em Marepequi (Marapicu?), que foi de Bernardo Machado, havidas por dote de casamento.

AMSBRJ, Seção 8, Documento 1008
Data - 1632
Descrição
Escritura de partilha que fazem Gonçalo Correia de Sá e Martim de Sá dos campos de Camorim e restinga - Dizem que por serem meeiros dos bens de seu pai se compõem para partirem as terras da seguinte forma, "a saber, que os ditos campos de Camury serão sempre de entre ambos eles ditos senhores e dita senhora Dona Esperança e de seus herdeiros para neles terem seus currais e criações e a data da restinga começarão eles senhores Gonçalo Correia de Sá e Dona Esperança a medir do pé da serra que fica da banda de Guaratiba para a banda da Tijuca uma légua, e do Senhor Dom Luis de Cespedes e da Senhora sua mulher Dona Vitória, sobrinha e filha deles ditos senhores, e donde ... a mais terra que ... a dita restinga tomará cada um deles a metade e Dona Esperança começará a partir com a légua da dita senhora sua filha Dona Vitória, e o Senhor Martim de Sá ficará com a sua metade da banda da Tijuca, em que só estão compostos e havindos partirão o sertão delas igualmente, vindo correndo para os campos de Irajá e tomará cada um deles o sertão que tiver conforme a costa de cada uma das ditas partes, e que ambos de dous se servirão pelo caminho e estrada que têm aberto de carro de Jacarepaguá para o dito Campo de Irajá, e descobrindo outro caminho melhor usarão dele na mesma conformidade misticamente e assim entre seus herdeiros ...". Está escrito à margem: "Viciado e incompleto".

AN, 1º Ofício de Notas, 31, p. 47
Data - 1632
Descrição
Escritura de quitação de venda de um partido que dá Manoel Garcez [Palha], como procurador de seus pais Bento Garcez e Maria da Silveira, a Mateus Antunes, no valor de 32 réis – sito na banda d’além, no engenho São Francisco, com obrigação de 9 anos e 15 tarefas de cana anuais de 16 carros cada ano.

AN, 1º Ofício de Notas, 31, p. 51v
Data - 1632
Descrição
Escritura de venda de terras que fazem José de Castilho e sua mulher Ana de Oliveira a Sebastião Coelho Damim, no valor de 12 réis - com 50 braças de testada e 800 de sertão, sitas no rio de Guapimirim, partindo de uma banda com terras de Baltazar da Costa e da outra com Pedro Luiz Ferreira, correndo o sertão para terras de Alexandre Lopes, herdadas de seu pai e sogro Jerônimo Pereira.

AN, 1º Ofício de Notas, 31, p. 83v; AGCRJ, Códice 42-3-55, p. 65
Data - 1633
Descrição
Escritura de venda das benfeitorias de um partido de canas que faz Francisco de Caldas, o velho, a Francisco de Marequina [ou Marchena – Rheingantz, II, 16], no valor de 150 réis – com casa de taipa de ... coberta de palha, um pomar novo, árvores de espinho, etc., sitas no seu engenho de invocação Santo Antonio, situado nos limites da Lagoa.. Francisco de Marequina e sua mulher vendem novamente estas benfeitorias em 1635.

Apud Eduardo Marques Peixoto, Apontamentos sobre a freguesia de Guaratiba. RIHGB, Tomo 67, Parte II, 1905, pp. 243-262
Data - 1633
Descrição
Escritura de dote de casamento que faz Manoel Veloso de Espinha a Belchior da Fonseca [Dória], por se casar com sua filha Catarina Veloso – Doa metade das terras que possui em Guaratiba com a metade do campo que nelas há para o gado. Seu genro recebe também 20 peças de guiné, 12 cavalgaduras, 80 cabeças de gado vacum fêmeas, todo o enxoval da casa, e metade de todos os chãos que tinha no bairro de Nossa Senhora da Ajuda. No dote entrou parte da herança que sua filha tinha direito por morte de sua mãe Isabel de Bitencor.Com declaração que caso a ermida do Salvador ficasse na terra dotada, ficaria ela livre, sendo-lhe dotada terra equivalente na metade da que ficava. (Escritura do 2° Ofício).

AN, 1º Ofício de Notas, 31, p. 93; AGCRJ, Códice 42-3-55, p. 65
Data - 1633
Descrição
Escritura de dote e casamento que faz Isabel dos Rios, viúva de Sebastião Lobo Pereira, à sua filha Dona Antonia, prometida em casamento a Cristóvão de Melo de Vasconcelos – Doa um partido com 60 tarefas de cana de 16 carros cada tarefa, plantadas em duas folhas de terras do seu engenho da invocação da Trindade, sito nas terras de Guaxandiba, para nele lhe moer em cada ano 40 tarefas por tempo de dois nove anos de meias como é costume.

AN, 1º Ofício de Notas, 31, p. 102; AGCRJ, Códice 42-3-55, p. 66
Data - 1633
Descrição
Escritura de venda de um curral de gado que fazem o Governador Duarte Correia Vasqueanes e Gonçalo Correia de Sá a João de Oliveira(?) e Gonçalo Lopes de Távora - com 43 vacas parideiras e 7 bezerros, que pertenceu a Martim de Sá. Vendem também 15 novilhos por 1$442 cada e mais 16 cabeças de novilhos a 1$446 e mais 31 cabeças, etc. Valor de 3.366 réis cada cabeça. 

AMSBRJ, Documento Nº 1087
Data - 1633
Descrição
Escritura de doação de terras que fazem o Capitão Gonçalo Correia de Sá e sua mulher Dona Esperança de Sá a Diogo Mendes [Coluna] - Dizem que possuem metade de uma ilha [do Governador], onde está um engenho de fazer açúcar, herdados de seu pai e sogro Salvador Correia de Sá. Na mesma ilha está aposentado o dito Diogo Mendes com casas, canaviais, roças e outras plantas. Em pagamento aos muitos serviços que lhe devem, doam, por esta escritura, 600 braças em quadra das terras a que têm direito, exatamente as terras onde o dito Diogo está aposentado, que é na praia a que chamam da ama, começando a medir do princípio da dita praia da banda do sudoeste para diante quando vão para Magé. Com condição de que as canas e canaviais que ele fizer moerá no engenho ou engenhos que na dita ilha há e ao diante fizerem, como é uso e costume. Com declaração também que, sendo caso que fazendo-se partilhas não lhes caibam as ditas 600 braças de terras à sua posse, ficam contentes que o dito Diogo tenha outras 600 braças na parte que lhes couber.

AN, 1º Ofício de Notas, 31, p. 117; AGCR J, Códice 42-3-55, p. 69
Data - 1633
Descrição
Escritura de venda de um engenho que faz Isabel Gomes, viúva de Simão de Ospina(?), a seu filho João Luiz Mafra e sua mulher Mécia Barbosa, no valor de 5000 cruzados pagos em dívidas - de invocação Nossa Senhora de Betancor, sito em Tarairaponga, com 600 braças de terra em quadra, com casa de engenho e casa de purgar, com as canas dos partidos, ... donde parte com o caminho de carro ... que partem com Baltazar de Azevedo. Pagos em dívidas.

AN, 1º Ofício de Notas, 31, p. 122v
Data - 1633
Descrição
Escritura de dinheiro a juros com hipoteca de um engenho que fazem João Luiz Mafra e sua mulher Mécia Barbosa, devedores, a Gaspar Aranha Coutinho e sua mulher Isabel de P..., no valor de 440 réis – Os devedores hipotecam seu engenho de Nossa Senhora de Betancor, sito em Tarairaponga.

AN, 1º Ofício de Notas, 31, p. 135v; AGCRJ, Códice 42-3-55, p. 71
Data - 1633
Descrição
Escritura de venda de um partido de canas que fazem João Luiz Mafra e sua mulher Mécia Barbosa a Isabel Gomes, dona viúva e sua mãe e sogra, no valor de 300 réis – sito em seu engenho em Tarairaponga, da invocação de Nossa Senhora do Betancor, com obrigação de 30 tarefas de canas de 16 carros a cada ano, por 9 anos.

AN, 1º Ofício de Notas, 31, p. 138; AGCRJ, Códice 42-3-55, p. 71
Data - 1633
Descrição
Escritura de obrigação de um partido de cana que fazem Heitor de Barros [Pereira] e sua mulher Margarida Pinta [da Fonseca], proprietários do engenho de Nossa Senhora do Ó, a Francisco Gomes de Gouveia e sua mulher Maria Pereira - sito em Mereti, com obrigação de 30 tarefas de 12 carros cada ano por tempo de dois nove anos.

AN, 1º Ofício de Notas, 31, p. 139v; AGCRJ, Códice 42-3-55, p. 72
Data - 1633
Descrição
Escritura de venda de terras que faz Vitória de Mariz, viúva de Álvaro Gomes Osório, a André Tavares, no valor de 110 réis – com 500 braças de testada, sitas pelo rio de Leri [Iriri], até as terras dos Padres do Carmo, conforme carta de sesmaria concedida a Baltazar da Costa pelo Governador Cristóvão de Barros.

AN, 1º Ofício de Notas, 47
Data - 1633
Descrição
Escritura de partido e obrigação que fazem João Álvares Pereira e sua mulher Isabel de Montarroio a Gonçalo Lopes de Távora – para moer no engenho deles outorgantes [sito em Gericinó].

AMSBRJ, Seção 13.2, Nº 1074
Data - 1633
Descrição
Escritura de partilha dos bens deixados na Ilha do Governador por morte de Salvador Correia de Sá, o velho, pelos herdeiros Salvador Correia de Sá e Benevides, herdeiro de Martim de Sá, e Dona Esperança e Dona Vitória, herdeiras de Gonçalo Correia de Sá, Martim e Gonçalo também já falecidos, no valor de 1937.73 réis. 
Participam da escritura o juiz ordinário Clemente Nogueira; os avaliadores Manoel dos Rios (louvado por Benevides), Baltazar Leitão (louvado pelas duas senhoras) e Baltazar de Seixas Rabelo (louvado pelas duas partes para as dúvidas que houverem), além dos pilotos Lourenço Pereira, Rodrigo Dias e Manoel de Andrade. O inventário das peças de escravos, indicou a presença na propriedade dos seguintes escravos: Escravos que ficam pertencendo a Salvador Correia de Sá e Benevides: 1) Mateus de guiné, negro velho e antigo, o qual serve nesta fazenda de mestre de açúcar, avaliado em 40$000; 2) Antonio da guiné, caldeireiro, 80$000; 3) Violante da guiné com duas crianças de 10 meses de idade, ambas gêmeas e fêmeas, 50$000; 4) Bastião de guiné, crioulo de 14 anos, aleijado em um ..., 35$000; 5) Duarte de guiné, aleijado de um pé, 16 anos, 35$000; 6) Lucrécia, moleca crioula, 35$000; 7) Manoel, carreiro, de guiné, crioulo, 65$000; 8) Antonia de guiné, 85$000; 9) Laura, moleca d’alcunha, negra velha, mulher(?) do carreiro, 15$000; 10) ...io, com uma mulatinha ... nove anos, avaliados em 30$000; 11) Isabel, mulher do dito negro, 40$000; 12) uma filha e um filho em ... mulher Isabel ...; 13) dois negros solteiros ... Miguel ... e ... sua mulher Clara ... 14) Luiza. Escravos que ficam pertencendo a Dona Esperança: 1) Jerônimo; 2) Estevão, 3) seu filho Antonio, 4) seu filho Tomé, 5) seu filho Duarte, 6) Amaro, 7) Luiza com uma criança, 8) Grácia. Não foram avaliados uns mulatos que estão forros. Há também outros escravos da terra que estão arrolados separadamente, a saber, Bartolomeu tapanhum, arrolado a Benevides, e seu irmão Salvador, arrolado a Dona Esperança, os quais não foram avaliados por já estarem na propriedade de um e de outro. Couberam também a Dona Esperança Domingos Tinga e sua mulher Bárbara e duas crias, e a Salvador Correia de Sá e Benevides Belchior e Pelônia, tingas, também com duas crias. Coube mais a Dona Esperança uma mulata forra e a Salvador ... Andreza, também de guiné. Informa-se que "a casa do engenho, a moenda e telha(?) dela, que é o mais essencial, por ser a dita casa muito velha e estar para cair, foram avaliadas em 130$000. Os cobres, a saber, duas caldeiras gastas e desbaratadas, que se avaliaram como cobre, e 3 tachos, e os cobres miúdos e bacia de resfriar, e assim mais uma caldeira que h... ...lhor com e ...rada e remendada - 254$000; 800 formas, 32$000; 24 bois, 8$000 cada um, totalizando 192$000; 2 carros, 8$000 por ambos; várias ferramentas, avaliadas em 1--$000; casa de purgar com seus pertences, 208$000; 1 barca, 30$000. Fazem muitas outras partilhas. Calculou-se ainda o que rendeu a safra de açúcar de 1632, abatendo-se do total dívidas e gastos de Dona Esperança". A propriedade foi medida e demarcada para ficar dividida em duas partes, cabendo a Salvador Correia de Sá e Benevides a metade da ilha, da banda dos canaviais, porque assim foram concertados, e a Dona Esperança e Dona Vitória a outra metade, para a banda das madeiras, com declaração que sendo caso que nas partes partidas e demarcadas da dita ilha em nenhuma delas haja vantagem, eles se concertarão de novo .. por .. em banda fiquem madeiras e tenha melhorias e outras fiquem ... dita ilha partes iguais. Demarcadores informam que a demarcação começou "além do outeiro que está detrás da olaria do engenho para a banda do loeste, começando do dito alto à vista do dito engenho, cortando ... que de presente tem uma vivenda e ... Rodrigo Dias que é ou sua morada antigamente morou João Brás e a parte que cabe à senhora Dona Esperança é e será a que fica do dito rumo para leste; da banda do mto ficam os canaviais que cabem ao Senhor Salvador Correia de Sá".
AMSBRJ, Documento Seção 16, Nº 1088
Data - 1633
Descrição
Escritura de venda de metade de um engenho que faz Dona Esperança de Sá, viúva do Capitão Gonçalo Correia de Sá, a seu sobrinho Salvador Correia de Sá e Benevides, no valor de 1937.73 réis - com tudo o que lhe pertencer de terras, peças, bois, partidos, etc., sito na ilha do Senhor Salvador Correia de Sá. Informa que ela e seu sobrinho estão concertados que a dita ilha se parta entre ambos da forma seguinte: que ela dita Dona Esperança começaria a medir a sua parte do meio do ... outeiro que fica junto ao engenho, a cujo sopé está a olaria de ... outeiro .. da p... que chamam de Ig..., e dali ... o rumo direto ... atravessando toda a dita ilha de mar a mar, a entestar com o porto da fazenda ... que tem Rodrigo Dias na dita ilha que fica da Ponta de Tubiacanga .. a mais terra que fica ... da dita de mar a mar ... do dito engenho e ponta que chamam de Manoel de Castilho(?) ... dito Salvador Correia de Sá até entestarem ... uma e outra borda, com todos os partidos de canas e lavouras de lavradores e demais cousas ...

AN, 1º Ofício de Notas, 32, p. 21v; AGCRJ, Códice 42-3-55, p. 77
Data - 1633
Descrição
Escritura de louvamento que faz Antonio Pacheco Calheiros, por si e como procurador de sua mulher Isabel Coutinho, com Francisco Pais Ferreira, por si e como procurador de sua mulher Maria da Cunha - Para dirimirem dúvida que tinham sobre os pastos, lenhas e madeiras que estão em 400 braças de terras em Geresalem(?), termo desta cidade.

AGCRJ, Códice 2-4-9, p. 91v
Data - 1634
Descrição
Escritura de transação e amigável composição que fazem Cristóvão Osório, por si e como procurador de sua mãe Vitória de Mariz, e André Tavares - Sobre a demarcação de 500 braças de terras que André Tavares comprou a Baltazar da Costa no rio de Rondi, que partem com outras dele Cristóvão e de sua mãe. Medição deve partir do porto que foi de Baltazar Rodrigues, onde está outra terra que André Tavares tem, e se botará um rumo conforme a carta de sesmaria dos frades do Carmo, e a partir daí se começarão a medir as 500 braças encostadas aos rumos dos ditos frades, e acabada de medir se irá pelo travessão ao rio de Orindi. Com obrigação dele André Tavares fazer moenda de açúcar, obrigando-se a moer a cana de Cristóvão.

Rudge, As sesmarias de Jacarepaguá, p. 69
Data -1634
Descrição
Escritura de venda de terras que faz Salvador Correia de Sá e Benevides, por si e como procurador de sua mulher Dona Catarina de Velasco, a Jorge de Souza Coutinho – Diz que possui uma sorte de terras de 3 ou 4 léguas no termo desta cidade, onde chamam Jacarepaguá, herdadas por morte de seu pai Martim de Sá. Por esta escritura, vende meia légua em quadra dessas terras do dito Jacarepaguá, começando a medir do marco do rio Itatindiba. Segundo Rudge, "a testada da área era a linha reta que, partindo do marco do rio Itatindiba – situado quase no atual largo do Tanque – passava no adro da Capela de Nossa Senhora da Pena, terminando à margem da estrada do Gabinal. A linha lateral direita, do marco do Itatindiba à Serra dos Pretos Forros, correspondia aproximadamente ao curso do mesmo rio Itatindiba e ao rumo da atual estrada da Covanca.

Rudge, As sesmarias de Jacarepaguá, pp. 61-62
Data - 1634
Descrição
Escritura de venda de terras que faz Salvador Correia de Sá e Benevides, por si e como procurador de sua mulher Dona Catarina de Velasco, a Pedro Martins Negrão, no valor de 1500 cruzados – Diz que possui no termo desta cidade uma sorte de terras de 3 ou 4 léguas, onde chamam Jacarepaguá, herdadas por morte de seu pai Martim de Sá. Por esta escritura, vende meia légua em quadra dessas terras do dito Jacarepaguá, começando a medir do rio de Itatindiba, no lugar onde começa Jorge de Souza [Coutinho] a sua medição, e daí medirá para a banda de Irajá a testgada de meia légua, e donde acabar medirá 750 braças para a banda da serra, rumo direito, e as outras 750 braças medirá do caminho para baixo, ficando o caminho em meio, e irá correndo o rumo do sertão da banda de Jorge de Souza, na conformidade da escritura que tem da venda de outra meia légua de terra que parte com esta, que é a que fica atrás, de que lhe fica servindo de marco o dito rio, com metade de toda a pertenção da água do dito rio. Com declaração de que, faltando alguma terra para a banda de Irajá, lha inteirará ele vendedor da banda de baixo, até se perfazer a quantidade da dita meia légua de terra em quadra. (Escritura do 1º Ofício).

AN, Caixa 1146, No 13, Galeria A, fp. 8v, 13v
Data - 1635
Descrição
Escritura de venda de terras que fazem Francisco Fernandes de Aguiar e sua mulher Francisca de Matos a Antonio Vaz Viçoso, no valor de 60 réis – com meia légua de testada e 2.250 braças de sertão, sitas em Gericinó, termo desta cidade, com sua testada do pé da serra de Gericinó, onde Lázaro Fernandes acaba, correndo a meia légua de terra que com ele parte, onde tem o seu engenho, correndo para a banda do campo, perto dos Coqueiros, onde Antonio Vaz Viçoso comprou um curral de gado ao Padre Paulo Sanches, com casas e outras benfeitorias, e o sertão das ditas terras corre para a banda de Juari, como melhor consta dos títulos de sesmaria, terras herdadas de seu pai e sogro Reverendo Padre Martim Fernandes, que Deus tem, vigário que foi desta cidade. Auto de posse diz que essas terras estavam na fralda da Serra de Gerecinó, onde acaba Lázaro Fernandes com a sua meia légua, onde tem o engenho, as quais correm para os palmares, indo para Juari, que partem com as terras que comprou ele Antonio Vaz Viçoso de Gaspar da Costa, conforme as cartas de sesmaria. Conforme determinação do Juiz Ordinário Jordão Homem da Costa, a posse é realizada em 29/9/1635, tendo lugar nos Palmares, passante o curral de Pedro Mendes de Souza e passante uma restinga de mato, ao passar de um rio por nome Indahasutiba.

Apud Rudge, As sesmarias de Jacarepaguá, pp. 77-78
Data - 1635
Descrição
Escritura de venda de terras que faz Salvador Correia de Sá e Benevides, por si e como procurador de sua mulher Dona Catarina de Velasco, a João Rodrigues Bravo, no valor de 450 réis – com meia légua em quadra, sitas onde chamam Jacarepaguá, que partem de uma banda com terras de Jorge de Souza Coutinho, também vendidas por eles vendedores, e da outra com terras de Pedro Martins Negrão, que também houve de compra dos mesmos senhores, [pela parte de cima] com terras de Gregório Mendes, também havidas de compra dos mesmos vendedores, e pela parte de baixo com terras deles vendedores, ou de quem quer que nelas entrar, herdadas de seu pai e sogro Martim de Sá.
Observações: Com declaração que estas terras são as mesmas que eles vendedores haviam antes vendido a Matias de Mendonça, de que não fizeram escritura.

6LTMSBRJ, p. 239
Data - 1635
Descrição
Escritura de venda de terras que fazem Pedro de Siqueira e sua mulher Anastácia de Távora aos religiosos de São Bento, no valor de 30 réis – com meia légua de testada, sitas na praia de Maricá, com o sertão que lhe pertencer, conforme a sua carta de sesmaria.

AN, 1º Ofício de Notas, 32, p. 43; AGCRJ, Códice 42-3-55, p 81
Data - 1635
Descrição
Escritura de dote de casamento que faz Manoel da Costa a Francisco Barbosa de Caldas e à sua filha Maria da Costa - o seu engenho de Irajá, com toda a sua fábrica de casas de vivenda, casas de negros, caldeiras com seus cobres, a saber: duas caldeiras, duas tachas e bacia de resfriar e cobres miúdos, com 23 bois e 21 peças de meneio do engenho, em que entram 3 peças da terra e 18 de guiné com as crias que tiverem ...

2LTMSBRJ, 243-246
Data - 1635
Descrição
Escritura de transação e amigável composição que fazem os religiosos de São Bento com Manoel de Brito de Melo, sobrinho de Diogo de Brito de Lacerda – sobre uma sorte de terras no rio de Inhomirim, pelo rio de Acaraí.

AMSBRJ, Seção 6.2, Nº 182, Laxe, p. 269
Data- 1635
Descrição
Escritura de venda de terras que fazem Diogo Teixeira de Carvalho e sua mulher Dona Clemência [Coutinha?] aos religiosos de São Bento, no valor de 60 réis – com três léguas de testada e todo o seu sertão, na lagoa de Mariatiba, correndo pelo rio para Cabo Frio, da banda de Maricá, [até meia légua antes de chegar ao outeiro de Mariatiba] partindo de uma banda com as terras que haviam sido vendidas um ano antes e de outra com terras que foram de Diogo Martins Mourão, principiando na paragem onde se abre a lagoa de Maricá. (Escritura original do 2º Ofício).

AN, 1º Ofício de Notas, 32, p. ?; AGCRJ, Códice 42-3-55, p 90

Data - 1635
Descrição
Escritura de venda de um engenho que fazem Salvador Correia de Sá e Benevides e sua mulher Catarina Ugarte a Pedro de Oliveira, no valor de 33000 cruzados - com moendas aparelhadas com 4 caldeiras de cobre, 3 tachos, 2 bacias de resfriar e uma de fazer decoada, 4 cubas de guindar o caldo, 2 repartideiras, 4 pombas, 2 batedeiras, 5 remonhois, uma balança com 2 arrobas de ferro e outros pesos miúdos, 3 ...entes de ferro, 3 erseis velhos com seus aguilhões de sobressalente, a casa do engenho, com casa de purgar e casa de meles, com todas as formas que nela se acharem, 2 barcas com suas fateixas, cordas e velas, tirado a mezena de uma, 4 carros, uma ermida com toda a fábrica nela, um missal e mais 30 peças de guiné e mais 16 cabeças [de gado], com declaração dos vendedores que a metade da ilha que vendiam herdaram por falecimento de seu pai Martim de Sá.Escritura de ratificação de venda deste engenho passada por Dona Catarina Ugarte logo a seguir (AN, 1ON, 32, p. 40; AGCRJ, Códice 42-3-55, p. 94). Escritura de débito e obrigação assinada por Pedro de Oliveira (AN, 1ON, 32, p. 41); AGCRJ, Códice 42-3-55, p. 94). Escritura de quitação da dívida passada por Salvador Benevides a Pedro de Oliveira, pela compra do engenho da ilha, com duas moendas e todos os pertences, passada em 1636 (AN, 1ON, 34, p. 122; AGCRJ, Códice 42-3-55, p. 146).

AN, 1º Ofício de Notas, 32, p. 5; AGCRJ, Códice 42-3-55, p. 85
Data - 1635
Descrição
Escritura de partido de canas que faz Pero Peixoto Castelão, casado com Antonia Rodrigues de Azevedo, com sua sogra Branca do Porto – localizado no engenho Santo Antonio, pertencente à sua sogra, sito na barra de Meriti.

AN, 1º Ofício de Notas, 32, p. 6; AGCRJ, Códice 42-3-55, p. 85
Data - 1635
Descrição
Escritura de venda de terras que fazem Luiz Fernandes (ou Freire) da Costa e sua mulher Águeda Lopes a Manoel Moreira – com 50 braças de testada e meia légua de sertão, sitas em Suruí, compradas a Pero Gonçalves de Abreu.

AN, 1º Ofício de Notas, 32, p. 18; AGCRJ, Códice 42-3-55, p. 87
Data - 1635
Descrição
Escritura de venda de terras que faz Salvador Correia de Sá e Benevides a Gregório Mendes da Silva, no valor de 325 réis – sitas em Iagarapa (Jacarepaguá?), partindo com Jorge de Souza [Coutinho] de uma banda e da banda de Guaratuba com outra meia légua que fica ao dito Gregório Mendes ...

AN, 1º Ofício de Notas, 32, p. 22v; AGCRJ, Códice 42-3-55, p 87
Data - 1635
Descrição
Escritura de arrendamento de uma ilha que fazem os reverendos padres de São Bento a Simão Dias Guterres – localizada fora da barra de Inhomirim.

AN, 1º Ofício de Notas, 32, p. 39; AGCRJ, Códice 42-3-55, p. ?
Data - 1635
Descrição
Escritura de venda de umas benfeitorias de canas de açúcar que fazem Francisco de Marequina [ou Marchena – Rheingantz, II, 16] e sua mulher Maria de Melo [filha de Luiz de Melo Camelo e de Margarida Soares] ao Padre João de Caldas, no valor de 200 réis - um partido de canas que possuíam no engenho Santo Antônio, sito no caminho da Lagoa.

AN, 1º Ofício de Notas, 32, p. ?; AGCRJ, Códice 42-3-55, p. 88
Data - 1635
Descrição
Escritura de venda de terras que fazem Martim Afonso de Souza, índio da terra, e sua mulher Domingas Ferreira, índios da Aldeia de São Barnabé, a Bernardo de Almeida, no valor de 12 réis – com 125 braças de testada, sitas pelo rio de Aguapeí-açu.

AN, 1º Ofício de Notas, 32, p. 42v; AGCRJ, Códice 42-3-55, p. 95
Data - 1635
Descrição
Escritura de quitação que dá Diogo Teixeira de Carvalho a Fernão Rodrigues Ribeiro - quitação da quantia de 793$000 (793 réis) resto da compra do engenho de Guaxindiba, pagamento este a que Fernão Ribeiro foi condenado por sentença que alcançou da justiça.

AN, 1º Ofício de Notas, 32, p. 65; AGCRJ, Códice 42-3-55, p. 97
Data - 1635
Descrição
Escritura de partido que fazem Pedro de Oliveira e sua mulher Joana de Andrade com Diogo Mendes Coluna e sua mulher Maria de Albernaz – [sito em suas terras da ilha do Governador, compradas a Salvador Correia de Sá e Benevides e sua mulher].

AN, 1º Ofício de Notas, 32, p. 66v; AGCRJ, Códice 42-3-55, p 97
Data - 1635
Descrição
Escritura de débito que faz Pedro de Oliveira ao Capitão Gregório Mendes da Silva – da quantia de 1:511$000 (1511 réis pagos em açúcares brancos e mascavados), que lhe pagaria pelo Senhor Salvador Correia de Sá e Benevides, a quem os devia pela compra do engenho da ilha, pagando-os em açúcares brancos e mascavados. Logo a seguir Gregório Mendes da Silva faz escritura de quitação de dívida a Salvador Correia de Sá e Benevides e a seu pai, Martim de Sá, de todas as contas que até ao presente tiver.

AN, 1º Ofício de Notas, 32, p. 142v; AGCRJ, Códice 42-3-55, p 109
Data - 1636
Descrição
Escritura de contrato e obrigação que faz Luiz Peres com seu sogro Manoel Delgado – sobre um partido de canas que Luiz Peres tinha no engenho de Álvaro de Matos, que Luiz agora cede ao sogro em contrato de meias, que entra com quatro peças de guiné.

AN, 1º Ofício de Notas, 32, p. 147v
Data - 1636
Descrição
Escritura de débito e obrigação que faz Pedro de Oliveira ao Capitão João Rodrigues Bravo, no valor de 1046 réis – da quantia de 1:046$400, que lhe devia o Senhor Salvador Correia de Sá, de quem havia comprado o engenho e ilha. Com autógrafos de Pedro de Oliveira e Salvador Correia de Sá e Benevides.

AN, 1º Ofício de Notas, 32, p. 154v; AGCRJ, Códice 42-3-55, p. 111
Data - 1636
Descrição
Escritura de venda de terras que fazem Francisco Gonçalves e sua mulher Felipa Delgada a Domingos de Freitas, no valor de 170 réis. 

AN, 1º Ofício de Notas, 32, p. 151; AGCRJ, Códice 42-3-55, p. 111
Data - 1636
Descrição
Escritura de venda de terras que fazem Luiz da Costa e sua mulher Águeda Lopes a Antônio Cavaco, no valor de 32 réis – com 250 braças de testada e meia légua de sertão, sitas em Suruí, compradas a Pedro Gonçalves de Abreu.

AN, 1º Ofício de Notas, 32, p. 159; AGCRJ, Códice 42-4-89, p. 921
Data - 1636
Descrição
Escritura de distrato que fazem Manoel Moreira e sua mulher Joana da Silva com Luiz Fernandes da Costa e sua mulher Águeda Lopes – sobre umas terras com 300 braças de testada e meia légua de sertão, sitas em Suruí, que os segundos venderam aos primeiros por 30$000 réis. 

AN, 1º Ofício de Notas, 32, p. 74v
Data - 1636
Descrição
Escritura de débito e obrigação com hipoteca de um engenho que faz João Barbosa Calheiros, devedor, ao Capitão Gregório Mendes da Silva, credor. A escritura possui o valor de 440 réis. 

AN, 1º Ofício de Notas, 32, p. 75; AGCRJ, Códice 42-3-55, p. 100
Data - 1636
Descrição
Escritura de quitação que dá João Ferreira Dormondo a Jorge de Souza, no valor de 140 réis, valor de um partido de canas que sua mulher, Francisca da Costa, vendera ao dito Jorge de Souza.

AN, 1º Ofício de Notas, 32, p. 157; AGCRJ, Códice 42-3-55, p. 111
Data - 1636
Descrição
Escritura de venda de terras que fazem Francisco da Costa Homem e sua mulher Maria de Araújo a João Homem de Andrade, no valor de 100 réis – com 186 braças de testada e uma légua de sertão, sitas em Sapopema, na data dos mais heréus, partindo de uma banda com terras de Sebastião de Sampaio e da outra com Francisco e Antonio de Alvarenga, e da outra com terras de Manoel de Andrade, havidas por dote de seu sogro e pai João de Araújo.

AN, 1º Ofício de Notas, 34, p. 8; AGCRJ, Códice 42-3-55, p. 118
Data - 1636
Descrição
Escritura de quitação que dá Gabriel Gomes, como procurador de sua mãe Isabel Gomes, a João Luiz Mafra – da quantia de 5.000 cruzados, pela qual lhe venderam o engenho de Nossa Senhora de Betancor.

AN, 1º Ofício de Notas, 32, p. 159; AGCRJ, Códice 42-3-55, p. 112
Data - 1636
Descrição
Escritura de venda de terras que faz o Padre Francisco Carneiro, reitor do Colégio da Companhia de Jesus, a Maria da Rocha, no valor de 1000 cruzados – uns sobejos sitos no rio de Macacu, que ficam em circuito de meia légua de terras que o Colégio tinha vendido a Manoel Coelho, defunto, partindo de uma banda pelo rio Macacu acima até onde está o último marco do Colégio, pela cabeceira com terras que foram de Pero de Azevedo e do outro lado do rio de Aguapeiaçu toda a terra que se achar depois de medidos .... Sardinha, .... Rebelo, ...gel, ...Jerônimo Vieira, Antonio Cubas, Antonio Dias, Baltazar Pinto, Antonio Martins da Palma.

AN, 1º Ofício de Notas, 34, p. 25
Data - 1636
Descrição
Escritura de débito e obrigação que faz João Dias, devedor, a Duarte Vaz Pinto – da quantia de 362$000, valor dos cobres e mais coisas que comprara para o seu engenho, que pagará em açúcar.

AN, 1º Ofício de Notas, 34, p. 33; AGCRJ, Códice 42-3-55, p. 121
Data - 1636
Descrição
Escritura de venda de terras que faz o reverendo padre Francisco Carneiro, reitor do Colégio da Companhia de Jesus, a Pero Pinheiro, no valor de 230 réis – com 750 braças de comprido e meia légua de sertão, sitas no rio Macacu, onde chamam Nhemboy, partindo com terras de Afonso Pereira, começando-se a medir o sertão 30 braças do marco de Afonso Pereira, que está junto do rio, para dentro, pelo rumo que as terras de Afonso Pereira levam por aquela ilharga.

AGCRJ, Códice 42-3-55
Data - 1636
Descrição
Escritura de venda de terras que faz Diogo da Mota a Francisco Cabral de Távora, no valor de 20 réis – sitas em Guaxindiba.

AN, 1º Ofício de Notas, 34, p. 61v; AGCRJ, Códice 42-3-55, p. 120
Data - 1636
Descrição
Escritura de venda de terras que fazem Belchior da Fonseca e sua mulher Simoa de Cális a Matias de Mendonça e sua mulher Isabel Cardosa, no valor de 60 réis - com 200 braças de testada e 550 de sertão, sitas no rio de Macacu, partindo de uma banda com terras que foram de Paulo da Cruz e da outra com terras dos padres da Companhia.
Não teve efeito.

AN, 1º Ofício de Notas, 34, p. 69; AGCRJ, Códice 42-3-55, p. 127
Data - 1636
Descrição
Escritura de dote que fazem Manoel Correia e sua mulher Maria de Alvarenga à sua filha Maria Correia - dentre outras coisas, incluem o engenho da Cruz, com todas as suas benfeitorias e peças de serviço, correndo as terras do engenho até entestar com a dada que eles dotadores deram a Francisco de Alvarenga, seu cunhado e irmão. Doam também uma morada de casas de sobrado, sita no alto e praça desta cidade e outros bens móveis. 

AN, 1º Ofício de Notas, 34, p. 74
Data - 1636
Descrição
Escritura de dote de casamento que faz João de Cális, viúvo de Maria Corneles (?), a Belchior da Fonseca, por se casar com sua neta Simoa de Cális – Diz que prometera o dote em tempos passados mas que não oficializara a doação. Por esta escritura doa 200 braças de terras de testada, sitas em Macacu, junto à aldeia dos padres da Companhia, que começam a medir da tapera onde esteve Simão Luiz, partindo de uma banda com as terras de Palos da Cruz e da outra com terras dos padres da Companhia.

AN, 1º Ofício de Notas, 34, p. 62v; AGCRJ, Códice 42-3-55, p. 120
Data - 1636
Descrição
Escritura de venda de terras que fazem Belchior da Fonseca e sua mulher Simoa de Cális a Matias de Mendonça e sua mulher Isabel Cardosa - sitas no rio de Macacu e no porto da aldeia de São Barnabé. 

AN, 1º Ofício de Notas, 34, p. 74; AGCRJ, Códice 42-3-55, p. 127
Data - 1636
Descrição
Escritura de venda de terras que fazem Bartolomeu de Vasconcelos e sua mulher Beatriz Cardosa a Matias de Mendonça, no valor de 100 réis – com 300 braças de testada, sitas no rio de Macacu, correndo o sertão até o caminho que vai da casa de Tomé de Cális para Tambeí, e do dito caminho correrá o travessão conforme a compra que Paulo da Cruz fez aos padres, rumo direito.

AN, 1º Ofício de Notas, 34, p. 76; AGCRJ, Códice 42-3-55
Data - 1636
Descrição
Escritura de venda de terras que fazem Belchior da Fonseca e sua mulher Simoa de Cális a Matias de Mendonça, no valor de 60 réis – com 200 braças de testada e 550 de sertão, sitas no rio de Macacu e no porto da aldeia de São Barnabé, partindo de uma banda com terras que foram de Paulo da Cruz e da outra com terras dos padres da Companhia, havidas de dote de casamento.
Observações: Por esta mesma escritura os compradores Matias de Mendonça e sua mulher Isabel Cardosa transferem aos vendedores a mesma quantidade de terras que eles possuíam no fim do sertão das terras compradas, que estão no caminho que vai das casas de Tomé de Cális para Tambeí.

FF, HCRJ, 384-385
Data - 1636
Descrição
Escritura de venda de terras que faz o reverendo padre Francisco Carneiro, reitor do Colégio, a Maurícia Gomes e a seu marido, no valor de 400 reis - um pedaço de terras que está no termo desta cidade, onde chamam Iguaçu, no qual pedaço têm feito os compradores um engenho, partindo da banda desta cidade com terras do Conselho, e começa do nascimento do dito rio de Iguaçu, vindo pelas voltas do rio abaixo até dar no mar, e da outra banda com terras que o dito Colégio vendeu a Francisco Viegas e Baltazar Leitão e Manoel Fernandes, as quais estão já demarcadas, e da banda da costa brava partem com terras do Conselho pelo rumo do sudoeste que se começará a lançar da nascente do dito rio do marco que ali está, donde se começa a medição de todas as terras que o Colégio e padres aí têm.
Observações: Escritura não teve efeito (AN, 1ON, 34, p. 89v; AGCRJ, Códice 42-3-55, p. 131). Esta escritura não teve efeito, provavelmente porque Maurícia morreu logo depois, já que há no mesmo livro uma escritura de partilhas entre Diogo Martins Madeira e Pero de Andrade, referente ao inventário de Maurícia Gomes, que era casada com o primeiro e sogra do segundo. 

AN, 1º Ofício de Notas, 34, p. 91; AGCRJ, Códice 42-3-55, p. 134
Data - 1636
Descrição
Escritura de concerto e composição entre o Convento do Carmo e Manoel da Rocha e sua mulher Maria Sardinha - sobre um partido de canas para moer no engenho de Nossa Senhora do Carmo, [sito em Suruí]. 

AN, 1º Ofício de Notas, 34, p. 94; AGCRJ, Códice 42-3-55, p. 144
Data - 1636
Descrição
Escritura de débito que faz Pedro de Oliveira aos padres da Companhia – da quantia de 1:464$464, referente a dívidas de Salvador Correia de Sá e Benevides, que ele teria que pagar pela compra da ilha do Governador.

AN, 1º Ofício de Notas, 34, p. 97; AGCRJ, Códice 42-3-55, p. 145
Data - 1636
Descrição
Escritura de venda de um partido que faz André de Ossina [do Sim] a Mateus Antunes e Francisco de Faria, no valor de 64 réis – da pretensão de 10 tarefas de canas e do aforamento das terras.

AN, 1º Ofício de Notas, 34, p. 108v; AGCRJ, Códice 42-3-55, p. 145
Data - 1636
Descrição
Escritura de louvamento sobre um partido de canas entre o Padre Reitor do Colégio da Companhia de Jesus e Pedro de Oliveira. 

AN, 1º Ofício de Notas, 34, p. 116v; AGCRJ, Códice 42-3-55, p. 145
Data
1636-01-01
Descrição
Escritura de venda de um curral de gado em Campo Grande que faz Miguel Aires Maldonado a Pero Bentes de...

AN, 1º Ofício de Notas, 34, p. 114; AGCRJ, Códice 42-3-55, p. 137
Data - 1637
Descrição
Escritura de venda de terras que fazem Francisco de Andrade e sua mulher Inês Rodrigues a Antonio Cardoso, no valor de 45 réis – com 250 braças de testada e uma légua de sertão, sitas no rio de Inhomirim, partindo de uma banda com terras dos vendedores e da outra com terras que foram de João Botelho, defunto, compradas a Heitor de Barros Pereira.

AN, Caixa 1146, No 13, Galeria A, p.. 4
Data - 1637
Descrição
Escritura de venda de terras que fazem Lourenço de Sampaio, seu filho Antonio de Sampaio e a mulher deste último Francisca de Almeida a Antonio Vaz Viçoso, no valor de 32 réis – sitas na serra e fralda de Gericinó, termo desta cidade, acabando a testada do engenho de Diogo de Montarroio, o que se entende até o cume da serra, e acabada a testada do engenho de Lázaro Fernandes, até o cume da dita serra, e começará a medir meia légua de terra do engenho de Diogo de Montarroio, até encher a meia légua, que é a testada do dito seu engenho, e daí para diante disseram que vendiam ao comprador todas as demais terras que se achar serem deles vendedores, que se entende toda a dita serra e terras que houverem para a banda dos campos de Juari, para a banda de Marapicu, terras aqui vendidas que herdaram de seu sogro e avô João de Basto e de sua sogra e avó Maria de Oliveira.Com declaração de que vendiam todas as terras que herdaram, conforme seus títulos, reservando para si apenas as duas testadas dos ditos dois engenhos de Diogo de Montarroio e de Lázaro Fernandes, até o cume da serra, que são meia légua cada uma.

Cf. Eduardo Marques Peixoto. Tijuca. Aldeia de Guiraguadú-Mirim. RIHGB, 73, Parte 2, 1910, pp. 147-154
Data - 1636
Descrição
Auto de medição das terras de Salvador Correia de Sá e Benevides: "No mesmo mês (de outubro) se abriu na laje natural, que estava junto ao sítio da tapera e aldeia de Guiraguaçu-mirim uma cruz ao picão, em forma de hábito de Cristo, a qual ficou para a parte mais baixa da dita laje, e o dito marco se arrumou pelo demarcador e piloto um outeiro alto que estava sobre o engenho novamente situado, de Manoel Caldeira, para, do dito outeiro, se lançar o rumo direito à tapera de Sapupema, de que a carta de sesmaria fazia menção. O outeiro demorava da laje e aldeia de Guiraguaçu-mirim a Sudeste e quarta de sudoeste ... Do dito rumo foram os demarcadores cortando pelos matos para sudeste e quarta de sudoeste. Atravessaram um canavial novo, de João de Souro, feito nas terras dos herdeiros de Manoel Caldeira, e continuando atravessaram um rumo que se dizia ser dos sobreditos sangrados(?), do mar para o sertão, entre eles e as terras que foram de Inácio de Andrade, onde cruzaram o dito rumo e meteram um marco de pedra com um hábito de Cristo. Continuando, foram dar na fazenda e engenho que foi do Doutor Manoel Leitão [já falecido] e era de sua mulher [Antônia de Aguiar] e herdeiros, cortando por cima do forno da olaria, passando por canaviais do engenho da parte do sul, atravessaram o caminho real que ia da praia para a cidade, onde meteram um marco de pedra, com outro hábito de Cristo. Este marco ficava na borda do caminho, para o sul. Cortaram pelo canavial de Diogo Lopes Ramos, pelos matos, continuando o rumo por cima de um monte alto, que ficava em frente do engenho de Diogo de Sá da Rocha, picando a coroa do dito monte para a parte do sul. Foram por matos virgens, por onde fizeram várias cruzes, atravessaram o caminho e estrada que de Jacarepaguá ia para o campo de Irajá, onde meteram um marco de pedra com o hábito de Cristo, que ficou da parte do norte da dita estrada, e foram entestar com a tapera de Sapupema, onde esteve e estava um marco antigo, que foi de Salvador Correia de Sá, capitão-mor e governador que foi desta cidade, o qual marco é de pedra e tem um "3" e um "S". Do referido marco se lançou o rumo de Sudoeste, conforme a carta de sesmaria, cortando por vários montes e vales até o sopé de uma serra de baeta roxa, onde em uma pedra muito grande, por debaixo da qual corria um ribeiro d’água, se fez uma cruz ao picão. Daquele ponto em diante, por ser demasiadamente fragosa, se não passou, protestando o Senhor Salvador Correia de Sá e Benevides correr com o rumo por diante, cada vez que lhe fosse necessário, para acabar de encher a sua data. Fez-se a declaração que com o rumo do sudoeste se atravessou o caminho novo que abriram os reverendos padres da Companhia do Campo Grande para a cidade, e por várias partes do rumo fizeram muitas cruzes em árvores, e assim marcaram a data sem contradição de pessoa alguma. O auto de medição foi assinado por Salvador Correia de Sá e Benevides, pelo Tesoureiro e Almoxarife Gregório de Barros, em comissão de Provedor da Fazenda, e, em seu impedimento, pelo Piloto Manoel da Costa, pelo medidor e demarcador Antonio Monteiro, pelo escrivão ordinário das medições Pero da Costa. Escreveu o auto Baltazar da Costa, escrivão da fazenda e juiz da Alfândega. Em 2 de novembro de 1638 foi o auto de medição concluído ao Provedor da Fazenda, Capitão Domingos Correia, que o confirmou no mesmo dia. Entregue na mesma data ao escrivão Baltazar da Costa, notificou este a Frutuoso da Fonseca, que disse estava prestes a despejar a terra que pela dita medição se lhe tomava, e que ficava dentro do rumo e demarcação de Salvador Correia de Sá e Benevides, pois a sua carta era mais antiga, como se tinha averiguado.

Félix Ferreira, A Santa Casa da Misericórdia Fluminense, p. 136
Data - 1638
Descrição
Escritura de doação de terras que faz o irmão Baltazar de Abreu à Santa Casa da Misericórdia – com 400 braças de testada, sitas juntas ao seu engenho de açúcar [Serra da Misericórdia]. 

AN, 1º Ofício de Notas, 56, p. 59
Data - 1639
Descrição
Escritura de venda de terras que faz [o padre reitor do Colégio desta cidade] ao Licenciado Jorge Fernandes da Fonseca - sitas no Engenho Pequeno (Escritura original do 2º Ofício). Aí terá uma moenda que ficará conhecida como Engenho Pequeno. Será vendido em 23/10/1675 por seu filho Doutor Francisco da Fonseca Diniz [por alcunha, o Gadelha] e sua mulher Isabel Rangel [de Macedo] ao Capitão Fernão Faleiro [Homem].

AN, Caixa 1146, No 13, Galeria A, p. 6v
Data - 1639
Descrição
Escritura de venda de terras que fazem Luiz Fernandes da Costa e sua mulher Águeda Lopes a Antonio Vaz Viçoso, no valor de 20 réis – Dizem os vendedores que eles vendiam ao comprador a parte que lhe coubesse de umas terras sitas em Gericinó, que eles haviam herdado, junto com outros herdeiros, de seu pai e sogro Reverendo Padre Martim Fernandes, vigário que foi da Sé Matriz desta cidade, que as havia recebido por carta de sesmaria. Declaram que as terras aqui vendidas partem de uma banda com terras do engenho que foi de Lázaro Fernandes e da outra com terras que foram de Gaspar da Costa, para os Palmares.
Escritura lavrada na casa de Frutuoso da Fonseca, sita no caminho de Santo Antonio.

AMSBRJ, Seção 6.2, Nº 170
Data - 1639
Descrição
Escritura de venda de terras que faz o Mosteiro de São Bento a Luiz Mendes Coluna, no valor de 120 réis - Mosteiro diz que tem 750 braças para cada lado do rio Guaguaçu. Vende nas 750 braças que tem de largo, no lado onde fica o rio Morobaí, 300 braças ao longo do dito rio de Morobaí e 800 de comprido, as quais terras se acharão da forma seguinte: pelo rio de Morobaí acima se medirão 450 braças da barra do dito rio, por ele acima, e as 300 que ficam até entestar com terras do dito comprador são as que lhe são vendidas por esta escritura, com 800 de comprido. (Escritura do 2º Ofício).

AGCRJ, Códice 42-3-57, p. 248
Data - 1640
Descrição
Escrito particular que fazem entre si Domingos Coelho e Jordão Homem da Costa – "... de conformidade de sobre estas terras onde estamos com nossas fazendas, e assentamos e repartimos de hoje para todo o sempre, assim para nós como para nossos filhos, que é este concerto por nós ambos assinados valerá como escritura pública, e aquele que isto distratar e negar não deve ter justiça ... razão, e assim como nos ajustamos em parte don... tabelião se fará escritura, declarando as forças do dito ... declaramos e partimos as ditas terras desta maneira, .... da borda do canavial de Antonio Machado pelo caminho ... direito, a mesma casas nela pelo canto do curral defronte ... partindo rumo direito para o oiteiro, e reme.....hihi, atravessando a terra, tudo o que se achar ser de Jordão Homem começa do rio, que é a demarcação, que da outra banda todo o direito que o dito Domingos Velho(sic) tem, larga ao dito João(sic) Homem pela ilharga nas cabeceiras a sua terra, e eu direi correndo ao longo do rio, lado onde tenho as casas, e roças e curral, correndo para Tarehirato até dar em uma lagoa que está em o pé de um oiteiro que tem um pau grosso de etindolim, pela borda do caminho que vai para a roça de Jordão Homem que se chama Ita...., donde hoje atualmente tem sua roça e casas, até aí chegará a dita minha terra à dita lagoa e pau, que é a demarcação da outra ilharga assim como para o rio com pe.... serra da tiga há a terra que se achar, assim minha como do dito Jordão Homem, entrando aqui a terra do dito meu sobrinho órfão Manoel Homem".

Apud Rudge, As sesmarias de Jacarepaguá, pp. 79-80
Data - 1640
Descrição
Escritura de composição que fazem André da Silveira Vilalobos [e sua mulher Dona Isabel do Souto Maior] com o Senhor Salvador Correia de Sá e Benavides – Sobre as terras que o casal havia comprado a João Rodrigues Bravo em 2/11/1635, e por ele João Rodrigues Bravo compradas a Salvador Correia de Sá e Benavides em 15/2/1635. Esta escritura define os limites definitivos dessas terras: "que começarão a medir no rio de Itatindiba, no meio do caminho, e medirão 1.500 braças pelo rumo de oeste, quarta de noroeste, entre o engenho que foi do Capitão Pedro Martins Negrão e os ditos compradores [André de Vilalobos da Silveira e sua mulher]; e acabantes as ditas 1.500 braças, medirão 1.150 braças ao sul, quarta de sudoeste; e donde acabam as ditas 1.150 braças tornarão caminho ao caminho pelo mesmo rumo que levaram o dito Capitão Pedro Martins Negrão e eles compradores, e medirão outras 1.500 braças; donde acabarem as ditas 1.500 braças se porá um marco, e daí medirão um rumo direito até o caminho; e essa terra que fica ente este marco e o caminho, disse ele dito senhor Salvador Correia de Sá e Benavides que largava, como com efeito logo largou, a els ditos compradores, porquanto a terra que tinham comprado ao dito Capitão João Rodrigues Bravo era 1.500 braças em quadra ... de modo que se entende que o rumo de sul, quarta de sudoeste, há de ser ao longo do caminho, indo para Irajá, e donde ele acabar se hão de medir as 1.500 braças para o sertão; e as terras que houver de sobejo entre o caminho e o dito marco, estas são as que larga ele dito Senhor Salvador Correia de Sá e Benavides em recomposição das 350 braças, que é a quantidade que compraram eles ditos compradores ao dito Capitão João Rodrigues Bravo"

AN, 1º Ofício de Notas, 35, f. 103
Data - 1640
Descrição
Escritura de venda de sobejos de terras que faz Dona Maria de Mendonça, viúva de Miguel Carvalho, a Gabriel Gomes, no valor de 16 réis – sitas no rio de Sarapuí, indo para o porto, chegando até os mangues, partindo com terras do comprador, havidos pelo marido da vendedora por título de herança(?).
Observações: O dito Miguel já havia vendido esses sobejos ao comprador, sem escritura.

AN, 1º Ofício de Notas, 35, p. ?
Data - 1641
Descrição
Escritura de obrigação de partido que faz João de Pontes Fróis a Mateus Nunes Lobão e sua mulher Maria Fagundes – Diz o casal que eles possuíam um engenho em Cruará, termo desta cidade. Por esta escritura fazem obrigação de partido de doze tarefas de doze carros cada ano, partido que parte com Vicente de Andrade Ribeiro.


AN, 1º Ofício de Notas, 35, pp. 63-67
Data - 1641
Descrição
Escritura de venda de um engenho que fazem o Capitão Manoel Homem Albernaz e sua mulher Maria Cubas ao Capitão Bento do Rego Barbosa, no valor de 12000 cruzados – com casa de engenho e caldeiras coberta de telhas, com outra moenda ainda no chão, por levantar, com 36 bois de carro e roda e mais benfeitorias, com 12 escravos de guiné e uma ermida de taipa de mão coberta de telhas, de invocação Santo Antonio, sito em Jacutinga, havido por títulos de herança e de compra.

AN, 1º Ofício de Notas, 35, p. 72
Data - 1641
Descrição
Escritura de débito e obrigação que faz Rui Dias Bravo a Baltazar Maciel, como procurador de Inácia Nunes, viúva de André ... – Diz que é devedor da quantia de 801$000, que o marido de Inácia havia lhe emprestado para fazer um engenho. Por esta escritura paga metade da dívida e se compromete a pagar o restante em dois anos

AN, 1º Ofício de Nota, 35, p. 81
Data – 1641
Descrição
Escritura de venda de dois partidos de canas que fazem Pantaleão Duarte e sua mulher Dona Maria Coutinha a Lucas do Couto, no valor de 400 réis – .... Engenho foi de Miguel Gomes Bravo, defunto, .... Comprou ele dito vendedor a Domingos da ...

AN, 1º Ofício de Nota, 35, p. ?
Data - 1641
Descrição
Escritura de hipoteca de terras e obrigação que faz Lourenço Esteves a Pascoal Pais Vidigal e sua mulher Ana Barbosa – com 140 braças de testada e meia légua de sertão, sitas no termo desta cidade, que partem de uma banda com terras de Jorge de Souza [Coutinho] e Baltazar de Abreu e da outra com terras de sua irmã Joana ... Hipoteca as terras enquanto Pascoal faz o dito engenho junto a elas ou junto às de sua irmã, e sendo caso que não se faça o dito engenho ficam as terras desobrigadas. A obrigação que Lourenço faz é de 30 tarefas de canas de 16 carros cada ano. Querendo Pascoal vender o dito engenho, Lourenço terá preferência.

AN, 1º Ofício de Notas, 35, p. ?
Data - 1641
Descrição
Escritura de venda de uma ilha e compra que faz Dona Ana da Costa, viúva de Manoel Caldeira, a seu genro Mateus de Moura Fogaça, no valor de 35 réis – Diz que seu marido havia vendido a seu genro uma ilha que se chama Ver a Pedra, sita defronte da terra de seu engenho, que parte por uma banda com uma ilha ... que está sita pelo rio acima .... Por esta escritura vende novamente a ilha.

AN, 1º Ofício de Notas, 35, p. ?
Data - 1641
Descrição
Escritura de venda de um engenho que fazem João Homem de Andrade e sua mulher Beatriz Dorneles a Cláudio Antonio Besançon, no valor de 6000 cruzados – de invocação Nossa Senhora do Desterro, sito no termo desta cidade, em Sapopema, com 400 braças de terra de testada e ... de sertão, partindo pela testada com terra .... e por ... Capitão Belchior de Andrade e pela ilharga com terras de Francisco e Antonio de Alvarenga, que de presente possui o dito João, e da outra banda com Sebastião de Sampaio, com uma moenda, uma .. de cobre e duas ..., e uma bacia de resfriar, uma repartideira com dois remunhóis, uma batedeira, uma pomba, duas escumadeiras e mais benfeitorias, com 14 bois de carro e moenda, com as obrigações dos lavradores, a saber, ... da Silveira, com obrigação de 30 tarefas de 12 carros cada tarefa, Francisco de Medina(?), 20 tarefas de 12 carros.

AN, 1ON, 35, p. ?
Data - 1641
Descrição
Escritura de dote de casamento que faz Maria de Mariz a sua filha Paula Rangel e seu genro Marcos de Azeredo Coutinho – um partido de canas que foi de Baltazar Leitão, sito no engenho São Lourenço, com toda a cana que houver. Doa também uma morada de casas, de pedra, sita ... porta nova da cidade, nas quais de presente mora ...., foreira à Santa Casa da Misericórdia

AN, 1ON, 35, p. ?
Data - 1641
Descrição
Escritura de venda de terras que fazem Rodrigo Dias e sua mulher Andreza de Castilho a Manoel Cardoso, no valor de 30 réis – com 90 braças de testada e 500 de sertão, sitas em Curuará, rio de Inhomirim, partindo de uma banda com terras de Miguel (?) Cardoso e da outra com Bartolomeu Dias, compradas a Domingos ...

AN, 1ON, 35, p. 40v
Data - 1641
Descrição
Escritura de doação e obrigação de partido de canas que faz Dona Joana de Andrade, viúva de Pedro de Oliveira, a seu sobrinho Manoel Lopes Ravasco – toda a cachaça e remeles que se produzir em seu engenho por invocação Nossa Senhora do Pópulo, pelos bons serviços que dele e de sua mulher recebeu, enquanto o dito engenho for engenho, e sendo caso que ela ou seus herdeiros hajam de vender este dito engenho, o não poderão vender sem esta condição, e caso se faça outro engenho na dita ilha ... Doa também ao seu sobrinho uma morada de casas térrea, de taipa de mão, coberta de telha, sita na ... açougue velho, partindo de uma banda com Gaspar Pereira e da outra com casas dela doadora, a qual casa ela e o dito seu marido já haviam dado a seu sobrinho em vida sem fazer escritura, por haverem dado em dote de casamento a sua irmã (?) Maria de Oliveira, que Deus tem. Com declaração que ela doadora havia feito escritura de um partido de canas na ilha, o qual foi de Francisco Duarte, já defunto, e outro de Antonio Jorge, seu irmão, junto a ele, em que se obrigou a ele moer em seu engenho 30 tarefas de canas em cada um ano, e ela dita doadora se obriga novamente a lhe moer as canas dos ditos partidos, cujos estão (?).. dos canaviais de Afonso Pereira, que olha para os ditos partidos ....
"""

text1  = text1.split("\n") # irá dividir todo o texto e transformar a string em lista
opo = int()
for i in range (len(text1)-1,-1,-1): #Laço para retirar todas as posições desnecessárias
    if text1[i] == '' or text1[i] == 'Descrição':
        del(text1[i])
        opo = i
    elif 'Data - ' in text1[i]:
        del(text1[i])
        opo = i
    opo -= 1    
    if "Escritura" in text1[opo]: #Condição que irá adicionar as Escrituras (que tem os nomes) na variável [text]
        text.append(text1[opo])
del(text1)

for p in range (len(text)): #Loop para apagar tudo que estiver dentro de colchetes
    try:
        text[p] = text[p].replace(text[p][text[p].index("["):text[p].index("]")], "")
    except ValueError:
        continue






