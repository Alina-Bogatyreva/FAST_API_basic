from fastapi import FastAPI

from api.product.views import router_product
from api.user.views import router_user



app = FastAPI()
app.include_router(router_product)
app.include_router(router_user)
