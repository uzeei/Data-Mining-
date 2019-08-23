import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9]
y=[2,4,5,7,-45459,13,145323,18,22]


y_interp=np.polyfit(x,y,10)

print(y_interp)

p=np.poly1d(y_interp)
print(p)
print(6,p(6))

plt.plot(x,y,'r-')
plt.plot(x,p(x),'b+')
plt.show()
