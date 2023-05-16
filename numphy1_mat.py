import numpy as np
 mat1 = np.zeros ((3, 3))
 mat2 = np.random.rand (2, 4)
 mat3 = np.ones ((4, 2))
 mat4 = np.matmul (mat2, mat3)
print ("Matrix1: \n", mat1)
print ("Matrix2: \n", mat2)
print ("Matrix3: \n", mat3)
print ("Matrix4: \n", mat4) sum = np.sum (mat2) print (sum)
