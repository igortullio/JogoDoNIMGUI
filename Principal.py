from tkinter import *
from menuJogar import menuJogar
from menuInstrucao import menuInstrucao

class principal:
    def __init__(self):
        self.janelaPrincipal = Tk()

        #CRIACAO
        self.lbSuperior = Label(self.janelaPrincipal, bg="black")
        self.lbInferior = Label(self.janelaPrincipal, bg="black")
        self.lbDireito = Label(self.janelaPrincipal, bg="black", text="    ")
        self.lbEsquerdo = Label(self.janelaPrincipal, bg="black", text="    ")
        self.lbTitulo = Label(self.janelaPrincipal, text="Jogo do NIM", width=200, font=("Courier", 80))
        self.lbEspaco1 = Label(self.janelaPrincipal, height=3)
        self.btJogar = Button(self.janelaPrincipal, bg="white", text="Jogar", width=15, font=("Courier", 55), command=menuJogar)
        self.lbEspaco2 = Label(self.janelaPrincipal, height=1)
        self.btInstrucoes = Button(self.janelaPrincipal, bg="white", text="Instruções", width=15, font=("Courier", 55), command=menuInstrucao)
        self.lbDireitos = Label(self.janelaPrincipal, text="© Igor Túllio 2017", font=("Courier", 12))

        #ADICAO
        self.lbSuperior.pack(side=TOP, fill=X)
        self.lbInferior.pack(side=BOTTOM, fill=X)
        self.lbDireito.pack(side=RIGHT, fill=Y)
        self.lbEsquerdo.pack(side=LEFT, fill=Y)
        self.lbTitulo.pack(side=TOP, fill=X)
        self.lbEspaco1.pack(side=TOP)
        self.btJogar.pack(side=TOP)
        self.lbEspaco2.pack(side=TOP)
        self.btInstrucoes.pack(side=TOP)
        self.lbDireitos.pack(side=BOTTOM, fill=X)

        self.janelaPrincipal.geometry("800x600+300+100")
        self.janelaPrincipal.title("Jogo do NIM")
        self.janelaPrincipal.mainloop()

if __name__ == '__main__':
    janela = principal()