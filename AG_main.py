from monedero import *
from AG import *

def main():
    coins = [ 1, 20, 5, 1, 2, 5, 5, 1, 5, 2, 2, 1, 10, 5, 10, 5, 20, 20, 20, 5, 1, 1, 20, 20, 1, 10, 2, 10, 5, 2, 10, 1, 20, 1, 20, 10, 5, 5, 20, 2, 10, 1, 2, 5, 10, 20, 10, 2, 5, 5, 20, 1, 1, 5, 10, 10, 10, 1, 5, 2, 1, 2, 10, 20, 2, 10, 10, 20, 5, 10, 1, 2, 1, 5, 20, 2, 5, 1, 5, 10, 2, 5, 10, 2, 1, 1, 1, 10, 20, 10, 20, 2, 2, 10, 20, 10, 1, 1, 5, 2]
    monedas = Monedero(coins)
    alelos = len(coins)
    individuos = 40
    tamano_gen = 1 
    generaciones = 5000
    factor_mutacion = 0.01
    ag = AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, monedas)
    ag.run()

main()