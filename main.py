from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional
from datetime import datetime

#User Model
class User(BaseModel): #Schema
    id:int
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    creation_user:datetime =datetime.now()

class UserId(BaseModel):
    id:int

app = FastAPI()

usuarios=[]

@app.get('/ruta1')
def ruta1():
    return {"mensaje: bevenido a tu primar api..."}

@app.get('/user')
def obtener_usuarios():
    return usuarios

@app.post('/crear_usuario')
def crear_usuario(user:User):
    usuario = user.dict()
    usuarios.append(usuario)
    return {"respuesta":"usuario creado correctamente"}

@app.post('/user/{user_id}')
def obtener_usuario(user_id:int):
    for user in usuarios:
        if user["id"] == user_id:
            return {"usuario":user}
    return{"respuesta":"usuario no encontrado"}

@app.post('/obtener_usuario')
def obtener_usuario_2(user_id: UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            return {"usuario": user}
    return {"response":"usuario no encontrado"}
