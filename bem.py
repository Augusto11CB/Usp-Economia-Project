import numpy as np 

class bem:
    def __init__(self,ano,preco,quantidade):
        self.anos = np.array(ano)
        self.preco = np.array(preco)
        self.quantidade = np.array(quantidade)