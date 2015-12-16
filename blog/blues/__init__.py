import os, sys

path_to_here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, path_to_here)
generator_walk = os.walk(path_to_here)
blues_list = []
for x in next(generator_walk)[1]:
    blues_list.append(__import__(x).blue)

__all__ = ['blues_list']
