"""
Program menghitung luas segitiga
"""
alas=10
tinggi=6
luas_segitiga=alas*tinggi/2
print(f'Segitiga dengan alas {alas} dan tinggi {tinggi} memiliki luas {luas_segitiga}')

print('\nmembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas,tinggi):
    luas_segitiga=alas*tinggi/2
    return luas_segitiga

print(hitung_luas_segitiga(10,6))
print(hitung_luas_segitiga(20,2))