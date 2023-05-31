from functools import reduce
from random import randint
def id_prod():
    aux = []
    base = "StreetSneakStore#"
    numbers = ""
    for i in range(10):
        aux.append(f"{randint(1,9)}")
    last_number = f"000{randint(0,9)}"
    return (base + numbers.join(aux) + last_number)

