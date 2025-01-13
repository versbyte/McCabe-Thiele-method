import main as mc
xf = 0.458 # Feed composition
xd = 0.965 # Distillate composition
xb = 0.011  # Bottoms composition
R = 1.4  # Reflux ratio
q = 1 # Feed thermal condition
Pa = 95 # Saturation vapor pressure of the most volatile component (mmHg)
Pb = 23.76 # Saturation vapor pressure of the less volatile component (mmHg)
nm = 0.75 #murphy efficieny (60-70)%

mc.McabeThiele(xf, xd, xb, R, q, Pa, Pb, nm)
