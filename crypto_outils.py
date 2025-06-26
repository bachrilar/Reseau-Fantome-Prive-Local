import cryptography
from cryptography.fernet import Fernet
import os 

def generate_key():
    " Genere une clé Fernet et la sauvagarde dans key/secret.key"

    key = Fernet.generate_key()
    os.makedirs("key", exist_ok= True)
    with open("key/secret.key" , "wb") as key_file:
        key_file.write(key)
        print("Clé générée et sauvegardé")



def load_key():
    "Charge la key pour utilisation depuis key/secret.key"

    with open("key/secret.key", "rb") as key_file:
        return key_file.read()

def chiffrer_message(message: str, key: bytes):
    f = Fernet(key)
    return f.encrypt(message.encode())

def dechiffrer_message(message : str, key: bytes):
    f = Fernet(key)
    return f.decrypt(message)

def bytes_to_str(data: bytes) -> str:
    return data.decode("utf-8")

