import numpy as np


snames = np.array(["Sam", "Manoj", "vicky","Karan", "zadan"], dtype=str)
nums = np.array([126,343,55,77,885,3434], dtype=np.int32)
print(snames)
print(nums)
s1 = np.arange(10)
print("s1 : ",s1)

s2 = np.zeros(10)
print("s2 : ", s2)

s3 = np.ones(10)
print("s3 : ",s3)

s4 = np.random.rand(10)
print("s4 : ",s4)


s5 = (np.random.rand(10)*1000).astype(int)
print("s5 : ", s5)

t1 = np.array([[112,434,66],[331,55,616],[100,200,3100],[10001,8300,4800]])
print("t1 : \n", t1)
t2 = np.arange(1,10).reshape(3,3)
print("t2 : \n", t2)
t3 = (np.random.rand(9)*100).astype(int).reshape(3,3)
print("t3 : ", t3)