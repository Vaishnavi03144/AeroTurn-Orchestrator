import uvicorn
from main import app

def main():
    """Callable entry point for the validator."""
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
