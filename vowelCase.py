str1 = input("Enter a string:: ")
str1 = str1.upper()
# countA, countE, countI, countO, countU, countC = 0
countA = 0
countE = 0
countI = 0
countO = 0
countU = 0
countC = 0
great = ""
for v in str1:
    print(v)
    if v == "A":
        countA += 1
    elif v == "E":
        countE += 1
    elif v == "I":
        countI += 1
    elif v == "0":
        countO += 1
    elif v == "U":
        countU += 1
    else:
        countC += 1
print("A=", countA, "E=", countE, "I=", countI, "O=",
      countO, "U=", countU, "Consonant=", countC)

if countA > countE and countA > countI and countA > countI and countA > countO and countA > countU:
    great = countA
elif countE > countA and countE > countI and countE > countI and countE > countO and countE > countU:
    greate = countE
elif countI > countE and countI > countA and countI > countI and countI > countO and countI > countU:
    greate = countI
# checkPrime(countA)
