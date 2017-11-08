from tkinter import *

class menuInstrucao:
    def __init__(self):
        self.janelaInstrucao = Tk()

        # CRIACAO
        self.lbSuperior = Label(self.janelaInstrucao, bg="black")
        self.lbInferior = Label(self.janelaInstrucao, bg="black")
        self.lbDireito = Label(self.janelaInstrucao, bg="black", text="    ")
        self.lbEsquerdo = Label(self.janelaInstrucao, bg="black", text="    ")
        self.lbEspaco1 = Label(self.janelaInstrucao, height=2)
        self.lbOqueETitulo = Label(self.janelaInstrucao, font=("Courier", 20), text="O que é:")
        self.lbOqueE = Label(self.janelaInstrucao, font=("Courier", 12), text="Esse é um jogo composto por um número qualquer de peças \n(é muito usado em "
                                                                "sua versão física, palitos de fósforos ou de dente) \nonde dois jogadores vão tirando "
                                                                "alternadamente essas peças com base \nem um limite pré-estabelecido por jogada."
                                                                " Perde o jogador,\n que na sua vez, só disponha de uma peça disposta para ser pega. ")
        self.lbEspaco2 = Label(self.janelaInstrucao, height=3)
        self.lbComoJogarTitulo = Label(self.janelaInstrucao, font=("Courier", 20), text="Como jogar:")
        self.lbComoJogar = Label(self.janelaInstrucao, font=("Courier", 12), text=""
                                                                        "\n# Perde o jogador que retirar a última peça.")

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

        self.janelaInstrucao.geometry("800x600+300+100")
        self.janelaInstrucao.title("Jogo do NIM - Instruções")

        #janelaPrincipal.destroy()  # Fechar janelaPrincipal

        self.janelaInstrucao.mainloop()