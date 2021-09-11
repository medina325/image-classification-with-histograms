from image import Image
from heuristic import DistanceHeuristic as dh
from util import *

# ------------------------------------------------------------------------------------------------------------------------------------------

def get_accuracy(search_image: Image, n_most_similar_images: list[Image]):
  """Calculate accuracy of n most similar images obtained"""
  
  search_image_class = search_image.class_name()
  similar_img_classes = [img.class_name() for img in n_most_similar_images]

  print(search_image_class)
  print(similar_img_classes)

  matches = sum([1 for img_class in similar_img_classes if img_class == search_image_class])
  return matches / len(n_most_similar_images) * 100

# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
  number_results, images_path, search_image, as_gray = get_user_input()
  print(as_gray)
  try:
    filenames = open_images_w_path(images_path)

    search_image = initialize_search_image(search_image, images_path, as_gray)
    imgs_to_be_searched = initialize_images(search_image.filename, filenames, images_path, as_gray)
    
    # while True:
    #   print("Escolha o método que deseja usar:")
    #   appro

    # Distância Euclidiana
    ed_similar_imgs = n_most_similar_imgs(dh.ED, search_image, imgs_to_be_searched, number_results)

    # Chi-quadrado
    # s_chi_similar_imgs = n_most_similar_imgs(dh.SC, search_image, imgs_to_be_searched, number_results)

    # Chi modificado
    # mod_chi_similar_imgs = n_most_similar_imgs('mod_chi', search_image, imgs_to_be_searched, number_results)
    
    accuracy_ed = get_accuracy(search_image, ed_similar_imgs)
    # accuracy_sc = get_accuracy(search_image, s_chi_similar_imgs)
      
    print(f'Acurácia ED: {accuracy_ed}%')
    # print(f'Acurácia SC: {accuracy_sc}%')

  except FileNotFoundError as e:
    print(e)
