from fastapi import FastAPI, Header, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

#Modelo de datos 
class MessagePayload(BaseModel):
    message: str
    to: str
    from_user: str 
    timeToLifeSec: int

@app.post("/DevOps")
async def devops_post(
    payload: MessagePayload, 
    x_parse_rest_api_key: str = Header(None, alias="X-Parse-REST-API-Key"),
    x_jwt_kwy: str = Header(None, alias="X-JWT-KWY")
):
    #Validacion
    if x_parse_rest_api_key != "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c":
        return JSONResponse(status_code=403, content={"detail": "Invalid API Key"})
    
    #Validación de JWT
    if not x_jwt_kwy:
        return JSONResponse(status_code=401, content={"detail": "JWT Required"})
    return {"message": f"Hello {payload.to} your message will be send"}

@app.api_route("/DevOps", methods=["GET", "PUT", "DELETE", "PATCH"])
async def error_handler():
    return JSONResponse(content="ERROR")