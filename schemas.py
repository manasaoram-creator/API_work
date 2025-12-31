# app/schemas.py
from pydantic import BaseModel
from typing import Optional

from datetime import date

# Schema for a process returned by the API
class Process(BaseModel):
    PROCESS_ID: Optional[int] = None
    PROCESS_NAME: str
    PROJECT: Optional[str] = None
    STATUS_ID: Optional[int] = None
 
    class Config:
        # allow reading from ORM models if you use SQLAlchemy
        from_attributes = True
 
# Schema for starting an audit log (request body)
class AuditLogStartIn(BaseModel):
    process_id: int
    queued: int
    completed: int

# Schema for a customer record returned by the API
class Customer(BaseModel):
    CUSTOMER_ID: int
    CUSTOMER_NAME: Optional[str] = None
    CUSTOMER_EMAIL: Optional[str] = None
    ACCOUNT_STATUS: Optional[str] = None
    ACCOUNT_TYPE: Optional[str] = None
    MAILING_ADDRESS: Optional[str] = None

    class Config:
        # allow reading from ORM models if you use SQLAlchemy
        from_attributes = True