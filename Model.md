# Arquituras de Modelo: RNN e LSTM

## 1. Redes Neurais Recorrentes (RNN):

![Representação de uma RNN](https://cdn.discordapp.com/attachments/1184622679685333042/1184622892764377118/1_eHTWi-gXzh3oC4A3iRvruQ.png?ex=658ca50a&is=657a300a&hm=b32f790d65de4d5e196f7a50c597adb089628426b0089b33fe8fde80a20af246&)

#### Explicação:
As Redes Neurais Recorrentes (RNNs) são projetadas para processar sequências de dados, como séries temporais ou linguagem natural. A principal característica é a presença de uma conexão retroativa (loop) que permite que informações anteriores influenciem o processamento no tempo seguinte.

A lógica matemática da RNN para uma etapa de tempo t é dada por:

\[ h_t = \sigma(W_{hh} \cdot h_{t-1} + W_{xh} \cdot x_t + b_h) \]

Onde:
- \( h_t \) é o estado oculto no tempo t.
- \( x_t \) é a entrada no tempo t.
- \( W_{hh} \) é a matriz de pesos para a conexão retroativa.
- \( W_{xh} \) é a matriz de pesos para a entrada.
- \( b_h \) é o vetor de viés.
- \( \sigma \) é a função de ativação.

## 2. Long Short-Term Memory (LSTM):

![Representação de uma LSTM](https://cdn.discordapp.com/attachments/1184622679685333042/1184622778557665362/16127Screenshot_2021-01-19_at_11.50.55_PM.png?ex=658ca4ef&is=657a2fef&hm=34defd5982e0379bde19e94620405a626d1be869207b182b3a3fb99b4a0efd21&)

#### Explicação:
As Long Short-Term Memories (LSTMs) são uma melhoria das RNNs, projetadas para superar o problema do "desaparecimento do gradiente". Elas introduzem uma estrutura de células de memória e portões (esquecimento, entrada, saída).

A lógica matemática da LSTM para uma etapa de tempo t é dada por:

\[ f_t = \sigma(W_{hf} \cdot h_{t-1} + W_{xf} \cdot x_t + b_f) \]
\[ i_t = \sigma(W_{hi} \cdot h_{t-1} + W_{xi} \cdot x_t + b_i) \]
\[ o_t = \sigma(W_{ho} \cdot h_{t-1} + W_{xo} \cdot x_t + b_o) \]
\[ \tilde{c}_t = \tanh(W_{hc} \cdot h_{t-1} + W_{xc} \cdot x_t + b_c) \]
\[ c_t = f_t \cdot c_{t-1} + i_t \cdot \tilde{c}_t \]
\[ h_t = o_t \cdot \tanh(c_t) \]

Onde:
- \( f_t, i_t, o_t \) são os portões (esquecimento, entrada, saída).
- \( \tilde{c}_t \) é o candidato a novo valor de célula.
- \( c_t \) é o estado da célula de memória.
- \( h_t \) é o estado oculto.

# Observações sobre a Aplicação:

### Pontos Fortes:
- A combinação de Redes Neurais Recorrentes (RNN), Long Short-Term Memory (LSTM) e Modelos de Linguagem de Longa Escala (LLM) oferece uma compreensão profunda do contexto e das dependências temporais, resultando em modelos mais avançados e precisos para a classificação de texto.

### Pontos de Atenção:
- O treinamento e a otimização desses modelos podem exigir recursos computacionais significativos devido à complexidade das arquiteturas, especialmente ao empregar modelos pré-treinados como o RoBERTa. É essencial realizar uma validação robusta para garantir a generalização do modelo para novos dados.

Lembre-se de documentar adequadamente as escolhas de arquitetura, hiperparâmetros e métricas de avaliação, bem como considerar estratégias de otimização para mitigar demandas computacionais.

## Perspectivas das Áreas: Ciência de Dados, Engenharia de Software e Ciências da Computação

### 1. Ciência de Dados:

#### Perspectiva:
Na Ciência de Dados, a escolha de modelos como LSTMs e LLM é alinhada ao desejo de obter insights mais profundos a partir dos dados. Essas arquiteturas são fundamentais para tarefas que exigem uma compreensão contextualizada e semântica, como análise de sentimentos em texto.

#### Referências Adicionais:
- [Hochreiter, S., & Schmidhuber, J. (1997). Long Short-Term Memory. Neural Computation, 9(8), 1735–1780.](https://www.bioinf.jku.at/publications/older/2604.pdf)

### 2. Engenharia de Software:

#### Perspectiva:
Na Engenharia de Software, é vital considerar a escalabilidade e eficiência do código. Modelos mais complexos, como LSTMs e LLM, podem exigir mais recursos computacionais, e a modularidade do código é essencial para facilitar a manutenção e o desenvolvimento futuro.

#### Referências Adicionais:
- [Colah, C. (2015). Understanding LSTM Networks.](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

### 3. Ciências da Computação:

#### Perspectiva:
Em Ciências da Computação, a aplicação de modelos como LSTMs destaca o entendimento das complexidades do processamento de sequências. Essas arquiteturas são fundamentais para abordar desafios específicos relacionados à análise de dados sequenciais, como no processamento de linguagem natural.

#### Referências Adicionais:
- [Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.](https://arxiv.org/abs/1810.04805)

Lembre-se de que a aplicação dessas perspectivas deve ser ajustada de acordo com as necessidades específicas do projeto e o contexto da aplicação.
