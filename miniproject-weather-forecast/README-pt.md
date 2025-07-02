# Previsão do Tempo - Mini Projeto

Este projeto é um sistema MCP simples de previsão do tempo, composto por um servidor e um cliente escritos em Python. O objetivo é demonstrar como consumir e fornecer dados meteorológicos de forma prática e didática.

## Instalação

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd miniproject-weather-forecast
   ```
3. Instale as dependências necessárias (recomenda-se o uso de ambiente virtual):
   ```bash
   pip install -r ../requirements.txt
   ```
   Ou, se estiver usando o `pyproject.toml`:
   ```bash
   pip install -r ../uv.lock
   ```

## Como usar

### Servidor
Execute o servidor para fornecer dados de previsão do tempo:
```bash
python server-weather-forecast.py
```

### Cliente
Execute o cliente para consultar a previsão do tempo:
```bash
python client-weather-forecast.py
```

O cliente solicitará o nome de uma cidade e exibirá a previsão do tempo correspondente.

## Exemplo de uso
```
Digite o nome da cidade: São Paulo
Previsão para São Paulo: Ensolarado, 25°C
```

## Estrutura dos arquivos
- `server-weather-forecast.py`: Servidor que fornece dados de previsão do tempo.
- `client-weather-forecast.py`: Cliente que consome os dados do servidor.
- `README-pt.md`: Este arquivo, documentação em português.
- `README.md`: Documentação em inglês.

## Licença
Este projeto é apenas para fins educacionais e não possui uma licença específica.
