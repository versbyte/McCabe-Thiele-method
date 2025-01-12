import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0, 1, 100000)

def courbeEQ(Pa, Pb, nm):
    """
    This function draws the x-y equilibrium diagram of the most volatile component based
    on the their saturation vapor pressure.
    Pa = Saturation vapor pressure of the most volatile component
    Pb = Saturation vapor pressure of the less volatile component
    """
    global yeq
    y1 = (Pa*x)/(x*Pa + (1-x)*Pb) #y = f(x)
    yeq = (y1 - x)*nm + x #murphy efficiency
    plt.plot(x,x, color = 'k') # y = x
    plt.plot(x,yeq, color = '#006400')

#Operating Line of the Rectifying section
def DOZE(xa, xd, R, q):
  global xdoze, ydoze, Ydoze
  Ydoze = (R / (R + 1)) * x + (xd / (R + 1))
  xdoze = -((xd/(R+1)) + (xa/(q-1)))/((R/(R+1))-(q/(q-1)))
  ydoze = (R/(R+1))*xdoze + (xd/(R+1))
  plt.plot([xd, xd],[0, xd], color = 'k',  linestyle = '--')
  plt.plot([xd, xdoze], [xd, ydoze], color = 'k')

#Operating Line of the Stripping section
def DOZA(xa, xd, xb, R, q):
  global Ydoza
  Ydoza = ((ydoze - xb) / (xdoze - xb)) * x + (ydoze - ((ydoze - xb)/(xdoze - xb))*xdoze)
  plt.plot([xb, xb],[0, xb], color = 'k',  linestyle = '--')
  plt.plot([xb, xdoze], [xb, ydoze], color = 'k')

#Q-line
def DA(xa, xd, R, q):
  global Yda
  Yda = (q / (q - 1)) * x - (xa / (q - 1))
  xda = ((-xd/(R+1)) - (xa/(q-1)))/((R/(R+1))-(q/(q-1)))
  yda = (q/(q-1))*xda - (xa/(q-1))
  plt.plot([xa, xa],[0, xa], color = 'k',  linestyle = '--')
  plt.plot([xa, xda], [xa, yda], 'k-')
  fda = interp1d(x,yeq, kind = 'linear')
  
  #Rmin calculation
  ydaeq = fda(xa)
  ymin = ((ydaeq - xd)/(xa - xd)) * x + xd * (1- (ydaeq - xd)/(xa - xd))
  fmin = interp1d(x, ymin, kind = 'linear')
  global Rmin
  Rmin = xd/fmin(0) - 1


#Plotting and Calculating the number of theoritical trays
def theoTrays(xd, xb):
    #interpolations
    feq = interp1d(yeq, x, kind = 'linear')
    fdoze = interp1d(x, Ydoze, kind = 'linear')
    fdoza = interp1d(x, Ydoza, kind = 'linear')
    current_x = xd
    current_y = xd
    global tray_count
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
def McabeThiele(xa, xd, xb, R, q, Pa, Pb, nm):
  courbeEQ(Pa, Pb, nm)
  DOZE(xa, xd, R, q)
  DOZA(xa, xd, xb, R, q)
  DA(xa, xd, R, q)
  theoTrays(xd, xb)
  #---------------------------------------------------------
  plt.text(0.1, 0.9, "Murphy effiency: %.2f" %(nm), fontsize = 8)
  plt.text(0.1, 0.87, "Number of trays: %.d" %(tray_count), fontsize = 8)
  plt.text(0.1, 0.84, "Rectification ratio: R = %.2f" %(R), fontsize = 8)
  plt.text(0.1, 0.81, "Minimal rectification ratio: Rmin = %.2f" %(Rmin), fontsize = 8)

  plt.xlabel('x (Mole fraction of component A in liquid)')
  plt.ylabel('y (Mole fraction of component A in vapor)')
  plt.xlim(0,1)
  plt.ylim(0,1)
  plt.grid()
  plt.show()


# Example usage
xf = 0.458 # Feed composition
xd = 0.965 # Distillate composition
xb = 0.011  # Bottoms composition
R = 1.4  # Reflux ratio
q = 0.99 # Feed thermal condition
Pa = 127 # Saturation vapor pressure of the most volatile component (mmHg)
Pb = 23.76 # Saturation vapor pressure of the less volatile component (mmHg)
nm = 0.80 #murphy efficieny (60-70)%
McabeThiele(xf, xd, xb, R, q, Pa, Pb, nm)