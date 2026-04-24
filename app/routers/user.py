from fastapi import APIRouter
from app.schemas import User, UserId

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


usuarios=[]

@router.get('/ruta1')
def ruta1():
    return {"mensaje: bevenido a tu primar api..."}

@router.get('/')
def obtener_usuarios():
    return usuarios

@router.post('/crear_usuario')
def crear_usuario(user:User):
    usuario = user.dict()
    usuarios.append(usuario)
    return {"respuesta":"usuario creado correctamente"}

@router.post('/{user_id}')
def obtener_usuario(user_id:int):
    for user in usuarios:
        if user["id"] == user_id:
            return {"usuario":user}
    return{"respuesta":"usuario no encontrado"}

@router.post('/obtener_usuario')
def obtener_usuario_2(user_id: UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            return {"usuario": user}
    return {"response":"usuario no encontrado"}

@router.delete('/{user_id}')
def eliminar_usuario(user_id:int):
    for index, user in enumerate(usuarios):
        if user["id"]==user_id:
            usuarios.pop(index)
            return {"respuesta": "usuario eliminado correctamente"}
    return {"respuesta": "usuario no encontrado"}

@router.put('/{user_id}')
def actualizar_usuario(user_id:int, updateUser:User):
    for index, user in enumerate(usuarios):
        if user["id"]==user_id:
            usuarios[index]["nombre"]= updateUser.dict()["nombre"]
            usuarios[index]["apellido"]= updateUser.dict()["apellido"]
            usuarios[index]["direccion"]= updateUser.dict()["direccion"]
            usuarios[index]["telefono"]= updateUser.dict()["telefono"]
            return {"respuesta": "usuario editado correctamente"}
    return {"respuesta": "usuario no encontrado"}