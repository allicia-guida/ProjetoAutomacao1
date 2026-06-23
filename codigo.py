import pyautogui
import time
import pandas


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(4)

link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4)

pyautogui.click(x=505, y=546, clicks=2)
time.sleep(8)

pyautogui.click(x=1770, y=552)
time.sleep(1)

pyautogui.click(x=1444, y=532)
time.sleep(1)

caminho = r"C:\Users\allicia.brant\Downloads\Vendas - Dez.xlsx"
tabela = pandas.read_excel(caminho)
time.sleep(6)

print(tabela)

faturamento = tabela["Valor Final"].sum()
qtde_produtos = tabela["Quantidade"].sum()

print(faturamento)
print(qtde_produtos)
