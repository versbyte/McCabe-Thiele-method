import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0, 1, 1000)

def courbeEQ(Pa, Pb):
    """
    This function draws the x-y equilibrium diagram of the most volatile component based
    on the their saturation vapor pressure.
    Pa = Saturation vapor pressure of the most volatile component
    Pb = Saturation vapor pressure of the less volatile component
    """
    global yeq
    yeq = (Pa*x)/(x*Pa + (1-x)*Pb) #y = f(x)
    plt.plot(x,x, color = 'k') # y = x
    plt.plot(x,yeq, color = 'k')

#Operating Line of the Rectifying section
def DOZE(xa, xd, R, q):
  global xdoze, ydoze, Ydoze
  Ydoze = (R / (R + 1)) * x + (xd / (R + 1))
  xdoze = ((-xd/(R+1)) - (xa/(q-1)))/((R/(R+1))-(q/(q-1)))
  ydoze = (R/(R+1))*xdoze + (xd/(R+1))
  plt.plot([xd, xdoze], [xd, ydoze], color = 'b')

#Operating Line of the Stripping section
def DOZA(xa, xd, xb, R, q):
  global Ydoza
  Ydoza = ((ydoze - xb) / (xdoze - xb)) * x + xb * (1 - ((ydoze - xb) / (xdoze - xb)))
  xdoza = ((-xd/(R+1)) - (xa/(q-1)))/((R/(R+1))-(q/(q-1)))
  ydoza = (R/(R+1))*xdoza + (xd/(R+1))
  plt.plot([xb, xdoza], [xb, ydoza], color = 'r')

#Q-line
def DA(xa, xd, R, q):
  global Yda
  Yda = (q / (q - 1)) * x - (xa / (q - 1))
  xda = ((-xd/(R+1)) - (xa/(q-1)))/((R/(R+1))-(q/(q-1)))
  yda = (R/(R+1))*xda + (xd/(R+1))
  plt.plot([xa, xda], [xa, yda], color = 'g')

#Plotting and Calculating the number of theoritical trays
def theoTrays(xd, xb):
    #interpolations
    feq = interp1d(yeq, x, kind = 'linear')
    fdoze = interp1d(x, Ydoze, kind = 'linear')
    fdoza = interp1d(x, Ydoza, kind = 'linear')
    current_x = xd
    current_y = xd
    tray_count = 0


    while current_x > xb:
        if(current_x >= xdoze):
           # Step 1: Move vertically to equilibrium curve (liquid to vapor)
          next_x = feq(current_y)
          plt.plot([current_x, next_x], [current_y, current_y], 'k-')  # Vertical line
          # Step 2: Move horizontally to operating line (vapor to liquid
          next_y = fdoze(next_x)
          plt.plot([next_x, next_x], [current_y, next_y], 'k-')  # Horizontal line
          # Update for next iteration
          current_x = next_x
          current_y = next_y
          tray_count += 1
        else:
          # Step 1: Move vertically to equilibrium curve (liquid to vapor)
          next_x = feq(current_y)
          plt.plot([current_x, next_x], [current_y, current_y], 'k-')  # Vertical line
          # Step 2: Move horizontally to operating line (vapor to liquid
          next_y = fdoza(next_x)
          plt.plot([next_x, next_x], [current_y, next_y], 'k-')  # Horizontal line
          # Update for next iteration
          current_x = next_x
          current_y = next_y
          tray_count += 1
    print("boiler + " ,tray_count-1)

#Mcabe-Thiele Diagram
def McabeThiele(xa, xd, xb, R, q, Pa, Pb):
  courbeEQ(Pa, Pb)
  DOZE(xa, xd, R, q)
  DOZA(xa, xd, xb, R, q)
  DA(xa, xd, R, q)
  theoTrays(xd, xb)
  #---------------------------------------------------------

  plt.xlabel('x (Mole fraction of component A in liquid)')
  plt.ylabel('y (Mole fraction of component A in vapor)')
  plt.xlim(0,1)
  plt.ylim(0,1)
  plt.grid()
  plt.show()


# Example usage
xa = 0.55 # Feed composition
xd = 0.95  # Distillate composition
xb = 0.05  # Bottoms composition
R = 4   # Reflux ratio
q = 0.99  # Feed thermal condition
Pa = 28.4 # Saturation vapor pressure of the most volatile component (mmHg)
Pb = 5.55 # Saturation vapor pressure of the less volatile component (mmHg)

McabeThiele(xa, xd, xb, R, q, Pa, Pb)