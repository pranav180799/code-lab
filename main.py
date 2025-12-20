from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal
from schemas import BiltyCreate

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/bilty/create", status_code=201)
def create_bilty(bilty: BiltyCreate, db: Session = Depends(get_db)):
    new_bilty = models.Bilty(
        bilty_no=bilty.bilty_no,
        from_station=bilty.from_station,
        to_station=bilty.to_station,
        total_amount=bilty.total_amount,
        created_by=bilty.created_by
    )

    db.add(new_bilty)
    db.commit()
    db.refresh(new_bilty)

    return {
        "message": "Bilty created successfully",
        "bilty_no": new_bilty.bilty_no
    }


@app.get("/")
def root():
    return {"status": "Bilty API running"}

@app.get("/bilty/{bilty_no}")
def get_bilty_details(bilty_no: int, db: Session = Depends(get_db)):
    bilty = db.query(models.Bilty).filter(
        models.Bilty.bilty_no == bilty_no
    ).first()

    if not bilty:
        raise HTTPException(status_code=404, detail="Bilty not found")

    ewaybill = db.query(models.EWayBill).filter(
        models.EWayBill.bilty_no == bilty_no
    ).first()

    if not ewaybill:
        raise HTTPException(status_code=404, detail="No ewaybill found")

    return {
        "bilty_no": bilty.bilty_no,
        "from_station": bilty.from_station,
        "to_station": bilty.to_station,
        "total_amount": float(bilty.total_amount),
        "ewaybill_status": 1,
        "ewaybill_no": ewaybill.ewaybill_no
    }

from schemas import EWayBillCreate

@app.post("/ewaybill/create", status_code=201)
def create_ewaybill(ewaybill: EWayBillCreate, db: Session = Depends(get_db)):
    new_ewaybill = models.EWayBill(
        bilty_no=ewaybill.bilty_no,
        ewaybill_no=ewaybill.ewaybill_no
    )

    db.add(new_ewaybill)
    db.commit()
    db.refresh(new_ewaybill)

    return {
        "message": "EWayBill created successfully",
        "ewaybill_no": new_ewaybill.ewaybill_no
    }
