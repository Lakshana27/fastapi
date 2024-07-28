from fastapi import FastAPI
import uvicorn
from routes import user_router

# Initialize the FastAPI app
app = FastAPI()

# Include the user router
app.include_router(user_router.router, prefix="/users")

# Run the app with uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
