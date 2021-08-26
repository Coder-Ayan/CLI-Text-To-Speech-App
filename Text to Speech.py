# importing the pyttsx library
import pyttsx3
  
# initialisation
engine = pyttsx3.init()

# Taking input of the file path
file = input("Enter the path of the txt file: ")

# Trying to open the file
try:
    f = open(file)
except FileNotFoundError:
    raise FileNotFoundError("The file does not found")

# Reading the content of the file
content = f.read()
# Closing the file
f.close()

# testing
pyttsx3.speak(str(content))
