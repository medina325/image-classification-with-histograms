import numpy as np
from skimage import io
import os
import sys
from image import Image

# ------------------------------------------------------------------------------------------------------------------------------------------
def open_images_w_path(path: str) -> list[str]:
  if (not os.path.exists(path)):
    raise FileNotFoundError(f'Caminho {path} não existente.')
  
  return os.listdir(path)

def initialize_images(search_image: str, files: list, path: str) -> list[Image]:
  return [Image(file, io.imread(f'{path}/{file}')) for file in files if file != search_image]
  
def initialize_search_image(search_image, path) -> Image:
  return Image(search_image, io.imread(f'{path}/{search_image}'))

# ------------------------------------------------------------------------------------------------------------------------------------------
def euclidian_distance(pe, pi) -> float:
  return np.sum(np.square(pe - pi))

def square_chi(pe, pi) -> float:
  pass

# TODO
# Criar consts para dizer qual método usar para calcular as distâncias

def most_similar_imgs(approach, search_img: Image, imgs_to_be_searched: list[Image], number_results: int) -> list[str]:  
  for img in imgs_to_be_searched:
    img.calc_pdfs_distances(search_img.pdfs, approach)

  return sorted(imgs_to_be_searched, key=lambda x: x.distances['red'])[:number_results]

# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
  # Entradas:
  # - Imagem de busca
  # - Caminho de uma pasta contendo imagens a serem buscadas
  # - Inteiro n que indica o número de imagens parecidas a serem retornadas

  print("Syntax to use this tool:\n")
  print("python image_recovery.py <images_path> <search_image_name> <number_of_images_to_be_recovered>", end="\n\n")

  if (len(sys.argv) > 1):
    images_path = sys.argv[1]
    search_image = sys.argv[2]
    number_results = int(sys.argv[3])
  else:
    images_path = input("Digite caminho das imagens:\n")
    search_image = input("Digite nome da imagem a ser buscada:\n")
    number_results = int(input("Digite número de imagens semelhantes a serem retornadas:\n"))
  
  try:
    # Initialize all images with it's histograms and pdfs
    files = open_images_w_path(images_path)

    search_image = initialize_search_image(search_image, images_path)
    imgs_to_be_searched = initialize_images(search_image.filename, files, images_path)
    
    # Faça a recuperação das imagens usando diferentes métodos
    # Distância Euclidiana
    ed_similar_imgs = most_similar_imgs(euclidian_distance, search_image, imgs_to_be_searched, number_results)
    
    # Chi-quadrado
    # s_chi_similar_imgs = most_similar_imgs('square_chi', search_image, imgs_to_be_searched, number_results)

    # Chi modificado
    # mod_chi_similar_imgs = most_similar_imgs('mod_chi', search_image, imgs_to_be_searched, number_results)

    # TODO
    # Avaliar resultados (porcentagem de classificação correta)
    filenames = [img.filename for img in ed_similar_imgs]
    print(filenames)

  except FileNotFoundError as e:
    print(e)
