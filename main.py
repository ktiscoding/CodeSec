from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2

# Class which opens the home screen and everything on it
class HomeScreen(Screen):
    pass


class LevelSelect(Screen):
    pass


class LevelOne(Screen):
    pass


class LevelOneImage(Screen):
    pass


class LevelOneImage2(Screen):
    pass


# Class which builds the app
class CodesecApp(App):
    def build(self):
        image = ("letter.png")
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="HomeScreen"))
        sm.add_widget(LevelSelect(name="LevelSelect"))
        sm.add_widget(LevelOne(name="LevelOne"))
        sm.add_widget(LevelOneImage(name="LevelOneImage"))
        sm.add_widget(LevelOneImage2(name="LevelOneImage2"))
        return sm

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
        #cv2.imshow('letter', frame)

        # Saves the image to a file

        cv2.imwrite("letter.png", frame)

        cap.release()

        cv2.destroyAllWindows()
        
    def machineLearning(self):
        # Load the model
        model = load_model('keras_model.h5', compile=False)

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open('letter.png')
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        letter=""
        # run the inference
        prediction = model.predict(data)
        print(prediction)
        if prediction[0][0]>prediction[0][1]:
            letter="A"
        else:
            letter="not A"
        print(letter)


# This calls the App creating function
if name == 'main':
    CodesecApp().run()
