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
  
  
 