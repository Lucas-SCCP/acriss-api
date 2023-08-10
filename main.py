import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.acriss.org/car-codes/'
response = requests.get(url)

if response.status_code == 200:
    page_content = response.content
else:
    print('Falha')


soup = BeautifulSoup(page_content, "html.parser")

titles = soup.find_all("table", class_="table")
cabecalho = []
conteudo = []
for index, title in enumerate(titles):
    if index == 0:
        if title.text is None:
            print('Nulo')
        else:
            teste = title.text.split('\n\n\n')
            for idx, te in enumerate(teste):
                if idx == 0:
                    tratado = te.split('\n\n')
                    cabecalho = [valor for valor in tratado if valor != '']
                else:
                    tratado = te.split('\n')
                    dados = [valor for valor in tratado if valor != '']
                    conteudo.append(dados)

dados = []
dados_com_cabecalho = []
teste = {}
retorno = []
category = []
type = []
drive = []
fuel = []

print(cabecalho[0])

for index, cnt in enumerate(conteudo):
    pares_divididos = [cnt[i:i+2] for i in range(0, len(cnt), 2)]
    if len(pares_divididos) > 1:
        category.append(pares_divididos[0])
        type.append(pares_divididos[1])
        drive.append(pares_divididos[2])
        fuel.append(pares_divididos[3])

teste[cabecalho[0]] = category
teste[cabecalho[1]] = type
teste[cabecalho[2]] = drive
teste[cabecalho[3]] = fuel

json_string = json.dumps(teste, indent=4)
print(json_string)