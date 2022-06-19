import os
from tqdm import tqdm
import ctypes
import tkinter as Tk
from tkinter import messagebox, filedialog
from tkinter import *



#Ocultando a janela raiz do tkinter
root = Tk()
root.withdraw()

# Mensagem de iformação
messagebox.showinfo("File_Rename", "Selecione a pasta que contenha os arquivos para conversão.")

# Selecionando pasta
folder = filedialog.askdirectory()



#Definindo variaveis
prefix_name = input('Insira o nome do prefixo --> ')
extension = input('Insira a extensão dos arquivos a serem renomeados --> ')
print()

#Encontrando os arquivos de acordo com as variáveis definidas 
encontrar_files = os.listdir(folder)

#Laço de repetição que renomeia os arquivos
for file in tqdm(encontrar_files):
    if file.endswith("." + extension):
        os.rename(folder + "/" + file, folder + "/"+ prefix_name + "_" + file)


ctypes.windll.user32.MessageBoxW(0, "Programa finalizado com sucesso.", "File_Rename", 1)

