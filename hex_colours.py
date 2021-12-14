HEX_COLOURS = {"Amber": "#ffbf00", "Aqua": "#00ffff", "Beige": "#9f8170", "Beaver": "#f5f5dc", "Black": "#000000",
               "Blue": "#0018a8", "Caml": "#c19a6b", "Denim": "#1560bd", "Ebony": "#555d50", "Fawn": "#e5aa70"}

print(HEX_COLOURS)

color_choice = input("What color would you chose? ")
while color_choice != "":
    if color_choice in HEX_COLOURS:
        print(f"You have chose {color_choice} as your color, the code of this color is {HEX_COLOURS[color_choice]}")
        color_choice = input("What color would you chose? ")
    else:
        print("Invalid input")
        color_choice = input("What color would you chose? ")
