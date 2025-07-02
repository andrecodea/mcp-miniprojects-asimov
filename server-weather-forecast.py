# Importing dependencies
from dotenv import find_dotenv, load_dotenv
import dotenv
import os
import requests
from fastmcp import FastMCP

# Creating MCP server
mcp_server = FastMCP("mcp-weather-forecast")


# Defining tool
@mcp_server.tool()

# Getting current weather through openweather
def get_current_weather(location: str ) -> dict:
    """
    Gets real time weather conditions from openweather's API.

    Args:
        location: forecast's target location (city).

    Returns:
        JSON object containing weather conditions.
    """
    dotenv.load_dotenv()
    app_id = os.environ['CHAVE_API_OPENWEATHER']
    url = f'https://api.openweathermap.org/data/2.5/weather'

    # Defining GET parameters
    params = {
        "q": location,
        "appid": app_id,
        "units": "metric",
        "lang":"pt_br"
    }

    response = requests.get(url=url, params=params)

    return response.json()

# Defining tool
@mcp_server.tool()

# Getting weather forecast from openweather
def get_weather_forecast(location: str ) -> dict:
    """
    Gets weather forecast from openweather's API.

    Args:
        location: forecast's target location (city).

    Returns:
        JSON object containing forecast.
    """
    dotenv.load_dotenv()
    app_id = os.environ['CHAVE_API_OPENWEATHER']
    url = f'https://api.openweathermap.org/data/2.5/forecast'

    # Defining params
    params = {
        "q": location,
        "appid": app_id,
        "units": "metric",
        "lang":"pt_br"
    }

    response = requests.get(url=url, params=params)

    return response.json()

# Protecting main execution:
if __name__ == "__main__":
    mcp_server.run(transport='sse')