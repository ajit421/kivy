from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

# Window settings
Window.size = (600, 400)
Window.clearcolor = (1, 0.5, 0, 1)

class MyTextInputApp(App):
    def build(self):
        # Create TextInputs
        self.email = TextInput(hint_text="Enter your Email ID", multiline=False)
        self.password = TextInput(hint_text="Enter your Password", multiline=False, password=True)

        # Create Button
        self.submit_btn = Button(text="Submit")
        self.submit_btn.bind(on_press=self.submit)

        # Layout
        layout = BoxLayout(orientation="vertical", padding=100, spacing=20)
        layout.add_widget(self.email)
        layout.add_widget(self.password)
        layout.add_widget(self.submit_btn)

        return layout

    def submit(self, obj):
        # Access text correctly
        print(f"Email: {self.email.text}")
        print(f"Password: {self.password.text}")

# Run app
MyTextInputApp().run()
