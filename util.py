from skimage import io
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

def get_accuracy(search_image: Image, n_most_similar_images: list[Image]):
  """Calculate accuracy of n most similar images obtained"""
  
  search_image_class = search_image.class_name()
  similar_img_classes = [img.class_name() for img in n_most_similar_images]

  print(search_image_class)
  print(similar_img_classes)

  matches = sum([1 for img_class in similar_img_classes if img_class == search_image_class])
  return matches / (len(n_most_similar_images)-1) * 100
  
def get_classifications():
  pass
