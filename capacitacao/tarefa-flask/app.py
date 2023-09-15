from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

# Carregar a base de dados de pessoas
df = pd.read_csv('/Users/alvarenga/analytica/AULAFLASK/Tarefa/dados-flask-treino.csv')

df['salario'] = df['salario'].str.replace('$', '').astype(float)

def acharIndicePaisNaAPI(pais):
    database = pd.read_json("https://servicodados.ibge.gov.br/api/v1/paises/{paises}")
    with open('conversoes.json', 'r') as arquivo_json:
        dados = json.load(arquivo_json)
    for i in dados:
        if i['nome'] == pais:
            siglaPais = i['codigo']    
    for i in range(len(database)):
        if database['id'][i]['ISO-3166-1-ALPHA-2'] == siglaPais:
            capital = database['governo'][i]['capital']['nome']
            moeda = database['unidades-monetarias'][i][0]['nome']
    return capital, moeda

# Rota para a página inicial que lista os países
@app.route('/')
def index():
   paises = sorted(df['pais'].unique())

   return render_template('index.html', paises=paises)

# Rota para calcular a média salarial de um país específico
@app.route('/pais/<pais>')
def dados_pais(pais):

    # Filtrar o DataFrame para as pessoas do país específico
    pessoas_no_pais = df[df['pais'] == pais]

    # Calcular a média salarial para esse país
    media_salarial = pessoas_no_pais['salario'].mean()

 # Definir a função para calcular média salarial por faixa etária
    def calcular_media_por_faixa_etaria():
        faixas_etarias = [(1, 20), (20, 40), (40, 60), (60, 80), (80, 101)]
        medias = []
        for faixa in faixas_etarias:
            faixa_inferior, faixa_superior = faixa
            filtro = (pessoas_no_pais['idade'] >= faixa_inferior) & (pessoas_no_pais['idade'] < faixa_superior)
            media_salarial = pessoas_no_pais.loc[filtro, 'salario'].mean()
            medias.append({"faixa_etaria": f"{faixa_inferior}-{faixa_superior}", "media_salarial": media_salarial})
        return medias

    # Calcular a média salarial por faixa etária
    media_por_faixa_etaria = calcular_media_por_faixa_etaria()

    # Calcular a representatividade de gênero em porcentagem
    total_pessoas = len(pessoas_no_pais)
    total_homens = len(pessoas_no_pais[pessoas_no_pais['genero'] == 'Male'])
    total_mulheres = len(pessoas_no_pais[pessoas_no_pais['genero'] == 'Female'])
    outros_pessoas = pessoas_no_pais[(pessoas_no_pais['genero'] != 'Male') & (pessoas_no_pais['genero'] != 'Female')]
    total_outros = len(outros_pessoas)

    representatividade_genero = {
        'Homens': (total_homens / total_pessoas) * 100,
        'Mulheres': (total_mulheres / total_pessoas) * 100,
        'Outros': (total_outros / total_pessoas) * 100
    }

    capital, moeda = acharIndicePaisNaAPI(pais)

    # Renderizar a página HTML com informações específicas para o país e médias por faixa etária
    return render_template('pais.html', pais=pais, media_salarial=media_salarial, media_por_faixa_etaria=media_por_faixa_etaria, representatividade_genero=representatividade_genero, capital=capital, moeda=moeda)

if __name__ == '__main__':
    app.run(debug=True)
