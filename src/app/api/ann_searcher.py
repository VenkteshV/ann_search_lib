from typing import List,Any
from fastapi import Header, APIRouter
from app.api.models import Neighbours, Content

from app.api.ann_retriever import get_top_n_neighbours


ann_searcher  = APIRouter()




@ann_searcher.post('/get_n_neighbours',response_model=Neighbours)
async def get_n_neighbours(payload: Content):
    return get_top_n_neighbours(payload)


# @ann_searcher.post('/get_distance',response_model=Neighbours)
# async def get_distance(payload: Content):
#     return get_distance(payload.skill)


    