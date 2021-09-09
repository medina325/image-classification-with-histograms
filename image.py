import numpy as np
import matplotlib.pyplot as plt

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
    'red': np.zeros(256, np.uint),
    'green': np.zeros(256, np.uint),
    'blue': np.zeros(256, np.uint)
  }
  distances = {
    'red': 0.0,
    'green': 0.0,
    'blue': 0.0
  }

  def __init__(self, filename: str, contents: list) -> None:
      self.filename = filename
      self.contents = np.array(contents, np.uint8)

      self.create_histogram()
      self.create_pdfs()

  def create_histogram(self, gray=False) -> None:
    """Create Image's histograms"""
    
    if not gray:
      self.histograms['red'][self.contents[:, :, 0]] += 1
      self.histograms['green'][self.contents[:, :, 1]] += 1
      self.histograms['blue'][self.contents[:, :, 2]] += 1
    else:
      self.histograms['gray'][self.contents[:, :]] += 1

  def create_pdfs(self) -> None:
    """Create Image's PDFs (Probability Density Function)"""
    
    histogram_length = self.histograms['red'].shape[0]

    self.pdfs['red'] = self.histograms['red'] / histogram_length
    self.pdfs['green'] = self.histograms['green'] / histogram_length
    self.pdfs['blue'] = self.histograms['blue'] / histogram_length

  def calc_pdfs_distances(self, search_img_pdfs, approach) -> None:
    """Calculate Image's PDF's distances to another Image's PDFs"""
    
    self.distances['red'] = approach(search_img_pdfs['red'], self.pdfs['red'])
    self.distances['green'] = approach(search_img_pdfs['green'], self.pdfs['green'])
    self.distances['blue'] = approach(search_img_pdfs['blue'], self.pdfs['blue'])

  def class_name(self) -> str:
    return self.filename.split('_')[0]

  def image_name(self) -> str:
    return self.filename.split('_')[1]

  def plot_histogram(histogram: np.array, color: str):
    indexes = np.arange(np.size(histogram))
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(indexes, histogram, edgecolor='black', color=color)
    ax.set_ylabel('Oin')
    # ax.set_title(f'{color.capitalize()} Channel Histogram')
    ax.set_title('Oin')
    # ax.set_xticks(indexes, ('G1', 'G2', 'G3', 'G4'))
    ax.set_yticks(np.arange(0, 81, 10))
    # ax.legend(labels=['Men', 'Women'])
    plt.show()