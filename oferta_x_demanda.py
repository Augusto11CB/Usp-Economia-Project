import numpy as np
import matplotlib.pyplot as plt
import pandas

class oferta_x_demanda():

    def __init__(self):
        self.file = None
        self.tipo_de_imposto = None
        self.ofertas = np.array([])
        self.demandas = np.array([])
        self.quantidades = np.array([])
        self.imposto = 0.0

    #oferta: ro = 4x+2
    #demanda: rd = 9-3x
    # x = quantidade
    # r0 e rd são preços
    #ID - > recai sobre a demanda
    #IO - >

    def setup_wizard(self):
        print("----------------------------\n")
        print("Calculo da variação da curva de oferta e demanda dado criação de imposto")
        print("----------------------------\n")
        print("Nós estimamos o impacto da criação de imposto nas curvas de demanda e oferta\n")
        print("Entrada: São as quantidades demandadas, ofertadas no mercado, além do imposto em um arquivo csv\n(a primeira coluna representa quantidade a segunda representa o preço da demanda e a terceira coluna representa o preço da ofertada)\n")
        print("Saida: Gráfico com a curva de oferta e demanda deslocadas devido ao imposto \n")
        print("----------------------------\n")

    def input_data(self):
        print("----------------------------\n")
        self.file = input("Digite o nome do arquivo csv de entrada (o arquivo deve estar no mesmo diretorio do executavel ou deve ser passado o caminho global como parametro) : ")
        self.tipo_de_imposto = input("Digite o tipo do imposto (demanda ou oferta): ")
        self.imposto = float(input("Digite o valor do imposto : "))
        print("----------------------------\n")

    def open_csv(self):
        Df = pandas.read_csv(self.file)
        self.demandas = np.array(Df.iloc[:, 1])
        self.ofertas = np.array(Df.iloc[:,2])
        self.quantidades = np.array(Df.iloc[:,0])


    def curva_oferta_demanda(self):
        plt.title("Curva de oferta e demanda")
        plt.subplot(121)
        plt.plot(self.quantidades,self.demandas,label="demanda sem imposto")        
        plt.plot(self.quantidades,self.ofertas,label="oferta sem imposto")
        plt.legend()
        plt.subplot(122)
        if(self.tipo_de_imposto=="demanda"):
            self.demandas = self.demandas + (self.demandas * self.imposto)
        else:
            self.ofertas = self.ofertas + (self.ofertas * self.imposto)

        plt.plot(self.quantidades,self.demandas,label="demanda com imposto")        
        plt.plot(self.quantidades,self.ofertas,label="oferta com imposto")
        plt.legend()
        plt.show()


if __name__=="__main__":
    ofertaDemanda = oferta_x_demanda()
    ofertaDemanda.setup_wizard()
    ofertaDemanda.input_data()
    ofertaDemanda.open_csv()
    ofertaDemanda.curva_oferta_demanda()



