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


# This calls the App creating function
if name == 'main':
    CodesecApp().run()
