from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (600, 400)
Window.clearcolor = (1, 1, 1, 1)

class mybttonAApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=60)
        # layout = BoxLayout(orientation="horizontal")

        btn1 = Button(text="button 1")
        btn2 = Button(text="button 2")
        btn3 = Button(text="button 3")
        btn4 = Button(text="button 4")
        btn5 = Button(text="button 5")

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)

        return layout

mybttonAApp().run()