import os
import uvicorn
import socket
from fastapi import FastAPI
from routers import base, user
from fastapi.middleware.cors import CORSMiddleware

"""
uvicorn main:app --reload
uvicorn main:app --reload --host xxx --port xxx

http://127.0.0.1:8000/docs
https://fastapi.tiangolo.com/zh/
"""

loc = locals()
app = FastAPI()

# BASE_URL = 'http://127.0.0.1:8000/dev-api'
router_prefix = '/dev-api'
# router_prefix_base = '/basic-api'
app.include_router(base.router)
app.include_router(user.router, prefix=router_prefix)


def get_variable_name(variable):
    """
    获取变量名
    :param variable:
    :return:
    """
    for k, v in loc.items():
        if loc[k] is variable:
            return k


origins = [
    "http://localhost",
    "http://localhost:3100",
]

# CORS 跨域
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    file_name = os.path.basename(__file__).replace('.py', '')
    app_name = get_variable_name(app)
    host_name = socket.gethostbyname(socket.gethostname())
    # uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True)
    uvicorn.run(app=f'{file_name}:{app_name}', host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run(app=f'{file_name}:{app_name}', host=host_name, port=8000, reload=True)
