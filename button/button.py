from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        # Creating a button
        button = Button(text="Click Me", size_hint=(0.4, 0.3), pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size="44sp", on_press=self.btn_click)
        return button
    
    def btn_click(self, btn):
        print("Button Clicked")

# Running the app
ButtonApp().run()