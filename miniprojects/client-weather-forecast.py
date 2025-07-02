# Importing dependencies
import asyncio
import openai
from dotenv import load_dotenv, find_dotenv
from fastmcp import Client

# Loading environment variables
_ = load_dotenv(find_dotenv())

# Setting up OpenAI client
openai_client = openai.Client()

# Setting up server path and server client:
SERVER_PATH = 'http://localhost:8000/sse'
CLIENT = Client(SERVER_PATH)

# Defining function to test server locally
async def test_server(client, location):
    """
    Tests server locally.

    Args:
        client: MCP client.
        location: forecast's target location (city).

    Returns:
        JSON object containing weather forecast and current weather.
    """

    # Testing server locally
    async with client:
        arguments = {"location": location}

        current_weather = await client.call_tool("get_current_weather", arguments=arguments)

        weather_forecast = await client.call_tool("get_weather_forecast", arguments=arguments)

        system_prompt = f"""
        You are an AI assistant that gets weather forecasts and compiles an answer.

        User searched for the forecast of the following location {location}.

        For this search you received the following forecast: {weather_forecast}.

        Besides that, the current weather is: {current_weather}.

        From this information, compile a friendly answer for the user
        """
        response = openai_client.responses.create(
            model="gpt-4.1-mini",
            instructions=system_prompt,
            input="What is the forecast of the indicated location?"
        )
        
        print(response.output_text)

# Protecting main execution:
if __name__ == "__main__":
    asyncio.run(test_server(
        client=CLIENT,
        location="Rio de Janeiro"
    ))