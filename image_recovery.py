import numpy as np
from skimage import io
import os
from zipfile import ZipFile
import re
import matplotlib.pyplot as plt
import sys

# Every image is gonna be represented by a Image class
class Image:
  filename = ''
  contents = []
  histograms = {
    "red": np.zeros(256, np.uint),
    "green": np.zeros(256, np.uint),
    "blue": np.zeros(256, np.uint)
  }
  pdf = {
    "red": np.zeros(256, np.uint),
    "green": np.zeros(256, np.uint),
    "blue": np.zeros(256, np.uint)
  }

  def __init__(self, filename: str, contents: list) -> None:
      self.filename = filename
      self.contents = np.array(contents, np.uint8)

      self.create_histogram()
      self.create_pdfs()

  """
    Initialize Image's histograms
  """
  def create_histogram(self):
    histogram_r = np.zeros(256, np.uint)
    histogram_g = np.zeros(256, np.uint)
    histogram_b = np.zeros(256, np.uint)
    
    w, h, _ = self.contents.shape

    for x in range(w):
      for y in range(h):
        histogram_r[self.contents[x][y][0]] += 1
        histogram_g[self.contents[x][y][1]] += 1
        histogram_b[self.contents[x][y][2]] += 1

    self.histograms['red'] = histogram_r
    self.histograms['green'] = histogram_g
    self.histograms['blue'] = histogram_b

  def create_pdfs(self):
    histogram_length = self.histogram['red'].shape[0]
    
    self.pdf['red'] = self.histogram['red'] / histogram_length
    self.pdf['green'] = self.histogram['green'] / histogram_length
    self.pdf['blue'] = self.histogram['blue'] / histogram_length

# --------------------------------------------------------------------------------------------
def initialize_images():
  # Abra o zip e coloque as imagens em uma lista

  if (not os.path.exists('Vistex')):
    with ZipFile('Vistex.zip', 'r') as zip:
      for filename in zip.namelist():
        if re.match(r'Vistex/.+\.png', filename):
          zip.extract(filename)
    zip.close()

  files = os.listdir('Vistex')

  # imgs = []
  # for i in range(0,3):
  #   imgs.append(Image(files[i], io.imread(f'Vistex/{files[i]}')))
  # return imgs

  return [Image(file, io.imread(f'Vistex/{file}')) for file in files]

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

if __name__ == "__main__":
  # Entradas:
  # - Imagem de busca
  # - Caminho de uma pasta contendo imagens a serem buscadas
  # - Inteiro N que indica o número de imagens parecidas a serem retornadas

  print("Syntax to use this tool:")
  print("python image_recovery <search_image_name> <images_path> <number_of_images_to_be_recovered>")

  search_image = sys.argv[1]
  images_path = sys.argv[2]
  number_results = sys.argv[3]
  
  # Initialize all images with it's histograms and pdfs
  imgs = initialize_images()

  print(imgs[0].filename)
  print(imgs[0].contents)
  print(imgs[0].filename)
  print(imgs[0].filename)
  print(imgs[0].filename)

  # Faça a recuperação das imagens usando diferentes métodos