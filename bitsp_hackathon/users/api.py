# users/api.py
from typing import List
from ninja import NinjaAPI
from .models import HealthRecord
from .schemas import HealthRecordSchema, HealthRecordCreateSchema

users = NinjaAPI(urls_namespace="users_api")

# List all health records
@users.get("/health-records", response=List[HealthRecordSchema])
def list_health_records(request):
    records = HealthRecord.objects.all()  # No user filtering for now
    return records

# Create a health record
@users.post("/health-records", response=HealthRecordSchema)
def create_health_record(request, payload: HealthRecordCreateSchema):
    record = HealthRecord.objects.create(**payload.dict())
    return record

# Update a health record
@users.put("/health-records/{record_id}", response=HealthRecordSchema)
def update_health_record(request, record_id: int, payload: HealthRecordCreateSchema):
    record = HealthRecord.objects.get(id=record_id)
    for attr, value in payload.dict().items():
        setattr(record, attr, value)
    record.save()
    return record

# Delete a health record
@users.delete("/health-records/{record_id}")
def delete_health_record(request, record_id: int):
    record = HealthRecord.objects.get(id=record_id)
    record.delete()
    return {"success": True}
