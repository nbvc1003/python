import numpy as np

ar = np.arange(15).reshape(5,3)

print(ar)

br = ar[np.ix_([0,2,4],[0,2])]
print(br)
br[0,:] = 100
print(br)
print(ar)
