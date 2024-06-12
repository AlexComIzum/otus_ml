
alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Алгоритм для шифрования сообщения на английском
def encrypt(message: str, step: int):
    result = ""
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + step
        if i in alfavit_EU:
            result += alfavit_EU[new_mesto]
        else:
            result += i

    return result

# Алгоритм для дешифрования сообщения на английском
def decrypt(message: str, step: int):
    result = ""
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto - step
        if i in alfavit_EU:
            result += alfavit_EU[new_mesto]
        else:
            result += i
    return result

step = int(input('Шаг шифровки: '))
message = input("Сообщение для шифровки: ").upper()

encrypt_result = encrypt(message, step)

print(f" Зашифрованное сообщение: " + encrypt_result)

decrypt_result = decrypt(encrypt_result, step)

print(f" Расшифрованное сообщение: " + decrypt_result)

#step = int(input('Шаг шифровки: '))
#message = input("Сообщение для Дешифровки: ").upper()