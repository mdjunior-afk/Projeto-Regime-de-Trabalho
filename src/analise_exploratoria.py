import pandas as pd 
  
 # Carregar os dados 
 file_path = "/mnt/data/The Impacts of Working Remotely and in an Office Survey.new.csv" 
 df = pd.read_csv(file_path) 
  
 # Exibir as primeiras linhas do dataset 
 df.head() 
  
 # Recarregar os dados com o delimitador correto 
 df = pd.read_csv(file_path, delimiter=";") 
  
 # Exibir as primeiras linhas novamente 
 df.head() 
  
 # Verificar o tamanho do dataset 
 num_rows, num_cols = df.shape 
  
 # Verificar valores ausentes 
 missing_values = df.isnull().sum() 
  
 # Resumo da análise inicial 
 num_rows, num_cols, missing_values 
  
  
  
 import matplotlib.pyplot as plt 
 import seaborn as sns 
  
 # Configurar estilo dos gráficos 
 sns.set(style="whitegrid") 
  
 # Selecionar perguntas de múltipla escolha para visualização 
 questions = [ 
     "Have you ever experienced working from home?", 
     "Do you think that working from home increases your work productivity?", 
     "Do you think that working from home prevents you from going out?", 
     "Do you think that working from home gives you more flexibility?", 
     "Do you think that working from home saves you more time?", 
     "Which work type keeps you focused while working?", 
     "Which work type do you prefer the most?" 
 ] 
  
 # Criar gráficos de barras para cada pergunta 
 fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(14, 12)) 
 axes = axes.flatten() 
  
 for i, question in enumerate(questions): 
     if i < len(axes):  # Garantir que não ultrapasse o número de subplots 
         sns.countplot(y=df[question], order=df[question].value_counts().index, ax=axes[i], palette="viridis") 
         axes[i].set_title(question) 
         axes[i].set_xlabel("Quantidade") 
         axes[i].set_ylabel("") 
  
 # Remover subplot extra caso o número de perguntas seja ímpar 
 if len(questions) < len(axes): 
     fig.delaxes(axes[-1]) 
  
 plt.tight_layout() 
 plt.show() 
  



  # Importando bibliotecas necessárias

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from matplotlib.backends.backend_pdf import PdfPages  # Para salvar em PDF



# Criando dicionário com os dados fornecidos

dados = {

    "Trabalhou em casa": [60, 40],

    "Acha que aumenta a produtividade": [70, 30],

    "Acha que impede de sair": [70, 30],

    "Acha que dá mais flexibilidade": [100, 0],

    "Acha que economiza tempo": [40, 60],

    "Maior risco físico ao trabalhar em casa": [80, 20],

    "Maior risco mental ao trabalhar em casa": [60, 40],

    "Impede contato social": [60, 40],

    "Mantém mais foco ao trabalhar em casa": [40, 60],

    "Prefere modo de trabalho misto": [50, 50]

}



# Criando DataFrame

df = pd.DataFrame(dados, index=["Sim (%)", "Não (%)"]).T



# Criando o arquivo PDF

pdf_filename = "graficos_correlacao.pdf"

with PdfPages(pdf_filename) as pdf:

    

    # Criando gráficos de correlação

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))



    # Correlação entre "Trabalhou em casa" e produtividade

    sns.scatterplot(ax=axes[0, 0], x=df["Trabalhou em casa"], y=df["Acha que aumenta a produtividade"], color='blue')

    axes[0, 0].set_title("Trabalhou em casa vs Produtividade")



    # Correlação entre "Trabalhou em casa" e contato social

    sns.scatterplot(ax=axes[0, 1], x=df["Trabalhou em casa"], y=df["Impede contato social"], color='red')

    axes[0, 1].set_title("Trabalhou em casa vs Contato Social")



    # Correlação entre riscos físicos e mentais

    sns.scatterplot(ax=axes[1, 0], x=df["Maior risco físico ao trabalhar em casa"], y=df["Maior risco mental ao trabalhar em casa"], color='green')

    axes[1, 0].set_title("Risco Físico vs Risco Mental")



    # Correlação entre economia de tempo e foco

    sns.scatterplot(ax=axes[1, 1], x=df["Acha que economiza tempo"], y=df["Mantém mais foco ao trabalhar em casa"], color='purple')

    axes[1, 1].set_title("Economia de Tempo vs Foco")



    plt.tight_layout()

    

    # Salvando os gráficos no PDF

    pdf.savefig(fig)

    plt.close(fig)



print(f"Gráficos salvos com sucesso em '{pdf_filename}'!")


 