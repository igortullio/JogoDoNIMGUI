from tkinter import *
from random import randint
from tkinter import messagebox

class menuJogar:

    ultima = 0  # Variável que será usada no metodo tirar

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

        #self.janelaJogar.geometry("800x600+300+100")
        self.janelaJogar.geometry("800x600+0+0")
        self.janelaJogar.title("Jogo do NIM - Jogar")

        #janelaPrincipal.destroy() #Fechar janelaPrincipal

        self.janelaJogar.mainloop()

    def janelaJogarPartida(self):
        self.janelaPartida = Toplevel()

        self.fundo = PhotoImage(file="Imagens\\fundo.gif")
        self.palito = PhotoImage(file="Imagens\\palito.gif")

        self.lbSuperior = Frame(self.janelaPartida, bg="black", height = 21)
        self.lbInferior = Frame(self.janelaPartida, bg="black", height = 21)
        self.lbDireito = Frame(self.janelaPartida, bg="black", width=18)
        self.lbEsquerdo = Frame(self.janelaPartida, bg="black", width=18)

        self.frame1 = Frame(self.janelaPartida, width=800)
        self.frameEspaco = Frame(self.janelaPartida, height = 10, width=800)
        self.frame2 = Frame(self.janelaPartida, width=800)

        self.lbFundo = Label(self.frame1, image=self.fundo)
        self.lbQtdPecasTitulo = Label(self.frame1, font=("Courier", 20), text="Peças no tabuleiro: ")
        self.lbQtdPecas = Label(self.frame1, font=("Courier", 20), text="X")
        self.lbVezTitulo = Label(self.frame1, font=("Courier", 20), text="Vez: ")
        self.lbVez = Label(self.frame1, font=("Courier", 20), text="1")
        self.lbLimiteJogadaTitulo = Label(self.frame1, font=("Courier", 20), text="Limite de retirada: ")
        self.lbLimiteJogada = Label(self.frame1, font=("Courier", 20), text="X")
        self.lbQtdTirarTitulo = Label(self.frame1, font=("Courier", 20), text="Remover quantas peças?")
        self.lbQtdTirar = Label(self.frame1, font=("Courier", 20), text="1")
        self.btMenos = Button(self.frame1, font=("Courier", 20), text="-", command=self.menos)
        self.btMais = Button(self.frame1, font=("Courier", 20), text="+", command=self.mais)
        self.lbEspaco01 = Label(self.frame1, text="   ")
        self.btTirar = Button(self.frame1, font=("Courier", 20), text="Tirar", command=self.tirar)

        self.imagens = []
        self.lbImagem1 = Label(self.frame2, image=self.palito)
        self.lbImagem2 = Label(self.frame2, image=self.palito)
        self.lbImagem3 = Label(self.frame2, image=self.palito)
        self.lbImagem4 = Label(self.frame2, image=self.palito)
        self.lbImagem5 = Label(self.frame2, image=self.palito)
        self.lbImagem6 = Label(self.frame2, image=self.palito)
        self.lbImagem7 = Label(self.frame2, image=self.palito)
        self.lbImagem8 = Label(self.frame2, image=self.palito)
        self.lbImagem9 = Label(self.frame2, image=self.palito)
        self.lbImagem10 = Label(self.frame2, image=self.palito)
        self.lbImagem11 = Label(self.frame2, image=self.palito)
        self.lbImagem12 = Label(self.frame2, image=self.palito)
        self.lbImagem13 = Label(self.frame2, image=self.palito)
        self.lbImagem14 = Label(self.frame2, image=self.palito)
        self.lbImagem15 = Label(self.frame2, image=self.palito)
        self.lbImagem16 = Label(self.frame2, image=self.palito)
        self.lbImagem17 = Label(self.frame2, image=self.palito)
        self.lbImagem18 = Label(self.frame2, image=self.palito)
        self.lbImagem19 = Label(self.frame2, image=self.palito)
        self.lbImagem20 = Label(self.frame2, image=self.palito)

        self.imagens.append(self.lbImagem1)
        self.imagens.append(self.lbImagem2)
        self.imagens.append(self.lbImagem3)
        self.imagens.append(self.lbImagem4)
        self.imagens.append(self.lbImagem5)
        self.imagens.append(self.lbImagem6)
        self.imagens.append(self.lbImagem7)
        self.imagens.append(self.lbImagem8)
        self.imagens.append(self.lbImagem9)
        self.imagens.append(self.lbImagem10)
        self.imagens.append(self.lbImagem11)
        self.imagens.append(self.lbImagem12)
        self.imagens.append(self.lbImagem13)
        self.imagens.append(self.lbImagem14)
        self.imagens.append(self.lbImagem15)
        self.imagens.append(self.lbImagem17)
        self.imagens.append(self.lbImagem16)
        self.imagens.append(self.lbImagem18)
        self.imagens.append(self.lbImagem19)
        self.imagens.append(self.lbImagem20)

        self.numeroPecas = randint(5, 20)
        self.lbQtdPecas["text"]=self.numeroPecas

        self.limite = randint(1, self.numeroPecas//2)
        self.lbLimiteJogada["text"]=self.limite



        #ADIÇÃO
        self.lbSuperior.pack(side=TOP, fill=X)
        self.lbInferior.pack(side=BOTTOM, fill=X)
        self.lbDireito.pack(side=RIGHT, fill=Y)
        self.lbEsquerdo.pack(side=LEFT, fill=Y)
        self.frame1.pack()
        self.frameEspaco.pack()
        self.frame2.pack()

        self.lbQtdPecasTitulo.grid(row=0, column=0, sticky=W)                
        self.lbQtdPecas.grid(row=0, column=3)
        self.lbVezTitulo.grid(row=0, column=6)
        self.lbVez.grid(row=0, column=8)
        self.lbLimiteJogadaTitulo.grid(row=1, column=0, sticky=W)
        self.lbLimiteJogada.grid(row=1, column=3)
        self.lbQtdTirarTitulo.grid(row=2, column=0)
        self.btMenos.grid(row=2, column=1)
        self.lbQtdTirar.grid(row=2, column=3)
        self.btMais.grid(row=2, column=5)
        self.lbEspaco01.grid(row=2, column=6)
        self.btTirar.grid(row=2, column=8)

        linha = 0
        coluna = 0
        for x in range(0, self.numeroPecas):
            self.imagens[x].grid(row=linha, column=coluna)
            if(coluna < 4):
                coluna=coluna+1
            else:
                linha=linha+1
                coluna=0

        #self.janelaPartida.geometry("800x600+300+100")
        self.janelaPartida.geometry("800x600+0+0")
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

        #self.janelaCampeonato.geometry("800x600+300+100")
        self.janelaCampeonato.geometry("800x600+0+0")
        self.janelaCampeonato.title("Jogo do NIM - Jogar Campeonato")
        self.janelaCampeonato.mainloop()

    def menos(self):
        if(int(self.lbQtdTirar["text"]) > 1 and int(self.lbQtdTirar["text"]) <= int(self.lbLimiteJogada["text"])):
            self.lbQtdTirar["text"]=int(self.lbQtdTirar["text"]) - 1

    def mais(self):
        if (int(self.lbQtdTirar["text"]) < int(self.lbLimiteJogada["text"])):
            self.lbQtdTirar["text"] = int(self.lbQtdTirar["text"]) + 1

    def tirar(self):
        self.tirar = int(self.lbQtdTirar["text"])
        self.numeroPecas = int(self.lbQtdPecas["text"]) - self.tirar
        self.lbQtdPecas["text"] = self.numeroPecas
        self.inicio = self.ultima

        if int(self.lbVez["text"]) == 1:
            for x in range(self.inicio, self.tirar + self.inicio):
                self.imagens[x]["state"] = DISABLED
                self.ultima = self.ultima + 1
            if self.numeroPecas <= 0:
                messagebox.showinfo("Vencedor", "Jogador 1 ganhou!")

            self.lbVez["text"] = "2"
        else:
            for x in range(self.inicio, self.tirar + self.inicio):
                self.imagens[x]["state"] = DISABLED
                self.ultima = self.ultima + 1
            if self.numeroPecas <= 0:
                messagebox.showinfo("Vencedor", "Jogador 2 ganhou!")

            self.lbVez["text"] = "1"