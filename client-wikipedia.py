# Importing dependencies
import asyncio
import openai
from dotenv import load_dotenv, find_dotenv
from fastmcp import Client

# Loading environment variables
_ = load_dotenv(find_dotenv())

# Setting up OpenAI client
openai_client = openai.Client()

# Setting up server path and server client
SERVER_PATH = 'http://localhost:8000/sse'
CLIENT = Client(SERVER_PATH)

# Defining function to test server locally
async def search(client, search):
    """
    Tests server locally.

    Args:
        client: MCP client.
        search: search's target topic.

    Returns:
        JSON object containing search's result.
    """
    # Testing server locally
    async with client:
        arguments = {"search": search}
        result = await client.call_tool("search_wikipedia", arguments=arguments)
        print(result)
        system_prompt = f"""
        You are an AI assistant that searches through Wikipedia. 
        
        The user searched for the following topic: {search}.

        For this search, you received the following result: {result}.

        Based on the result and the search, build a summary in a friendly format for
        the user.
        """
        response = openai_client.responses.create(
            model="gpt-4.1-mini",
            instructions=system_prompt,
            input="Can you make a summary about this?"
        )
        
        print(response.output_text)

# Protecting main execution:
if __name__ == "__main__":
    asyncio.run(search(
        client=CLIENT,
        search="Isaac Asimov"
    ))