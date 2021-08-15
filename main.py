import pandas as pd
# Bibliotecas:

# pandas - Integração do python c/ excel
# openpyxl - Integração do python c/ excel
# twilio -  Integração do python c/ SMS


# Passo a passo de solução:

# Abrir os 6 arquivo do excel
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

tabela_vendas = pd.read_excel("janeiro.xlsx")

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    print(tabela_vendas)

    # verificar se em cada arquivo alguém vendeu 55.000

    if (tabela_vendas["Vendas"] > 55000).any():
        print(f"No mês de {mes} Encontrou alguém com mais de 55000")

