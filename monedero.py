class Monedero:
    def __init__(self, coins):
        self._coins = coins

    def f(self, cromosoma):
        f = 0
        take = bool
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                take = True

                if i > 0:
                    if cromosoma[i-1]:
                        take = False

                if i < len(cromosoma)-1:
                    if cromosoma[i+1]:
                        take = False
                        
            else:
                take = False
            
            if take:
                f += self._coins[i]
        
        return f
