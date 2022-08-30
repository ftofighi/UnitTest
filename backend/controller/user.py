from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from db.schemas import UserCreate
from db.database import get_db
from services.user import create_user

router = APIRouter()


@router.post('/Add')
def add_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(user=user, db=db)

