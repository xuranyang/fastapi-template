from fastapi import APIRouter, Depends

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
