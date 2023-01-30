"""
Create
Read
Update
Delete
"""
from typing import List

from fastapi import HTTPException

from api.product.schemas import ProductIn, ProductOut, ProductInPut
from api.common.helper import check_token
from db.session import db_session


def create_product(product_in: ProductIn, token: str) -> ProductOut:
    errors = check_token(token)
    if errors is None:
        product = ProductOut(**product_in.dict(), id=db_session.next_product_id)
        db_session.db_product[product.id] = product
        return product
    else:
        raise HTTPException(status_code=400, detail=errors)


def get_product_by_id(product_id: int, token: str) -> ProductOut:
    errors = check_token(token)
    if errors is None:
        if product_id in db_session.db_product:
            return db_session.db_product[product_id]
        else:
            raise HTTPException(status_code=404, detail={"message": "Product not found"})
    else:
        raise HTTPException(status_code=400, detail=errors)


def get_products(token: str) -> List[ProductOut]:
    errors = check_token(token)
    if errors is None:
        products = list(db_session.db_product.values())
        return products
    else:
        raise HTTPException(status_code=404, detail=errors)


def put_product(product_id: int, product_in: ProductInPut, token: str) -> ProductOut:
    errors = check_token(token)
    if errors is None:
        if product_id in db_session.db_product:
            product = db_session.db_product[product_id].dict()
            for i, j in product_in.dict().items():
                if i in product and j is not None:
                    product[i] = j

            product_out = ProductOut(**product)
            db_session.db_product[product_id] = product_out

            return product_out
        else:
            raise HTTPException(status_code=404, detail={"message": "Product not found"})
    else:
        raise HTTPException(status_code=404, detail=errors)



def delete_product(product_id: int, token: str) -> None:
    errors = check_token(token)
    if errors is None:
        if product_id in db_session.db_product:
            del db_session.db_product[product_id]
        else:
            raise HTTPException(status_code=404, detail={"message": "Product not found"})
    else:
        raise HTTPException(status_code=404, detail=errors)