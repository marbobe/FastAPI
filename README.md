# FastAPI

## Iniciar proyecto con python/fastAPI

1.  ` python -m venv venv` , Crea un entorno virtual, una copia aislada del ecosistema Python para el proyecto. Si no se hace todas las librerias se instalan globalmente.

2.  windows: `venv\Scripts\activate` Mac/Linux: `source venv/bin/activate`, activar el entorno.

3.  `pip install fastapi uvicorn`, instalar FastAPI y el servidor ASGI(Asynchronous Server Getaway Interface) (uvicorn). Instalar las librerias. También se pueden instalar ambos a la vez con `pip install "fastapi[standard]"`. ASGI es asíncrono frente al WSGI tradicional que es síncrono (gestiona los accesos con una cola), asgi al ser asíncrono da acceso a todos los ususarios simultaneamente sin colas.

4.  `pip freeze > requirements.txt`, Guardar las dependencias, en el archivo requirements.txt, guardas el estado. De esta forma se puede tener el mismo entorno haciendo: `pip install -r requirements.txt`

5.  crear archivo `app/main.py`

## Como ejecutar FastAPI

- Endpoint: `http://127.0.0.1:8000`
- Documentación `http://127.0.0.1:8000/docs`, swagger automático

#### Dos formas de ejecutar fastAPI

- Ejecutar `uvicorn app.main:app --reload`, ruta del archivo:nombre de la instancia Fast API --auto-reload (para desarrollo). Ejecutas el servidor.

- Añadir en app/main.py el siguiente código y ejecutar `python .\main.py`

  ```
  if __name__=="__main__":
      uvicorn.run("main:app",port=8000)
  ```

## Principales librerías

#### fastapi

El framework central. Proporciona los enrutadores (routers), el manejo de dependencias (Dependency Injection) y la gestión de las peticiones HTTP.

#### pydantic

El motor de validación de datos. Definirás la estructura esperada de tus datos mediante clases que heredan de `pydantic.BaseModel`. Pydantic garantiza que la entrada (request) y salida (response) de tu API cumplan estrictamente con las reglas de negocio y los tipos de datos definidos.

#### uvicorn

El servidor ASGI. FastAPI es un framework, no un servidor web. Uvicorn se encarga de escuchar las peticiones HTTP entrantes a nivel de red y enviarlas a la aplicación FastAPI de manera asíncrona.

#### salalchemy

Es el ORM (Object-Relational Mapper) más utilizado para interactuar con bases de datos relacionales sin escribir SQL directo. Para nuestro primer CRUD básico, utilizaremos una lista en memoria (diccionarios de Python) para aislar los conceptos de FastAPI antes de introducir persistencia en base de datos.

## Estructura proyecto con FastAPI

#### Arquitectura por capas

    mi_proyecto/
    ├── app/
    │   ├── main.py                Punto de entrada de la aplicación
    │   ├── core/                  Configuraciones, seguridad, variables de entorno
    │   ├── db/                    Configuración de base de datos (engine, session)
    │   ├── models/             Entidades de la base de datos (ORMs como SQLAlchemy)
    │   ├── schemas/               Modelos Pydantic (Validación de datos y DTOs)
    │   ├── repositories/          Capa de acceso a datos (Queries a la DB)
    │   ├── services/              Capa de lógica de negocio
    │   └── routers/               Enrutadores / Endpoints (Controladores HTTP)
    ├── requirements.txt           O pyproject.toml / uv.lock
    └── .env                       Variables de entorno locales

- **models (Entidades de Datos)**

  Aquí defines cómo se estructura la tabla en la base de datos utilizando tu ORM. Estas clases no tienen lógica de negocio, solo mapean la base de datos.

- **schemas (Modelos Pydantic / DTOs)**

  Definen la estructura de los datos que entran (Requests) y salen (Responses) de tu API. Aíslan tu base de datos del exterior.

- **repositories (Acceso a Datos)**

  Su única responsabilidad es interactuar con la base de datos. Ninguna otra capa debe ejecutar consultas SQL o llamar al ORM directamente.

- **services (Lógica de Negocio)**

  Aquí reside el núcleo de tu aplicación. El servicio recibe datos, aplica reglas de negocio, realiza cálculos y orquesta llamadas a uno o varios repositorios. Nunca debe saber nada sobre HTTP, códigos de estado o JSON.

- **routers (Controladores / Capa de Presentación)**

  Su única responsabilidad es recibir la petición HTTP, pasar los parámetros al servicio correspondiente, y devolver la respuesta HTTP adecuada (o lanzar excepciones HTTP como 404 Not Found). En FastAPI, el sistema de inyección de dependencias (Depends) se utiliza extensamente aquí para instanciar los servicios y repositorios.
