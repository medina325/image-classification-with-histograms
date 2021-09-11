import numpy as np
from image import Image
from heuristic import DistanceHeuristic as dh
from util import open_images_w_path,\
                 initialize_images,\
                 initialize_search_image,\
                 get_user_input

# ------------------------------------------------------------------------------------------------------------------------------------------

def n_most_similar_imgs(approach, search_img: Image, imgs_to_be_searched: list[Image], number_results: int) -> list[Image]:  
  for img in imgs_to_be_searched:
    img.calc_pdfs_distances(search_img.pdfs, approach)
  
  return sorted(imgs_to_be_searched, key=lambda x: (x.distances['red'] + x.distances['green'] + x.distances['blue']) / 3)[:number_results]

def get_accuracy(search_image: Image, n_most_similar_images: list[Image]):
  """Calculate accuracy of n most similar images obtained"""
  
  search_image_class = search_image.class_name()
  similar_img_classes = [img.class_name() for img in n_most_similar_images]

  matches = 0
  for img_class in similar_img_classes:
    if img_class == search_image_class:
      matches += 1

  return matches / len(n_most_similar_images) * 100

# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
  images_path, search_image, number_results = get_user_input()
  
  try:
    filenames = open_images_w_path(images_path)

    search_image = initialize_search_image(search_image, images_path)
    imgs_to_be_searched = initialize_images(search_image.filename, filenames, images_path)
    
    # Distância Euclidiana
    ed_similar_imgs = n_most_similar_imgs(dh.ED, search_image, imgs_to_be_searched, number_results)

    # Chi-quadrado
    # s_chi_similar_imgs = n_most_similar_imgs('square_chi', search_image, imgs_to_be_searched, number_results)

    # Chi modificado
    # mod_chi_similar_imgs = n_most_similar_imgs('mod_chi', search_image, imgs_to_be_searched, number_results)
    
    accuracy = get_accuracy(search_image, ed_similar_imgs)
    
    print([img.distances for img in ed_similar_imgs], sep="\n" ,end="\n")
    print(f'{accuracy}%')

  except FileNotFoundError as e:
    print(e)
