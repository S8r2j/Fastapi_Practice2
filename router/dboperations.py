import datetime

from MMSystem.structure import Person,Member,Address,College,InputCollege,InputPerson,InputMember,InputAddress
from fastapi import FastAPI, APIRouter,Depends
from sqlmodel import SQLModel,select
from sqlalchemy.orm import Session
from MMSystem import model,dbconnection
from dbconnection import sessionlocal,engine

model.base.metadata.create_all(bind=engine)

router=APIRouter()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/")
def welcome():
    return {'message': "Welcome to SEDS API"}


@router.get("/api/members")
def get_all_members(db:Session=Depends(get_db))->list[Member]:
    return db.query(model.Member).all()

@router.get("/api/members/{id}")
def get_members_by_id(id:int,db:Session=Depends(get_db)):
    return db.query(model.Member).filter(model.Member.id==id).first()

@router.get("/api/colleges")
def get_colleges(db:Session=Depends(get_db)):
    return db.query(model.College).all()

@router.get("/api/people")
def get_people(db:Session=Depends(get_db)):
    return db.query(model.Person).all()

@router.post("/api/new_members")
def new_register(member:InputMember,college:InputCollege,personnel:InputPerson,address:InputAddress,db:Session=Depends(get_db)):
    db.query(model.Address.address_id).filter(model.Address.city==address.city)
    return db.query(model.Address.address_id).filter(model.Address.province==address.province)
    # db_address=model.Address(city=address.city,province=address.province,postal_code=address.postal_code)
    # db.add(db_address)
    # db.commit()
    # db.refresh(db_address)
    # db.query(model.Address).filter(model.Address.city == address.city)
    # adrss = db.query(model.Address).filter(model.Address.province == address.province).first()
    # id2=adrss['adress_id']
    # print(id2)
    # db_personnel=model.Person(prsn_id=personnel.prsn_id,prsn_position=personnel.prsn_position)
    # db.add(db_personnel)
    # db.commit()
    # db.refresh(db_personnel)
    # db.query(model.College).filter(model.College.clz_name==college.clz_name).all()
    # db.query(model.College).filter(model.College.clz_website==college.clz_website).first()
    # if(db):
    #     id=db['clz_id']
    # else:
    #     db_college=model.College(clz_name=college.clz_name,clz_address=college.clz_address,clz_website=college.clz_website)
    #     db.add(db_college)
    #     db.commit()
    #     db.refresh(db_college)
    # db.query(model.College).filter(model.College.clz_name == college.clz_name).all()
    # db.query(model.College).filter(model.College.clz_website == college.clz_website).first()
    # id=db['clz_id']
    # print(id)
    # db_member=model.Member(firstname=member.firstname,lastname=member.lastname,M_name=member.M_name,email=member.email,major=member.major,phone_number=member.phone_number,prsn_id=personnel.prsn_id,college_id=id,address_id=id2)
    # db.add(db_member)
    # db.commit()
    # db.refresh(db_member)


