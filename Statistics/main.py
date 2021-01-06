import csv
#import statistics
import math
import matplotlib.pyplot as plot
import sys

def medie(data):
    return sum(data) / len(data)

#print(medie(list_int))

def mediana(data):
    sortedlist = sorted(data)
    llen = len(data)
    i = (llen - 1) // 2
    #print(i)
    if (llen % 2 != 0):
        return sortedlist[i]
    return (sortedlist[i] + sortedlist[i + 1]) / 2

#print(statistics.median(list_int))
#print(mediana(list_int))

def varianta(data):
    n = len(data)
    m = medie(data)
    dev = [(x - m) ** 2 for x in data]
    var = sum(dev) / n
    return var

def devstd(data):
    var = varianta(data)
    std_dev = math.sqrt(var)
    return std_dev

#print(devstd([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))
#print(statistics.pstdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))

def maxim(data):
    max = data[0]
    for i in range (1, len(data)):
        if data[i] > max:
            max = data[i]
    return max

def minim(data):
    min = data[0]
    for i in range (1, len(data)):
        if data[i] < min:
            min = data[i]
    return min

#print(maxim(list_int))
#print(minim(list_int))

def cvartile(data):
    n = len(data)
    data = sorted(data)
    i = n // 2
    if n % 2:
        lowdata = data[:i]
        highdata = data[i + 1:]
    else:
        lowdata = data[:i]
        highdata = data[i:]

    q1 = mediana(lowdata)
    q2 = mediana(data)
    q3 = mediana(highdata)

    return (q1, q2, q3)

#print(cvartile([1,2,3,4,5,6,7,8,9]))

def covarianta(data1, data2):
    n = len(data1)
    numarator = []
    x = medie(data1)
    y = medie(data2)
    dif_d1 = [round((xi - x), 3) for xi in data1]
    dif_d2 = [round((yi - y), 3) for yi in data2]
    #print(dif_d2)
    for i in range (0, n):
        numarator.append(dif_d1[i] * dif_d2[i])
    suma_numarator = sum(numarator)
    #print(numarator)
    #print(suma_numarator)
    covar = suma_numarator / n
    #print(covar)
    return covar

#X = [1,2,3,4,5]
#Y = [3,5,11,11,16]
#print(covarianta(X,Y))

def corelatie(data1 ,data2):
    cov = covarianta(data1, data2)
    pdevstd = devstd(data1) * devstd(data2)
    return round(cov / pdevstd, 3)

"""X = [14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2]
Y = [215,325,185,332,406,522,412,614,544,421,445,408]
print(corelatie(X,Y))
"""


with open(sys.argv[1], "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    list = []
    list2 = []
    listN = []
    listS = []
    suma = 0
    for lines in csv_reader:
      list.append(lines[1])
      list2.append(lines[3])
    list.pop(0)
    list2.pop(0)
    for i in list:
        for j in i:
            a = ord(j)
            #print(a)
            suma = suma + a
        listS.append(suma)
        suma = 0
    #print(listS)
    for i in list2:
        for j in i:
            a = ord(j)
            #print(a)
            suma = suma + a
        listN.append(suma)
        suma = 0
    #print(listN)
    #print(list2)
    #print(statistics.mean(listN))


listIQ = []
with open(sys.argv[1], "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        listIQ.append(lines[2])
listIQ.pop(0)
for i in range(0, len(list)):
    listIQ[i] = int(listIQ[i])
#print(listIQ)

listV = []
with open(sys.argv[1], "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        listV.append(lines[0])
listV.pop(0)
for i in range(0, len(list)):
    listV[i] = int(listV[i])
#print(listV)


while True:
    x = input("Alegeți o coloană (scrisă cu litere mari). Introduceți tasta Q pentru a ieși din program. ")
    if(x == "q" or x == "Q"):
        break
    if(x != "VARSTA" and x != "SEX" and x != "IQ" and x != "NATIONALITATE"):
        print("Ați introdus o coloană greșită. Încercați din nou. Coloanele sunt: VARSTA, SEX, IQ și NATIONALITATE.")
        continue

    if(x == "VARSTA"):
        print(listV)
        print("Media coloanei VARSTA este " + str(medie(listV)) + ".")
        print("Mediana coloanei VARSTA este " + str(mediana(listV)) + ".")
        print("Deviatia standard a coloanei VARSTA este " + str(devstd(listV)) + ".")
        print("Minimul coloanei VARSTA este " + str(minim(listV)) + ".")
        print("Maximul coloanei VARSTA este " + str(maxim(listV)) + ".")
        print("Cvartilele coloanei VARSTA sunt " + str(cvartile(listV)) + ".")

    if (x == "SEX"):
        print(listS)
        print("Media coloanei SEX este " + str(medie(listS)) + ".")
        print("Mediana coloanei SEX este " + str(mediana(listS)) + ".")
        print("Deviatia standard a coloanei SEX este " + str(devstd(listS)) + ".")
        print("Minimul coloanei SEX este " + str(minim(listS)) + ".")
        print("Maximul coloanei SEX este " + str(maxim(listS)) + ".")
        print("Cvartilele coloanei SEX sunt " + str(cvartile(listS)) + ".")

    if (x == "IQ"):
        print(listIQ)
        print("Media coloanei IQ este " + str(medie(listIQ)) + ".")
        print("Mediana coloanei IQ este " + str(mediana(listIQ)) + ".")
        print("Deviatia standard a coloanei IQ este " + str(devstd(listIQ)) + ".")
        print("Minimul coloanei IQ este " + str(minim(listIQ)) + ".")
        print("Maximul coloanei IQ este " + str(maxim(listIQ)) + ".")
        print("Cvartilele coloanei IQ sunt " + str(cvartile(listIQ)) + ".")

    if (x == "NATIONALITATE"):
        print(listN)
        print("Media coloanei NATIONALITATE este " + str(medie(listN)) + ".")
        print("Mediana coloanei NATIONALITATE este " + str(mediana(listN)) + ".")
        print("Deviatia standard a coloanei NATIONALITATE este " + str(devstd(listN)) + ".")
        print("Minimul coloanei NATIONALITATE este " + str(minim(listN)) + ".")
        print("Maximul coloanei NATIONALITATE este " + str(maxim(listN)) + ".")
        print("Cvartilele coloanei NATIONALITATE sunt " + str(cvartile(listN)) + ".")

    print("Covarianta dintre VARSTA si IQ este " + str(covarianta(listV, listIQ)) + ".")
    print("Coeficientul de corelatie dintre VARSTA si IQ este " + str(corelatie(listV, listIQ)) + ".")
    plot.scatter(listV, listIQ)
    plot.title('Relația dintre vârstă și IQ')
    plot.xlabel('Vârstă')
    plot.ylabel('IQ')
    plot.show()
