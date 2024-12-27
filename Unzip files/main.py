from zipfile import ZipFile

with ZipFile('ai.zip', 'r') as zip_object:
    zip_object.extractall()

print(zip_object.namelist())