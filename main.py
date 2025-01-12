import numpy as np
import matplotlib.pyplot as plt


def courbeEQ(vol_a_b):
    x = np.linspace(0, 1, 1000)
    y = (vol_a_b*x)/(x*(vol_a_b-1)+1)
    plt.plot(x,x, color = 'k')
    plt.plot(x,y, color = 'k')

def DOZE(xa, xd, R, q):
  xdoze = ((-xd/(R+1)) - (xa/(q-1)))/((R/(R+1))-(q/(q-1)))
  ydoze = (R/(R+1))*xdoze + (xd/(R+1))
  plt.plot([xd, xdoze], [xd, ydoze], color = 'b')


def DOZA(xa, xd, xb, R, q):
  xdoza = ((-xd/(R+1)) - (xa/(q-1)))/((R/(R+1))-(q/(q-1)))
  ydoza = (R/(R+1))*xdoza + (xd/(R+1))
  plt.plot([xb, xdoza], [xb, ydoza], color = 'r')

def DA(xa, xd, R, q):
  xda = ((-xd/(R+1)) - (xa/(q-1)))/((R/(R+1))-(q/(q-1)))
  yda = (R/(R+1))*xda + (xd/(R+1))
  plt.plot([xa, xda], [xa, yda], color = 'g')
  

def McabeThiele(xa, xd, xb, R, q, vol_a_b):
  #Construction de McAbe Thiele
  courbeEQ(vol_a_b)
  DOZE(xa, xd, R, q)
  DOZA(xa, xd, xb, R, q)
  DA(xa, xd, R, q)
  
  plt.xlabel('x (Mole fraction of component A in liquid)')
  plt.ylabel('y (Mole fraction of component A in vapor)')
  plt.xlim(0,1)
  plt.ylim(0,1)
  plt.grid()
  plt.show()


McabeThiele(0.4, 0.9, 0.1, 2, 0.99, 3)