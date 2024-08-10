# Desafios e Soluções em Projetos de Machine Learning

| Nr. | Categoria   | Desafios                                                                                                         | Soluções                                                                                                           | Itens | Links                                                                                                                                                                                         |
|-----|-------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Requisitos  | No momento do design, as informações disponíveis são insuficientes para entender os clientes ou os projetos.   | Realizar simulações para coletar dados. Usar experiências passadas. Medir e documentar fontes de incerteza.        | 🔴     | N/A                                                                                                                                                                                           |
| 2   | Requisitos  | Os componentes de ML não possuem requisitos funcionais.                                                         | Usar métricas como requisitos funcionais. Incluir compreensibilidade e explicabilidade das saídas.                 | 🟢     | [Requisitos](https://github.com/Neural-Matheus/TextClassifier/blob/main/docs/project_documentation.md)                                                                                        |
| 3   | Requisitos  | Os projetos de ML têm restrições regulatórias e podem estar sujeitos a auditorias.                              | Analisar restrições regulatórias antecipadamente. Adotar um código de conduta de IA. Projetar trilhas de auditoria. | 🔴     | N/A                                                                                                                                                                                           |
| 4   | Dados       | A preparação de dados pode resultar em uma selva de etapas de raspagem, junção e amostragem, frequentemente com saídas intermediárias. | Projetar módulos/serviços separados para coleta e preparação de dados. Integrar ferramentas externas.              | 🟢     | [Processamento dos dados](https://github.com/Neural-Matheus/TextClassifier/blob/main/notebooks/data_preprocessing.ipynb)                                                                       |
| 5   | Dados       | A qualidade dos dados é difícil de testar e pode ter consequências inesperadas.                                | Projetar módulos/serviços separados para avaliação da qualidade dos dados. Integrar ferramentas externas.          | 🟢     | [Análise dos Dados](https://github.com/Neural-Matheus/TextClassifier/blob/main/notebooks/exploratory_data_analysis.ipynb)                                                                      |
| 6   | Design      | Separar preocupações entre treinamento, teste e serviço, mas reutilizar código entre eles.                     | Padronizar interfaces de modelo. Usar um middleware. Reutilizar virtualização, infraestrutura e scripts de teste.  | 🔴     | N/A                                                                                                                                                                                           |
| 7   | Design      | Distinguir falhas entre os componentes de ML e outras lógicas de negócios.                                      | Separar lógica de negócios de componentes de ML. Padronizar interfaces e usar um middleware entre eles.            | 🔴     | N/A                                                                                                                                                                                           |
| 8   | Design      | Os componentes de ML estão altamente acoplados, e erros podem ter efeitos em cascata.                          | Projetar módulos/serviços independentes para ML e dados. Padronizar interfaces e usar um middleware.               | 🟡     | [Processamento dos dados](https://github.com/Neural-Matheus/TextClassifier/blob/main/notebooks/data_preprocessing.ipynb)<br>[Modelo Completo](https://github.com/Neural-Matheus/TextClassifier/blob/main/notebooks/text_classifier.ipynb)<br>[Treinamento do Modelo](https://github.com/Neural-Matheus/TextClassifier/blob/main/notebooks/model_training.ipynb)<br>[Análise dos Dados](https://github.com/Neural-Matheus/TextClassifier/blob/main/notebooks/exploratory_data_analysis.ipynb) |
| 9   | Design      | Os componentes de ML trazem incerteza inerente a um sistema.                                                   | Usar n-versioning. Projetar e monitorar métricas de incerteza. Empregar modelos interpretáveis/intervenção humana.  | 🟡     | [Modelos Diferentes Treinados](https://drive.google.com/drive/folders/1C7Ex30MxISQcdFwlWCiLyknUEOCYP-_P?usp=drive_link)                                                                        |
| 10  | Design      | Os componentes de ML podem falhar silenciosamente. Essas falhas podem ser difíceis de detectar, isolar e resolver. | Usar monitoramento de métricas e alertas para detectar falhas. Usar n-versioning. Empregar modelos interpretáveis.  | 🟢     | [Análises Diferentes Modelos](https://github.com/Neural-Matheus/TextClassifier/blob/main/notebooks/model_training.ipynb)                                                                       |
| 11  | Design      | Os componentes de ML são intrinsecamente opacos, e o raciocínio dedutivo a partir dos artefatos de arquitetura, código ou metadados não é eficaz. | Instrumentar o sistema ao máximo. Usar n-versioning. Empregar modelos interpretáveis. Projetar módulos de log para agregar/visualizar métricas. | 🔴     | N/A                                                                                                                                                                                           |
| 12  | Design      | Evitar componentes não estruturados que conectam frameworks ou APIs (por exemplo, código de cola).            | Envolver componentes em APIs/módulos/serviços. Usar interfaces padrão e um middleware. Usar virtualização.         | 🔴     | N/A                                                                                                                                                                                           |
| 13  | Design      | A automação e compreensão das tarefas de ML são difíceis (AutoML).                                             | Arquivar arquivos de configuração. Projetar os sistemas de log e versionamento para suportar a recuperação de dados do AutoML. | 🟢     | [Repositório](https://github.com/Neural-Matheus/TextClassifier)                                                                                                                                |
| 14  | Testes      | Os testes de ML vão além de bugs de programação para problemas que surgem de erros de modelo, dados ou incerteza. | Projetar testes de modelo e dados. Usar CI/CD. Usar testes de integração e unitários. Usar propriedade de dados para módulos de teste. | 🔴     | N/A                                                                                                                                                                                           |
| 15  | Testes      | A validação dos componentes de ML para produção é difícil.                                                      | Usar métricas e CI/CD para validação. Usar alertas, visualizações, intervenção humana. Projetar processos de lançamento. | 🔴     | N/A                                                                                                                                                                                           |
| 16  | Operações   | Os componentes de ML requerem manutenção contínua, retrabalho e evolução.                                       | Projetar para retrabalho contínuo automático. Usar CI/CD. Usar retorno automático. Usar infraestrutura como código. Adotar processos de lançamento padrão. | 🔴     | N/A                                                                                                                                                                                           |
| 17  | Operações   | Gerenciar as dependências e os consumidores de aplicativos de ML.                                               | Encapsular componentes de ML em módulos/serviços identificáveis. Usar autenticação e controle de acesso. Registrar consumidores de componentes de ML. | 🔴     | N/A                                                                                                                                                                                           |
| 18  | Operações   | Equilibrar latência, throughput e tolerância a falhas, necessários para treinamento e serviço.                   | Projetar para processamento em lote (treinamento) e processamento de fluxo (serviço), ou seja, arquitetura lambda. Isolar fisicamente as cargas de trabalho. Usar virtualização. | 🔴     | N/A                                                                                                                                                                                           |
| 19  | Operações   | Rastrear decisões para modelos, dados e reproduzir resultados passados.                                         | Projetar para rastreabilidade e reprodutibilidade; registrar ponteiros para artefatos versionados, configurações de versão, modelos e dados. | 🔴     | N/A                                                                                                                                                                                           |
| 20  | Organização | Os aplicativos de ML usam pilhas de tecnologia heterogêneas que exigem experiências e habilidades diversas.      | Formar equipes multidisciplinares. Adotar um código de conduta de IA. Definir processos para tomada de decisão. Conscientizar sobre os riscos de ML dentro da equipe. | 🔴     | N/A                                                                                                                                                                                           |