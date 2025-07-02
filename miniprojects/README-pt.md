# Mini Projetos: Consulta à Wikipedia & Previsão do Tempo

Este repositório contém dois mini projetos simples em Python:

- **Consulta à Wikipedia**: Consulte resumos da Wikipedia via um servidor e cliente local.
- **Previsão do Tempo**: Obtenha o clima atual e previsões usando a API OpenWeather via um servidor e cliente local.

Ambos os projetos são didáticos, demonstrando como consumir e fornecer informações usando Python, APIs e uma arquitetura simples cliente-servidor.

---

## Instalação

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd miniprojects
   ```
3. Instale as dependências necessárias (recomenda-se o uso de ambiente virtual):
   ```bash
   pip install -r ../requirements.txt
   ```
   Ou, se estiver usando o `pyproject.toml`:
   ```bash
   pip install -r ../uv.lock
   ```
4. Para o projeto de Previsão do Tempo, crie um arquivo `.env` com sua chave da API OpenWeather:
   ```env
   CHAVE_API_OPENWEATHER=sua_chave_openweather
   ```

---

## Consulta à Wikipedia

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

#### Exemplo
```
Digite o termo de busca: Inteligência Artificial
Resumo: Inteligência artificial (IA) é a inteligência demonstrada por máquinas...
```

---

## Previsão do Tempo

### Servidor
Execute o servidor para fornecer dados do clima (requer chave da API OpenWeather no `.env`):
```bash
python server-weather-forecast.py
```

### Cliente
Execute o cliente para consultar informações do clima:
```bash
python client-weather-forecast.py
```
O cliente solicitará o clima e a previsão para uma localidade e exibirá um resumo amigável.

#### Exemplo
```
Clima atual e previsão para: Rio de Janeiro
Resumo: [Resumo gerado por IA com base nos dados do OpenWeather]
```

---

## Estrutura dos arquivos
- `server_wikipedia.py`: Servidor que fornece dados da Wikipedia.
- `client-wikipedia.py`: Cliente que consome dados da Wikipedia.
- `server-weather-forecast.py`: Servidor que fornece dados do clima.
- `client-weather-forecast.py`: Cliente que consome dados do clima.
- `README-pt.md`: Este arquivo, documentação em português.
- `README.md`: Documentação em inglês.

## Licença
Você pode ver detalhes sobre a licença em [LICENSE](LICENSE.txt)
