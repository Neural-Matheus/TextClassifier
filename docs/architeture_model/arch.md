## Contexto:
O sistema é um classificador de texto baseado em BERT que é treinado e testado em um conjunto de dados de texto. Ele usa a biblioteca transformers para acessar modelos de linguagem pré-treinados.

## Container:
O sistema pode ser dividido em vários contêineres:

- **Pré-processamento de dados:** Limpa e codifica os dados de texto.
- **Modelo de aprendizado de máquina:** Usa um modelo BERT para classificar o texto.
- **Treinamento e teste:** Treina o modelo nos dados de treinamento e o testa nos dados de teste.

## Componente:
Dentro do contêiner "Text Classifier System", temos os seguintes componentes:

- **Data Cleaning Function (DCF):** Responsável por limpar os dados de texto brutos.
- **Data Encoding Function (DEF):** Encarregado de codificar os dados limpos.
- **DCNNBERTEmbedding Class (DC):** Fornece a arquitetura do modelo.
- **Model Compilation Code (MCC):** Compila o modelo para prepará-lo para o treinamento.
- **Model Training Code (MTC):** Treina o modelo nos dados fornecidos.
- **Model Testing Code (MTEC):** Testa o modelo e retorna os resultados da classificação.

Além disso, o ator "User" interage com o sistema, fornecendo dados de texto brutos e realizando o treinamento do modelo.

As relações entre os componentes são:

- O usuário fornece dados de texto brutos para a função de limpeza de dados.
- A função de limpeza de dados fornece dados limpos para a função de codificação de dados.
- A função de codificação de dados fornece dados codificados para a classe DCNNBERTEmbedding.
- O usuário treina o modelo usando o código de compilação do modelo.
- A classe DCNNBERTEmbedding fornece a arquitetura do modelo para o código de compilação do modelo.
- O código de compilação do modelo fornece o modelo compilado para o código de treinamento do modelo.
- O código de treinamento do modelo fornece o modelo treinado para o código de teste do modelo.
- O código de teste do modelo retorna os resultados da classificação para o usuário.