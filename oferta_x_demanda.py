import numpy as np
import matplotlib.pyplot as plt

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

    def read_csv(self):

        lines = open("../Arquivos_de_Entrada/oferta_demanda.csv").readlines()
        lines = [li.strip() for li in lines]
        lines = [[float(x) for x in li.split(",")] for li in lines]
        return np.array(lines)



    def setup_wizard(self):
        print("----------------------------\n")
        print("Calculo da variação da curva de oferta e demanda dado criação de imposto")
        print("----------------------------\n")
        print("Nós estimamos o impacto da criação de imposto nas curvas de demanda e oferta\n")
        print("Entrada: O arquivo oferta_demanda.csv \n")
        print("Saida: Gráfico com a curva de oferta e demanda deslocadas devido ao imposto \n")
        print("----------------------------\n")

    def input_data(self):
        print("----------------------------\n")
        #self.file = input("Digite o nome do arquivo csv de entrada (o arquivo deve estar no mesmo diretorio do executavel ou deve ser passado o caminho global como parametro) : ")
        self.tipo_de_imposto = input("Digite o tipo do imposto (demanda ou oferta): ")
        self.imposto = float(input("Digite o valor do imposto : "))
        print("----------------------------\n")

    def open_csv(self):
        Df = self.read_csv()
        self.demandas = Df[:, 1]
        self.ofertas = Df[:,2]
        self.quantidades = Df[:,0]


    def curva_oferta_demanda(self):
        plt.title("Curva de oferta e demanda")
        plt.subplot(121)
        plt.xlabel("Quantidade")
        plt.ylabel("Preço")
        plt.plot(self.quantidades,self.demandas,label="demanda sem imposto")

        plt.plot(self.quantidades,self.ofertas,label="oferta sem imposto")
        plt.legend()
        plt.subplot(122)
        if(self.tipo_de_imposto=="demanda"):
            if(self.imposto>=1):
                self.imposto = 0.99
            self.demandas = self.demandas - (self.demandas * self.imposto)
            print("O imposto na demanda implica a retração do consumo, puxando a curva de demanda para esquerda\n")
        else:
            self.ofertas = self.ofertas + (self.ofertas * self.imposto)
            print("O imposto na oferta implica no aumento de preços, puxando a curva da oferta para a esquerda\n")

        plt.xlabel("Quantidade")
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




