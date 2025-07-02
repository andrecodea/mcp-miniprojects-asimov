from fastmcp import FastMCP

import wikipedia

mcp_server = FastMCP("mcp-search-wikipedia-local")


@mcp_server.tool()
async def search_wikipedia_local(search:str ) -> str:
    print(f"Search: {search}")
    return wikipedia.summary(search)

if __name__ == "__main__":
    mcp_server.run(transport='stdio')