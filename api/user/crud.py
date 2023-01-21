"""
Create
Read
Update
Delete
"""

from api.user.schemas import UserIn, UserOut, UserInPut
from api.user.helper import Helper


helper = Helper()


def create_user(user_in: ProductIn) -> UserOut:
    user = UserOut(**user_in.dict(), id=helper.next_id)
    helper.usres_db[user.id] = user
    return user


def get_user_by_id(user_id: int) -> UserOut:
    user = helper.users_db[user_id]
    return user


def get_users() -> list[UserOut]:
    users = list(helper.users_db.values())
    return users


def put_user(user_id: int, user_in: UserInPut) -> UserOut:
    user = helper.users_db[user_id].dict()
    for i, j in user_in.dict().items():
        if i in user and j is not None:
            user[i] = j

    user_out = UserOut(**user)
    helper.users_db[user_id] = user_out

    return user_out


def delete_user(user_id: int) -> None:
    if user_id in helper.users_db:
        del helper.users_db[user_id]