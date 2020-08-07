#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:27:16 2020

@author: jesus_lara
"""

import pandas as pd
import csv           #Gestion de ficheros csv
import urllib3       #Navegar y acceder a info meidante url



#%% Abrir ficheros Excel XLS y XLSX
dirorigen = "/home/jesus_lara/git_workspace/MLearning/python-ml-course/datasets/"
infile = "titanic/titanic3.xlsx"

data1 = pd.read_excel(dirorigen+infile, "titanic3" )   #Hay que indicarle la hoja de calculo

#%% Crear un csv a partir de los datos modelados
data1.to_csv(dirorigen+"titanic/titanic Guardado.csv")
#%% Crear un excel a partir de los datos modelados
data1.to_excel(dirorigen+"titanic/titanic Guardado.xlsx")
#%% Crear un json a partir de los datos modelados
data1.to_json(dirorigen+"titanic/titanic Guardado.json")
