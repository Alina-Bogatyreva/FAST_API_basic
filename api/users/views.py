from typing import List

from fastapi import APIRouter

from api.users import crud
from api.users.schemas import UserIn, UserOut, UserInPut


router_user = APIRouter(prefix="/users", tags=["User"])


@router_user.post("", response_model=UserOut)
def create_user(user_in: UserIn) -> UserOut:
    return crud.create_user(user_in)


@router_user.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, token: str) -> UserOut:
    return crud.get_user_by_id(user_id, token)


@router_user.get("s", response_model=List[UserOut])
def get_users(token: str) -> List[UserOut]:
    return crud.get_users(token)


@router_user.delete("/{user_id}")
def delete_user(user_id: int, token: str) -> None:
    return crud.delete_user(user_id, token)


@router_user.put("/{user_id}")
def put_user(user_id: int, user_in: UserInPut, token: str) -> UserOut:
    return crud.put_user(user_id, user_in, token)
