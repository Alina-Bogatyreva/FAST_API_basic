from pydantic import BaseModel, validator


class Catalog(BaseModel):
    name: str
    category: str

    @validator("category")
    def check_city(cls, value):
        if value not in ["food", "phones", "furniture", "vehicle"]:
            raise ValueError(f"{value} is not found")
        return value


class UserBase(BaseModel):
    username: str
    age: int
    address: str
    dimensions: Catalog = None


class UserIn(UserBase):
    pass


class UserInPut(UserBase):
    username: str = None
    age: int = None


class UserOut(UserBase):
    id: int

