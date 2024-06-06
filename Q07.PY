def situação (media):
    if media >=6:
        return "aprovado(a)"
    else:
        return "reprovado(a)"
    
nome = input("digite seu nome: ")
disciplina = input("digite a disciplina que você deseja calcular a média: ")
nota1 = int(input("digite nota 1: "))
nota2 = int(input("digite nota2: "))
media = (nota1+nota2)/2
print(f'{nome} está {situação (media)} na disciplina {disciplina}')