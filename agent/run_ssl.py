# run_ssl.py

# 1) import your FastAPI app at the top level
from src.react_agent.webapp import app

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "run_ssl:app",               # import string: module_name:attribute_name
        host="localhost",
        port=2024,
        reload=True,                 # hot‑reload on code changes
        ssl_keyfile="localhost+2-key.pem",
        ssl_certfile="localhost+2.pem",
        log_level="debug",
    )
