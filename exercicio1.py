import os
carros=[]

class carro:
    nome=""
    pot=0
    velmax=0
    ligado=False
    def __init__(self,nome,pot):
        self.nome=nome
        self.pot=pot
        self.velmax=int(pot)*2
        self.ligado=False

    def ligar(self):
        self.ligado=True

    def desligar(self):
        self.ligado=False

    def info(self):
        print("nome.................:"+self.nome)
        print("potençia.............:"+str(self.pot))
        print("veloçidade maxima....:"+str(self.velmax))
        print("ligado...............:"+("sim" if self.ligado==True else "não"))

def menu():
    os.system("cls") or None
    print("1 - novo carro")
    print("2 - informações do carro")
    print("3 - excluir carro")
    print("4 - ligar carro")
    print("5 - desligar carro")
    print("6 - listar os carros")
    print("7 - sair do programa")
    print("quantidade de carros "+str(len(carros)))
    opc=input("digite uma opção: ")
    return opc

def NovoCarro():
    os.system("cls") or None
    nomedocarro=input("Nome do Carro....: ")
    potenciadocarro=input("Potençia do carro....: ")
    caro=carro(nomedocarro,potenciadocarro)
    carros.append(caro)
    print("novo carro criado")
    os.system("pause")

def informacoes():
    os.system("cls") or None
    n=input("informe o numero do carro que deseja ver as informações: ")
    try:
        carros[int(n)].info()
    except:
        print("carro mão existe na lista")
    os.system("pause")

def excluircarro():
    os.system("cls") or None
    n=input("informe o numero do carro que deseja excluir: ")
    try:
        del carros[int(n)]
    except:
        print("carro mão existe na lista")
    os.system("pause")

def ligarcarro():
    os.system("cls") or None
    n=input("informe o numero do carro que deseja ligar: ")
    try:
        carros[int(n)].ligar()
        print("Carro ligado")
    except:
        print("carro mão existe na lista")
    os.system("pause")

def desligarcarro():
    os.system("cls") or None
    n=input("informe o numero do carro que deseja desligar: ")
    try:
        carros[int(n)].desligar()
        print("Carro desligado")
    except:
        print("carro mão existe na lista")
    os.system("pause")

def listarcarros():
    os.system("cls") or None
    p=0
    for c in carros:
        print(str(p) + " - " + c.nome)
        p=p+1
    os.system("pause")


ret=menu()
while ret < "7":
    if ret== "1":
        NovoCarro()
    elif ret=="2":
        informacoes()
    elif ret=="3":
        excluircarro()
    elif ret=="4":
        ligarcarro()
    elif ret=="5":
        desligarcarro()
    elif ret=="6":
        listarcarros()
    ret=menu

os.system("cls") or None
print("programa finaliado")