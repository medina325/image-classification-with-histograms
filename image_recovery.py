import numpy as np
from skimage import io
import os
from zipfile import ZipFile
import re
import matplotlib.pyplot as plt
import sys

class Image:
  """Represents an image with the properties required for the problem"""

  filename = ''
  contents = []
  histograms = {
    "red": np.zeros(256, np.uint),
    "green": np.zeros(256, np.uint),
    "blue": np.zeros(256, np.uint)
  }
  pdfs = {
    "red": np.zeros(256, np.uint),
    "green": np.zeros(256, np.uint),
    "blue": np.zeros(256, np.uint)
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

# --------------------------------------------------------------------------------------------
def open_images_w_path(path: str) -> list[str]:
  if (not os.path.exists(path)):
    raise FileNotFoundError(f'Caminho {path} não existente.')
  
  return os.listdir(path)

def initialize_images(search_image: str, files: list, path: str) -> list[Image]:
  return [Image(file, io.imread(f'{path}/{file}')) for file in files if file != search_image]
  
def initialize_search_image(search_image, path) -> Image:
  return Image(search_image, io.imread(f'{path}/{search_image}'))

# --------------------------------------------------------------------------------------------
def n_most_similar_imgs(n, imgs_w_distances: dict) -> list[str]:
  pass

def euclidian_distance(pe, pi) -> float:
  pass

def most_similar_imgs(approach: str, search_img: Image, imgs_to_be_searched: list[Image], number_results: int) -> list[str]:
  imgs_w_distances = []
  
  for img in imgs_to_be_searched:
    imgs_w_distances.append({
      'img': img.filename,
      'distance': approach(search_img.pdfs, img.pdfs)
    })

  return n_most_similar_imgs(number_results, imgs_w_distances)

def extract_images_from_vistex_zip() -> None:
  """Abra o zip e coloque as imagens em uma lista"""

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
  print("python image_recovery <images_path> <search_image_name> <number_of_images_to_be_recovered>", end="\n\n")

  images_path = sys.argv[1]
  search_image = sys.argv[2]
  number_results = sys.argv[3]
  
  try:
    # Initialize all images with it's histograms and pdfs
    files = open_images_w_path(images_path)

    search_image = initialize_search_image(search_image, images_path)
    imgs_to_be_searched = initialize_images(search_image, files, images_path)
    
    # Faça a recuperação das imagens usando diferentes métodos
    # Distância Euclidiana
    ed_similar_imgs = most_similar_imgs('ed', search_image, imgs_to_be_searched, number_results)

    # Chi-quadrado
    s_chi_similar_imgs = most_similar_imgs('square_chi', search_image, imgs_to_be_searched, number_results)

    # Chi modificado
    mod_chi_similar_imgs = most_similar_imgs('mod_chi', search_image, imgs_to_be_searched, number_results)

    # Avaliar resultados (porcentagem de classificação correta)
    



  except FileNotFoundError as e:
    print(e)
