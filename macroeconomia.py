import bem 
import numpy as np
from prettytable import PrettyTable

class macroEconomia:
    def __init__(self):
        self.bens = None
        self.pib_nominal = None
        self.pib_real = None
        self.inflacao = None
        self.deflacao = None
        self.bens10 = []
        self.matriz_transposta = None


    def setup_wizard(self):
        print("----------------------------\n")
        print("Calculo do PIB real, PIB nominal, inflação e deflação")
        print("----------------------------\n")
        print("Calculamos os valores do PIB real e nominal a partir dos valores e quantidades de bens disponíveis\n")
        print("Entrada: Em um arquivo .txt cada linha representa um bem e os valores separados por ; representam os diferentes parâmetros, y para ano, p para preço e q para quantidade.\n")
        print("Saida: PIB real, PIB nominal, inflação e deflação \n")
        print("----------------------------\n")

    def open_txt(self):
        print("----------------------------\n")
        self.file = input("Digite o nome do arquivo txt de entrada (o arquivo deve estar no mesmo diretorio do executavel ou deve ser passado o caminho global como parametro) : ")
        print("----------------------------\n")
        f = open(self.file)
        self.bens = f.readlines()
        self.bens = [x.strip() for x in self.bens] #y:ano,p:preco,q:quantidade;

        for obj in self.bens:
            registros = obj.split(";")# todos os regis do bem
            anos = []
            precos = []
            quantidades = []

            for regi in registros:
                valores = regi.split(",")
                anos.append(int(valores[0][2:]))
                precos.append(float(valores[1][2:]))
                quantidades.append(float(valores[2][2:]))    

            b = bem.bem(anos,precos,quantidades)  
            self.bens10.append(b)
 

        
    def calcular_pib_real(self):
        my_pib_real = np.zeros(self.bens10[0].anos.shape)
        preco_base = None        
        for bem in self.bens10:
            preco_base = np.full(self.bens10[0].preco.shape,bem.preco[0])
            my_pib_real = my_pib_real + preco_base * bem.quantidade
        self.pib_real = np.round(my_pib_real,decimals=2)  

    def calcular_pib_nominal(self):
        my_pib_nominal = np.zeros(self.bens10[0].anos.shape)
        for bem in self.bens10:
            my_pib_nominal = bem.preco * bem.quantidade + my_pib_nominal        
        self.pib_nominal = np.round(my_pib_nominal,decimals=2)  

    
    def calcular_deflator(self):
        self.deflacao = np.round(100*self.pib_nominal/self.pib_real,decimals=2)

    def calcular_inflacao(self):        
        self.inflacao = [self.deflacao[x+1]-self.deflacao[x] for x in range(len(self.deflacao)-1)]
        self.inflacao.insert(0,0)

    def gerar_table(self):
        t = PrettyTable(["ANO","PIB_REAL","PIB_NOMINAL","DEFLACAO","INFLACAO"])
        for n in self.matriz_transposta:
            t.add_row(list(n))
        print(t)


    def transpuser(self):
        self.matriz_transposta = np.stack([self.bens10[0].anos, self.pib_real, self.pib_nominal, self.deflacao, self.inflacao])
        self.matriz_transposta = np.transpose(self.matriz_transposta)



if __name__=="__main__":
    macroEco = macroEconomia()
    macroEco.setup_wizard()
    macroEco.open_txt()
    macroEco.calcular_pib_nominal()
    macroEco.calcular_pib_real()
    macroEco.calcular_deflator()
    macroEco.calcular_inflacao()
    macroEco.transpuser()
    macroEco.gerar_table()

