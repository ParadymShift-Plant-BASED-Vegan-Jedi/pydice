from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class ShoppingList(App):
    def build(self):
        self.thelist = []
        self.suggestions = {}
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
    
    def additem(self, instance):
        self.userinput.text = self.userinput.text.strip()
        if self.userinput.text not in self.thelist:
            self.thelist.append(self.userinput.text)
            self.intro.text = f'Item "{self.userinput.text}" added to shopping list.'
            self.button.unbind(on_press=self.additem)
            self.button.bind(on_press=self.callback)
        else:
            self.intro.text = "That item is already in your list!"
            self.button.unbind(on_press=self.additem)
            self.button.bind(on_press=self.callback)
    
    def removeitem(self, instance):
        if self.userinput.text in self.thelist:
            self.thelist.remove(self.userinput.text)
            self.intro.text = f'Item "{self.userinput.text}" removed from shopping list.'
            self.suggestions[self.userinput.text] = self.suggestions.get(self.userinput.text, 0) + 1
            self.button.unbind(on_press=self.removeitem)
            self.button.bind(on_press=self.callback)
        else:
            self.intro.text = "Sorry, we could not find that item in your list! \nPlease check spelling/capitalization and try again"
            self.button.unbind(on_press=self.removeitem)
            self.button.bind(on_press=self.callback)
    
    def suggest(self, instance):
        self.userinput.text = self.userinput.text.lower()
        self.userinput.text = self.userinput.text.strip()
        if self.userinput.text == "yes" or self.userinput.text == "y":
            try:
                self.intro.text = f"{self.keys_sorted_by_count[self.index + 1]}\nWould you like another suggestion? Type y/n:"
                self.index = self.index + 1
            except:
                self.intro.text = "No more suggestions."
                self.button.unbind(on_press=self.suggest)
                self.button.bind(on_press=self.callback)
        elif self.userinput.text == "no" or self.userinput.text == "n":
            self.intro.text = "Okay!"
            self.button.unbind(on_press=self.suggest)
            self.button.bind(on_press=self.callback)

    def callback(self, instance):
        self.userinput.text = self.userinput.text.lower()
        self.userinput.text = self.userinput.text.strip()
        if self.userinput.text == "lv" or self.userinput.text == "listview":
            if self.thelist == []:
                self.intro.text = "There are no items in your list. \nAdd new items with the `la` command."
            else:
                self.intro.text = ""
                for item in self.thelist:
                    self.intro.text += f"- {item}\n"
        elif self.userinput.text == "la" or self.userinput.text == "listadd":
            self.intro.text = "Type the item you would like to add."
            self.button.unbind(on_press=self.callback)
            self.button.bind(on_press=self.additem)
        elif self.userinput.text == "lr" or self.userinput.text == "listremove":
            self.intro.text = "Type the item you would like to remove."
            self.button.unbind(on_press=self.callback)
            self.button.bind(on_press=self.removeitem)
        elif self.userinput.text == "vc" or self.userinput.text == "viewcommands":
            self.intro.text = """Welcome to the shopping list app.
Here is a list of all of the commands:
listview or lv: View shopping list
listadd or la: Add item to shopping list
listremove or lr: Mark item as bought 
(it will disappear from the list and can 
be added again the same way it was added before)
suggest or suggestion: Suggest an item to add 
based on past history of items
viewcommands or vc: Show this list of commands"""
        elif self.userinput.text == "suggest" or self.userinput.text == "suggestion":
            if self.suggestions == {}:
                self.intro.text = "There are currently no items which have been added and removed.\nTo get suggestions, add some items and remove them!\nMore popular items will be suggested first."
            else:
                self.index = 0
                self.keys_sorted_by_count = [k for k, v in sorted(self.suggestions.items(), key=lambda item: item[1], reverse=True)]
                self.intro.text = f"{self.keys_sorted_by_count[0]}\nWould you like another suggestion? Type y/n:"
                self.button.unbind(on_press=self.callback)
                self.button.bind(on_press=self.suggest)
        else:
            self.intro.text = "Error. Command not recognized."
            



if __name__ == '__main__':
    app = ShoppingList()
    app.run()
