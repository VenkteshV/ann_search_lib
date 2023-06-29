
import zope.interface
import numpy as np
from app.api.AnnInterface import AnnInterface
from app.api import AnnConstant
import scann
from sentence_transformers import SentenceTransformer

@zope.interface.implementer(AnnInterface)
class ScannSearch:
    def generate_embeddings(data_ls):
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        embeddings = model.encode(data_ls)
        return embeddings
    def __init__(self,data=None, num_leaves=None):
        self.num_leaves=num_leaves

    def get_top_n_neighbours():
        pass
    def get_index(self,):
        pass