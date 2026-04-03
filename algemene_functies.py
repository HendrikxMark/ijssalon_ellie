def mijn_functie_1(a):
    tabel = {
        2: 4,
        4: 16,
        10: 100,
        12: 144
    }
    return tabel[a]

def mijn_functie_2(a, b):
    return [a + b, a - b, a * b, a // b]

print(mijn_functie_1(4))
print(mijn_functie_2(10, 5))