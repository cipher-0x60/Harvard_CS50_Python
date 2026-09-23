file = input("File name: ").casefold().strip()

media_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

for ext, mime in media_types.items():
    if file.endswith("." + ext):
        print(mime)
        break
else:
    print("application/octet-stream")
