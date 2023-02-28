from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class ShoppingList(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.intro = Label(
                     text = """Welcome to the shopping list app.
Here is a list of all of the commands:
listview or lv: View shopping list
listadd or la: Add item to shopping list
listremove or lr: Mark item as bought 
(it will disappear from the list and can 
be added again the same way it was added before)
suggest or suggestion: Suggest an item to add 
based on past history of items
viewcommands or vc: Show this list of commands""",
                      font_size = 18
                       )
        self.window.add_widget(self.intro)

        self.userinput = TextInput(
                         multiline = False,
                         padding_y = (20, 20),
                         size_hint = (1, 0.2)
                         )

        self.window.add_widget(self.userinput)

        self.button = Button(
                      text = "Enter Command",
                      size_hint = (1, 0.2),
                      bold = True,
                      background_color = '#ba0606',
                      background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.intro.text = "Test Complete."



if __name__ == '__main__':
    app = ShoppingList()
    app.run()
