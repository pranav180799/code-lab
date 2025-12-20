from sqlalchemy import Column, Integer, String, DateTime, DECIMAL
from datetime import datetime
from database import Base

class Bilty(Base):
    __tablename__ = "bilty_information"

    id = Column(Integer, primary_key=True, index=True)
    bilty_no = Column(Integer, unique=True, nullable=False)
    from_station = Column(String(50))
    to_station = Column(String(50))
    total_amount = Column(DECIMAL(10, 2))
    created_date = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String(50))


class EWayBill(Base):
    __tablename__ = "ewaybill"

    id = Column(Integer, primary_key=True, index=True)
    bilty_no = Column(Integer, nullable=False)
    ewaybill_no = Column(Integer, nullable=False)
