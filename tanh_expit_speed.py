import time
import numpy as np
from scipy.special import expit






repeats = 1000000

start1 = time.time()
a = 0.0
for i in range(0, repeats):
   a = np.tanh(np.random.random())
ende1 = time.time()
diff1 = ende1-start1


start2 = time.time()
b = 0.0
for i in range(0, repeats):
   b = expit(np.random.random())
ende2 = time.time()
diff2 = ende2-start2

timediff = diff2-diff1

print("tanh:  " + str(round(diff1,10)) + "s")
print("expit: " + str(round(diff2,10)) + "s")
print("----------------------")
print("diff:  " + str(round(timediff,10)) + "s")
print("(expit - tanh)")
print("(repeats: " + str(repeats) + ")")
