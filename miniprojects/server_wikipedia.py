# Importing dependencies
from fastmcp import FastMCP
import wikipedia

# Creating MCP server
mcp_server = FastMCP("mcp-search-wikipedia")

# Defining tool
@mcp_server.tool()

# Searching wikipedia
async def search_wikipedia(search:str ) -> str:
    """
    Searches wikipedia and returns a summary of the search.

    Args:
        search: search's target topic.

    Returns:
        String containing search's result.
    """
    print(f"Search: {search}")
    return wikipedia.summary(search)

# Protecting main execution:
if __name__ == "__main__":
    mcp_server.run(transport='sse')