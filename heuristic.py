import numpy as np
from enum import Enum

class DistanceHeuristic(Enum):
  """Collection of Heuristics"""

  ED = 0
  SC = 1
  
  def euclidian_distance(pe, pi) -> dict:
    """Returns the Euclidian Distance for every given channel"""

    distances = {}

    for key in pe.keys():
      distances = distances | {key: np.sum(np.square(pe[key] - pi[key]))}
      
    return distances

  def square_chi(pe, pi) -> dict:
    """Returns the Square Chi Distance for every given channel"""

    fix = 0.00000001
    distances = {}

    for key in pe.keys():
      distances = distances | {key: np.sum(np.square(pe[key] - pi[key]) / (pe[key] + pi[key] + fix))}

    return distances
