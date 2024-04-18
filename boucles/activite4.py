def decode_message(message_code):
    # Diviser la chaîne de nombres en une liste de nombres
    nombres = message_code.split()
    
    # Convertir chaque nombre en sa valeur ASCII correspondante puis en caractère
    message_decode = ''.join(chr(int(nombre)) 
    for nombre in nombres)
    
    return message_decode

# Demander à l'utilisateur d'entrer le message encodé
message_code = input("Entrez le message encodé (séparé par des espaces) : ")

# Appeler la fonction pour décoder le message
message_decode = decode_message(message_code)
print("Message décodé est :", message_decode)
