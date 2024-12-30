# users/schemas.py
from ninja import Schema
from typing import Dict

class HealthRecordSchema(Schema):
    id: int
    title: str
    description: str
    date: str
    data: Dict

class HealthRecordCreateSchema(Schema):
    title: str
    description: str
    date: str
    data: Dict
