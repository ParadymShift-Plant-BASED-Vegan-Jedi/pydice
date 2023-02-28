thelist = []
suggestions = {}
print("""Welcome to the shopping list app. Here is a list of all of the commands:
listview or lv: View shopping list
listadd or la: Add item to shopping list
listremove or lr: Mark item as bought (it will disappear from the list and can be added again the same way it was added before)
suggest or suggestion: Suggest an item to add based on past history of items""")
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
        litem = litem.strip()
        thelist.append(litem)
        print(f'Item "{litem}" added.')
    elif userprompt == "listremove" or userprompt == "lr":
        ritem = input("Please enter the bought item here: ")
        ritem = ritem.strip()
        if ritem in thelist:
            thelist.remove(ritem)
            print(f'Item "{ritem}" removed.')
        else:
            print("Sorry, we can't seem to find that item. Check your spelling and capitalization and please try again.")
        suggestions[ritem] = suggestions.get(ritem, 0) + 1
    elif userprompt == "suggest" or userprompt == "suggestion":
        if suggestions == {}:
            print("There are currently no items which have been added and removed. To get suggestions, add some items and remove them! More popular items will be suggested first.")
        else:
            keys_sorted_by_count = [k for k, v in sorted(suggestions.items(), key=lambda item: item[1], reverse=True)]
            print(keys_sorted_by_count[0])
            index = 0
            while True:
                decision = input("Would you like another suggestion? Type y/n: ")
                decision = decision.lower()
                decision = decision.strip()
                if decision == "yes" or decision == "y":
                    print(keys_sorted_by_count[index + 1])
                elif decision == "no" or decision == "n":
                    break
            """
            largest_val = 0
            best_suggestion = None
            for suggestion, count in suggestions.items():
                if count > largest_val:
                    largest_val = count
                    best_suggestion = suggestion
            print(best_suggestion)
            while True:
                decision = input("Would you like another suggestion? Type y/n: ")
                decision = decision.lower()
                decision = decision.strip()
                if decision == "yes" or decision == "y":
                    sugglist = []
                    for sugg, num in suggestions.items():
            """
    else:
        print("Error. Command not recognized.")
