from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyCalApp(App):
    def build(self):
        layout = GridLayout(cols=4, rows=5, padding=10, spacing=10)

        AC = Button(text="AC")
        bracket = Button(text="()")
        percent = Button(text="%")
        divison = Button(text="/")
        sevan = Button(text="7")
        eight = Button(text="8")
        nine = Button(text="9")
        multiply = Button(text="*")
        four = Button(text="4")
        five = Button(text="5")
        six = Button(text="6")
        minus = Button(text="-")
        one = Button(text="1")
        two = Button(text="2")
        three = Button(text="3")
        plus = Button(text="+")
        zero = Button(text="0")
        dot = Button(text=".")
        cross = Button(text="X")
        equal = Button(text="=")


        layout.add_widget(AC)
        layout.add_widget(bracket)
        layout.add_widget(percent)
        layout.add_widget(divison)
        layout.add_widget(sevan)
        layout.add_widget(eight)
        layout.add_widget(nine)
        layout.add_widget(multiply)
        layout.add_widget(four)
        layout.add_widget(five)
        layout.add_widget(six)
        layout.add_widget(minus)
        layout.add_widget(one)
        layout.add_widget(two)
        layout.add_widget(three)
        layout.add_widget(plus)
        layout.add_widget(zero)
        layout.add_widget(dot)
        layout.add_widget(cross)
        layout.add_widget(equal)

        return layout

MyCalApp().run()