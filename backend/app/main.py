from fastapi import FastAPI

app = FastAPI(
    title="CodeGraph API",
    description="AI Software Engineer powered by FalkorDB",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "CodeGraph API is running",
        "status": "ok"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }