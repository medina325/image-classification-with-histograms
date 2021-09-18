from heuristic import DistanceHeuristic as dh
from util import *
from image import *

# ------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
  images_path, search_image, number_results = get_user_input()

  try:
    filenames = get_imgs_filenames(images_path)

    search_image = initialize_search_image(search_image, images_path)
    imgs_to_be_searched = initialize_images(search_image.filename, filenames, images_path)
  
    results = search_image.n_most_similar_imgs(imgs_to_be_searched, number_results)
    
    for result in results:
      print(f"Distance Heuristic: {result['distance_heuristic'].value} - Channel Heuristic: {result['channel_heuristic']}")
      print(f"Classification: {result['classification']} - Accuracy: {result['accuracy']:.2f} %")
      print(f" N Most Similar Images: {[img.filename for img in result['n_most_similar']]}")
      print(f" N Most Similar Classes: {[img.class_name() for img in result['n_most_similar']]}")

      print(40 * '-')

      save_result_figures(result, number_results)

  except FileNotFoundError as e:
    print(e)
