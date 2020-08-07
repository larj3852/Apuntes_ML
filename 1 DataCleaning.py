#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:50:55 2020

@author: jesus_lara
"""

#%% LECTURA DE DATOS CSV
import pandas as pd
import csv           #Gestion de ficheros csv
import urllib3       #Navegar y acceder a info meidante url

dirorigen = "/home/jesus_lara/git_workspace/MLearning/python-ml-course/datasets/"
archivo = "titanic/titanic3.csv"
frame = pd.read_csv(dirorigen+archivo)
print(frame.head())


#%%
#Extraccion columnas y combinar con frame
archivo = "customer-churn-model/Customer Churn Columns.csv"
columnas = pd.read_csv(dirorigen+archivo)
columnas = columnas["Column_Names"].tolist()

archivo = "customer-churn-model/Customer Churn Model.csv"
frame = pd.read_csv(filepath_or_buffer=dirorigen+archivo,
                    header=None, 
                    names = columnas)

print (frame.columns.values)
#%%FUNCIÓN OPEN --> Cargar datos manual
dirorigen = "/home/jesus_lara/git_workspace/MLearning/python-ml-course/datasets/"
archivo = "customer-churn-model/Customer Churn Model.txt"
data3 = open(dirorigen+archivo,"r")

cols = data3.readline().strip().split(",") #Strip elimina todo lo que esté en blanco, split separa
n_cols = len(cols)  #Num columnas

'''Contar numero de filas'''
counter = 0 
main_dic = {}   #Diccionario vacio
for col in cols:
    main_dic[col] = []  #De esta forma se pasan los nombres de las columnas al diccionario

for line in data3:
    values = line.strip().split(",")
    for i in range(len(cols)):
        main_dic[cols[i]].append(values[i])
    counter+= 1
print(f"EL dataset tiene {n_cols} columnas x {counter} filas")
# %% LECTURA ESCRITURA DE NUEVO FICHERO
dirorigen = "/home/jesus_lara/git_workspace/MLearning/python-ml-course/datasets/"
infile = "customer-churn-model/Customer Churn Model.txt"
outfile = "customer-churn-model/Tab Customer Churn Model.txt"
with open(dirorigen+infile,"r") as infile:
    with open(dirorigen+outfile,"w") as outfile:
        for line in infile:
            fields = line.strip().split(",")
            outfile.write("\t".join(fields))    #Separacion por tabulador
            outfile.write("\n")
#%%
outfile = "customer-churn-model/Tab Customer Churn Model.txt"
data4 = pd.read_csv(filepath_or_buffer = dirorigen+outfile,sep="\t")
print(data4.head())

#%% LECTURA MEDIANTE URL
url=    "http://winterolympicsmedals.com/medals.csv" 
medallas = pd.read_csv(filepath_or_buffer = url)
medallas.head()


#%% CREACION FUNCION LECTURA Y CONVERSION A DATA FRAME DE DATOS MEDIANTE URL

def url2dataframe(url,sep,delimitador,encoding):
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    r.status
    datos = r.data #Como están en bin se pueden decodificar
    datos = datos.decode('utf8')
    datos = datos.split("\n")   #Separacion por filas
    #Extraccion de encabezados y creacion de diccionario
    dic = {}
    cols = []
    
    for dato in datos[0].split(","):    #1 columna encabezados, separarados por ","
        dic[dato]=[]
        cols.append(dato)
    
    for linea in datos[1:-1]:
        dato = linea.split(",")
        for i in range(len(cols)) :
            dic[cols[i]].append(dato[i])
        
    df = pd.DataFrame(dic)
    
    return df
    
#argumentos --> url,separador,delimitador,encoding origen
url=    "http://winterolympicsmedals.com/medals.csv" 
http = urllib3.PoolManager()
r = http.request('GET',url)
r.status

datos = r.data #Como están en bin se pueden decodificar
datos = datos.decode('utf8')
datos = datos.split("\n")   #Separacion por filas
#Extraccion de encabezados y creacion de diccionario
dic = {}
cols = []
for dato in datos[0].split(","):    #1 columna encabezados, separarados por ","
    dic[dato]=[]
    cols.append(dato)
    
for linea in datos[1:-1]:
    dato = linea.split(",")
    for i in range(len(cols)) :
        dic[cols[i]].append(dato[i])
    
dataframe_medallas = pd.DataFrame(dic)













