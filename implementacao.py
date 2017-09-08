import random
import time
import math

class Ordena():
    def __init__(self):
        self.vetor1 = []
        self.vetor2 = []
        self.vetor3 = []
        #1 - crescente
        #2 - decrescente
        #3 - aleatorio
    def gerar(self,tamanho):
        for x1 in range(int(tamanho)):
            self.vetor1.append(x1)
        for x2 in range(int(tamanho),0,-1):
            self.vetor2.append(x2)
        for x3 in range(int(tamanho)):
            self.vetor3.append(random.randint(0,int(tamanho)))
    def zerar(self):
        self.vetor1 = []
        self.vetor2 = []
        self.vetor3 = []

    def quickSort(self,vetor):
        a = time.time()
        self.__qs(vetor, 0,len(vetor)-1)
        return time.time() - a
    def __qs(self,vetor,primeiro,ultimo):
        pilhaAux = [0] * len(vetor) #pilha auxiliar para armazenar primeiros e ultimos
        aux = 0
        pilhaAux[aux] = primeiro
        aux += 1
        pilhaAux[aux] = ultimo
        while aux >= 0: #ate primeiro e ultimo se cruzarem
            ultimo = pilhaAux[aux]
            aux -= 1
            primeiro = pilhaAux[aux]
            aux -= 1
            p = self.__particao(vetor,primeiro,ultimo)
            if p-1 > primeiro: #elementos a esquerda
                aux += 1
                pilhaAux[aux] = primeiro
                aux += 1
                pilhaAux[aux] = p - 1
            if p+1 < ultimo: #elementos a direita
                aux += 1
                pilhaAux[aux] = p + 1
                aux += 1
                pilhaAux[aux] = ultimo
    def __particao(self,vetor,primeiro,ultimo):
        pivo = vetor[primeiro]
        esq = primeiro+1
        dire = ultimo
        while True:
            while esq <= dire and vetor[esq] <= pivo:
                esq += 1
            while vetor[dire] >= pivo and dire >= esq:
                dire -= 1
            if dire < esq:break
            #trocar
            aux = vetor[esq]
            vetor[esq] = vetor[dire]
            vetor[dire] = aux
        aux = vetor[primeiro]
        vetor[primeiro] = vetor[dire]
        vetor[dire] = aux
        return dire

    def insertionSort(self,vetor):
        a = time.time()
        for x in range(1,len(vetor)):
            aux = vetor[x]
            y = x
            while y > 0 and vetor[y-1] > aux:
                vetor[y]= vetor[y-1]
                y -= 1
            vetor[y] = aux
        return time.time() - a

    def radixSort(self,vetor):
        a = time.time()
        balde = []
        for i in range(10):
            balde.append([])
        maior = -1
        for x in vetor: 
            aux = len(str(x))
            if aux > maior:
                maior = aux
        for x in range(0, maior):
            for y in vetor:
                balde[y // 10**x % 10].append(y)
            del vetor[:]
            for z in balde:
                vetor.extend(z)
                del z[:]
        return time.time() - a 
