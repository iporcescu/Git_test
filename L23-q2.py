import numpy as np

a= np.zeros((22, 22))
#print(a)
for i in range(22):
    a[i][i]=1

print(a.trace())