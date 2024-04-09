# Serving List of Pokemons

## Description

This project is a RESTful API built with FastAPI that serves a list of Pokémon data. It fetches data from the [PokeAPI](https://pokeapi.co/), stores it in a PostgreSQL database, and provides endpoints to retrieve Pokémon information, filter by name and type, and more.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Installation

1. **Clone the Repository:**
   ```shell
   git clone https://github.com/balibabu/pokeapi
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

## Configuration

Configure your PostgreSQL database connection by adding the `config.ini` file. Ensure that the database connection details are correctly set in the configuration.
```shell
[database]
user=
host=
password=
database=
```

## Usage

- **Start the FastAPI Server:**
  Start the FastAPI server by running:

  ```shell
  python main.py
  ```

- **API Endpoints:**

  - **Get List of Pokemons:**
    - Endpoint: `/api/v1/pokemons`
    - Description: Retrieve a list of all Pokemons with their names, images, and types.

  - **Filter Pokemons:**
    - Endpoint: `/api/v1/pokemons/params?type=_&name=_`
    - Description: Filter Pokemons by name and/or type.

- **Example Requests:**
  - Get all Pokemons: `http://localhost:8000/api/v1/pokemons`
  - Filter Pokemons by type and name: `http://127.0.0.1:8000/api/v1/pokemons/params?type=grass&name=charmeleon`
  - Filter Pokemons by type: `http://127.0.0.1:8000/api/v1/pokemons/params?type=grass`
  - Filter Pokemons by name: `http://127.0.0.1:8000/api/v1/pokemons/params?name=charmeleon`


## Authors

- Bali Babu Chauhan

## Acknowledgments

- [PokeAPI](https://pokeapi.co/): The API used to fetch Pokémon data.
- [FastAPI](https://fastapi.tiangolo.com/): The Python framework used to create the RESTful API.
