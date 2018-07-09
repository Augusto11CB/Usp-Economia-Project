import pandas
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

    def setup_wizard(self):
        print("----------------------------\n")
        print("Cálculo de Lucro Máximo \n ")
        print("----------------------------\n")
        print("Calculamos as quantidade ideais de venda de um produto a partir de seus valores de custos fixo e variável de produção. \n")
        print("Entrada: o preço do produto e o nome de um arquivo csv com 3 colunas, a primeira com as quantidades produzidas, a segunda com os custos fixos pela quantidade produzida, e a terceira os custos variaveis pela quantidade produzida. \n")
        print("Saida: Um gráfico com as variáveis economicas e os valor de quantidade ideal para determinado preço\n")

    def input_data(self):

        self.file = input("Digite o nome do arquivo csv de entrada (o arquivo deve estar no mesmo diretorio do executavel ou deve ser passado o caminho global como parametro) : ")
        self.preco = float(input("Digite o preço do produto :"))

    def open_csv(self):
        Df = pandas.read_csv(self.file)
        self.quantidades_produzidas = np.array(Df.iloc[:, 0])
        self.custos_fixos = np.array(Df.iloc[:,1])
        self.custos_variaveis = np.array(Df.iloc[:,2])

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





if __name__=="__main__":
    maxLucro = MaxLucro()
    maxLucro.setup_wizard()
    maxLucro.input_data()
    maxLucro.open_csv()
    maxLucro.calcula_variaveis()
    maxLucro.plota_grafico()