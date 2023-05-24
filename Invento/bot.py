from urllib import request
import json

bottoken = open("bot_token.txt","r")
bot_token = str(bottoken.read())
bottoken.close()

 
def downloadstl(firstname,file_path):
    """
    This function downloads an STL file from a Telegram bot API and saves it with a given filename.
    
    :param firstname: The first name of the user who requested the STL file download
    :param file_path: The file path of the STL file to be downloaded from the Telegram bot API
    """
    url = 'https://api.telegram.org/file/bot' + bot_token + '/' + file_path
    file_path = firstname + " pieza.stl"
    request.urlretrieve(url, file_path)
    print("Descarga completa. Archivo guardado como: ", file_path)
    
    
def filepath(file_ids):
    """
    This function retrieves the file path of a file from Telegram using its file ID and a bot token.
    
    :param file_ids: The parameter "file_ids" is a string that represents the unique identifier of a
    file in the Telegram server. This identifier is obtained when a user sends a file to a Telegram bot
    :return: the file path of a file with the given file ID using the Telegram Bot API.
    """
            
    try:

        r = request.urlopen('https://api.telegram.org/bot' + bot_token + '/getFile?file_id=' + file_ids)
        
        data = json.loads(r.read().decode())["result"]
        file_path = data['file_path']
        
        return file_path
    except Exception as e:
        print(e)
            
    
def new_messages_bot():
    """
    This is a Python function for a Telegram bot that checks for new messages and handles them
    accordingly, including text messages and messages with attached documents.
    """
    __last = None
    __last_time = None
    while True:
        
        try:

            r = request.urlopen('https://api.telegram.org/bot' + bot_token + '/getUpdates')

            si = json.loads(r.read().decode())["result"]

            si = si[-1]

            if __last == si["message"]["message_id"]:
                continue                
            else:
                __last = si["message"]["message_id"]
            if not __last_time:
                __last_time = si["message"]["date"]
                continue
            elif __last_time < si["message"]["date"]:
                
                __last_time = si["message"]["date"]
            else:
                continue
            
            chat_id = si['message']['chat']['id']
            firstname = si['message']['chat']['first_name']
            
            if "text" in si["message"]:
                # Es un mensaje de texto
                txt = si['message']['text']
                print("Mensaje de texto:")
                print("Nombre:", firstname)
                print("Chat ID:", chat_id)
                print("Texto:", txt)
                # Resto de la lógica para manejar el mensaje de texto
            elif "document" in si["message"]:
                # Es un mensaje con un documento adjunto
                file_ids = si['message']['document']['file_id']
                print("File path: ",filepath(file_ids))
                file_path = filepath(file_ids)
                downloadstl(firstname, file_path)
                
                print("Mensaje con documento adjunto:")
                print("Nombre:", firstname)
                print("Chat ID:", chat_id)
                print("File ID:", file_ids)
            
        except Exception as e:           
            print(e)
            #print("Esperando Mensaje Inicial...")


while True:
    print(new_messages_bot())


