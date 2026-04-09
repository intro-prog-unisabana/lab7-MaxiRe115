import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, 'r') as archivo:
        password = archivo.read().strip()
    call = caesar_encrypt(password)
    with open(filename, 'w') as documento:
        documento.write(call)



def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    with open(filename, 'r') as f:
        lista= []

        leer= csv.reader(f)
        for row in leer:
            if row:
                lista.append(row)
    for index, row in enumerate(lista):
        if index != 0:
            row[2] = caesar_encrypt(row[2])
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(lista)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
