'''
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif - image/gif
.jpg - image/jpeg
.jpeg - image/jpeg
.png - image/png
.pdf - application/pdf
.txt - text/plain
.zip - application/zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
'''

# prompt the user for the name of a file
prompt = input("File name: ").lower().strip().split(".")[-1]

# outputs that file’s media type  if .gif | .jpg | .jpeg | .png | .pdf | .txt | .zip.
if prompt == "gif" or prompt == "jpeg" or prompt == "png":
    print(f"image/{prompt}")
elif prompt == "jpg":
    print("image/jpeg")
elif prompt == "pdf" or prompt == "zip":
    print(f"application/{prompt}")
elif prompt == "txt":
    print("text/plain")
else:
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead
    print("application/octet-stream")