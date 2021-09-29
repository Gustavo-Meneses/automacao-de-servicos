 automacao-de-servicos
automação iniciante!

import pyautogui
import pyperclip
import time

 PARTE 1:

pyautogui.PAUSE = 1

 Passo 1 - Entrar no nosso sistema (entrar no link: Link que o arquivo a ser analisado está. )
pyautogui.hotkey("ctrl", "t")
link = "Link que o arquivo a ser analisado está"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

 Passo 2 - Navegar no sistema (entrar na pasta Exportar)
time.sleep(5) - espera 5 segundos
pyautogui.click(x=, y=, clicks=2)

 Passo 3 - baixar o arquivo de vendas
time.sleep(2)
pyautogui.click(x=, y=)
pyautogui.click(x=, y=)
pyautogui.click(x=, y=)
time.sleep(3) - esperar ele fazer o download

 Vamos agora ler o arquivo baixado para pegar os indicadores

- Faturamento
- Quantidade de Produtos

- Passo 4 - Calcular faturamento e quantidade de produtos vendidos
import pandas as pd

tabela = pd.read_excel(r"C:\Users\alonp\Downloads\Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
display(tabela)

- VAMOS AGORA ENCAMINHAR UM EMAIL PELO GMAIL

- Passo 5 - Enviar o email para a diretoria
pyautogui.hotkey("ctrl", "t") - abre uma nova aba
link = "https://mail.google.com/"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

- clicar no botão escrever
time.sleep(5)
pyautogui.click(x=, y=)

 escrever pra quem eu to mandando o email
pyautogui.write("@gmail.com")
pyautogui.press("tab") - escolher o email
pyautogui.press("tab") - passar pro campo de assunto

- escrever o assunto
assunto = "Relatório de Vendas"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab") - passar pro corpo do email

- escrever o corpo do email
texto = f"""
Prezados, bom dia

O faturamento foi de R${faturamento:,.2f}
A quantidade de produtos foi de {quantidade:,}

Abs
Gustavo Meneses"""
pyautogui.write(texto)

- enviar o email
pyautogui.hotkey("ctrl", "enter")

====================================================================================================================================================================

- Para localizar as coordenadas de cada item a ser selecionado, usar o código:

import time
time.sleep(5)
pyautogui.position()




