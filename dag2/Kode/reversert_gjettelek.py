maks_forsøk = 10

min_tall = 0
maks_tall = 100

def midtpunkt(lavt, høyt):
    return (lavt+høyt)/2

print(f"Tenk på et tall mellom {min_tall} og {maks_tall}")

for forsøk in range(maks_forsøk):
    gjett = int(midtpunkt(min_tall, maks_tall))
    print(f"Tenker du på {gjett}?")
    svar = input("Var dette for høyt, for lavt eller riktig?")
    if svar == "riktig":
        print(f"Yay, jeg klarte det på {forsøk} forsøk!")
        break
    elif svar == "for høyt":
        maks_tall = gjett
    elif svar == "for lavt":
        min_tall = gjett
    else:
        print("Svar 'for høyt', 'for lavt' eller 'riktig'.")