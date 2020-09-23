# example of zoom image augmentation
from numpy import expand_dims
from keras_preprocessing.image import load_img
from keras_preprocessing.image import img_to_array
from keras_preprocessing.image import image_data_generator
from cv2 import VideoCapture
from cv2 import namedWindow
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import imwrite
from cv2 import CAP_GSTREAMER
import os

print("Nombre: ")
name = input()

directory = name
parent_dir = "Photos"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
dir = parent_dir + "/" + name
img_n = name + ".png"

cam = VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv flip-method=rotate-180 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , CAP_GSTREAMER)
namedWindow("test")
img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    imshow("test", frame)
    k = waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = img_n.format(img_counter)
        imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        break
cam.release()
destroyAllWindows()

# load the image
img = load_img(img_n)
# convert to numpy array
data = img_to_array(img)
# expand dimension to one sample
samples = expand_dims(data, 0)
# create image data augmentation generator
datagen = image_data_generator.ImageDataGenerator(zoom_range=[0.5,1.0])
# prepare iterator
it = datagen.flow(samples, batch_size=1, save_to_dir= dir)
# create image data augmentation generator
for i in range(10):
	# generate batch of images
	batch = it.next()
	# convert to unsigned integers for viewing
	image = batch[0].astype('uint8')
datagen = image_data_generator.ImageDataGenerator(rotation_range=90)
# prepare iterator
it = datagen.flow(samples, batch_size=1, save_to_dir= dir)
# create image data augmentation generator
for i in range(10):
	# generate batch of images
	batch = it.next()
	# convert to unsigned integers for viewing
	image = batch[0].astype('uint8')
datagen = image_data_generator.ImageDataGenerator(horizontal_flip=True)
# prepare iterator
it = datagen.flow(samples, batch_size=1, save_to_dir= dir)
# create image data augmentation generator
for i in range(10):
	# generate batch of images
	batch = it.next()
	# convert to unsigned integers for viewing
	image = batch[0].astype('uint8')
datagen = image_data_generator.ImageDataGenerator(shear_range= 30)
# prepare iterator
it = datagen.flow(samples, batch_size=1, save_to_dir= dir)
# generate samples and plot
for i in range(10):
	# generate batch of images
	batch = it.next()
	# convert to unsigned integers for viewing
	image = batch[0].astype('uint8')
os.remove(img_n)