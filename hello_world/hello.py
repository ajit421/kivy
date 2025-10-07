from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

# Setting the window size
Window.size = (600, 400)
Window.clearcolor = (1, 1, 1, 1)

# Creating a class
class MyApp(App):
    def build(self):
        # Creating a label
        label = Label(text="Hello World", font_size="100sp", bold=True, color=(1, 0, 0, 1))
        return label

# Running the app
MyApp().run()