import random

def Number(data,alt, ust):
    number=0
    for i in data:
        if (i>=alt and i<ust):
            number +=1
    return number

def Ustel(nm,P):
    avg=P[0]
    data=[]
    for i in range(nm):
        data.append(random.expovariate(avg))
    return data

def Normal(nm,P):
    avg=P[0]
    std=P[1]
    data=[]
    for i in range(nm):
        data.append(random.normalvariate(avg,std))
    return data

def Weibull(nm,P):
    alpha=P[0]
    beta=P[1]
    data=[]
    for i in range(nm):
        data.append(random.weibullvariate(alpha,beta))
    return data

def Lognormal(nm,P):
    avg=P[0]
    std=P[1]
    data=[]
    for i in range(nm):
        data.append(random.lognormvariate(avg,std))
    return data

def Beta(nm,P):
    alpha = P[0]
    beta = P[1]
    data = []
    for i in range(nm):
        data.append(random.betavariate(alpha, beta))
    return data

def Uniform(nm,P):
    alpha = P[0]
    beta = P[1]
    data = []
    for i in range(nm):
        data.append(random.uniform(alpha, beta))
    print(data)
    return data

def WriteToExcel(alldata):
    import xlwt
    wb = xlwt.Workbook()
    ws1 = wb.add_sheet('Dağılım Eğitim ve Test verisi')  # First sheet
    ws2 = wb.add_sheet('Dağılım Verileri')  # Second sheet
    s1 = 1
    s2 = 1


    for i in range(10):
        ws1.write(0, i, "Aralık_" + str(i))
    ws1.write(0, 10, "Çıktı")
    ws1.write(0, 11, "Dağılım")
    ws1.write(0, 12, "Parametre")

    # Write headers for the second sheet
    ws2.write(0, 0, "Dağılım")
    ws2.write(0, 1, "Parametre")
    ws2.write(0, 2, "Veri")

    for j in alldata:
        frekans = Gruplama(j[3])
        su = 0
        ll = []
        for i in frekans:
            ll.append(i[2])
        mmx = max(ll)
        if mmx > 0:
            for i in frekans:
                ws1.write(s1, su, i[2] / mmx)
                su += 1
            ws1.write(s1, su, str(j[1]))
            ws1.write(s1, su + 1, str(j[0]))
            ws1.write(s1, su + 2, str(j[2]))
            s1 += 1


        ws2.write(s2, 0, str(j[0]))
        ws2.write(s2, 1, str(j[2]))
        ws2.write(s2, 2, ', '.join(str(x) for x in j[3]))
        s2 += 1

    wb.save("d://DagilimEgitimSeti.xls")

def Gruplama(data):
    mx=max(data)
    mn=min(data)
    step=(mx-mn)/10
    alt =mn
    ust = mn + step
    print ("Min =", mn, "  Max=", mx, "  Avg=",sum(data)/len(data) )
    print("--------------------------------------------------")
    gruplar=[]
    for i in range(10):
        nm=Number(data,alt,ust)
        print(i+1,"[",alt,",",ust,"]=",nm)
        gruplar.append([alt,ust,nm])
        alt = ust
        ust = alt + step
    return gruplar

dic={0:Ustel, 1:Normal, 2:Weibull, 3:Lognormal, 4:Beta, 5:Uniform}
distName={0:"Ustel", 1:"Normal", 2:"Weibull", 3:"Lognormal", 4:"Beta", 5:"Uniform"}
distCode={0:"0,0,0,0,0,1", 1:"0,0,0,0,1,0", 2:"0,0,0,1,0,0", 3:"0,0,1,0,0,0", 4:"0,1,0,0,0,0", 5:"1,0,0,0,0,0"}
#distCode={0:"1", 1:"10", 2:"100", 3:"1000", 4:"10000", 5:"100000"}
allData=[]
for i in range(100):
    n=int(random.randint(0,5))
    dist=dic[n]
    print(distName[n])
    P=[random.randint(1,10), random.randint(1,20)/10]
    data=dist(100,P)
    #Gruplama(data)
    allData.append([distName[n],distCode[n],P,data])
WriteToExcel(allData)



