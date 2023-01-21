from fastapi import FastAPI, Path, Query, Body  # external modules, i.o. which used pip install
from fastapi.responses import JSONResponse

from models import UserRequest, UserResponse, Family, ProductRequest, ProductResponse   # custom modules, our self python files
from api.product.helper import Helper
from api.product.views import router_product
from api.user.views import router_user



app = FastAPI()
app.include_router(router_product)
app.include_router(router_user)
helper = Helper()


@app.get("/")
def home():
    return {"hello": "world"}


@app.get('/user/{user_id}')
def get_user_by_id(user_id: int = Path(..., gt=0, description="user id in DataBase"),
                   user_type: str = Query(..., max_length=15, description="user type"),
                   address: str = Query(None, min_length=3, description="address of user")):
    """
    :param user_id: is parameter of url (required-обязательно)
    :param user_type: is parameter of query (optional-необязательно)
    :param address: is parameter of query (optional-необязательно)
    :return: simple json
    """
    return {'key': user_id, 'user_type': user_type, 'address': address}


@app.get("/user/check/{username}")
def check_username(username):
    if username not in ["alex", "ivan", "al123"]:
        return username


@app.post("/user", response_model=UserResponse, response_model_exclude={"address", "birthdate"})
def create_user(user: UserRequest, family: Family, email: str = Body(...)):
    if user.work_experience[0].number_of_years > user.age:
        return JSONResponse(status_code=400, content={"error": "number_of_years can't more than age"})

    return UserResponse(**user.dict(), id=100, family=family, email=email)


@app.post("/product", response_model=ProductResponse)
def create_product(product: ProductRequest):
    prod_id = helper.generate_id()
    return ProductResponse(id=prod_id, **product.dict())


@app.put("/add_user/{user_id}")
def add_user(user: UserRequest, user_id: int = Path(..., gt=0)):
    return user_id