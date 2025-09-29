from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

API_TITLE = "Duruzi Serve"
API_VERSION = "0.1.0"

class InferRequest(BaseModel):
    input: str
    params: Optional[dict] = None

app = FastAPI(title=API_TITLE, version=API_VERSION)

# Simple auth stub: require Authorization: Bearer <any-non-empty>
def require_auth(authorization: Optional[str]):
    if not authorization or not authorization.lower().startswith("bearer ") or len(authorization.split()) != 2:
        raise HTTPException(status_code=401, detail={"error":"unauthorized","message":"Missing or invalid API key"})

@app.exception_handler(Exception)
async def unhandled_exc(request: Request, exc: Exception):
    # Basic error mapper
    return JSONResponse(
        status_code=500,
        content={"error":"internal_error","message":str(exc),"request_id":request.headers.get("X-Request-ID","")},
    )

@app.get("/healthz")
def healthz():
    return {"status": "ok", "service": "duruzi-serve", "version": API_VERSION}

@app.post("/v1/infer/{endpoint_id}")
def infer(endpoint_id: str, req: InferRequest, authorization: Optional[str] = Header(default=None)):
    require_auth(authorization)
    text = req.input
    usage = {"prompt_tokens": len(text), "completion_tokens": len(text)}
    return {"output": text[::-1], "endpoint_id": endpoint_id, "usage": usage}
