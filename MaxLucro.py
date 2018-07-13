import numpy as np
import matplotlib.pyplot as plt

class MaxLucro:
    def __init__(self):
        self.quantidades_produzidas = None
        self.custos_fixos = None
        self.custos_variaveis = None
        self.file = None
        self.custo_medio_fixo =None
        self.custo_medio_variado = None
        self.custo_medio = None
        self.custo_marginal = None
        self.preco = None
        self.custo_total = None
        self.intersectk = None
        np.warnings.filterwarnings('ignore')

    def read_csv(self):

        lines = open("../Arquivos_de_Entrada/max_lucro.csv").readlines()
        lines = [li.strip() for li in lines]
        lines = [[float(x) for x in li.split(",")] for li in lines]
        return np.array(lines)



    def calcula_ponto_interseccao(self):
        x=None
        for y in range(len(self.custo_medio)):
            if(self.custo_marginal[y]>=self.custo_medio[y]):
                x=y-1

        intersect = self.custo_marginal[x]
        cmarg = self.custo_marginal[x]
        cmedio = self.custo_medio[x]

        while(cmarg<=cmedio):
            intersect = intersect + (self.custo_marginal[x+1]-self.custo_marginal[x])*0.01
            cmarg =cmarg + (self.custo_marginal[x+1]-self.custo_marginal[x])*0.01
            cmedio = cmedio + (self.custo_medio[x+1]-self.custo_medio[x])

        self.intersectk = intersect

    def setup_wizard(self):
        print("----------------------------\n")
        print("Cálculo de Lucro Máximo \n ")
        print("----------------------------\n")
        print("Calculamos as quantidade ideais de venda de um produto a partir de seus valores de custos fixo e variável de produção. \n")
        print("Entrada: o arquivo max_lucro.csv\n")
        print("Saida: Um gráfico com as variáveis economicas e os valor de quantidade ideal para determinado preço\n")
        print("----------------------------\n")
    def input_data(self):
        print("----------------------------\n")
        #self.file = input("Digite o nome do arquivo csv de entrada (o arquivo deve estar no mesmo diretorio do executavel ou deve ser passado o caminho global como parametro) : ")
        self.preco = float(input("Digite o preço do produto :"))
        print("----------------------------\n")

    def open_csv(self):
        Df = self.read_csv()
        self.quantidades_produzidas = Df[:,0]
        self.custos_fixos = Df[:,1]
        self.custos_variaveis = Df[:,2]

    def calcula_variaveis(self):

        self.custo_total = self.custos_fixos + self.custos_variaveis
        self.custo_medio = self.custo_total/self.quantidades_produzidas
        self.custo_medio_fixo = self.custos_fixos/self.quantidades_produzidas
        self.custo_medio_variado = self.custos_variaveis/self.quantidades_produzidas

        self.custo_marginal = [0]

        for i in range(len(self.custos_variaveis)-1):
            self.custo_marginal.append(self.custos_variaveis[i+1]-self.custos_variaveis[i])
        self.custo_marginal = np.array(self.custo_marginal)

    def plota_grafico(self):

        plt.title("Maximização de Lucro")
        plt.plot(self.custo_medio, label = "custo medio total")
        plt.plot(self.custo_medio_variado, label = "custo medio variado")
        plt.plot(self.custo_marginal, label ="custo marginal")
        plt.plot(np.full(self.custo_medio.shape,self.preco), label= "preco")
        plt.legend()
        plt.show()

    def print_explicacao(self):
        print('No ponto de intersecção das curvas "preço" e "custo marginal" encontra-se o lucro máximo para o cenário em estudo.\nNo ponto de intersecção das curvas "custo marginal" e  "custo médio total" obtemos o custo total médio mínimo.\nNeste ponto a empresa  utiliza de maneira mais eficiente os recursos disponíveis para produzir um bem ou serviço')




if __name__=="__main__":
    maxLucro = MaxLucro()
    maxLucro.setup_wizard()
    maxLucro.input_data()
    maxLucro.open_csv()
    maxLucro.calcula_variaveis()
    maxLucro.print_explicacao()
    maxLucro.plota_grafico()
