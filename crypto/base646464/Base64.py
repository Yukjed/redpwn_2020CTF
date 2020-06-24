#Multiple Base64 Conversions in Python
import base64

file = open("cipher.txt", "r")
base64String = file.read()

for i in range(25):
    base64String = base64.b64decode(base64String)
   
print(base64String)

