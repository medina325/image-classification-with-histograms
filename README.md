# Image Classification with Histograms
First project from the Computer Vision discipline.

## Description:
The work consists in finding the N Most Similar Images to a given Search Image, based on it's histograms, and determine the class of the Search Image based on the most frequent class in the N most similar set of Images.

The images being used come from the Vistex set, where every image is named as "{class}_{filename}.png" - e.g.: c001_001.png is the image "001" from the "c001" class.

Given a Search Image, the program is going to get the N Most Similar Images with different heuristics, and output the results in terminal and the images in the /results directory.

## Key Concepts:
- Search Image: reference image to get the n most similar images from
- Target Images: set of images to be searched (search image is not a part of it)
- N Most Similar Images: subset of Target Images set, with only the N most similar images to the Search Image 
- Channel: can be gray, red, green and blue
- Histogram: an Image's histogram (every Image has 1 histogram for every channel)
- Probability Density Function (PDF): an Image has 1 PDF for each one of it's histograms
- Distance Heuristic: heuristic used to calculate the distances between 2 different PDFs 
- Channels Heuristic: heuristic used to combine the channels
- Classification: from the N most similar images, the most frequent class is used to determine the classification
- Classification Accuracy

## How it works:
The application is CLI based, and it's arguments are:

```bash
  python image_recovery.py path search_image n
```
Where "path" is where the images are stored (including the search image), "search_image" is the fullname of the search image and n is the number of most similar images to be recovered.

Obs.: right now the only path is Vistex and this folder has to be downloaded and extracted from the zip found in this [link](https://www.dropbox.com/s/thh2axm9z4g68kd/Vistex.zip?dl=0).

## Results:
The results are gonna be outputed in the same terminal where the application was executed, giving details such as: classification, classification accuracy, distance heuristic, channels heuristic, n most similar images and it's classes.

Also figures displaying the search image and it's n most similar images with it's histograms, are gonna be stored in the directory 'results'.
