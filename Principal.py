from tkinter import *

def jogarPartida ():
    janelaPartida = Toplevel()

    fundo = PhotoImage(file="fundo.gif")
    palito = PhotoImage(file="palito.gif")

    lbSuperior = Label(janelaPartida, bg="black")
    lbInferior = Label(janelaPartida, bg="black")
    lbDireito = Label(janelaPartida, bg="black", text="    ")
    lbEsquerdo = Label(janelaPartida, bg="black", text="    ")
    lbFundo = Label(janelaPartida, image=fundo)
    lbQtdPecasTitulo = Label(janelaPartida, font=("Courier", 20), text="Peças no tabuleiro: ")
    lbQtdPecas = Label(janelaPartida, font=("Courier", 20), text="X")
    lbImagem1 = Button(janelaPartida, image=palito)
    lbImagem2 = Button(janelaPartida, image=palito)
    lbImagem3 = Button(janelaPartida, image=palito)
    lbImagem4 = Button(janelaPartida, image=palito)
    lbImagem5 = Button(janelaPartida, image=palito)
    lbImagem6 = Button(janelaPartida, image=palito)
    lbImagem7 = Button(janelaPartida, image=palito)
    lbImagem8 = Button(janelaPartida, image=palito)
    lbImagem9 = Button(janelaPartida, image=palito)
    lbImagem10 = Button(janelaPartida, image=palito)

    # ADICAO
    #lbSuperior.pack(side=TOP, fill=X)
    #lbInferior.pack(side=BOTTOM, fill=X)
    #lbDireito.pack(side=RIGHT, fill=Y)
    #lbEsquerdo.pack(side=LEFT, fill=Y)
    lbFundo.pack()
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

    janelaPartida.geometry("800x600+300+100")
    janelaPartida.title("Jogo do NIM - Jogar Partida")
    janelaPartida.mainloop()

def jogarCampeonato():
    janelaCampeonato = Tk()

    lbSuperior = Label(janelaCampeonato, bg="black")
    lbInferior = Label(janelaCampeonato, bg="black")
    lbDireito = Label(janelaCampeonato, bg="black", text="    ")
    lbEsquerdo = Label(janelaCampeonato, bg="black", text="    ")

    # ADICAO
    lbSuperior.pack(side=TOP, fill=X)
    lbInferior.pack(side=BOTTOM, fill=X)
    lbDireito.pack(side=RIGHT, fill=Y)
    lbEsquerdo.pack(side=LEFT, fill=Y)

    janelaCampeonato.geometry("800x600+300+100")
    janelaCampeonato.title("Jogo do NIM - Jogar Campeonato")
    janelaCampeonato.mainloop()

def menuJogar():
    janelaJogar = Tk()

    # CRIACAO
    lbSuperior = Label(janelaJogar, bg="black")
    lbInferior = Label(janelaJogar, bg="black")
    lbDireito = Label(janelaJogar, bg="black", text="    ")
    lbEsquerdo = Label(janelaJogar, bg="black", text="    ")
    lbEspaco1 = Label(janelaJogar, height=2)
    lbTitulo = Label(janelaJogar, font=("Courier", 40), text="Escolha uma opção:")
    lbEspaco2 = Label(janelaJogar, height=2)
    btPartida = Button(janelaJogar, bg="white", text="Partida", width=15, font=("Courier", 55), command=jogarPartida)
    lbEspaco3 = Label(janelaJogar, height=2)
    btCampeonato = Button(janelaJogar, bg="white", text="Campeonato", width=15, font=("Courier", 55), command=jogarCampeonato)

    # ADICAO
    lbSuperior.pack(side=TOP, fill=X)
    lbInferior.pack(side=BOTTOM, fill=X)
    lbDireito.pack(side=RIGHT, fill=Y)
    lbEsquerdo.pack(side=LEFT, fill=Y)
    lbEspaco1.pack(side=TOP)
    lbTitulo.pack(side=TOP)
    lbEspaco2.pack(side=TOP)
    btPartida.pack(side=TOP)
    lbEspaco3.pack(side=TOP)
    btCampeonato.pack(side=TOP)

    janelaJogar.geometry("800x600+300+100")
    janelaJogar.title("Jogo do NIM - Jogar")

    #janelaPrincipal.destroy() #Fechar janelaPrincipal

    janelaJogar.mainloop()

def menuInstrucao():
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

    #janelaPrincipal.destroy()  # Fechar janelaPrincipal

    janelaInstrucao.mainloop()

def menuPrincipal():
    janelaPrincipal = Tk()

    #CRIACAO
    lbSuperior = Label(janelaPrincipal, bg="black")
    lbInferior = Label(janelaPrincipal, bg="black")
    lbDireito = Label(janelaPrincipal, bg="black", text="    ")
    lbEsquerdo = Label(janelaPrincipal, bg="black", text="    ")
    lbTitulo = Label(janelaPrincipal, text="Jogo do NIM", width=200, font=("Courier", 80))
    lbEspaco1 = Label(janelaPrincipal, height=3)
    btJogar = Button(janelaPrincipal, bg="white", text="Jogar", width=15, font=("Courier", 55), command=menuJogar)
    lbEspaco2 = Label(janelaPrincipal, height=1)
    btInstrucoes = Button(janelaPrincipal, bg="white", text="Instruções", width=15, font=("Courier", 55), command=menuInstrucao)
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

def main():
    menuPrincipal()

main()

''' 
imagem = PhotoImage(file="C:\\Users\\igorgoncalves\\Desktop\\JogoDoNimGUI\\palito.jpg")
w = Label(janela, image=imagem)
w.imagem = imagem

w.pack()
'''