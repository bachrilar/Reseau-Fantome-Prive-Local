import cryptography
from cryptography.fernet import Fernet
import os 
import time



# Genere une Key qui va etre utilise pour verfiier l'accès aux messages
def generate_key():
    " Genere une clé Fernet et la sauvagarde dans key/secret.key"

    key = Fernet.generate_key()
    os.makedirs("key", exist_ok= True)
    with open("key/secret.key" , "wb") as key_file:
        key_file.write(key)
        print("Clé générée et sauvegardé")


# Utilise cette clé pour pouvoir acceder aux messages
def load_key():
    "Charge la key pour utilisation depuis key/secret.key"

    with open("key/secret.key", "rb") as key_file:
        return key_file.read()
    
# fonction qui va etre utilisé dans ecrire_message pour encrypter ce message mais non visible par l'utilisateur

def chiffrer_message(message: str, key: bytes):
    f = Fernet(key)
    return f.encrypt(message.encode())

# fonction qui va etre utilisé dans lire_et_supp_message pour decrypter ce message et le rendre lisible par l'utilisateur
def dechiffrer_message(message : str, key: bytes):
    f = Fernet(key)
    return f.decrypt(message)

# fonction qui nettoie l'ecirtutre binaire et rend plus lisible
def bytes_to_str(data: bytes) -> str:
    return data.decode("utf-8")

# fonction qui va ecrire le message en str et le stocker dans un dossier partagé accesible par les 2 utilisateurs 
# toujours besoin de key pour fonctionner
# f.write va permettre de l'ecrire de facon encrypte pour assurer la confidentialité de ce message

def ecrire_message(message: str, chemin_fichier="comm/message.enc"):
    key = load_key()
    encrypted = chiffrer_message(message, key)
    os.makedirs("comm", exist_ok=True)
    with open(chemin_fichier, "wb") as f:
        f.write(encrypted)


# fonction qui va lire et supprimer le message une fois lu 

def lire_et_supp_message(chemin_fichier="comm/message.enc"):
    if not os.path.exists(chemin_fichier):
        print("Aucun message trouvé.")
        return

    key = load_key()
    with open(chemin_fichier, "rb") as f:
        encrypted = f.read()
    
    try:
        decrypted = dechiffrer_message(encrypted, key)
        print("Message reçu :", bytes_to_str(decrypted))
    except Exception as e:
        print("Erreur de déchiffrement :", e)

    os.remove(chemin_fichier)


# cette fonction permet d'ecrire un message vers B et verifier si B a envoyé des messages. Boucle While True a l'infini pour envoyer des messages a l'infini 


def station_a():
    print("En ligne : ")
    while True:
        message = input("A: Message à envoyer : ")
        ecrire_message(message , "comm/messageA_B.enc")
        print("Envoyé")

        while True:
            if os.path.exists("comm/messageB_A.enc"):
                print("Nouveau message reçu : ")
                lire_et_supp_message("comm/messageB_A.enc")
                break
            time.sleep(1)

# Même chose mais pour B. Cette fonction permet d'ecrire un message vers A et verifier si A a envoyé des messages. Boucle While True a l'infini pour envoyer des messages a l'infini 

def station_b():
    print("En ligne")
    while True:
        while True:
            if os.path.exists("comm/messageA_B.enc"):
                print("Nouveau message : ")
                lire_et_supp_message("comm/messageA_B.enc")

                reponse = input("Ecrire… ")
                ecrire_message(reponse, "comm/messageB_A.enc")
                print("Envoyé")
                break
            time.sleep(1)
