from pydantic import BaseModel
from datetime import date
from typing import Optional

class BiltyCreate(BaseModel):
    bilty_no: int
    from_station: str
    to_station: str
    total_amount: float
    created_date: Optional[date] = None
    created_by: str


class EWayBillCreate(BaseModel):
    bilty_no: int
    ewaybill_no: int
