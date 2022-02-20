from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from kivy.uix.popup import Popup
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf
from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import RMSprop
import sklearn
import pandas as pd
from kivy.uix.label import Label

# Class which opens the home screen and everything on it
class HomeScreen(Screen):
    pass

# Class which opens the level select screen
class LevelSelect(Screen):
    pass

# Class which opens the level one screen
class LevelOne(Screen):
    pass

# Class which opens the image screen
class LevelOneImage(Screen):
    pass

# Class which builds the app
class CodesecApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="HomeScreen"))
        sm.add_widget(LevelSelect(name="LevelSelect"))
        sm.add_widget(LevelOne(name="LevelOne"))
        sm.add_widget(LevelOneImage(name="LevelOneImage"))
        sm.add_widget(Success(name="Success"))
        sm.add_widget(Failure(name="Failure"))
        return sm

    # Function to take picture from webcam
    
    def camera(self):
        cap = ""

        # Checks that it can access the camera

        while cap == "":
            cap = cv2.VideoCapture(0)
            if not (cap.isOpened()):
                print('Could not open video device')
                cap = ""

        # Takes a picture from the webcam

        ret, frame = cap.read()
        # cv2.imshow('letter', frame)

        # Saves the image to a file

        cv2.imwrite("letter.png", frame)

        cap.release()

        cv2.destroyAllWindows()
        
    # Function to access whether the letter pictured is correct or not. 

    def machineLearning(self):
        # Load the model
        model = load_model('keras_model.h5', compile=False)

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open('letter.png')
        # resize the image to a 224x224 with the same strategy as in TM2:
        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        # turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        letter = ""
        # run the inference
        prediction = model.predict(data)
        print(prediction)
        if prediction[0][0] > prediction[0][1]:
            letter = "A"
            popup = Popup(title='Result',
                          content=Label(text='Correct!'),
                          size_hint=(None, None), size=(400, 400))
        else:
            letter = "not A"
            popup = Popup(title='Result',
                          content=Label(text='Wrong!'),
                          size_hint=(None, None), size=(400, 400))
        popup.open()


# This calls the App creating function
CodesecApp().run()
