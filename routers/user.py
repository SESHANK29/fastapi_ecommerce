from fastapi import APIRouter

from models.user import User
from config.db import conn 
from schemas.user import userEntity,usersEntity
user= APIRouter()
@user.get("/users")
async def get_users():
    return {"message": "list of users"}
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()))
    return usersEntity(conn.local.user.find())