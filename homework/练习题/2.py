

import math
for i in range(1,10):
     for j in range(1,10):
       s=i*j
       print(min(i,j),"*",max(i,j),"=",format(i*j,"-3d"),end=" ")
    print()