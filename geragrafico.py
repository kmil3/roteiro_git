from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt

def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores() 
    for serie in valores:
       plt.plot(serie)
    print(valores)
    plt.plot(valores)
    plt.title('Gráfico de linhas')
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    plt.show()
    
 
main()