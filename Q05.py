hora = int(input("digite um horario entre 0 e 23: "))

if 0 <= hora <=11:
    print("é manhã")
elif 12 <= hora <=17: 
    print("é tarde")
elif 18 <= hora <=23:
    print("é noite")