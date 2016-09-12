"""Color picker
by Simon Richards"""

color_codes = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4", "azure": "#f0ffff",
               "beige": "#f5f5dc", "black": "#000000", "blue": "#0000ff", "blueviolet": "#8a2be2"}
color = input("Please enter the color you would like to see the code for: ").lower()
while color != "":
    if color in color_codes:
        print(color_codes[color])
    else:
        print("invalid Color")
    color = input("Please enter the color you would like to see the code for: ")
