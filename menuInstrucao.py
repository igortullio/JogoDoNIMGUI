from tkinter import *
import webbrowser

class menuInstrucao:
    def link(self, event):
        webbrowser.open_new(r"https://github.com/igortullio/JogoDoNIMGUI")

    def __init__(self):
        self.janelaInstrucao = Tk()

        # CRIACAO
        self.lbSuperior = Label(self.janelaInstrucao, bg="black")
        self.lbInferior = Label(self.janelaInstrucao, bg="black")
        self.lbDireito = Label(self.janelaInstrucao, bg="black", text="    ")
        self.lbEsquerdo = Label(self.janelaInstrucao, bg="black", text="    ")
        self.lbEspaco1 = Label(self.janelaInstrucao, height=2)
        self.lbOqueETitulo = Label(self.janelaInstrucao, font=("Courier", 20), text="O que é:")
        self.lbOqueE = Label(self.janelaInstrucao, font=("Courier", 12), text="Esse é um jogo composto por um número qualquer de peças (é muito usado em\n"
                                                                              "sua versão física palitos de fósforos ou de dentes) onde dois jogadores vão\n"
                                                                              "tirando alternadamente essas peças com base em um limite pré-estabelecido \n"
                                                                              "por jogada. Quem tirar as últimas peças possíveis ganha o jogo.")
        self.lbEspaco2 = Label(self.janelaInstrucao, height=3)
        self.lbComoJogarTitulo = Label(self.janelaInstrucao, font=("Courier", 20), text="Como jogar:")
        self.lbComoJogar = Label(self.janelaInstrucao, font=("Courier", 12), text="# Um número x de peças são distribuídas no tabuleiro;"
                                                                        "\n# Os dois jogadores vão tirando alternadamente as peças (no mínimo uma);"
                                                                        "\n# Perde o jogador que na sua vez não disponha de nenhuma peça para pegar.")
        self.lbEspaco3 = Label(self.janelaInstrucao, height=3)
        self.lbLinkTitulo = Label(self.janelaInstrucao, font=("Courier", 20), text="Links relacionados:")
        self.lbLink = Label(self.janelaInstrucao, font=("Courier", 15), text="Git do Projeto", fg="blue", cursor="hand2")
        #self.lbLink2 = Label(self.janelaInstrucao, font=("Courier", 15), text="Matemática Jogada - Jogo do NIM", fg="blue", cursor="hand2")

        # ADICAO
        self.lbSuperior.pack(side=TOP, fill=X)
        self.lbInferior.pack(side=BOTTOM, fill=X)
        self.lbDireito.pack(side=RIGHT, fill=Y)
        self.lbEsquerdo.pack(side=LEFT, fill=Y)
        self.lbEspaco1.pack(side=TOP)
        self.lbOqueETitulo.pack(side=TOP)
        self.lbOqueE.pack(side=TOP)
        self.lbEspaco2.pack(side=TOP)
        self.lbComoJogarTitulo.pack(side=TOP)
        self.lbComoJogar.pack(side=TOP)
        self.lbEspaco3.pack(side=TOP)
        self.lbLinkTitulo.pack(side=TOP)
        self.lbLink.pack(side=TOP)
        self.lbLink.bind("<Button-1>", self.link)

        #self.janelaInstrucao.geometry("800x600+300+100")
        self.janelaInstrucao.geometry("800x600+0+0")
        self.janelaInstrucao.title("Jogo do NIM - Instruções")

        #janelaPrincipal.destroy()  # Fechar janelaPrincipal

        self.janelaInstrucao.mainloop()

