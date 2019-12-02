

import numpy as np
# 0  1  2     2  1  0    1  0  2
# 2  3  2  -> 2  3  2 -> 3  2  2
ar = np.array([
                [
                    [1,2],[3,4],[5,6]
                ],
                [
                    [71,72],[73,74],[75,76]
                ]
            ]
            )
# 복습 필요..
print(ar.transpose())
print(ar.transpose(2,1,0))
print(ar.transpose(1,0,2))
