import requests 
import shutil 
import os
from git import Repo
from datetime import datetime as DT

os.makedirs("comic")

today = DT.now()
cyy = today.year
cmm = today.month
cdd = today.day
badmonths = [4, 6, 9, 11]
badyears = [1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2022]

n = 0
amount = 0
dc = 0
mc = 0

yy = "1978"
mm = "6"
dd = "19"

os.makedirs(f"comic/{yy}")
os.makedirs(f"comic/{yy}/{mm}")

while n == 0:
    if int(mm) < 10:
        mm = f"0{mm}"
        mc = 1
    if int(dd) < 10:
        dd = f"0{dd}"
        dc = 1

    response = requests.get(f"http://images.ucomics.com/comics/ga/{yy}/ga{yy[2:]}{mm}{dd}.gif")
    if response.status_code == 200:
        content = (f"http://images.ucomics.com/comics/ga/{yy}/ga{yy[2:]}{mm}{dd}.gif")
    else:
        content = (f"http://images.ucomics.com/comics/ga/{yy}/ga{yy[2:]}{mm}{dd}.jpg")
    amount = amount + 1
    print(content)

    
    if mc == 1:
        mm = mm[1:]
        mc = 0
    if dc == 1:
        dd = dd[1:]
        dc = 0

    res = requests.get(content, stream = True)
    with open(f"comic/{yy}/{mm}/{content[-12:]}",'wb') as f:
        shutil.copyfileobj(res.raw, f)

    repo = Repo("C:/Users/fluff/Downloads/CODE/OTHER/garfield/garfield/.git")
    repo.index.add([f'comic/{yy}/{mm}/{content[-12:]}"'])
    repo.index.commit(f'{content[-12:]}')
    origin = repo.remote('origin')
    origin.push()


    if int(yy) == today.year:
        if int(mm) == today.month:
            if int(dd) == today.day:
                n = 1

    for bm in badmonths:
        if int(mm) == bm:
            if int(dd) == 30:
                mm = int(mm) + 1
                mm = str(mm)
                os.makedirs(f"comic/{yy}/{mm}")
                dd = 0
        
        elif int(mm) == 2:
                if yy == "1980" or yy == "1984" or yy == "1988" or yy == "1992" or yy == "1996" or yy == "2000" or yy == "2004" or yy == "2008" or yy == "2012" or yy == "2016" or yy == "2022":
                    if int(dd) == 29:
                        mm = int(mm) + 1
                        mm = str(mm)
                        os.makedirs(f"comic/{yy}/{mm}")
                        dd = 0   
                else:
                    if int(dd) == 28:
                        mm = int(mm) + 1
                        mm = str(mm)
                        os.makedirs(f"comic/{yy}/{mm}")
                        dd = 0
        else:
            if int(dd) == 31:
                if int(mm) == 12:
                    yy = int(yy) + 1
                    yy = str(yy)
                    os.makedirs(f"comic/{yy}")
                    mm = 0
                    mm = str(mm)

                mm = int(mm) + 1
                mm = str(mm)
                os.makedirs(f"comic/{yy}/{mm}")
                dd = 0            

    dd = int(dd) + 1
    dd = str(dd)




print(f"\n\n\n\ndone in {str((DT.now() - today))}\n amount of comics: {amount}")
