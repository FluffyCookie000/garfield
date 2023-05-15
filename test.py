import os
from git import Repo

n=0

while n == 2:
    f = open(f"test/myfile{n}.txt", "x")
    n = n + 1