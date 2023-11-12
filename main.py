import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# hello


class Android_grid(GridLayout):
    def __init__(self, **kwargs):
        super(Android_grid, self).__init__()
        self.rows = 6

        self.add_widget(Label(text="Enter Name:"))

        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Enter Gender:"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.add_widget(Label(text="Enter Age:"))
        self.s_age = TextInput()
        self.add_widget(self.s_age)

        self.press = Button(text="Click Me")
        self.press.bind(on_press=self.clickme)
        self.add_widget(self.press)
        

    def clickme(self, instance):
        print("Name is : "+self.s_name.text)
        print("Gender is : "+self.s_gender.text)
        print("Age is : "+self.s_age.text)



class Android_app(App):
    def build(self):

        return Android_grid()
    

if __name__ == "__main__":
    Android_app().run()