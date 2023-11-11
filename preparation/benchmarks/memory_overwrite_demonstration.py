
import numpy as np


print("\n\n\n############ 1. Without `[:]` ############\n")

# Setup two variables referencing the same array, filled with ones
a = np.full(shape=4, fill_value=1)
b = a


# Both have the same id
print("#--- 1. Before ----#\n")
print(f"{id(a)} == {id(b)} : {a is b}")

# Same content
print(f"a = {a}")
print(f"b = {b}")


# Change `a` without the use of `[:]`
a = np.zeros_like(a)

print("\n\n#--- 1. After ----#\n")
print(f"{id(a)} == {id(b)} : {a is b}")                 # `a` is now a new object

print(f"a = {a}")
print(f"b = {b}")





# Same thing with `[:]`
print("\n\n\n\n############ 2. With `[:]` ############\n")

# Same setup
c = np.full(4, 1)
d = c


# Same id and content
print("#--- 2. Before ----#\n")
print(f"{id(c)} == {id(c)} : {c is d}")

# Same content
print(f"c = {c}")
print(f"d = {d}")


# Change `c` with `[:]`
c[:] = np.zeros_like(c)

print("\n\n#--- 2. After ----#\n")
print(f"{id(c)} == {id(d)} : {c is d}")                 # `c` is still pointing to the same memory

print(f"c = {c}")
print(f"d = {d}")                   # `d` has changed as well -> memory was overwritten, no new object was created
