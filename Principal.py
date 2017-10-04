from tkinter import *

janelaPrincipal = Tk()

def cliqueJogar():

    janelaJogar = Tk()

    # CRIACAO
    lbSuperior = Label(janelaJogar, bg="black")
    lbInferior = Label(janelaJogar, bg="black")
    lbDireito = Label(janelaJogar, bg="black", text="    ")
    lbEsquerdo = Label(janelaJogar, bg="black", text="    ")

    # ADICAO
    lbSuperior.pack(side=TOP, fill=X)
    lbInferior.pack(side=BOTTOM, fill=X)
    lbDireito.pack(side=RIGHT, fill=Y)
    lbEsquerdo.pack(side=LEFT, fill=Y)

    janelaJogar.geometry("800x600+300+100")
    janelaJogar.title("Jogo do NIM - Jogar")
    janelaJogar.mainloop()

def cliqueInstrucao():

    janelaInstrucao = Tk()

    # CRIACAO
    lbSuperior = Label(janelaInstrucao, bg="black")
    lbInferior = Label(janelaInstrucao, bg="black")
    lbDireito = Label(janelaInstrucao, bg="black", text="    ")
    lbEsquerdo = Label(janelaInstrucao, bg="black", text="    ")
    lbEspaco1 = Label(janelaInstrucao, height=2)
    lbOqueETitulo = Label(janelaInstrucao, font=("Courier", 20), text="O que é:")
    lbOqueE = Label(janelaInstrucao, font=("Courier", 12), text="Esse é um jogo composto por um número qualquer de peças \n(é muito usado em "
                                                            "sua versão física, palitos de fósforos ou de dente) \nonde dois jogadores vão tirando "
                                                            "alternadamente essas peças com base \nem um limite pré-estabelecido por jogada."
                                                            " Perde o jogador,\n que na sua vez, só disponha de uma peça disposta para ser pega. ")
    lbEspaco2 = Label(janelaInstrucao, height=3)
    lbComoJogarTitulo = Label(janelaInstrucao, font=("Courier", 20), text="Como jogar:")
    lbComoJogar = Label(janelaInstrucao, font=("Courier", 12), text=""
                                                                    "\n# Perde o jogador que retirar a última peça.")

    # ADICAO
    lbSuperior.pack(side=TOP, fill=X)
    lbInferior.pack(side=BOTTOM, fill=X)
    lbDireito.pack(side=RIGHT, fill=Y)
    lbEsquerdo.pack(side=LEFT, fill=Y)
    lbEspaco1.pack(side=TOP)
    lbOqueETitulo.pack(side=TOP)
    lbOqueE.pack(side=TOP)
    lbEspaco2.pack(side=TOP)
    lbComoJogarTitulo.pack(side=TOP)
    lbComoJogar.pack(side=TOP)


    janelaInstrucao.geometry("800x600+300+100")
    janelaInstrucao.title("Jogo do NIM - Instruções")
    janelaInstrucao.mainloop()


#CRIACAO
lbSuperior = Label(janelaPrincipal, bg="black")
lbInferior = Label(janelaPrincipal, bg="black")
lbDireito = Label(janelaPrincipal, bg="black", text="    ")
lbEsquerdo = Label(janelaPrincipal, bg="black", text="    ")
lbTitulo = Label(janelaPrincipal, text="Jogo do NIM", width=200, font=("Courier", 80))
lbEspaco1 = Label(janelaPrincipal, height=3)
btJogar = Button(janelaPrincipal, bg="white", text="Jogar", width=15, font=("Courier", 55), command=cliqueJogar)
lbEspaco2 = Label(janelaPrincipal, height=1)
btInstrucoes = Button(janelaPrincipal, bg="white", text="Instruções", width=15, font=("Courier", 55), command=cliqueInstrucao)
lbDireitos = Label(janelaPrincipal, text="© Igor Túllio 2017", font=("Courier", 12))

#ADICAO
lbSuperior.pack(side=TOP, fill=X)
lbInferior.pack(side=BOTTOM, fill=X)
lbDireito.pack(side=RIGHT, fill=Y)
lbEsquerdo.pack(side=LEFT, fill=Y)
lbTitulo.pack(side=TOP, fill=X)
lbEspaco1.pack(side=TOP)
btJogar.pack(side=TOP)
lbEspaco2.pack(side=TOP)
btInstrucoes.pack(side=TOP)
lbDireitos.pack(side=BOTTOM, fill=X)


janelaPrincipal.geometry("800x600+300+100")
janelaPrincipal.title("Jogo do NIM")
janelaPrincipal.mainloop()

''' 
imagem = PhotoImage(file="C:\\Users\\igorgoncalves\\Desktop\\JogoDoNimGUI\\palito.jpg")
w = Label(janela, image=imagem)
w.imagem = imagem

w.pack()
'''