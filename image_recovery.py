import numpy as np
from skimage import io
import os
from zipfile import ZipFile
import re
import matplotlib.pyplot as plt

def get_images():
  if (not os.path.exists('Vistex')):
    with ZipFile('Vistex.zip', 'r') as zip:
      for filename in zip.namelist():
        if re.match(r'Vistex/.+\.png', filename):
          zip.extract(filename)
    zip.close()

  files = os.listdir('Vistex')
  # imgs = [io.imread(f'Vistex/{file}') for file in files]
  imgs = [{'filename': file, 'contents': io.imread(f'Vistex/{file}')} for file in files]
  
  return imgs

"""
  Returns dictionary relating images to it's histograms
"""
def make_histograms(imgs):
  imgs_w_histograms = []

  for img in imgs[:2]:
    print("oi")
    histogram_r = histogram_g = histogram_b = np.zeros(256, np.uint)
    w, h, _ = img['contents'].shape
    img_np = np.array(img['contents'], np.uint8)
    
    for x in range(w):
      for y in range(h):
        histogram_r[img_np[x][y][0]] += 1
        histogram_g[img_np[x][y][1]] += 1
        histogram_b[img_np[x][y][2]] += 1

    imgs_w_histograms.append({
      **img,
      'histogram': {
        'red': histogram_r,
        'green': histogram_g,
        'blue': histogram_b
      }
    })
    
  plot_histogram(histogram_r, 'r')

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

  # 1. Abra o zip e coloque as imagens em uma lista
  imgs = get_images()

  # 2. Construa histograma de cada imagem
  histogram = make_histograms(imgs)
  # 3. Obtenha PDF (Probability Density Function) para cada imagem

  # 4. Faça a recuperação das imagens usando diferentes métodos
