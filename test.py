import time

x = 0

t0 = time.time()
for i in range(1000000):
    x += 1
    
t = time.time() - t0

print("one million iterations in ", t, " seconds")
# real python3 is about 100x faster

x = 0
t0 = time.time()
for i in range(1000000):
    x = x+1
    
t = time.time() - t0
print("one million iterations in ", t, " seconds")
# real python3 is about 100x faster
