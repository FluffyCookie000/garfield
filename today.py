import os
import shutil
import requests
from datetime import datetime as DT
from git import Repo

now = DT.now()
yy =  str(now.year)
mm = now.month
dd = now.day

print(f"{mm}  {yy}  {dd}")

#checks if year folder exists
if not os.path.exists(f'comic/{yy}'):
    os.makedirs(f'comic/{yy}')

#checks if month folder exists
if not os.path.exists(f'comic/{yy}/{mm}'):
    os.makedirs(f'comic/{yy}/{mm}')

md = mm
if int(mm) < 10:
    mm = f"0{mm}"
if int(dd) < 10:
    dd = f"0{dd}"

response = requests.get(f"http://images.ucomics.com/comics/ga/{yy}/ga{yy[2:]}{mm}{dd}.gif")
if response.status_code == 200:
    content = (f"http://images.ucomics.com/comics/ga/{yy}/ga{yy[2:]}{mm}{dd}.gif")
else:
    content = (f"http://images.ucomics.com/comics/ga/{yy}/ga{yy[2:]}{mm}{dd}.jpg")
print(content)

if len(str(mm)) == 2:
    if int(mm) < 10:
        mm = mm[1:]
if len(str(dd)) == 2:
    if int(dd) < 10:
        dd = dd[1:]


res = requests.get(content, stream = True)
with open(f"comic/{yy}/{md}/{content[-12:]}",'wb') as f:
    shutil.copyfileobj(res.raw, f)

repo = Repo("C:/Users/fluff/Downloads/git/garfield/.git")    
repo.index.add([f'comic/{yy}/{mm}/{content[-12:]}'])
repo.index.commit(f'{content[-12:]}')
origin = repo.remote('origin')
origin.push()