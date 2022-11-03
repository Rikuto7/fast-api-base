from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routers import routers
from backend.api import env


app = FastAPI(title='TYBY API', debug=env.DEBUG)

# CORS
origins: list[str] = []

# Set all CORS enabled origins
if env.BACKEND_CORS_ORIGINS:
    origins_raw = env.BACKEND_CORS_ORIGINS.split(',')
    for origin in origins_raw:
        use_origin = origin.strip()
        origins.append(use_origin)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


@app.exception_handler(Exception)   # type: ignore
async def unicorn_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'message': f'{exc.detail}', 'code': exc.status_code, 'data': None},
    )


app.include_router(routers.router, prefix='/api-v1/sample')


@app.get('/')
def health(request: Request):
    print(request)
    return True
