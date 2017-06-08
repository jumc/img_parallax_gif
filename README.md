# img_parallax_gif
GROUP 1
Members:
	Bárbara Darques Barros - 7243081
	Juliana de Mello Crivelli - 8909303
	Kaue Ueda Silveira - 7987498
 
Title: Conversion of static images into parallax animations
 
Abstract: Starting with a static image we try to retrieve objects at the same depth and separate them into images, each of them representing a different plane from the scene. Then we interpolate the blank spaces caused by the separation, extending the background. In order to produce the parallax effect we overlap the extended planes with slightly different displacements.
 
Roadmap:
Identify and separate planes
	We intend to detect borders and transitions applying Fourier Transform over the original image.
Interpolate the retrieved planes
Following the professor suggestion, we intend to use the Papoulis-Gerchberg in order to fill the areas covered by the foreground planes, avoiding blanks spaces to be displayed to the viewer.
Overlap new images with different relative positions
	The extended planes generated in the previous steps will be overlapped with a variable position difference, generating various frames that once put together simulate the relative movement of the scene objects.
Generate gif
We’ll use the OpenCV and Matplotlib modules in order to convert the output frames into a gif animation, making use of the function matplotlib.animation.ArtistAnimation.
 
	
 
 
References:
https://jaydenossiterghostart.wordpress.com/2016/05/12/the-history-of-the-parallax-effect/ (The History of the Parallax Effect)
http://www.nooganeer.com/his/projects/image-processing/making-a-gif-with-opencv-and-scikit-image-in-python (Making a GIF with OpenCV and Scikit-Image in Python)
http://sweet.ua.pt/pjf/PDF/Ferreira94e.pdf (Interpolation and the discrete Papoulis-Gerchberg Algorithm - Paulo J. S. G. Ferreira)
revistas.ua.pt/index.php/revdeti/article/download/1720/1597 (Teaching signal and image reconstruction algorithms -  Paulo J. S. G. Ferreira)
