from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyGridLayoutApp(App):
    def build(self):

        layout = GridLayout(rows=2)
        # layout = GridLayout(cols=3, row_force_default=True, row_default_height=100)

        btn1 = Button(text="button 1")
        btn2 = Button(text="button 2")
        btn3 = Button(text="button 3")
        btn4 = Button(text="button 4")

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout 
    

MyGridLayoutApp().run()