# gRPC Implementation Example

This is a example showing how you can create a service using gRPC.

This code was written as a example only and does not follow any good practice rules, since it wasn't on the scope of
this presentation.

### Requirements

- Python 3.9.X (This should work as-is in python 3.10.X)
- Node v17.3.0

### Server

To start the gRPC server just execute the following command:

1. `$ python -m venv venv`
2. `$ pip install -r requirements.txt`
3. `$ python -m server.main`

This will start an insecure gRPC server on `https://0.0.0.0:50051`

ps.: This server uses an insecure channel for communications, although this is not a problem for learning purposes this **SHOULD NOT** be used as-is in production.

ps².: The creation of a secure channel communication is beyond the scope of this example.

### Node client

To start the node.js client execute the following commands:

1. `$ cd client_node`
2. `$ yarn` (or `$ npm install`)
3. `$ yarn start` (or `$ npm start`)

This will start a client [Express](https://expressjs.com/pt-br/) app on `http://localhost:3000`

A file containing some requests examples can be found [here](client_node/requests.http).

### Python client

To start the python client execute the following command:

1. `$ uvicorn client_python.main:app --reload`

This will start a client [FastAPI](https://fastapi.tiangolo.com) app on `http://localhost:8000`

A file containing some requests examples can be found [here](client_python/requests.http).