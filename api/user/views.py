from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from api.user import crud
from api.user.schemas import UserIn, UserOut, UserInPut
from api.user.helper import Helper

# проверки временно (нужно вынести в другой файл)


router_user = APIRouter(prefix="/user", tags=["User"])
helper = Helper()


@router_user.post("", response_model=UserOut)
def create_user(user_in: UserIn) -> UserOut:
    return crud.create_user(user_in)


@router_user.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, token: str) -> UserOut:
    if len(token) == 36 and len(token.split('-')) == 5:
        if token in helper.cache_by_token:
            return crud.get_user_by_id(user_id)
    return JSONResponse(status_code=400, content={"error": "incorrect token"})


@router_user.get("s", response_model=List[UserOut])
def get_users(token: str) -> List[UserOut]:
    # crud.check_token(token)
    if len(token) == 36 and len(token.split('-')) == 5:
        if token in helper.cache_by_token:
            return crud.get_users()
    return JSONResponse(status_code=400, content={"error": "incorrect token"})


@router_user.delete("/{user_id}")
def delete_user_by_id(user_id: int, token: str) -> None:
    # crud.check_token(token)
    if len(token) == 36 and len(token.split('-')) == 5:
        if token in helper.cache_by_token:
            return crud.delete_user(user_id)
    return JSONResponse(status_code=400, content={"error": "incorrect token"})


@router_user.put("/{user_id}")
def put_user(user_id: int, user_in: UserInPut, token: str) -> UserOut:
    # crud.check_token(token)
    if len(token) == 36 and len(token.split('-')) == 5:
        if token in helper.cache_by_token:
            return crud.put_user(user_id, user_in)
    return JSONResponse(status_code=400, content={"error": "incorrect token"})

