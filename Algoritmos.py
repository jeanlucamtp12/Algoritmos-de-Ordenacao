#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:12:27 2021

@author: jean
"""
''' Algoritmo Insertion Sort'''
def insertionSort (lista):
    
    for i in range (1, len(lista)):
        
        chave = lista[i]
        
        j = i - 1
        
        while (j >= 0 and lista[j] > chave):
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave    

''' Algoritmo Selection Sort'''
def selectionSort(lista):
       
    for j in range (len(lista) - 1):
        menorIndice = j

        for i in range(j, len(lista)):
            if (lista[i] < lista[menorIndice]):
                menorIndice = i                
       
        if (lista[j] > lista[menorIndice]):
            aux = lista[j]
            lista[j] = lista[menorIndice]
            lista[menorIndice] = aux        
  
''' Algoritmo Shell Sort'''          
def shell_sort(lista):
	n = len(lista)
    
	for i in (lista):
		j = i
		while (j <= n - 1):
			aux = lista[j]
			k = j
			while (k>=i) and (lista[k-i] > aux):
				lista[k] = lista[k-i]
				k = k - i
			lista[k] = aux
			j = j + i

''' Algoritmo Merge Sort'''
def mergeSort(lista, i=0, f=None):
    
    if (f == None):
        f = len(lista)
    
    if (f - i > 1):
        m = (f + i)// 2
        mergeSort(lista, i , m)
        mergeSort(lista, m , f)
        
        merge(lista, i, m, f)   
    
def merge(lista, ini, m , f):
    
    esquerda = lista[ini:m]
    direita = lista[m:f]
    
    i, j = 0, 0
    
    for k in range (ini, f):
        
        if i >= len(esquerda):
            lista[k] = direita[j]
            j = j + 1
            
        elif j >= len(direita):
            lista[k] = esquerda[i]
            i = i + 1
        
        elif esquerda[i] < direita[j]:
            lista[k] = esquerda[i]
            i = i + 1
        else:
            lista[k] = direita[j]
            j = j + 1            
  
''' Algoritmo Bubble Sort'''    
def bubble_sort(listaT):
    
    verifica = False
    tamanho = len(listaT)
    while not verifica:
        verifica = True
        for i in range(tamanho-1):
            if (listaT[i] > listaT[i+1]):
                aux = listaT[i]
                listaT[i] = listaT[i+1]
                listaT[i+1] = aux
                verifica = False            

''' Algoritmo Heap Sort'''
def max_Heapfy(vetor,tamanho, indice):

    esq = 2*indice + 1
    di = 2*indice + 2
    maior = indice
    
    if (esq < tamanho and vetor[esq] > vetor[indice]):
        maior = esq
    
    if (di < tamanho and vetor[di] > vetor[maior]):
        maior = di
     
    if (maior != indice):
        aux = vetor[indice]
        vetor[indice] = vetor[maior]
        vetor[maior] = aux
        max_Heapfy(vetor, tamanho , maior)
    
def max_Heap(vetor):
    
    tamanho = len(vetor)
    
    for i in range(tamanho // 2 - 1, -1, -1):   
        max_Heapfy(vetor, tamanho, i)
        
def heapsort(vetor):
    
    max_Heap(vetor)
    tamanho = len(vetor)
    
    for i in range(tamanho-1, 0,-1):
        
        aux = vetor[0] 
        vetor[0] = vetor[i]
        vetor[i] = aux
        max_Heapfy(vetor,i, 0)
                  
                   
            
            