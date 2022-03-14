from pylab import log, sign

def f(x):
    return -((x/100)**5 - 0.1*log((x+1)/100) - 0.5)

maks_forsøk = 100
min_tall = 0
maks_tall = 100
feilterskel = 0.00001

def midtpunkt(lavt, høyt):
    return (lavt+høyt)/2

for forsøk in range(maks_forsøk):
    gjett = midtpunkt(min_tall, maks_tall)
    print(f"Jeg gjetter {gjett}")
    print(f"f({gjett}) = {f(gjett)}")
    if abs(f(gjett)) < feilterskel:
        print(f"Yay, jeg klarte det på {forsøk} forsøk!")
        break
    elif sign(f(gjett)) == sign(f(maks_tall)):
        maks_tall = gjett
    else:
        min_tall = gjett

if abs(f(gjett)) >= feilterskel:
    print(f"Jeg brukte opp alle {maks_forsøk} forsøk.")
