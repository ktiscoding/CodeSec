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
    
#:kivy 1.0.9

<HomeScreen>:
    name: "HomeScreen"
    canvas:
        Color:
            rgba: 0.496, 0.95, 0.75, 0.9
        Rectangle:
            pos: 0, 0
            size: self.width, self.height

    BoxLayout:
        pos:0,0
        size: root.width, root.height
        orientation: "vertical"
        spacing: 10
        padding: 25
        Label:
            color: (0.168, 0.43, 0.957, 0.55)
            text: "Hand Right"
            font_size: 75
            top: root.top
            center_x: root.width/2
            size_hint: 1, 0.2

        Image:
            source: "hero_1.png"
            center_x: root.width/2
            center_y: root.height/2

        Button:
            id: start
            text: "Start"
            font_size: 50
            center_x: root.width/2
            size: self.width, 100
            size_hint: 1, 0.15
            background_normal: ''
            background_color: 0.75, 0.945, 0.43, 0.85
            background_down: ''
            on_press: start.background_color = 0.422, 0.891, 0.969, 0.85
            on_release:
                root.manager.current = "LevelSelect"


<LevelSelect>:
    name: "LevelSelect"
    canvas:
        Color:
            rgba: 0.496, 0.95, 0.75, 0.9
        Rectangle:
            pos: 0, 0
            size: self.width, self.height
    BoxLayout:
        pos:0,0
        size: root.width, root.height
        orientation: "vertical"
        spacing: 10
        padding: 10
        Label:
            color: (0.168, 0.43, 0.957, 0.55)
            text: "Level Select"
            font_size: 50
            top: root.top
            center_x: root.width/2
            size_hint: 1, 0.15


        GridLayout:
            spacing: 50
            padding: 50
            cols: 3
            rows: 4
            Button:
                id: one
                text: "1"
                font_size: 25
                background_normal: ''
                background_color: 0.75, 0.945, 0.43, 0.85
                background_down: ''
                on_press: one.background_color = 0.422, 0.891, 0.969, 0.85
                on_release:
                    root.manager.current = "LevelOne"
            Button:
                text: "2"
                font_size: 25
            Button:
                text: "3"
                font_size: 25
            Button:
                text: "4"
                font_size: 25
            Button:
                text: "5"
                font_size: 25
            Button:
                text: "6"
                font_size: 25
            Button:
                text: "7"
                font_size: 25
            Button:
                text: "8"
                font_size: 25
            Button:
                text: "9"
                font_size: 25
            Button:
                text: "10"
                font_size: 25
            Button:
                text: "11"
                font_size: 25
            Button:
                text: "12"
                font_size: 25

        Button:
            text: "Next Levels"
            font_size: 30
            size_hint: 1, 0.075


<LevelOne>:
    name: "LevelOne"
    canvas:
        Color:
            rgba: 0.496, 0.95, 0.75, 0.9
        Rectangle:
            pos: 0, 0
            size: self.width, self.height

    BoxLayout:
        pos:0,0
        size: root.width, root.height
        orientation: "vertical"
        spacing: 10
        padding: 10

        Label:
            color: (0.168, 0.43, 0.957, 0.55)
            text: "Try writing"
            font_size: 25
            top: root.top
            center_x: root.width/2
            size_hint: 1, 0.15

        Image:
            source: "Aa.png"
            center_x: root.width/2
            center_y: root.height/2
            size_hint:1, 0.35

        Button:
            id: A
            text: "press here to take picture"
            background_normal: ''
            background_color: 0.75, 0.945, 0.43, 0.85
            on_press: A.background_color = 0.422, 0.891, 0.969, 0.85
            on_release:
                app.camera()
                root.manager.current = "LevelOneImage"


<LevelOneImage>:
    name: "LevelOneImage"
    canvas:
        Color:
            rgba: 0.496, 0.95, 0.75, 0.9
        Rectangle:
            pos: 0, 0
            size: self.width, self.height
    BoxLayout:
        pos:0,0
        size: root.width, root.height
        orientation: "vertical"
        spacing: 10
        padding: 10

        Image:
            source: app.image
            center_x: root.width/2
            center_y: root.height/2
            size_hint: 1, 0.75

        BoxLayout:
            pos:0,0
            size: root.width, root.height
            orientation: "horizontal"
            spacing: 10
            padding: 10

            Button:
                id: Retake
                text: "Retake"
                background_normal: ''
                background_color: 0.75, 0.945, 0.43, 0.85
                on_press: Retake.background_color = 0.422, 0.891, 0.969, 0.85
                on_release:
                    app.camera()
                    root.manager.current = "LevelOneImage2"

            Button:
                id: Check
                text: "Check"
                background_normal: ''
                background_color: 0.75, 0.945, 0.43, 0.85
                on_press: Check.background_color = 0.422, 0.891, 0.969, 0.85

<LevelOneImage2>:
    name: "LevelOneImage2"
    canvas:
        Color:
            rgba: 0.496, 0.95, 0.75, 0.9
        Rectangle:
            pos: 0, 0
            size: self.width, self.height
    BoxLayout:
        pos:0,0
        size: root.width, root.height
        orientation: "vertical"
        spacing: 10
        padding: 10

        Image:
            source: app.image
            center_x: root.width/2
            center_y: root.height/2
            size_hint: 1, 0.75

        BoxLayout:
            pos:0,0
            size: root.width, root.height
            orientation: "horizontal"
            spacing: 10
            padding: 10

            Button:
                id: Retake
                text: "Retake"
                background_normal: ''
                background_color: 0.75, 0.945, 0.43, 0.85
                on_press: Retake.background_color = 0.422, 0.891, 0.969, 0.85
                on_release:
                    app.camera()
                    root.manager.current = "LevelOneImage"

            Button:
                id: Check
                text: "Check"
                background_normal: ''
                background_color: 0.75, 0.945, 0.43, 0.85
                on_press: Check.background_color = 0.422, 0.891, 0.969, 0.85
