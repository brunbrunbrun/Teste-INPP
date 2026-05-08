# teste-pantanal

## Descrição

Este projeto em Python foi desenvolvido com o objetivo de realizar a análise de dados ambientais contidos em um arquivo CSV.

Os dados analisados incluem:
- data;
- temperatura;
- nível do rio;
- NDVI.

O projeto realiza:
- leitura e organização dos dados;
- tratamento de valores ausentes;
- cálculo de estatísticas básicas;
- geração de gráficos para visualização dos dados.


## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib


## Como rodar o projeto

### 1 - Clone o repositório

```bash
git clone https://github.com/brunbrunbrun/Teste-INPP
```


### 2 - Acesse a pasta do projeto

```bash
cd Teste-INPP
```


### 3 - Crie e ative o ambiente virtual

#### Git Bash (Windows)

```bash
python -m venv venv
source venv/Scripts/activate
```


### 4 - Instale as dependências

```bash
pip install -r requirements.txt
```


### 5 - Execute o projeto

```bash
python main.py
```


## Justificativa das escolhas técnicas

A linguagem Python foi escolhida devido à sua ampla utilização em análise e processamento de dados.

A biblioteca Pandas foi utilizada para:
- leitura do arquivo CSV;
- organização dos dados;
- tratamento de valores ausentes;
- cálculo das estatísticas.

A biblioteca Matplotlib foi utilizada para a geração dos gráficos e visualização das variáveis ambientais ao longo do tempo.

Para o tratamento dos dados faltantes, foi utilizada interpolação linear, por se tratar de uma série temporal com variações graduais entre as medições.

No gráfico de nível do rio e NDVI, foi utilizado eixo duplo (`twinx`) devido às diferenças de escala entre as variáveis analisadas.

## Resultados

O projeto gera automaticamente:
- gráfico de temperatura ao longo do tempo;
- gráfico comparativo entre nível do rio e NDVI.

Os gráficos também são salvos em formato `.png`.