"""
Create
Read
Update
Delete
"""
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.employees.schemas import EmployeeIn, EmployeeOut
from db import db_employee


class Employee:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_employee(self, employee_in: EmployeeIn) -> EmployeeOut:
        employee = db_employee.create_employee(self.db_session, **employee_in.dict())
        employee_out = EmployeeOut(id=employee.id, name=employee.name, role=employee.role)
        return employee_out

    def get_employee_by_id(self, employee_id: int):
        employee = db_employee.get_employee_by_id(self.db_session, employee_id)
        if employee:
            return EmployeeOut(id=employee.id, name=employee.name, role=employee.role)
        else:
            raise HTTPException(status_code=404, detail={"message": "Employee not found!"})

    def get_all_employees(self) -> List[EmployeeOut]:
        results = db_employee.get_all_employees(self.db_session)
        employee_outs = []
        for e in results:
            eo = EmployeeOut(id=e.id, name=e.name, role=e.role)
            employee_outs.append(eo)
        return employee_outs

    def put_employee(self, employee_id: int, employee_in: EmployeeIn) -> EmployeeOut:
        employee = db_employee.update_employee(self.db_session, employee_id, employee_in)
        if employee:
            return EmployeeOut(id=employee.id, name=employee.name, role=employee.role)
        else:
            raise HTTPException(status_code=404, detail={"message": "Employee not found!"})

    def delete_employee(self, employee_id: int) -> None:
        if not db_employee.delete_employee(self.db_session, employee_id):
            raise HTTPException(status_code=404, detail={"message": "Employee not found!"})