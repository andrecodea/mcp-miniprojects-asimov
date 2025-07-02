# Wikipedia Query - Mini Project

This project is a simple Wikipedia query system, consisting of a server and a client written in Python. The goal is to demonstrate how to consume and provide Wikipedia information in a practical and didactic way.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Go to the project folder:
   ```bash
   cd miniproject-wikipedia
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
Run the server to provide Wikipedia data:
```bash
python server_wikipedia.py
```

### Client
Run the client to query Wikipedia information:
```bash
python client-wikipedia.py
```

The client will ask for a search term and display the corresponding Wikipedia summary.

## Usage example
```
Enter the search term: Artificial Intelligence
Summary: Artificial intelligence (AI) is intelligence demonstrated by machines...
```

## File structure
- `server_wikipedia.py`: Server that provides Wikipedia data.
- `client-wikipedia.py`: Client that consumes the server data.
- `README-pt.md`: This file, documentation in Portuguese.
- `README.md`: Documentation in English.

## License
You can see license details in [LICENSE](LICENSE.txt)
