"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif image/gif
.jpg image/jpg
.jpeg image/jpeg
.png image/png
.pdf application/pdf 
.txt text/plain
.zip application/zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""

file = input("File name: ").split(".")[1].lower()
image_type = f"image/{file}"
application_type = f"application/{file}"

# match file:
#   case "gif" | "jpg" | "jpeg" | "png":
#     print(image_type)
#   case "pdf" | "zip":
#     print(application_type)
#   case "txt":
#     print("text/plain")
#   case _:
#     print("application/octet-stream")
