# Erik setter inn 10 000 kr på BSU med 2.85 rente
# Hvor mye er etter 10 år?

penger = 10000
rente = 1.0285
antall_år = 10

for år in range(antall_år):
    penger *= rente
    print(f"Etter {år:2} år er det {penger:.2f} kr.")
