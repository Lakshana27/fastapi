from fastapi import FastAPI
import uvicorn

from OtpValidation.routes import route

app = FastAPI(title='OTP Validation')

app.include_router(route)

if __name__ == '__main__':
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)