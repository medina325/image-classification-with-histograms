import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from heuristic import DistanceHeuristic as dh
import os
from skimage import io

class Image:
  """Represents an image with all information required for the problem"""
  
  def __init__(self, filename: str, path: str) -> None:
    self.filename = filename
    self.contents = {
      'gray': io.imread(os.path.join(path, filename), as_gray=True),
      'rgb': io.imread(os.path.join(path, filename), as_gray=False) / 255
    }
    self.histograms = self.create_histograms()
    self.pdfs = self.create_pdfs()
    self.distances = {}

  def class_name(self) -> str:
    return self.filename.split('_')[0]

  def image_name(self) -> str:
    return self.filename.split('_')[1]

  def get_channel_contents(self, channel:str) -> list:
    ch_dict = {
      'red': 0,
      'green': 1,
      'blue': 2
    }

    return self.contents['rgb'][:, :, ch_dict[channel]].ravel() if channel != 'gray' else self.contents['gray'].ravel()

  def create_histograms(self):
    gray_pixels = self.get_channel_contents('gray')
    red_pixels = self.get_channel_contents('red')
    green_pixels = self.get_channel_contents('green')
    blue_pixels = self.get_channel_contents('blue')

    gray_hist, gray_bin_edges = np.histogram(gray_pixels, bins=256, range=(0, 1))
    red_hist, red_bin_edges = np.histogram(red_pixels, bins=256, range=(0, 1))
    green_hist, green_bin_edges = np.histogram(green_pixels, bins=256, range=(0, 1))
    blue_hist, blue_bin_edges = np.histogram(blue_pixels, bins=256, range=(0, 1))
    
    return {
      'gray': {'freq': gray_hist, 'bin_edges': gray_bin_edges}, 
      'red': {'freq': red_hist, 'bin_edges': red_bin_edges},
      'green': {'freq': green_hist, 'bin_edges': green_bin_edges},
      'blue': {'freq': blue_hist, 'bin_edges': blue_bin_edges}
    }

  def create_pdfs(self):
    """Create Image's PDFs (Probability Density Function)"""

    img_size = self.contents['gray'].size

    return {
      'gray': self.histograms['gray']['freq'] / img_size,
      'red': self.histograms['red']['freq'] / img_size,
      'green': self.histograms['green']['freq'] / img_size,
      'blue': self.histograms['blue']['freq'] / img_size
    }

  def calc_pdfs_distances(self, img_pdfs, heuristic) -> None:
      """Calculate Image's PDF's distances to another Image's PDFs"""
      
      if (heuristic == dh.ED):
        self.distances = dh.euclidian_distance(img_pdfs, self.pdfs)
      elif (heuristic == dh.SC):
        self.distances = dh.square_chi(img_pdfs, self.pdfs)

  def n_most_similar_imgs(self, heuristic, imgs_to_be_searched: list['Image'], n: int) -> list['Image']:  
    """Get n most similar images to this image"""

    for img in imgs_to_be_searched:
      img.calc_pdfs_distances(self.pdfs, heuristic)
   
    # return sorted(imgs_to_be_searched, key=lambda img: img.distances['gray'])[:n]
    return sorted(imgs_to_be_searched, key=lambda img: (img.distances['red'] + img.distances['green'] + img.distances['blue']) / 3)[:n]
    
  def plot_image_w_histograms(self):  
    fig = plt.figure()
    fig.suptitle("Image and it's Histograms")
    gs = GridSpec(4, 2, figure=fig)
    ax1 = fig.add_subplot(gs[:, 0])
    ax1.imshow(self.contents['rgb'])
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.hist(self.get_channel_contents('gray'), bins=self.histograms['gray']['bin_edges'], color='gray')
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.hist(self.get_channel_contents('red'), bins=self.histograms['red']['bin_edges'], color='red')
    ax4 = fig.add_subplot(gs[2, 1])
    ax4.hist(self.get_channel_contents('green'), bins=self.histograms['green']['bin_edges'], color='green')
    ax5 = fig.add_subplot(gs[3, 1])
    ax5.hist(self.get_channel_contents('blue'), bins=self.histograms['blue']['bin_edges'], color='blue')

    plt.show()
