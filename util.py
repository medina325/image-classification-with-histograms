import numpy as np
from skimage import io
import os
import sys
from image import Image

def get_user_input() -> tuple:
  if (len(sys.argv) > 1):
    return (sys.argv[1], sys.argv[2], int(sys.argv[3]))
  else:
    return (input("Digite caminho das imagens:\n"), \
            input("Digite nome da imagem a ser buscada:\n"),\
            int(input("Digite número de imagens semelhantes a serem retornadas:\n")))

def open_images_w_path(path: str) -> list[str]:
  if (not os.path.exists(path)):
    raise FileNotFoundError(f'Caminho {path} não existente.')
  
  return os.listdir(path)

def initialize_images(search_image: str, filenames: list, path: str) -> list[Image]:
  return [Image(f, io.imread(os.path.join(path, f))) for f in filenames if f != search_image]

def initialize_search_image(search_image: str, path: str) -> Image:
  return Image(search_image, io.imread(os.path.join(path, search_image)))
