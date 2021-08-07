from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemes, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=List[schemes.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db),current_user: schemes.User = Depends(oauth2.get_current_user)):
    return blog.get_all_blogs(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemes.Blog, db: Session = Depends(get_db),current_user: schemes.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemes.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db),current_user: schemes.User = Depends(oauth2.get_current_user)):
    return blog.get(id,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id: int, db: Session = Depends(get_db),current_user: schemes.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(id: int, request: schemes.Blog, db: Session = Depends(get_db),current_user: schemes.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
