import numpy as np
import matplotlib.pyplot as plt
from heuristic import DistanceHeuristic as dh,\
                      euclidian_distance,\
                      square_chi

class Image:
  """Represents an image with the properties required for the problem"""

  filename = ''
  contents = []
  histograms = {
    'red': np.zeros(256, np.uint),
    'green': np.zeros(256, np.uint),
    'blue': np.zeros(256, np.uint)
  }
  pdfs = {
    'red': np.zeros(256, np.float),
    'green': np.zeros(256, np.float),
    'blue': np.zeros(256, np.float)
  }
  distances = {
    'red': 0.0,
    'green': 0.0,
    'blue': 0.0
  }

  def __init__(self, filename: str, contents) -> None:
      self.filename = filename
      # self.contents = contents
      self.contents = np.array(contents, np.uint8)

      self.create_histograms()
      self.create_pdfs()

  def create_histograms(self, gray=False) -> None:
    """Create Image's histograms"""
    
    if not gray:
      # self.histograms['red'][self.contents[:, :, 0][0]] += 1
      # self.histograms['green'][self.contents[:, :, 1][0]] += 1
      # self.histograms['blue'][self.contents[:, :, 2][0]]+= 1
      red_pixels = self.contents[:, :, 0][0]
      green_pixels = self.contents[:, :, 1][0]
      blue_pixels = self.contents[:, :, 2][0]
      
      self.histograms['red'] = np.array([np.sum(red_pixels == i) for i in range(256)])
      self.histograms['green'] = np.array([np.sum(green_pixels == i) for i in range(256)])
      self.histograms['blue'] = np.array([np.sum(blue_pixels == i) for i in range(256)])
    else:
      self.histograms['gray'][self.contents[:, :]] += 1

  def create_pdfs(self) -> None:
    """Create Image's PDFs (Probability Density Function)"""
    
    histogram_length = self.histograms['red'].shape[0]

    self.pdfs['red'] = self.histograms['red'] / histogram_length
    self.pdfs['green'] = self.histograms['green'] / histogram_length
    self.pdfs['blue'] = self.histograms['blue'] / histogram_length

  def calc_pdfs_distances(self, img_pdfs, approach) -> None:
    """Calculate Image's PDF's distances to another Image's PDFs"""
    
    if (approach == dh.ED):
      self.distances['red'] = euclidian_distance(img_pdfs['red'], self.pdfs['red'])
      self.distances['green'] = euclidian_distance(img_pdfs['green'], self.pdfs['green'])
      self.distances['blue'] = euclidian_distance(img_pdfs['blue'], self.pdfs['blue'])

  def class_name(self) -> str:
    return self.filename.split('_')[0]

  def image_name(self) -> str:
    return self.filename.split('_')[1]

  def plot_histograms(self, color: str):
    indexes = np.arange(np.size(self.histograms[color]))
    # plt.hist(x=self.contents[:, :, 1][0], bins='auto', color=color, alpha=0.7, rwidth=0.85)    
    plt.bar(indexes, self.histograms[color], width=0.9, color=color)

    plt.ylabel('Frequência')
    plt.xlabel('Valor')
    plt.title(f'{color.capitalize()} Channel Histogram')
    plt.show()
