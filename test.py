import os
from git import Repo

n=0

repo = Repo("C:/Users/fluff/Downloads/CODE/OTHER/garfield/garfield/.git")


while n < 2:
    f = open(f"test/myfile{n}.txt", "x")
    n = n + 1
    repo.index.add([f'test/myfile{n}.txt'])



    repo.index.commit(f'testing')
    origin = repo.remote('origin')
    origin.push()