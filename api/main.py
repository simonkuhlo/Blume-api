import uvicorn

host: str = "0.0.0.0"
port: int = 8080
debug: bool = True

if __name__ == "__main__":
    uvicorn.run("app:app", host=host, port=port, reload=debug)

