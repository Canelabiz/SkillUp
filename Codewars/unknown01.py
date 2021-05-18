

def ddd(bob):
    d = {}
    for a in bob:
        it = iter(a.split())
        d += dict(zip(it, it))
    return d



b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
print(ddd(b))