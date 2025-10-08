from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window

# Setting the window size
Window.size = (600, 400)
Window.clearcolor = (1, 1, 1, 1)

class MyImageApp(App):
    def build(self):
        img = Image(source="image.jpg", size_hint=(None, None),
                    width=200, height=100, pos_hint={"center_x":0.7, "center_y":0.5})
        return img
    
MyImageApp().run()