import logging

from fastapi import APIRouter, Body, Request

"""
{
  userId: '1',
  username: 'vben',
  realName: 'Vben Admin',
  avatar: 'https://q1.qlogo.cn/g?b=qq&nk=190848757&s=640',
  desc: 'manager',
  password: '123456',
  token: 'fakeToken1',
  homePath: '/dashboard/analysis',
  roles: [
    {
      roleName: 'Super Admin',
      value: 'super',
    },
  ],
}
"""

router = APIRouter(
    prefix="/basic-api",
    tags=["base"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

"""
Login = '/login',
Logout = '/logout',
GetUserInfo = '/getUserInfo',
GetPermCode = '/getPermCode',
TestRetry = '/testRetry',
"""

from fastapi import status

# status.HTTP_200_OK
tokens = {
    'vben': 'fakeToken1'
}

user_infos = {
    'vben': {
        'userId': '1',
        'username': 'vben',
        'realName': 'Gali',
        'avatar': 'https://q1.qlogo.cn/g?b=qq&nk=190848757&s=640',
        'desc': 'manager',
        'password': '123456',
        'token': 'fakeToken1',
        'homePath': '/dashboard/workbench',
        'roles': [
            {
                'roleName': 'Super Admin',
                'value': 'super',
            },
        ],
    }
}


@router.post("/login")
async def login(body: dict = Body(embed=False)):
    """
    POST http://127.0.0.1:8000/basic-api/login
    :return:
    """
    username = body['username']
    password = body['password']

    # validate username&password
    real_password = user_infos[username]['password']

    token = ''
    if password == real_password:
        logging.info(f"[Login]:{username}校验成功,密码正确")
        check_user = True
        # set token
        token = tokens.get(username)
    else:
        check_user = False

    if check_user:
        return {
            'code': 200,
            'result': {
                'token': token,
                'role': {
                    'roleName': 'Super Admin',
                    'value': 'super',
                },
                'userId': '1',
            },
            'message': 'ok',
            'type': 'success'
        }
    else:
        return {
            'code': -1,
            'result': None,
            'message': 'Incorrect account or password!',
            'type': 'error'
        }


@router.get("/getUserInfo")
async def get_user_info(request: Request):
    # getRequestToken 从获取前端Request请求中 获取headers中的Token
    auth_token = request.headers.get("Authorization")
    logging.info(f"[getUserInfo][Token]:{auth_token}")

    # 校验Token
    # if auth_token is None:
    if not auth_token:
        # 非法Token
        logging.info(f"[非法Token]:{auth_token}")
        return {
            'code': -1,
            'result': None,
            'message': 'Invalid token',
            'type': 'error'
        }

    # check_user 校验用户
    is_user = False
    result = None
    for user, token in tokens.items():
        if token == auth_token:
            # 获取Token对应的user_info
            user_info = user_infos[user]
            is_user = True
            result = {
                'userId': user_info['userId'],
                'username': user_info['username'],
                'realName': user_info['realName'],
                'avatar': user_info['avatar'],
                'desc': user_info['desc'],
                'homePath': user_info['homePath'],
                'roles': user_info['roles']
            }
            break

    if not is_user:
        return {
            'code': -1,
            'result': None,
            'message': 'The corresponding user information was not obtained!',
            'type': 'error'
        }

    # 正常情况,返回token 对应的用户信息
    logging.info(f"[getUserInfo]:{auth_token}-Token验证成功")
    return {
        'code': status.HTTP_200_OK,
        'result': result,
        'message': 'ok',
        'type': 'success'
    }


@router.get("/logout")
async def logout(request: Request):
    # getRequestToken 从获取前端Request请求中 获取headers中的Token
    auth_token = request.headers.get("Authorization")
    logging.info(f"[logout][Token]:{auth_token}")

    # 校验Token
    if not auth_token:
        # 非法Token
        logging.info(f"[非法Token]:{auth_token}")
        return {
            'code': -1,
            'result': None,
            'message': 'Invalid token',
            'type': 'error'
        }

    is_user = False
    for user, token in tokens.items():
        if token == auth_token:
            # 获取Token对应的user_info
            user_info = user_infos[user]
            is_user = True
            break

    if not is_user:
        return {
            'code': -1,
            'result': None,
            'message': 'Invalid token!',
            'type': 'error'
        }

    # 正常情况,用户验证成功,可以登出
    # 删除过期Token
    logging.info(f"[logout]:{auth_token}-Token验证成功")
    # delete Token ...
    return {
        'code': status.HTTP_200_OK,
        'result': None,
        'message': 'Token has been destroyed',
        'type': 'success'
    }
