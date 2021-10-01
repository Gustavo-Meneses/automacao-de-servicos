#automacao de serviços.
#automação iniciante!


#PARTE 1:
#Passo 1

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

pyautogui.hotkey("ctrl", "t")
link = "Link que o arquivo a ser analisado está"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#Passo 2

time.sleep(5) - espera 5 segundos
pyautogui.click(x=, y=, clicks=2)

#Passo 3

time.sleep(2)
pyautogui.click(x=, y=)
pyautogui.click(x=, y=)
pyautogui.click(x=, y=)
time.sleep(3) #esperar ele fazer o download

#Passo 4

import pandas as pd

tabela = pd.read_excel(r"C:\Users\alonp\Downloads\Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
display(tabela)

#PARTE 2:

#Passo 1

pyautogui.hotkey("ctrl", "t") #abre uma nova aba
link = "https://mail.google.com/"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#Passo 2

time.sleep(5)
pyautogui.click(x=, y=)

#Passo 3

pyautogui.write("@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

#Passo 4

assunto = "Relatório de Vendas"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

#Passo 5

#escrever o corpo do email
texto = f"""
Prezados, bom dia

O faturamento foi de R${faturamento:,.2f}
A quantidade de produtos foi de {quantidade:,}

Abs
Gustavo Meneses"""
pyautogui.write(texto)

#Passo 6

pyautogui.hotkey("ctrl", "enter")

====================================================================================================================================================================

#Para localizar as coordenadas de cada item a ser selecionado, usar o código:

import time
time.sleep(5)
pyautogui.position()




