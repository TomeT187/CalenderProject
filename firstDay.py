import imp
from math import floor

#K = 2
# K = day

m = 6
# Month JFM AMJ JAS OND 144 025 036 146 March = 1, April = 2, ... Jan = 11, Feb = 12

#C = 20
#C = Century

Y = 22
#Year (jan and feb are year before)




#W = (K + floor(2.6 * (m) - 0.2) - 2 *C + Y + floor(Y/4) + floor(C/4) ) % 7


W = (floor(2.6 * (m) - 0.2) - 34 + Y + floor(Y/4) ) % 7
week = ("Sunday","Monday", "Tuesday", "Wednessday","Thursday", "Friday","Saturday")
print(week[W])