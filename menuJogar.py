from tkinter import *
from random import randint

class menuJogar:
    def __init__(self):
        self.janelaJogar = Tk()

        # CRIACAO
        self.lbSuperior = Label(self.janelaJogar, bg="black")
        self.lbInferior = Label(self.janelaJogar, bg="black")
        self.lbDireito = Label(self.janelaJogar, bg="black", text="    ")
        self.lbEsquerdo = Label(self.janelaJogar, bg="black", text="    ")
        self.lbEspaco1 = Label(self.janelaJogar, height=2)
        self.lbTitulo = Label(self.janelaJogar, font=("Courier", 40), text="Escolha uma opção:")
        self.lbEspaco2 = Label(self.janelaJogar, height=2)
        self.btPartida = Button(self.janelaJogar, bg="white", text="Partida", width=15, font=("Courier", 55), command=self.janelaJogarPartida)
        self.lbEspaco3 = Label(self.janelaJogar, height=2)
        self.btCampeonato = Button(self.janelaJogar, bg="white", text="Campeonato", width=15, font=("Courier", 55), command=self.janelaJogarCampeonato)

        # ADICAO
        self.lbSuperior.pack(side=TOP, fill=X)
        self.lbInferior.pack(side=BOTTOM, fill=X)
        self.lbDireito.pack(side=RIGHT, fill=Y)
        self.lbEsquerdo.pack(side=LEFT, fill=Y)
        self.lbEspaco1.pack(side=TOP)
        self.lbTitulo.pack(side=TOP)
        self.lbEspaco2.pack(side=TOP)
        self.btPartida.pack(side=TOP)
        self.lbEspaco3.pack(side=TOP)
        self.btCampeonato.pack(side=TOP)

        self.janelaJogar.geometry("800x600+300+100")
        self.janelaJogar.title("Jogo do NIM - Jogar")

        #janelaPrincipal.destroy() #Fechar janelaPrincipal

        self.janelaJogar.mainloop()

    def janelaJogarPartida(self):
        self.janelaPartida = Toplevel()

        self.fundo = PhotoImage(file="Imagens\\fundo.gif")
        self.palito = PhotoImage(file="Imagens\\palito.gif")

        self.lbSuperior = Label(self.janelaPartida, bg="black")
        self.lbInferior = Label(self.janelaPartida, bg="black")
        self.lbDireito = Label(self.janelaPartida, bg="black", text="    ")
        self.lbEsquerdo = Label(self.janelaPartida, bg="black", text="    ")
        self.lbFundo = Label(self.janelaPartida, image=self.fundo)
        self.lbQtdPecasTitulo = Label(self.janelaPartida, font=("Courier", 20), text="Peças no tabuleiro: ")
        self.lbQtdPecas = Label(self.janelaPartida, font=("Courier", 20), text="X")
        self.lbImagem1 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem2 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem3 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem4 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem5 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem6 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem7 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem8 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem9 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem10 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem11 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem12 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem13 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem14 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem15 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem16 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem17 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem18 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem19 = Button(self.janelaPartida, image=self.palito)
        self.lbImagem20 = Button(self.janelaPartida, image=self.palito)

        numeroPecas = randint(5, 20)

        self.lbFundo.pack()
        self.lbImagem1.pack()

        '''lbQtdPecasTitulo.grid(row=0, column=0)
        lbQtdPecas.grid(row=0, column=1)
        lbImagem1.grid(row=1, column=0)
        lbImagem2.grid(row=2, column=0)
        lbImagem3.grid(row=3, column=0)
        lbImagem4.grid(row=4, column=0)
        lbImagem5.grid(row=5, column=0)
        lbImagem6.grid(row=1, column=1)
        lbImagem7.grid(row=2, column=2)
        lbImagem8.grid(row=3, column=3)
        lbImagem9.grid(row=4, column=4)
        lbImagem10.grid(row=5, column=5)'''

        self.janelaPartida.geometry("800x600+300+100")
        self.janelaPartida.title("Jogo do NIM - Jogar Partida")
        self.janelaPartida.mainloop()

    def janelaJogarCampeonato(self):
        self.janelaCampeonato = Tk()

        self.lbSuperior = Label(self.janelaCampeonato, bg="black")
        self.lbInferior = Label(self.janelaCampeonato, bg="black")
        self.lbDireito = Label(self.janelaCampeonato, bg="black", text="    ")
        self.lbEsquerdo = Label(self.janelaCampeonato, bg="black", text="    ")

        # ADICAO
        self.lbSuperior.pack(side=TOP, fill=X)
        self.lbInferior.pack(side=BOTTOM, fill=X)
        self.lbDireito.pack(side=RIGHT, fill=Y)
        self.lbEsquerdo.pack(side=LEFT, fill=Y)

        self.janelaCampeonato.geometry("800x600+300+100")
        self.janelaCampeonato.title("Jogo do NIM - Jogar Campeonato")
        self.janelaCampeonato.mainloop()