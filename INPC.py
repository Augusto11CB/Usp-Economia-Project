import numpy as np
import matplotlib.pyplot as plt

class INPC:
	

    def setup_wizard(self):
        print("----------------------------\n")
        print("Calculo do INPC")
        print("----------------------------\n")
        print("Calculamos o índice INPC para uma cesta básica\n")
        print("Entrada: Um arquivo .csv que possui todos os itens da cesta basica, cada linha diz respeito a um item; a primeira coluna diz a quantidade daquele produto na cesta basica, as demais colunas dizem respeito aos valores de preço em cada ano.\n")
        print("Saida: Uma tabela com os INPC em relação ao primeiro ano do arquivo \n")
        print("----------------------------\n")

    def input_data(self):
        print("----------------------------\n")
        self.file = input("Digite o nome do arquivo csv de entrada (o arquivo deve estar no mesmo diretorio do executavel ou deve ser passado o caminho global como parametro) : ")
        print("----------------------------\n")

    def read_csv(self):

        lines = open(self.file).readlines()
        lines = [li.strip() for li in lines]
        lines = [[float(x) for x in li.split(",")] for li in lines]
        return np.array(lines)


    def open_csv(self):
        Df = self.read_csv()
        self.quantidade_de_itens = Df.shape[0]
        self.quantidade_demandada = Df[:,0]
        self.data = Df


    def calculo(self):

    	self.inpc = np.zeros((self.data.shape[0],self.data.shape[1]-1))

    	self.inpc = np.sum(np.transpose(self.data[:,1:])*self.quantidade_demandada,axis=0)
    	print(self.inpc)
    	self.inpc = self.inpc/self.inpc[:,0]

    def gerar_table(self):
        t = PrettyTable(["ANO","INPC"])
        
        t.add_column(list(range(self.data.shape[1]-1)))
        t.add_column(list(self.inpc))
        print(t)


if __name__ == '__main__':

	inpc = INPC()
	inpc.setup_wizard()
	inpc.input_data()
	inpc.open_csv()
	inpc.calculo()
	inpc.gerar_table()