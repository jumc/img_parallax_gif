# Conversion of static images into parallax animations
## GROUP 1
## Members:

	Bárbara Darques Barros - 7243081
	Juliana de Mello Crivelli - 8909303
	Kaue Ueda Silveira - 7987498
 
## Abstract: 
Starting with a static image we try to retrieve objects at the same depth and separate them into images, each of them representing a different plane from the scene. Then we interpolate the blank spaces caused by the separation, extending the background. In order to produce the parallax effect we overlap the extended planes with slightly different displacements.
 
## How to use it:
1. Inside ```main.py```, change the file path for the source image at ```line 14```, for example:
```python
img = io.imread('input_images/test3.jpg')
```
2. Run it:
```shell
python main.py
```
3. The outpuf animation will be stored at ```./generated_gifs/```

## Image base:
https://drive.google.com/open?id=0BxHj0zhF4J8-TXZYMmp3VDNXbW8

## Sample Results:
![Alt Text](https://github.com//jumc/img_parallax_gif/raw/master/generated_gifs/ready.gif)
![Alt Text](https://github.com//jumc/img_parallax_gif/raw/master/generated_gifs/ready2.gif)
 
 
## References:
https://jaydenossiterghostart.wordpress.com/2016/05/12/the-history-of-the-parallax-effect/ (The History of the Parallax Effect)

http://www.nooganeer.com/his/projects/image-processing/making-a-gif-with-opencv-and-scikit-image-in-python (Making a GIF with OpenCV and Scikit-Image in Python)

http://sweet.ua.pt/pjf/PDF/Ferreira94e.pdf (Interpolation and the discrete Papoulis-Gerchberg Algorithm - Paulo J. S. G. Ferreira)

http://revistas.ua.pt/index.php/revdeti/article/download/1720/1597 (Teaching signal and image reconstruction algorithms -  Paulo J. S. G. Ferreira)
