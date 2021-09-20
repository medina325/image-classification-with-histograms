# Image Classification with Histograms
First project from the Computer Vision discipline, that aims to recover the N most similar images to a given search image, based on it's histograms.

## Description:
The code is structured in a way to get the images with a fullname "{class}_{filename}.png" - e.g.: c001_001.png is the image "001" from the "c001" class - and based on the most returned classes, determine the class with a given accuracy associated with it.
<!-- O programa está estruturado de forma a receber imagens com nome completo da forma "{class}_{filename}.png" (e.g.: c001_001.png seria a imagem '001" da class "c001"), e com base nas classes retornadas, determinar a porcentagem de classes corretas. -->

## How it works:
The application is CLI based, and it's arguments are:

```bash
  python image_recovery.py path search_image n
```
Where "path" is where the images are stored (including the search image), "search_image" is the fullname of the search image and n is the number of most similar images to be recovered.
Obs.: right now the only path is Vistex and this folder has to be downloaded and extracted from the zip found in this [link](https://www.dropbox.com/s/thh2axm9z4g68kd/Vistex.zip?dl=0).

## Results:
The results are gonna be outputed in the same terminal where the application was executed, giving details such as: classification, accuracy, distance heuristic, channel heuristic, n most similar images and it's classes.

Also figures displaying the search image and it's n most similar images with it's histograms, are gonna be stored in the directory 'results'.