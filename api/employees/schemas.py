from pydantic import BaseModel
from enum import Enum
from typing import List

class RoleEnum(str, Enum):
    admin = "admin"
    seller = "seller"
    expert = "expert"


class EmployeeBase(BaseModel):
    name: str = None
    role: RoleEnum = None


class EmployeeIn(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int
