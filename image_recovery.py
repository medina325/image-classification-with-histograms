from heuristic import DistanceHeuristic as dh
from util import *
from image import *

# ------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
  images_path, search_image, number_results = get_user_input()

  try:
    filenames = open_images_w_path(images_path)

    search_image = initialize_search_image(search_image, images_path)
    imgs_to_be_searched = initialize_images(search_image.filename, filenames, images_path)

    # Distância Euclidiana
    ed_similar_imgs = search_image.n_most_similar_imgs(dh.ED, imgs_to_be_searched, number_results)

    # Chi-quadrado
    s_chi_similar_imgs = search_image.n_most_similar_imgs(dh.SC, imgs_to_be_searched, number_results)

    # Chi modificado
    # mod_chi_similar_imgs = n_most_similar_imgs('mod_chi', search_image, imgs_to_be_searched, number_results)
    
    accuracy_ed = get_accuracy(search_image, ed_similar_imgs)
    accuracy_sc = get_accuracy(search_image, s_chi_similar_imgs)
      
    print(f'Acurácia ED: {accuracy_ed:.2f}%')
    print(f'Acurácia SC: {accuracy_sc:.2f}%')

  except FileNotFoundError as e:
    print(e)
