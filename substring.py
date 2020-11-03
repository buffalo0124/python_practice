Barcode = "ACTGTCTTACC"
k_mer = 3

x = [Barcode[i:i+k_mer] for i in range(0, len(Barcode), k_mer)]
print(x)
