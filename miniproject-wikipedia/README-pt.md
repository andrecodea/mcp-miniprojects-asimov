# Consulta à Wikipedia - Mini Projeto

Este projeto é um sistema simples de consulta à Wikipedia, composto por um servidor e um cliente escritos em Python. O objetivo é demonstrar como consumir e fornecer informações da Wikipedia de forma prática e didática.

## Instalação

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd miniproject-wikipedia
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
Execute o servidor para fornecer dados da Wikipedia:
```bash
python server_wikipedia.py
```

### Cliente
Execute o cliente para consultar informações da Wikipedia:
```bash
python client-wikipedia.py
```

O cliente solicitará um termo de busca e exibirá o resumo correspondente da Wikipedia.

## Exemplo de uso
```
Digite o termo de busca: Inteligência Artificial
Resumo: Inteligência artificial (IA) é a inteligência demonstrada por máquinas...
```

## Estrutura dos arquivos
- `server_wikipedia.py`: Servidor que fornece dados da Wikipedia.
- `client-wikipedia.py`: Cliente que consome os dados do servidor.
- `README-pt.md`: Este arquivo, documentação em português.
- `README.md`: Documentação em inglês.

## Licença
Você pode ver detalhes sobre a licensa em [LICENSE](LICENSE.txt)
