from matplotlib import pyplot as plt
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

def get_imgs_filenames(path: str) -> list[str]:
  if (not os.path.exists(path)):
    raise FileNotFoundError(f'Caminho {path} não existente.')
  
  return os.listdir(path)

def initialize_images(search_image: str, filenames: list, path: str) -> list[Image]:
  return [Image(f, path) for f in filenames if f != search_image]
  
def initialize_search_image(search_image: str, path: str) -> Image:
  return Image(search_image, path)

def save_result_figures(result: dict, n: int) -> None:
  if (not os.path.exists('results')):
    os.mkdir('results')

  fig = plt.figure(figsize=(15, 15))
  axes = []
  rows = columns = n//2

  for i, img in zip(range(n), result['n_most_similar']):
    axes.append(fig.add_subplot(rows, columns, i + 1 ))
    axes[-1].set_title('Class: ' + img.class_name())
    plt.imshow(img.contents['rgb'])
  
  plt.savefig(f"results/results_{result['distance_heuristic']}_and_{result['channel_heuristic']}.png")

def print_result(result: dict) -> None:
  print(f"Distance Heuristic: {result['distance_heuristic'].value} - Channel Heuristic: {result['channel_heuristic']}")
  print(f"Classification: {result['classification']} - Accuracy: {result['accuracy']:.2f} %")
  print(f" N Most Similar Images: {[img.filename for img in result['n_most_similar']]}")
  print(f" N Most Similar Classes: {[img.class_name() for img in result['n_most_similar']]}")

  print(40 * '-')
