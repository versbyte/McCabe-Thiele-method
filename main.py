import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ax

def courbeEQ(vol_a_b):
    '''
    Dessine la courbe d'equilibre d'un melange binaire
    '''
    x = np.linspace(0, 1, 100)
    global y
    #Equation de la courbe d'equilibre
    y = (vol_a_b*x)/(x*(vol_a_b-1)+1)

    #Bissectrice
    plt.plot(x,x)

    #Courbe d'equilibre
    plt.plot(x,y)
    plt.grid()
    plt.show()


courbeEQ(3.39)

def McabeThiele(xd, xb, R):
  #Construction de McAbe Thiel
  return 0

