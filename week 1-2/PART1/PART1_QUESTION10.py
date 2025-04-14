Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''This program displays the unicode encoding of the user's name'''
"This program displays the unicode encoding of the user's name"
>>> name="Gyunish"
>>> unicode=[ord(char) for char in name]
>>> print("The unicode encoding for each character in",name,"is",unicode)
The unicode encoding for each character in Gyunish is [71, 121, 117, 110, 105, 115, 104]
