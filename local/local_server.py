from fastmcp import FastMCP

# Criando o servidor MCP
mcp_server = FastMCP("mcp-teste")

# Decorador que define a função abaixo dele como uma tool do servidor MCP
# 1. Registra a função como uma "tool" disponível no servidor
# 2. Adiciona metadados necessários para o protocolo MCP
# 3. Torna a função chamável remotamente pelo cliente
@mcp_server.tool()

# Função assíncrona: permite operações não-bloqueantes e melhor performance
# Operações não-bloqueantes não param o programa enquanto aguardam resposta
# Recomendado para tools que podem fazer I/O (rede, arquivos, etc.)
async def good_morning(user_name:str, user_id:int) -> str:
    return f'Hello, {user_name}! (ID: {user_id})'

# Criando a função para o código principal
def main():
    # Protocolo de transporte: standard input/output -> comunicação via texto
    # Adequado para MCPs locais executados como subprocessos
    mcp_server.run(transport='stdio') 

# Protegendo a execução do código principal
if __name__ == "__main__":
    main()
