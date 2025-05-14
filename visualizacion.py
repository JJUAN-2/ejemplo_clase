# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# seaborn para visualizacion mas estilizadas 
import seaborn as sns
import os
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox



from Analisis import DataAnalyzer

data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)

info = analizar.summary()

def informacion():
        
        text_area.delete("1.0", tk.END) #Para vaciar al ejecutar 
        info = analizar.summary()
        text_area.insert(tk.END, info)
  


ventana = tk.Tk()
ventana.title("Analizis de datos")
boton_summary = tk.Button(ventana, text= "info", command= informacion)
boton_summary.pack()

text_area = tk.scrolledtext.ScrolledText(ventana, width = 70, height = 30, )

text_area.pack()
ventana.mainloop()