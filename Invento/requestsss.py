import requests

url = "https://api.telegram.org/file/bot5949530712:AAEXYbn4ZKXcZnytdYi4JYv59WShJgrN7SQ/documents/file_1.stl"
file_path = "file_1.stl"

response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print("Descarga completa. Archivo guardado como", file_path)
else:
    print("Error al descargar el archivo. Código de estado:", response.status_code)
