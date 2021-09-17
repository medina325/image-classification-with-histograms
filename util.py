import numpy as np
import os
import sys
from image import Image

def get_user_input() -> tuple:
  if (len(sys.argv) > 1):
    return (sys.argv[1], sys.argv[2], int(sys.argv[3]))
  else:
    return (
            input("Digite o caminho das imagens:\n"), \
            input("Digite o nome da imagem a ser buscada:\n"),\
            int(input("Digite o número de imagens semelhantes a serem buscadas:\n"))
            )

def open_images_w_path(path: str) -> list[str]:
  if (not os.path.exists(path)):
    raise FileNotFoundError(f'Caminho {path} não existente.')
  
  return os.listdir(path)

def initialize_images(search_image: str, filenames: list, path: str) -> list[Image]:
  return [Image(f, path) for f in filenames if f != search_image]
  
def initialize_search_image(search_image: str, path: str) -> Image:
  return Image(search_image, path)
  
def get_classification(n_most_similar_images: list[Image], n: int) -> dict:
  similar_img_classes = [img.class_name() for img in n_most_similar_images]

  class_frequencies = []
  for similar_class, freq in zip(*np.unique(similar_img_classes, return_counts=True)):
    class_frequencies.append({'class': similar_class, 'freq': freq, 'accuracy': freq * 100 / n})

  return max(class_frequencies, key=lambda x: x['freq'])

