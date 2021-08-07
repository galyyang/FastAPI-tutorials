from fastapi import APIRouter, Depends, status
from .. import schemes, database
from sqlalchemy.orm import Session

from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemes.ShowUser)
def create_user(request: schemes.User, db: Session = Depends(get_db)):
    return user.create(request,db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemes.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id,db)
