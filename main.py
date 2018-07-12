from MaxLucro import MaxLucro
from  macroeconomia  import macroEconomia
from elasticidade import Elasticidade
from oferta_x_demanda import oferta_x_demanda
from ISLM import ISLM
import sys

if __name__=="__main__":

    maxLucro = MaxLucro()
    el = Elasticidade()
    mc = macroEconomia()
    ofertaDemanda = oferta_x_demanda()
    islm =ISLM()
            

    while True:
        print("----------------------------\n")
        print("PROGRAMA DE ECONOMIA\n")
        print("----------------------------\n")
        print("Digite o numero correspondente para acessar cada funcionalidade:\n")
        print("****MICROECONOMIA****\n")
        print("1 - Maximizacao do Lucro\n")
        print("2 - Elasticidade \n")
        print("3 - Oferta e Demanda \n")
        print("****MACROECONOMIA****\n")
        print("4 - PIB e inflacao\n")
        print("5 - Simulador IS-LM\n")

        print("Para sair digite 0 \n")

        
        i = input("Digite o comando: ")
      

        if(i =='1'):
            maxLucro = MaxLucro()
            maxLucro.setup_wizard()
            maxLucro.input_data()
            maxLucro.open_csv()
            maxLucro.calcula_variaveis()
            maxLucro.print_explicacao()
            maxLucro.plota_grafico()

        elif(i=='2'):
            el = Elasticidade()
            el.setup_wizard()
            el.input_data()
            el.open_csv()
            el.calculos()
            el.resultados()

        elif(i=='3'):
                
            ofertaDemanda.setup_wizard()
            ofertaDemanda.input_data()
            ofertaDemanda.open_csv()
            ofertaDemanda.curva_oferta_demanda()


        elif(i=='4'):
            macroEco = macroEconomia()
            macroEco.setup_wizard()
            macroEco.open_txt()
            macroEco.calcular_pib_nominal()
            macroEco.calcular_pib_real()
            macroEco.calcular_deflator()
            macroEco.calcular_inflacao()
            macroEco.transpuser()
            macroEco.gerar_table()

        elif(i=='5'):
            islm =ISLM()
            islm =ISLM()
            islm.setup_wizard()
            islm.inEvento()
            islm.plotar()

        elif(i=='0'):
            sys.exit(0)

        else:
            print("Error, digite uma entrada valida")
