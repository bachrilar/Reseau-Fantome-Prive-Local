import os
import cryptography


###test 1##

from crypto_outils import generate_key , load_key , chiffrer_message , dechiffrer_message , bytes_to_str

generate_key()

key = load_key()

message= input("Type… ")

message_chiffre = chiffrer_message(message, key)

message_dechiffre = dechiffrer_message(message_chiffre, key)
message_dechiffre = bytes_to_str(message_dechiffre)

print(message_dechiffre)

