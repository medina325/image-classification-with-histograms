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

  def create_histograms(self):
    red_pixels = self.contents['rgb'][:, :, 0][0]
    green_pixels = self.contents['rgb'][:, :, 1][0]
    blue_pixels = self.contents['rgb'][:, :, 2][0]

    gray_hist,_ = np.histogram(self.contents['gray'], bins=256, range=(0,1))
    red_hist,_ = np.histogram(red_pixels, bins=256, range=(0,1))
    green_hist,_ = np.histogram(green_pixels, bins=256, range=(0,1))
    blue_hist,_ = np.histogram(blue_pixels, bins=256, range=(0,1))
    
    return {
      'gray': gray_hist,
      'red': red_hist,
      'green': green_hist,
      'blue': blue_hist
    }

  def create_pdfs(self):
    """Create Image's PDFs (Probability Density Function)"""

    img_size = self.contents['gray'].size

    return {
      'gray': self.histograms['gray'] / img_size,
      'red': self.histograms['red'] / img_size,
      'green': self.histograms['green'] / img_size,
      'blue': self.histograms['blue'] / img_size
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
    
  def plot_histograms(self):
    # https://www.tutorialspoint.com/matplotlib/matplotlib_quick_guide.htm
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
