import pandas
import numpy as np

class MaxLucro:
    def __init__(self):
        self.quantidades_produzidas = None
        self.custos_fixos = None
        self.custos_variaveis = None
        self.file = None
        self.custo_marginal_fixo =None
        self.custo_marginal_variado = None
        self.custo_marginal = None

    def setup_wizard(self):
        print("----------------------------\n")
        print("Cálculo de Lucro Máximo \n ")
        print("----------------------------\n")
        print("Calculamos o preço e a quantidade ideais de venda de um produto a partir de seus valores de custos fixo e variável de produção. \n")
        print("Entrada: o nome de um arquivo csv com 3 colunas, a primeira com as quantidades produzidas, a segunda com os custos fixos pela quantidade produzida, e a terceira os custos variaveis pela quantidade produzida. \n")
        print("Saida: Um gráfico com as variáveis economicas e os valores de quantidade e preço ideais\n")

    def input_file(self):

        self.file = input("Digite o nome do arquivo csv de entrada (o arquivo deve estar no mesmo diretorio do executavel ou deve ser passado o caminho global como parametro) : ")

    def open_csv(self):
        Df = pandas.read_csv(self.file)
        self.quantidades_produzidas = np.array(Df.iloc[:, 0])
        self.custos_fixos = np.array(Df.iloc[:,1])
        self.custos_variaveis = np.array(Df.iloc[:,2])

    def calcula_variaveis(self):




if __name__=="__main__":
    maxLucro = MaxLucro()
    maxLucro.setup_wizard()
    maxLucro.input_file()
    maxLucro.open_csv()