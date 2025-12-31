from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List

from app.schemas import Process, AuditLogStartIn, Customer
from app.crud import (
    basic_select,
    get_processes,
    get_process,
    get_customer_by_id,
    audit_log_start,
)

from app.database import get_database
from sqlalchemy.orm import Session

app = FastAPI()

# The "Depends" wrapper is used to ensure the session is available
# to all endpoints.
Database = Annotated[Session, Depends(get_database)]

@app.get('/process', response_model=List[Process])
async def get_all_processes(database: Database):
    """Retrieve all processes."""
    results = await get_processes(database)
    return results


@app.get('/process/{process_id}', response_model=Process)
async def get_process_from_id(database: Database, process_id: int):
    """Retrieve a single process by its ID."""
    process = await get_process(database, process_id)
    if process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    return process

@app.get('/customer/{customer_id}', response_model=Customer)
async def get_customer_info(database: Database, customer_id: int):
    """Retrieve customer information by customer ID."""
    customer = await get_customer_by_id(database, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@app.post("/audit_log/start", status_code=202)
async def start_audit_log(database: Database, body: AuditLogStartIn):
    """Starts a new audit log for a process."""
    await audit_log_start(
        database,
        process_id=body.process_id,
        queued=body.queued,
        completed=body.completed,
    )
    return {"message": "Audit log start successful."}


@app.get("/health")
async def health(database: Database):
    try:
        await basic_select(database)
        return {"message": "Still alive."}
    except Exception:
        raise HTTPException(status_code=503, detail="Database connection is not healthy")