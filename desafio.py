nome_valido  = False
salario_valido = False
bonus_valido = False

while nome_valido is  False:
    try:
        nome_user = input("Digite seu nome:")

        if nome_user.isdigit():
            print("você digitou seu nome errado")
        elif nome_user.isspace():
            print("você digitou só espaço")

        elif len(nome_user)==0 :
            print("você não digitou nada ")
        else: 
            nome_valido = True
            print("ok")

    except ValueError as e:
        print(e)
    