from AnnInterface import OptimizerInterface
import AnnConstant
import toml
import scann
import time
import numpy as np
from algorithms.scann import ScannSearch
from algorithms.annoy import AnnoySearch
from algorithms.faiss import FaissSearch

index_data = pd.read_csv("data/skill_latest.csv")
print(index_data.shape[0])
class AnnFactory:
    @staticmethod
    def get_optimizer(config):
        if config.get("AnnClass").lower() == AnnConstant.SCANN_SEARCH.lower():
            return  ScannSearch(data=index_data)
        elif config.get("AnnClass").lower() == AnnConstant.FAISS_SEARCH.lower():
            return FaissSearch()

        elif config.get("AnnClass").lower() == AnnConstant.ANNOY_SEARCH.lower():
            return AnnoySearch()

        else:
            classname = config.get("AnnClass")
            if classname not in globals():
                raise ValueError("No implementation found for the custom data generator class specified: {}".format(classname))
            if OptimizerInterface.implementedBy(classname)==False:
                raise ValueError("custom data generator class specified, ie {}, doesn't correctly implement interface AnnInterface (in AnnInterface.py)".format(classname))
            #Note, currently, no params are passed into the custom class, add config to enable
            return globals()[classname]()

if __name__=="__main__":
    config = toml.load("config/config.toml")
    searchConfig = config.get('AnnSearch')
    optimizer = AnnFactory.get_optimizer(searchConfig)