from fastapi import APIRouter, Depends, Body

from model.user_model import LoginModel

router = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/home")
async def user_home():
    """
    GET http://127.0.0.1:8000/dev-api/user/home
    :return:
    """
    return {"message": "Hello World"}


@router.get("/info/{name}")
async def user_info(name: str):
    """
    GET http://127.0.0.1:8000/dev-api/user/info/xxx
    :return:
    """
    return {"message": f"Hello {name}"}


@router.get("/detail")
async def user_detail(name: str, age: int):
    """
    GET http://127.0.0.1:8000/dev-api/user/detail?name=abc&age=20
    :return:
    """
    return {
        "name": name,
        "age": age
    }


@router.post("/login")
async def user_login(user: LoginModel):
    """
    触发登录操作,验证用户的帐号和密码是否正确匹配
    POST http://127.0.0.1:8000/dev-api/user/login
    BODY
    {
        "username": "admin",
        "password": "admin123"
    }
    """

    username = user.username
    password = user.password

    if username == 'admin' and password == 'admin123':
        code = 200
        data = {
            'result': 'success',
            'token': 'admin-token'
        }
    else:
        code = 400
        data = {
            'result': 'error'
        }

    return {
        'code': code,
        'data': data
    }


@router.post("/json")
async def user_login(body: dict = Body(embed=False)):
    """
    POST http://127.0.0.1:8000/dev-api/user/json
    Body
    {
        "username": "root",
        "password": "123456"
    }
    :param body:
    :return:
    """
    return {
        'code': 200,
        'data': body
    }


@router.post("/json-embed")
async def user_login(info: dict = Body(embed=True)):
    """
    POST http://127.0.0.1:8000/dev-api/user/json-embed
    Body
    {
        "info": {
            "username": "root",
            "password": "123456"
        }
    }
    :param info:
    :return:
    """
    return {
        'code': 200,
        'data': info
    }
