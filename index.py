from fastapi import FastAPI
from routes.userRouter import user

app = FastAPI()
app.include_router(user)