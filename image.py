import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from heuristic import DistanceHeuristic as dh

class Image:
  """Represents an image with the properties required for the problem"""
  def __init__(self, filename: str) -> None:
    self.filename = filename
    self.distances = {}

  def class_name(self) -> str:
    return self.filename.split('_')[0]

  def image_name(self) -> str:
    return self.filename.split('_')[1]

class GrayImage(Image):
  def __init__(self, filename: str, contents) -> None:
    super().__init__(filename)

    self.contents = np.array(contents * 256, np.uint8)
    self.histograms = self.create_histograms()
    self.pdfs = self.create_pdfs()

  def create_histograms(self) -> dict:
    pixels = self.contents[:, :]
    
    return {
      'gray': np.array([np.sum(pixels == i) for i in range(256)])
    }

  def create_pdfs(self) -> dict:
    """Create Image's PDFs (Probability Density Function)"""
    
    return {
      'gray': self.histograms['gray'] / self.contents.size
    }

  def calc_pdfs_distances(self, img_pdfs, heuristic) -> None:
    """Calculate Image's PDF's distances to another Image's PDFs"""
    
    if (heuristic == dh.ED):
      self.distances = dh.euclidian_distance(img_pdfs, self.pdfs, True)
    elif (heuristic == dh.SC):
      self.distances = dh.square_chi(img_pdfs, self.pdfs, True)
  
  def n_most_similar_imgs(self, heuristic, imgs_to_be_searched: list[Image], n: int) -> list[Image]:
    """Get n most similar images to this image"""

    for img in imgs_to_be_searched:
      img.calc_pdfs_distances(self.pdfs, heuristic)
    
    return sorted(imgs_to_be_searched, key=lambda img: img.distances['gray'])[:n]      

  def plot_histograms(self):
    x_axis = np.arange(256)

    def make_subplot(color, sub):
      plt.subplot(*sub)
      plt.bar(x_axis, self.histograms[color], width=0.9, color='black')
      plt.title(f'{color.capitalize()} Channel Histogram')
      plt.ylabel('Frequência')
      plt.xlabel('Valor')

    # plt.hist(x=self.contents[:, :, 1][0], bins='auto', color=color, alpha=0.7, rwidth=0.85)    
    make_subplot('gray', (1,3,1))
    
    plt.show()

class ColoredImage(Image):
  def __init__(self, filename: str, contents) -> None:
    super().__init__(filename)

    self.contents = np.array(contents, np.uint8)
    self.histograms = self.create_histograms()
    self.pdfs = self.create_pdfs()

  def create_histograms(self) -> dict:
    # self.histograms['red'][self.contents[:, :, 0][0]] += 1
    # self.histograms['green'][self.contents[:, :, 1][0]] += 1
    # self.histograms['blue'][self.contents[:, :, 2][0]]+= 1
    red_pixels = self.contents[:, :, 0][0]
    green_pixels = self.contents[:, :, 1][0]
    blue_pixels = self.contents[:, :, 2][0]

    return {
      'red': np.array([np.sum(red_pixels == i) for i in range(256)]),
      'green': np.array([np.sum(green_pixels == i) for i in range(256)]),
      'blue': np.array([np.sum(blue_pixels == i) for i in range(256)])
    }

  def create_pdfs(self) -> dict:
    """Create Image's PDFs (Probability Density Function)"""

    img_size = self.contents.size

    return {
      'red': self.histograms['red'] / img_size,
      'green': self.histograms['green'] / img_size,
      'blue': self.histograms['blue'] / img_size
    }
  
  def calc_pdfs_distances(self, img_pdfs, heuristic) -> None:
    """Calculate Image's PDF's distances to another Image's PDFs"""
    
    if (heuristic == dh.ED):
      self.distances = dh.euclidian_distance(img_pdfs, self.pdfs, False)
    elif (heuristic == dh.SC):
      self.distances = dh.square_chi(img_pdfs, self.pdfs, False)

  def n_most_similar_imgs(self, heuristic, imgs_to_be_searched: list[Image], n: int) -> list[Image]:  
    """Get n most similar images to this image"""

    for img in imgs_to_be_searched:
      img.calc_pdfs_distances(self.pdfs, heuristic)
    
    most_similar = sorted(imgs_to_be_searched, key=lambda img: (img.distances['red'] + img.distances['green'] + img.distances['blue']) / 3)[:n]
    
    for i in most_similar:
      print(i.distances)
    print('\n')
    return sorted(imgs_to_be_searched, key=lambda img: (img.distances['red'] + img.distances['green'] + img.distances['blue']) / 3)[:n]

  def plot_histograms(self):
    x_axis = np.arange(256)

    def make_subplot(ax, color, row, col):
      ax = fig.add_subplot(gs[row, col])
      ax.bar(x_axis, self.histograms[color], width=3, color=color)
      # ax.hist(x=self.contents[:,:,0][0], bins=256, color=color)
      ax.set_title(f'{color.capitalize()} Channel Histogram')
      ax.set_ylabel('Frequency')
      ax.tick_params(axis='y', labelbottom='off')
      ax.set_xlabel('Pixel Intensity')
      ax.tick_params(axis='x', labelbottom='off')

    # plt.hist(x=self.contents[:, :, 1][0], bins='auto', color=color, alpha=0.7, rwidth=0.85)    
    fig = plt.figure()
    fig.suptitle("Histograms")
    gs = GridSpec(3, 2, figure=fig)
    ax1 = fig.add_subplot(gs[:, 0])
    ax1.imshow(self.contents)
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 1])
    ax4 = fig.add_subplot(gs[2, 1])
    make_subplot(ax2, 'red', 0, 1)
    make_subplot(ax3, 'green', 1, 1)
    make_subplot(ax4, 'blue', 2, 1)
    # make_subplot('red', (1,3,1))
    # make_subplot('green', (1,3,2))
    # make_subplot('blue', (1,3,3))
    
    plt.show()
