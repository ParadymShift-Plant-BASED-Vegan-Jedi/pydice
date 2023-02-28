thelist = []
print("""Welcome to the shopping list app. Here is a list of all of the commands:
listview or lv: View shopping list
listadd or la: Add item to shopping list
itembought or ib: Mark item as bought (it will disappear from the list and can be added again the same way it was added before)""")
while True:
    userprompt = input("Enter Command Here: ")
    userprompt = userprompt.lower()
    userprompt = userprompt.strip()
    if userprompt == "listview" or userprompt == "lv":
        if thelist == []:
            print("There are no items in your list! Add some items with `listadd` or `la`")
        else:
            for li in thelist:
                print("- " + li)
    elif userprompt == "listadd" or userprompt == "la":
        litem = input("Please enter your list item here: ")
        thelist.append(litem)
        print(f'Item "{litem}" added.')
    elif userprompt == "itembought" or userprompt == "ib":
        ritem = input("Please enter the bought item here: ")
        if ritem in thelist:
            thelist.remove(ritem)
            print(f'Item "{ritem}" removed.')
        else:
            print("Sorry, we can't seem to find that item. Check your spelling and capitalization and please try again.")
    else:
        print("Error. Command not recognized.")
