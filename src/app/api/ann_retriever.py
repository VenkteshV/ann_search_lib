from app.api.AnnInterface import AnnInterface
from app.api import AnnConstant
import toml
import scann
import time
import numpy as np
from app.api import AnnConstant
from app.api.algorithms.scann import ScannSearch
from app.api.algorithms.annoy import AnnoySearch
from app.api.algorithms import annoy

def get_top_n_neighbours(content):
    if content.approach.lower() == AnnConstant.SCANN_SEARCH.lower():
        ann_instance =  ScannSearch(data=index_data)
    # elif content.approach.lower() == AnnConstant.FAISS_SEARCH.lower():
    #     ann_instance = FaissSearch()

    elif content.approach.lower() == AnnConstant.ANNOY_SEARCH.lower():
        ann_instance =  AnnoySearch()
    #ann_instance.get_index()
    return ann_instance.get_top_n_neighbours(content.skill_name)


if __name__ =="__main__":
    ann_instance =  AnnoySearch()
    ann_instance.get_index()

