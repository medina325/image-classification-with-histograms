import numpy as np
from enum import Enum

class DistanceHeuristic(Enum):
  """Collection of Heuristics"""

  ED = 0
  SC = 1
  
  def euclidian_distance(pe, pi, gray) -> dict:
    if gray:
      return {
        'gray': np.sum(np.square(pe['gray'] - pi['gray']))
      }

    return {
      'red':   np.sum(np.square(pe['red'] - pi['red'])),
      'green': np.sum(np.square(pe['green'] - pi['green'])),
      'blue':  np.sum(np.square(pe['blue'] - pi['blue']))
    }

  def square_chi(pe, pi, gray) -> dict:
    if gray:
      return {
        'gray': np.sum(np.square(pe['gray'] - pi['gray']) / (pe['gray'] + pi['gray'] + 0.0001))
      }
    
    return {
      'red':   np.sum(np.square(pe['red'] - pi['red']) / (pe['red'] + pi['red'] + 0.00000001)),
      'green': np.sum(np.square(pe['green'] - pi['green']) / (pe['green'] + pi['green'] + 0.000000001)),
      'blue':  np.sum(np.square(pe['blue'] - pi['blue']) / (pe['blue'] + pi['blue'] + 0.000000001))
    }