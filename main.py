from fastapi import FastAPI
from modules.users.routes import createUser, readUser, updateUser, deleteUser

app = FastAPI()

app.include_router(createUser.router)
app.include_router(readUser.router)
app.include_router(updateUser.router)
app.include_router(deleteUser.router)