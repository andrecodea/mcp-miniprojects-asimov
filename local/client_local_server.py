import asyncio
from pathlib import Path
from fastmcp import Client

# Definindo o caminho para o arquivo servidor MCP
# O cliente se conectará a este servidor local
server_path = Path(__file__).parent / 'local_server.py'

# Criando uma instância do cliente MCP
client = Client(server_path)

# Função assíncrona para testar a comunicação com o servidor MCP
# Função retorna um *coroutine object*
# Deve ser executada com asyncio.run() ou await
# Permite operações não-bloqueantes -> await
async def test_server(client, user_name, user_id):
    # Context manager que gerencia o ciclo de vida da conexão com o servidor
    # Automatiza o setup e cleanup de recursos
    # Garante que a conexão seja estabelecida e fechada adequadamente
    # 1. Entrada: Estabelece conexão com o servidor MCP
    # 2. Execução: Mantém a conexão ativa durante o bloco
    # 3. Saída: Fecha a conexão automaticamente (mesmo se houver erro)
    async with client:
        # Preparando os argumentos para a tool do servidor
        arguments = {"user_name": user_name, "user_id": user_id}
        
        # Chamando a tool 'good_morning' no servidor MCP
        # await: pausa a execução até receber a resposta do servidor
        # 1. Cliente envia requisição para o servidor
        # 2. await pausa a execução
        # 3. Servidor processa e retorna resposta
        # 4. Execução continua com o resultado
        result = await client.call_tool("good_morning", arguments=arguments)
        print(f'Result obtained from MCP server: {result}')

# Criando a função para o código principal
def main():
# Executando a função de teste usando asyncio
    asyncio.run(test_server(
        client=client, 
        user_name='André',
        user_id=1  
    ))

# Protegendo a execução do código principal
if __name__ == "__main__":
    main()
