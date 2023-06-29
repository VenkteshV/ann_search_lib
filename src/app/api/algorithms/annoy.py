import annoy
from annoy import AnnoyIndex
import os
import pandas as pd
import numpy as np
from annoy import AnnoyIndex
import torch
from app.api.AnnInterface import AnnInterface
from sentence_transformers import SentenceTransformer
import zope.interface
from sklearn.metrics.pairwise import cosine_similarity


dir_path = os.path.dirname(os.path.realpath(__file__))


skill_data = pd.read_csv(os.path.join(dir_path, "../data/skill_latest.csv"))
print(skill_data.shape[0])

@zope.interface.implementer(AnnInterface)
class AnnoySearch:
    def __init__(self,data=None, num_trees=None,emb_dim=None):
        self.num_trees=num_trees
        self.emb_dim=emb_dim
    def get_embeddings_for_skills(self, data_ls):
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        embeddings = model.encode(data_ls)
        return embeddings

    def get_top_n_neighbours(self,skill_title):
        annoy = AnnoyIndex(384, metric="angular")
        annoy.load(os.path.join(dir_path, "../data/index.annoy"))
        new_emb = self.get_embeddings_for_skills(skill_title)
        print(skill_title,new_emb.shape)
        top_matches = annoy.get_nns_by_vector(new_emb,15)
        print(top_matches,skill_data)
        indices = [i for i in top_matches]
        results = [skill_data["skill_name"].values[i] for i in top_matches]
        print("results",results)
        article_emb = self.get_embeddings_for_skills(results)
        print("new_emb", new_emb.shape, article_emb.shape)
        text_sims = cosine_similarity(article_emb,[new_emb]).tolist()
        print("text_sims",text_sims)
        results_sims = zip(range(len(text_sims)), text_sims)
        sorted_similarities = sorted(results_sims, key=lambda x: x[1], reverse=True)
        print("text_sims",sorted_similarities)
        top_sentences = []
        distances = []
        for idx, item in sorted_similarities:
            top_sentences.append(results[idx])
            distances.append(item[0])
        return {"neighbours": top_sentences, "dist":distances}


    def get_index(self, embedding_dim = 384, number_of_trees=100):
        ann = AnnoyIndex(embedding_dim, metric = "angular")
        embeddings =  self.get_embeddings_for_skills(skill_data["skill_name"].values)
        for index, embed in enumerate(embeddings):
            ann.add_item(index, embed)
        ann.build(number_of_trees)
        ann.save(os.path.join(dir_path, "../data/index.annoy"))

if __name__=="__main__":
    annoy_instance = AnnoySearch()
    annoy_instance.get_index()