# Vi skal lage en gjettelek
# Vi tenker på et tall mellom 0 og 100
# Brukeren får 10 forsøk
# For hvert forsøk skal brukeren gjette et tall
# Vi sier ifra om tallet er riktig, for stort eller for lite
# Derson antall forsøk er brukt opp er spillet over og brukeren har tapt

import random

fasit = random.randint(0, 100)
print(f"Fasiten er {fasit}.")
maks_forsøk = 10

for forsøk in range(maks_forsøk):
    print(f"Forsøk nr. {forsøk}")
    gjett = int(input("Gjett et tall mellom 0 og 100: "))
    if gjett == fasit:
        print("Du klarte det!")
        print("WINNER!")
        break
    elif gjett > fasit:
        print("Du gjettet for høyt.")
    else:
        print("Du gjettet for lavt.")

if gjett != fasit:
    print(f"Du har brukt opp dine {maks_forsøk} forsøk.")
    print("GAME OVER!")