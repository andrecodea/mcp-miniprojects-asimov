# Weather Forecast - Mini Project

This project is a simple weather forecast MCP system, consisting of a server and a client written in Python. The goal is to demonstrate how to consume and provide weather data in a practical and didactic way.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Go to the project folder:
   ```bash
   cd miniproject-weather-forecast
   ```
3. Install the required dependencies (it is recommended to use a virtual environment):
   ```bash
   pip install -r ../requirements.txt
   ```
   Or, if you are using `pyproject.toml`:
   ```bash
   pip install -r ../uv.lock
   ```

## How to use

### Server
Run the server to provide weather forecast data:
```bash
python server-weather-forecast.py
```

### Client
Run the client to query the weather forecast:
```bash
python client-weather-forecast.py
```

The client will ask for a city name and display the corresponding weather forecast.

## Usage example
```
Enter the city name: São Paulo
Forecast for São Paulo: Sunny, 25°C
```

## File structure
- `server-weather-forecast.py`: Server that provides weather forecast data.
- `client-weather-forecast.py`: Client that consumes the server data.
- `README-pt.md`: This file, documentation in Portuguese.
- `README.md`: Documentation in English.

## License
This project is for educational purposes only and does not have a specific license.
