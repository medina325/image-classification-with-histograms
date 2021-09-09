import numpy as np
from enum import Enum

# TODO
# Criar consts para dizer qual método usar para calcular as distâncias
def euclidian_distance(pe, pi) -> float:
  return np.sum(np.square(pe - pi))

def square_chi(pe, pi) -> float:
  pass

class DistanceHeuristic(Enum):
  """Collection of heuristics"""
  ED = euclidian_distance
  SC = square_chi
  