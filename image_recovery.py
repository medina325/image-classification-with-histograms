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
  def create_histogram(self) -> None:
    self.histograms['red'][self.contents[:, :, 0]] += 1
    self.histograms['green'][self.contents[:, :, 1]] += 1
    self.histograms['blue'][self.contents[:, :, 2]] += 1

  def create_pdfs(self):
    histogram_length = self.histograms['red'].shape[0]

    self.pdf['red'] = self.histograms['red'] / histogram_length
    self.pdf['green'] = self.histograms['green'] / histogram_length
    self.pdf['blue'] = self.histograms['blue'] / histogram_length

# --------------------------------------------------------------------------------------------
def open_images_w_path(path: str):
  if (not os.path.exists(path)):
    # raise exception
    pass
  
  return os.listdir(path)

def initialize_images(search_image: str, files: list, path: str) -> list:
  return [Image(file, io.imread(f'{path}/{file}')) for file in files if file != search_image]
  
def initialize_search_image(search_image, path):
  return Image(search_image, io.imread(f'{path}/{search_image}'))

def extract_images_from_vistex_zip():
  # Abra o zip e coloque as imagens em uma lista

  if (not os.path.exists('Vistex')):
    with ZipFile('Vistex.zip', 'r') as zip:
      for filename in zip.namelist():
        if re.match(r'Vistex/.+\.png', filename):
          zip.extract(filename)

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

  print("Syntax to use this tool:\n")
  print("python image_recovery <search_image_name> <images_path> <number_of_images_to_be_recovered>", end="\n\n")

  search_image = sys.argv[1]
  images_path = sys.argv[2]
  number_results = sys.argv[3]
  
  # Initialize all images with it's histograms and pdfs
  try:
    files = open_images_w_path(images_path)

    imgs = initialize_images(search_image, files, images_path)
    search_image = initialize_search_image(search_image, images_path)
    
    # Faça a recuperação das imagens usando diferentes métodos
    # Distância Euclidiana

    # Chi-quadrado

    # Chi modificado

  except FileNotFoundError as e:
    print(e)
