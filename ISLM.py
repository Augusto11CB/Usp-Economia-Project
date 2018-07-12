import numpy as np
import matplotlib.pyplot as plt
class ISLM:
    
    def setup_wizard(self):
        print("----------------------------\n")
        print("Simulador de mudanças na IS-LM \n ")
        print("----------------------------\n")
        print("Simulamos as mudanças ocorridas na ISLM a partir de eventos predefinidos.\n")
        print("Entrada: Um evento predefinido que afeta a ISLM. \n")
        print("Saida: Um gráfico que mostra as modificações na IS-LM que esse evento causa\n")
        print("----------------------------\n")

    def inEvento(self):
        print("Digite o número da mudança que deseja analisar:\n")
        print("1 - Aumento do gasto público\n")
        print("2 - Diminuição do gasto público\n")
        print("3 - Aumento dos impostos\n")
        print("4 - Diminuição dos impostos\n")
        print("5 - Aumento da oferta de moeda\n")
        print("6 - Diminuição da oferta de moeda\n")
        print("7 - Aumento nas reservas bancárias\n")
        print("8 - Diminuição da taxa de reserva bancária\n")
        self.evento= int(input("Digite o numero do evento selecionado: "))

    def plotar(self):

        self.x = np.array([800,900,1000,1100,1200])
        self.IS = np.array([0.15,0.12,0.09,0.06,0.03])
        self.LM = np.array([0.03,0.06,0.09,0.12,0.15])

        plt.title("Deslocamento na IS-LM com o evento "+str(self.evento))

        plt.plot(self.x,self.IS, label = "IS")
        plt.plot(self.x, self.LM, label= "LM")


        if(self.evento==1):
            plt.plot(self.x,np.array([0.20,0.17,0.14,0.11,0.08]), label="IS deslocada")
            plt.xlabel("Deslocamento para direita da IS")
        elif(self.evento==2):
            plt.plot(self.x,np.array([0.12,0.09,0.06,0.03,0.0]), label="IS deslocada")
            plt.xlabel("Deslocamento para esquerda da IS")
        elif(self.evento==3):
            plt.plot(self.x,np.array([0.12,0.09,0.06,0.03,0.0]), label="IS deslocada")
            plt.xlabel("Deslocamento para esquerda da IS")
        elif(self.evento==4):
            plt.plot(self.x,np.array([0.20,0.17,0.14,0.11,0.08]), label="IS deslocada")
            plt.xlabel("Deslocamento para direita da IS")
        elif(self.evento==5):
            plt.plot(self.x,np.array([0.0,0.03,0.06,0.09,0.12]), label="LM deslocada")
            plt.xlabel("Deslocamento para direita da LM")
        elif(self.evento==6):
            plt.plot(self.x,np.array([0.06,0.09,0.12,0.15,0.18]), label="LM deslocada")
            plt.xlabel("Deslocamento para esquerda da LM")
        elif(self.evento==7):
            plt.plot(self.x,np.array([0.06,0.09,0.12,0.15,0.18]), label="LM deslocada")
            plt.xlabel("Deslocamento para esquerda da LM")
        elif(self.evento==8):
            plt.plot(self.x,np.array([0.0,0.03,0.06,0.09,0.12]), label="LM deslocada")
            plt.xlabel("Deslocamento para direita da LM")
        
        else:
            print("número invalido")
        plt.legend()
        plt.show()



if __name__ == '__main__':
    
    islm =ISLM()
    islm.setup_wizard()
    islm.inEvento()
    islm.plotar()