from skimage import io
import os
import sys
from image import *

def get_user_input() -> tuple:
  if (len(sys.argv) > 1):
    return (int(sys.argv[1]), sys.argv[2], sys.argv[3], bool(int(sys.argv[4])))
  else:
    return (int(input("Digite o número de imagens semelhantes a serem buscadas:\n"))),\
            input("Digite o caminho das imagens:\n"), \
            input("Digite o nome da imagem a ser buscada:\n"),\
            bool(input("Digite se a imagem deve ser tratada em tons de cinza [0 - Colorida, 1 - Cinza]:\n"))

def open_images_w_path(path: str) -> list[str]:
  if (not os.path.exists(path)):
    raise FileNotFoundError(f'Caminho {path} não existente.')
  
  return os.listdir(path)

def initialize_images(search_image: str, filenames: list, path: str, as_gray: bool) -> list[Image]:
  if as_gray:
    return [GrayImage(f, io.imread(os.path.join(path, f), as_gray=True)) for f in filenames if f != search_image]
    
  return [ColoredImage(f, io.imread(os.path.join(path, f), as_gray=False)) for f in filenames if f != search_image]
  
def initialize_search_image(search_image: str, path: str, as_gray: bool) -> Image:
  if as_gray:
    return GrayImage(search_image, io.imread(os.path.join(path, search_image), as_gray=True))

  return ColoredImage(search_image, io.imread(os.path.join(path, search_image), as_gray=False))

def get_accuracy(search_image: Image, n_most_similar_images: list[Image]):
  """Calculate accuracy of n most similar images obtained"""
  
  search_image_class = search_image.class_name()
  similar_img_classes = [img.class_name() for img in n_most_similar_images]

  print(search_image_class)
  print(similar_img_classes)

  matches = sum([1 for img_class in similar_img_classes if img_class == search_image_class])
  return matches / len(n_most_similar_images) * 100
  