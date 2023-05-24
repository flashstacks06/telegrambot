response = [
    {
        "update_id": 38762474,
        "message": {
            "message_id": 79,
            "from": {
                "id": 1630366614,
                "is_bot": False,
                "first_name": "Carlos",
                "last_name": "Bernal",
                "username": "CarlosBernal06",
                "language_code": "en"
            },
            "chat": {
                "id": 1630366614,
                "first_name": "Carlos",
                "last_name": "Bernal",
                "username": "CarlosBernal06",
                "type": "private"
            },
            "date": 1684812109,
            "document": {
                "file_name": "Pieza Carrito.stl",
                "mime_type": "application/vnd.ms-pki.stl",
                "file_id": "BQACAgEAAxkBAANPZGwxTcqwD5ZsXl9MAsaF0dOgekYAAtMCAAIYCFlH_iik4Sm2DDcvBA",
                "file_unique_id": "AgAD0wIAAhgIWUc",
                "file_size": 24884
            }
        }
    },
    {
        "update_id": 38762475,
        "message": {
            "message_id": 80,
            "from": {
                "id": 1630366614,
                "is_bot": False,
                "first_name": "Carlos",
                "last_name": "Bernal",
                "username": "CarlosBernal06",
                "language_code": "en"
            },
            "chat": {
                "id": 1630366614,
                "first_name": "Carlos",
                "last_name": "Bernal",
                "username": "CarlosBernal06",
                "type": "private"
            },
            "date": 1684812116,
            "text": "Hi"
        }
    }
]

# Verificar el tipo de estructura de cada mensaje
for message in response:
    if "document" in message["message"]:
        # Es un mensaje con un documento adjunto
        print("Es un mensaje con documento adjunto")
        # Aquí puedes realizar las operaciones específicas para manejar el mensaje con documento adjunto
        document = message["message"]["document"]
        file_name = document["file_name"]
        mime_type = document["mime_type"]
        # Resto de la lógica para manejar el mensaje con documento adjunto
    else:
        # Es un mensaje de texto
        print("Es un mensaje de texto")
        # Aquí puedes realizar las operaciones específicas para manejar el mensaje de texto
        text = message["message"]["text"]
        # Resto de la lógica para manejar el mensaje de texto