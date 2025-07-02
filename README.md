# Mini Projects: Wikipedia Query & Weather Forecast

This repository contains two simple Python mini projects:

- **Wikipedia Query**: Query Wikipedia summaries via a local server and client.
- **Weather Forecast**: Get current weather and forecasts using the OpenWeather API via a local server and client.

Both projects are educational, demonstrating how to consume and provide information using Python, APIs, and a simple client-server architecture.

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Enter the project folder:
   ```bash
   cd miniprojects
   ```
3. Install the required dependencies (using a virtual environment is recommended):
   ```bash
   pip install -r ../requirements.txt
   ```
   Or, if you are using `pyproject.toml`:
   ```bash
   pip install -r ../uv.lock
   ```
4. For the Weather Forecast project, create a `.env` file with your OpenWeather API key:
   ```env
   CHAVE_API_OPENWEATHER=your_openweather_key
   ```

---

## Wikipedia Query

### Server
Run the server to provide Wikipedia data:
```bash
python server_wikipedia.py
```

### Client
Run the client to query Wikipedia information:
```bash
python client-wikipedia.py
```
The client will prompt for a search term and display the corresponding Wikipedia summary.

#### Example
```
Enter search term: Artificial Intelligence
Summary: Artificial intelligence (AI) is intelligence demonstrated by machines...
```

---

## Weather Forecast

### Server
Run the server to provide weather data (requires OpenWeather API key in `.env`):
```bash
python server-weather-forecast.py
```

### Client
Run the client to query weather information:
```bash
python client-weather-forecast.py
```
The client will request the weather and forecast for a location and display a friendly summary.

#### Example
```
Current weather and forecast for: Rio de Janeiro
Summary: [AI-generated summary based on OpenWeather data]
```

---

## File Structure
- `server_wikipedia.py`: Server providing Wikipedia data.
- `client-wikipedia.py`: Client consuming Wikipedia data.
- `server-weather-forecast.py`: Server providing weather data.
- `client-weather-forecast.py`: Client consuming weather data.
- `README-pt.md`: This file, documentation in Portuguese.
- `README.md`: Documentation in English.

## License
You can see license details in [LICENSE](LICENSE.txt)
