# Visão Geral da Arquitetura:

## Escalabilidade Eficiente:
A arquitetura de microservices permite escalar partes específicas do sistema de forma independente, otimizando os recursos e facilitando a adaptação a diferentes demandas de carga.

## Manutenção Simplificada:
Com a separação em serviços independentes, as atualizações e manutenções podem ser realizadas de maneira isolada, minimizando impactos e simplificando o processo de desenvolvimento contínuo.

## Flexibilidade Tecnológica:
Cada microserviço pode ser desenvolvido utilizando tecnologias e linguagens adequadas ao seu propósito, proporcionando flexibilidade na escolha das ferramentas mais adequadas para cada componente.

## Resiliência e Tolerância a Falhas:
A falha em um microserviço não compromete o sistema como um todo. A arquitetura permite isolar falhas e manter a operacionalidade dos demais serviços.

## Rápido Desenvolvimento e Implantação:
O desenvolvimento paralelo de microserviços possibilita uma entrega rápida e contínua. Além disso, a implantação isolada de cada serviço reduz o impacto nos demais componentes do sistema.

## Adaptabilidade a Mudanças:
A modularidade dos microserviços facilita a introdução de novas funcionalidades e a adaptação a mudanças nos requisitos, proporcionando agilidade no desenvolvimento.

## Isolamento de Responsabilidades:
Cada microserviço é responsável por uma funcionalidade específica, promovendo a clareza nas responsabilidades e facilitando a compreensão do sistema como um todo.

## Facilitação de Equipes Distribuídas:
A separação em microserviços permite que equipes distribuídas foquem em áreas específicas do sistema, promovendo a colaboração eficiente em projetos complexos.

---

# Diagrama de Arquitetura:

Diagrama de Arquitetura disponível ![neste link](https://cdn.discordapp.com/attachments/1184622679685333042/1184667045430841475/ArquiCWD.jpg?ex=658cce29&is=657a5929&hm=707c9952fb89b87efd4c54c653f7da36b47f1d5318da997a560beb6ad5aa276d&).

---

# Descrição de Microsserviços:

## Serviço de Validação Textual:
Este microsserviço recebe o texto do usuário para verificação. Utiliza uma AWS Lambda para encaminhar a requisição ao modelo, sendo representado no diagrama como o próprio modelo.

## Serviço de Limpeza de Textos do Arquivo:
Recebe um arquivo de texto (md, docx, txt, json, etc.) e encaminha para o Serviço de Validação Textual. A interação é descrita no diagrama.

---

# Comunicação entre Microsserviços:

Comunicação realizada através de protocolos REST e gRPC.

---

# Bancos de Dados:

Utilização do PostgreSQL.

---

# Conceitos Computacionais:

- **Segurança (Security)**
- **Latência (Latency)**
- **Roteamento das Rotas (Routing)**
- **Descoberta de Serviços (Service Discovery)**
- **Response Cache**
- **Padrão de Tentativas (Retry Pattern / Circuit-Breaker)**
- **Limite de Consultas (Rate Limit)**
- **Balanceamento de Larga (Load Balancing / Reverse Proxy)**
- **Autenticação e Authorização (Authentication / Authorization)**
- **Query / Header transformation**
- **Agregação de Requests (Request composition / Aggregation)**

---

# Ferramentas de API Gateway:

- **Amazon API Gateway:** Oferece serviços para criar, publicar, manter, monitorar e proteger APIs em escala.
- **Apigee (Google Cloud):** Uma plataforma de gerenciamento de API que facilita a criação, gerenciamento e escala de APIs.
- **Azure API Management:** Uma solução da Microsoft para criar, publicar, proteger e analisar APIs.
- **Kong:** Um gateway de API de código aberto e escalável, oferecendo recursos como proxy reverso, autenticação e controle de acesso.
- **NGINX:** Embora seja conhecido principalmente como um servidor web, o NGINX também é usado como um gateway de API eficiente e escalável.
- **Express Gateway:** Um gateway de API construído com base no framework Node.js Express, projetado para ser simples e flexível.
- **WSO2 API Manager:** Uma plataforma completa para projetar, publicar e gerenciar APIs em um ambiente corporativo.
