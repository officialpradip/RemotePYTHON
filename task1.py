import zipfile

target = 'demo.zip'
print("Unzipping starting")

root = zipfile.ZipFile(target)
root.extractall(r"C:\Users\pradip\Desktop\result")

root.close()
print("\n Complete unzipping")
