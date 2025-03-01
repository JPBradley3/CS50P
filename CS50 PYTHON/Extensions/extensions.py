name = input("Give me a filename:").lower()
stripped_name = name.strip()
ext = stripped_name.rsplit('.', 1)[-1]

if ext in ("gif", "png", "jpeg"):
    print(f'image/{ext}')
elif ext in ( "jpg"):
    print(f'image/jpeg')
elif ext in ("pdf", "zip"):
    print(f'application/{ext}')
elif ext == "txt":
    print("text/plain")
else:
    print("application/octet-stream")
