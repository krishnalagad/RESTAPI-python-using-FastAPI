from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.userSchemas import userEntity, usersEntity, serializeDict, serializeList
from bson import ObjectId

user = APIRouter()

@user.get('/')
async def getAllUsers():
    # print(conn.local.user.find())
    # print(usersEntity(conn.local.user.find()))
    return serializeList(conn.local.user.find())

@user.get('/{id}')
async def getOneUser(id):
    return serializeDict(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.post('/')
async def createUser(user: User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())

@user.put('/{id}')
async def updateuser(id, user: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/{id}')
async def deleteUser(id):
    return userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))