
#importar biblioteca
import pyautogui as py
import time
import pandas
import pyperclip as pclip

link = ('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
py.PAUSE = 1

# passo 1: Entrar no sistema da empresa (link do drive)
py.press('win')
py.write('Google')
time.sleep(1)
py.press('enter')
time.sleep(2)
py.write(link)
py.press('enter')

#passo 2: Navegadr no sistema para encontrar a base de dados
time.sleep (4)
py.click(x=344, y=565, clicks=2)
time.sleep(2)

#passo 3: Exportar a base de dados (baixar o arquivo)
py.click(x=1338, y=558)
py.click(x=1212, y=206)
time.sleep(5)
#passo 4: Calcular os indicadores (faturamento e quantidade de produtos vendidos)
caminho = r'C:\Users\walte\Downloads\Vendas - Dez.xlsx'
planilha = pandas.read_excel(caminho)


#passo 5: Trasformar base de dados
faturamento = planilha['Valor Final'].sum()
qtd_produtos = planilha['Quantidade'].sum()
print(faturamento, qtd_produtos)

#passo 6: Formatar e-mail
py.hotkey('ctrl', 't')
py.write('https://mail.google.com')
py.press('enter')
time.sleep(5)
py.click(x=36, y=207)
time.sleep(3)
py.write('walter.garcia.silva@gmail.com')
py.press('tab')
py.press('tab')
time.sleep(2)
pclip.copy('Resultado do relatório de vendas')
py.hotkey('ctrl', 'v')
py.press('tab')
time.sleep(2)

texto = f''' 
    Prezados, 

    As vendas desse semestre foi um sucesso, segue os valores e a quantidade de produtos que foram vendidas.

    Estou embasbequecido com a capacidade do time. O faturamento total é de: R${faturamento:,.2f} e o total de 
    produtos vendidos é de: {qtd_produtos:,}

    Abraços!
'''

pclip.copy(texto)
py.hotkey('ctrl', 'v')

# Passo 7: Enviar e-mail
py.click(x=856, y=819)