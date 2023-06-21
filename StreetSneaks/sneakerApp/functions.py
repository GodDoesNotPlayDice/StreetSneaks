from random import randint, choices
import string
def id_prod():
    aux = []
    base = "StreetSneakStore#"
    numbers = ""
    for i in range(10):
        aux.append(f"{randint(1,9)}")
    last_number = f"000{randint(0,9)}"
    return (base + numbers.join(aux) + last_number)



def generar_id_boleta():
    parte_random = ''.join(choices(string.digits, k=5))
    random2 = ''.join(choices(string.digits, k=5))
    id_boleta = f"StreetSneaks#Boleta@{parte_random}-{random2}"
    return id_boleta