from abc import ABCMeta, abstractstaticmethod
import abc
import zope.interface

class AnnInterface(zope.interface.Interface):
    def get_similarity_distance(self):
        pass
    def get_top_n_neighbours(self):
        pass

    def get_index(self):
        pass