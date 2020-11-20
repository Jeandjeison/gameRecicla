def historico(nome, email):
    dados = open("historico.txt", "a")
    dados.write("Nome: "+nome+", E-mail: "+email+"\n")
    dados.close

def niveis(contador, velocidadeY):
    if contador == 5:
        velocidadeY = 2
    elif contador == 10:
        velocidadeY = 3
    elif contador == 15:
        velocidadeY = 4
    elif contador == 20:
        velocidadeY = 5
    elif contador == 25:
        velocidadeY = 6
    elif contador == 30:
        velocidadeY = 7
    elif contador == 0:
        velocidadeY = 1
    return velocidadeY
