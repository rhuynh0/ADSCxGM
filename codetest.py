import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot

#REALLY SHITTY FILE NAMES, IM SORRY D:
filepath = 'C:/Users/Lawrence/Documents/GM/vehpub.csv'
data = np.genfromtxt(filepath, delimiter=',', skip_header=1)
filepath2 = 'C:/Users/Lawrence/Documents/GM/hhpub.csv'
data2 = np.genfromtxt(filepath2, delimiter=',', skip_header=1)

#Below, i am generating a dictionary so we have direct access to each HOUSEHOLD so we can separate data little more


#for hhpub.csv
hhweight = {row[0]: row[1] for row in data2} #creates a dictionary of the household weight in form of id:weight
numadlt = {row[0]: row[4] for row in data2} #creates a dictionary of the number of adults in form of id:number of adults
homeown = {row[0]: row[5] for row in data2} #creates a dictionary of the home ownership in form of id:home ownership
hometype = {row[0]: row[6] for row in data2} #creates a dictionary of the home type in form of id:home type
rail = {row[0]: row[7] for row in data2} #creates a dictionary of the rail in form of id:rail
census_d = {row[0]: row[8] for row in data2} #creates a dictionary of the census division in form of id:census division
census_r = {row[0]: row[9] for row in data2} #creates a dictionary of the census region in form of id:census region
hh_hisp = {row[0]: row[10] for row in data2} #creates a dictionary of the household hispanic in form of id:household hispanic
drvrcnt = {row[0]: row[11] for row in data2} #creates a dictionary of the driver count in form of id:driver count
cnttdhh = {row[0]: row[12] for row in data2} #creates a dictionary of the count of the household in form of id:count of the household
cdivmsar = {row[0]: row[13] for row in data2} #creates a dictionary of the census division in form of id:census division
flag100 = {row[0]: row[14] for row in data2} #creates a dictionary of the flag100 in form of id:flag100
hhinc = {row[0]: row[16] for row in data2} #creates a dictionary of the household income in form of id:income
hhrace = {row[0]: row[17] for row in data2} #creates a dictionary
hhsize = {row[0]: row[18] for row in data2} #creates a dictionary
hhvehcnt = {row[0]: row[19] for row in data2} #creates a dictionary
hhrelatd = {row[0]: row[20] for row in data2} #creates a dictionary
lif_cyc = {row[0]: row[21] for row in data2} #creates a dictionary
msasize = {row[0]: row[23] for row in data2} #creates a dictionary
travday = {row[0]: row[24] for row in data2} #creates a dictionary
urban = {row[0]: row[25] for row in data2} #creates a dictionary
urbansize = {row[0]: row[26] for row in data2} #creates a dictionary
urbrur = {row[0]: row[27] for row in data2} #creates a dictionary
ppt517 = {row[0]: row[28] for row in data2} #creates a dictionary
youngchild = {row[0]: row[29] for row in data2} #creates a dictionary
resp_cnt = {row[0]: row[30] for row in data2} #creates a dictionary
urbrur_2010 = {row[0]: row[31] for row in data2} #creates a dictionary
wrkcount = {row[0]: row[33] for row in data2}


#NOTE: MAKE SURE THAT THE HOUSE ID IS UNIQUE OR THERES GONNA BE BIG BAD PROBLEMS



#getting all the house ids with evs (id = 5)
Houses_with_EVS = []
Houses_with_Hybrids = []
Houses_with_PlugInHybrids = []

#getting a list of all houses
typeofcar = [0]*99

for i in range(data.shape[0]):
    if data[i, 6] == 5:
        Houses_with_EVS.append(data[i, 0]) #gives id of houses with evs
        typeofcar[int(data[i, 3])] += 1 
    elif data[i, 6] == 6:
        Houses_with_Hybrids.append(data[i, 0])
    elif data[i, 6] == 4:
        Houses_with_PlugInHybrids.append(data[i, 0])






#turning it into np array so can run numpy commands on it
Houses_with_EVS = np.array(Houses_with_EVS)
unique_houses_with_evs = np.unique(Houses_with_EVS) #gets rid of duplicates
for i in range(len(typeofcar)):
    if typeofcar[i] != 0:
        print(i+1)

#print(unique_houses_with_evs)

#ford, chevrolet, other dom e.g tesla, volkswagen, audi,bmw, nissan/datsun, honda, hyundai, kia, other make
#no, yes, no, no, no volkswagen, no audi, no 
totalveh = 0
numvehgiveninc = [0,0,0,0,0,0,0,0,0,0,0] #income has 11 categories
numvehgiveninc1 = [0,0,0,0,0,0,0,0,0,0,0] #income has 11 categories
numvehgiveninc2 = [0,0,0,0,0,0,0,0,0,0,0] #income has 11 categories
#note: total veh = sum(num of vehicles per hh x hh weight)
totalrural = 0
totalweight = 0
totalurban = 0
homeown1 = [0] * 4
homeown2 = [0] * 4
homeown3 = [0] * 4
hometype1 = [0] * 4
hometype2 = [0] * 4
hometype3 = [0] * 4
census_d1= [0] * 9
census_d2 = [0] * 9
census_d3 = [0] * 9
census_r1 = [0] * 4
census_r2 = [0] * 4
census_r3 = [0] * 4
hh_hisp1 = [0] * 4
hh_hisp2 = [0] * 4
hh_hisp3 = [0] * 4
drvrcnt1 = [0] * 9
drvrcnt2 = [0] * 9
drvrcnt3 = [0] * 9
cnttdhh1 = [0] * 45
cnttdhh2 = [0] * 45
cnttdhh3 = [0] * 45
cdivmsar1 = [0] * 95
cdivmsar2 = [0] * 95
cdivmsar3 = [0] * 95
flag1001 = [0] * 9
flag1002 = [0] * 9
flag1003 = [0] * 9
hhinc1 = [0] * 11
hhinc2 = [0] * 11
hhinc3 = [0] * 11
hhrace1 = [0] * 99
hhrace2 = [0] * 99
hhrace3 = [0] * 99
hhsize1 = [0] * 9
hhsize2 = [0] * 9
hhsize3 = [0] * 9
hhvehcnt1 = [0] * 9
hhvehcnt2 = [0] * 9
hhvehcnt3 = [0] * 9
hhrelatd1 = [0] * 9
hhrelatd2 = [0] * 9
hhrelatd3 = [0] * 9
lif_cyc1 = [0] * 10
lif_cyc2 = [0] * 10
lif_cyc3 = [0] * 10
msasize1 = [0] * 9
msasize2 = [0] * 9
msasize3 = [0] * 9
travday1 = [0] * 9
travday2 = [0] * 9
travday3 = [0] * 9
urban1 = [0] * 9
urban2 = [0] * 9
urban3 = [0] * 9
urbansize1 = [0] * 9
urbansize2 = [0] * 9
urbansize3 = [0] * 9
urbrur1 = [0] * 9
urbrur2 = [0] * 9
urbrur3 = [0] * 9
ppt5171 = [0] * 9
ppt5172 = [0] * 9
ppt5173 = [0] * 9
youngchild1 = [0] * 9
youngchild2 = [0] * 9
youngchild3 = [0] * 9
resp_cnt1 = [0] * 9
resp_cnt2 = [0] * 9
resp_cnt3 = [0] * 9
urbrur_20101 = [0] * 9
urbrur_20102 = [0] * 9
urbrur_20103 = [0] * 9
wrkcount1 = [0] * 9
wrkcount2 = [0] * 9
wrkcount3 = [0] * 9
for i in Houses_with_PlugInHybrids:
    numvehgiveninc1[int(hhinc[i])-1] += hhweight[i] #split it based on income
    homeown2[int(homeown[i])-1] += hhweight[i]
    hometype2[int(hometype[i])-1] += hhweight[i]
    census_d2[int(census_d[i])-1] += hhweight[i]
    census_r2[int(census_r[i])-1] += hhweight[i]
    hh_hisp2[int(hh_hisp[i])-1] += hhweight[i]
    drvrcnt2[int(drvrcnt[i])-1] += hhweight[i]
    cnttdhh2[int(cnttdhh[i])-1] += hhweight[i]
    cdivmsar2[int(cdivmsar[i])-1] += hhweight[i]
    flag1002[int(flag100[i])-1] += hhweight[i]
    hhrace2[int(hhrace[i])-1] += hhweight[i]
    hhsize2[int(hhsize[i])-1] += hhweight[i]
    hhvehcnt2[int(hhvehcnt[i])-1] += hhweight[i]
    hhrelatd2[int(hhrelatd[i])-1] += hhweight[i]
    lif_cyc2[int(lif_cyc[i])-1] += hhweight[i]
    msasize2[int(msasize[i])-1] += hhweight[i]
    travday2[int(travday[i])-1] += hhweight[i]
    urban2[int(urban[i])-1] += hhweight[i]
    urbansize2[int(urbansize[i])-1] += hhweight[i]
    urbrur2[int(urbrur[i])-1] += hhweight[i]
    ppt5172[int(ppt517[i])-1] += hhweight[i]
    youngchild2[int(youngchild[i])-1] += hhweight[i]
    resp_cnt2[int(resp_cnt[i])-1] += hhweight[i]
    urbrur_20102[int(urbrur_2010[i])-1] += hhweight[i]
    wrkcount2[int(wrkcount[i])-1] += hhweight[i]
for i in Houses_with_Hybrids:
    numvehgiveninc2[int(hhinc[i])-1] += hhweight[i] #split it based on income
    homeown3[int(homeown[i])-1] += hhweight[i]
    hometype3[int(hometype[i])-1] += hhweight[i]
    census_d3[int(census_d[i])-1] += hhweight[i]
    census_r3[int(census_r[i])-1] += hhweight[i]
    hh_hisp3[int(hh_hisp[i])-1] += hhweight[i]
    drvrcnt3[int(drvrcnt[i])-1] += hhweight[i]
    cnttdhh3[int(cnttdhh[i])-1] += hhweight[i]
    cdivmsar3[int(cdivmsar[i])-1] += hhweight[i]
    flag1003[int(flag100[i])-1] += hhweight[i]
    hhrace3[int(hhrace[i])-1] += hhweight[i]
    hhsize3[int(hhsize[i])-1] += hhweight[i]
    hhvehcnt3[int(hhvehcnt[i])-1] += hhweight[i]
    hhrelatd3[int(hhrelatd[i])-1] += hhweight[i]
    lif_cyc3[int(lif_cyc[i])-1] += hhweight[i]
    msasize3[int(msasize[i])-1] += hhweight[i]
    travday3[int(travday[i])-1] += hhweight[i]
    urban3[int(urban[i])-1] += hhweight[i]
    urbansize3[int(urbansize[i])-1] += hhweight[i]
    urbrur3[int(urbrur[i])-1] += hhweight[i]
    ppt5173[int(ppt517[i])-1] += hhweight[i]
    youngchild3[int(youngchild[i])-1] += hhweight[i]
    resp_cnt3[int(resp_cnt[i])-1] += hhweight[i]
    urbrur_20103[int(urbrur_2010[i])-1] += hhweight[i]
    wrkcount3[int(wrkcount[i])-1] += hhweight[i]
"""
print("homeown: ", sum(homeown1))
print("hometype: ", sum(hometype1))
print("census_d: ", sum(census_d1))
print("census_r: ", sum(census_r1))
print("hh_hisp: ", sum(hh_hisp1))
print("drvrcnt: ", sum(drvrcnt1))
print("cnttdhh: ", sum(cnttdhh1))
print("cdivmsar: ", sum(cdivmsar1))
print("flag100: ", sum(flag1001))
print("hhinc: ", sum(numvehgiveninc))
print("hhrace: ", sum(hhrace1))
print("hhsize: ", sum(hhsize1))
print("hhvehcnt: ", sum(hhvehcnt1))
print("hhrelatd: ", sum(hhrelatd1))
print("lif_cyc: ", sum(lif_cyc1))
print("msasize: ", sum(msasize1))
print("travday: ", sum(travday1))
print("urban: ", sum(urban1))
print("urbansize: ", sum(urbansize1))
print("urbrur: ", sum(urbrur1))
print("ppt517: ", sum(ppt5171))
print("youngchild: ", sum(youngchild1))
print("resp_cnt: ", sum(resp_cnt1))
print("urbrur_2010: ", sum(urbrur_20101))
print("wrkcount: ", sum(wrkcount1))
"""
for i in Houses_with_EVS:
    numvehgiveninc[int(hhinc[i])-1] += hhweight[i] #split it based on income
    homeown1[int(homeown[i])-1] += hhweight[i]
    hometype1[int(hometype[i])-1] += hhweight[i]
    census_d1[int(census_d[i])-1] += hhweight[i]
    census_r1[int(census_r[i])-1] += hhweight[i]
    hh_hisp1[int(hh_hisp[i])-1] += hhweight[i]
    drvrcnt1[int(drvrcnt[i])-1] += hhweight[i]
    cnttdhh1[int(cnttdhh[i])-1] += hhweight[i]
    cdivmsar1[int(cdivmsar[i])-1] += hhweight[i]
    flag1001[int(flag100[i])-1] += hhweight[i]
    hhrace1[int(hhrace[i])-1] += hhweight[i]
    hhsize1[int(hhsize[i])-1] += hhweight[i]
    hhvehcnt1[int(hhvehcnt[i])-1] += hhweight[i]
    hhrelatd1[int(hhrelatd[i])-1] += hhweight[i]
    lif_cyc1[int(lif_cyc[i])-1] += hhweight[i]
    msasize1[int(msasize[i])-1] += hhweight[i]
    travday1[int(travday[i])-1] += hhweight[i]
    urban1[int(urban[i])-1] += hhweight[i]
    urbansize1[int(urbansize[i])-1] += hhweight[i]
    urbrur1[int(urbrur[i])-1] += hhweight[i]
    ppt5171[int(ppt517[i])-1] += hhweight[i]
    youngchild1[int(youngchild[i])-1] += hhweight[i]
    resp_cnt1[int(resp_cnt[i])-1] += hhweight[i]
    urbrur_20101[int(urbrur_2010[i])-1] += hhweight[i]
    wrkcount1[int(wrkcount[i])-1] += hhweight[i]
widths = 0.1
pyplot.figure(0)
x = np.arange(1, len(homeown1)+1)
pyplot.bar(x-widths, homeown1, label = 'evs', color = 'r',width=0.1) 
pyplot.bar(x, homeown2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, homeown3, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('homeown')

pyplot.figure(1)
x = np.arange(1, len(hometype1)+1)
pyplot.bar(x-widths, hometype1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, hometype2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, hometype3, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()

pyplot.title('hometype')
pyplot.figure(2)

x = np.arange(1, len(census_d1)+1)
pyplot.bar(x-widths, census_d1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, census_d2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, census_d3, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('census_d')
pyplot.figure(3)

x = np.arange(1, len(census_r1)+1)
pyplot.bar(x-widths, census_r1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, census_r2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, census_r3, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('census_r')
pyplot.figure(4)

x = np.arange(1, len(hh_hisp1)+1)
pyplot.bar(x-widths, hh_hisp1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, hh_hisp2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, hh_hisp3, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('hh_hisp')
pyplot.figure(5)

x = np.arange(1, len(drvrcnt1)+1)
pyplot.bar(x-widths, drvrcnt1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, drvrcnt2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, drvrcnt3, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('drvrcnt')
pyplot.figure(6)

x = np.arange(1, len(cnttdhh1)+1)
pyplot.bar(x-widths, cnttdhh1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, cnttdhh2, label = 'non-plug plug in hybrids', color = 'b',width=0.1)
pyplot.legend()
pyplot.title('cnttdhh')
pyplot.figure(7)
x = np.arange(1, len(cdivmsar1)+1)
pyplot.bar(x-widths, cdivmsar1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, cdivmsar2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, cdivmsar3, label = 'non-plug hybrids', color = 'g',width=0.1)


pyplot.legend()
pyplot.title('cdivmsar')
pyplot.figure(8)

x = np.arange(1, len(flag1001)+1)
pyplot.bar(x-widths, flag1001, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, flag1002, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, flag1003, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('flag100')
pyplot.figure(9)

x = np.arange(1, len(numvehgiveninc)+1)
pyplot.bar(x-widths, numvehgiveninc, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, numvehgiveninc1, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, numvehgiveninc2, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('hhinc')
pyplot.figure(10)

x = np.arange(1, len(hhrace1)+1)
pyplot.bar(x-widths, hhrace1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, hhrace2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, hhrace3, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('hhrace')
pyplot.figure(11)

x = np.arange(1, len(hhsize1)+1)
pyplot.bar(x-widths, hhsize1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, hhsize2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, hhsize3, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('hhsize')
pyplot.figure(12)

x = np.arange(1, len(hhvehcnt1)+1)
pyplot.bar(x-widths, hhvehcnt1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, hhvehcnt2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, hhvehcnt3, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('hhvehcnt')
pyplot.figure(13)

x = np.arange(1, len(hhrelatd1)+1)
pyplot.bar(x-widths, hhrelatd1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, hhrelatd2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, hhrelatd3, label = 'non-plug hybrids', color = 'g',width=0.1)
pyplot.legend()
pyplot.title('hhrelatd')
pyplot.figure(14)

x = np.arange(1, len(lif_cyc1)+1)
pyplot.bar(x-widths, lif_cyc1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, lif_cyc2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, lif_cyc3, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('lif_cyc')
pyplot.figure(15)

x = np.arange(1, len(msasize1)+1)
pyplot.bar(x-widths, msasize1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, msasize2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, msasize3, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('msasize')
pyplot.figure(16)

x = np.arange(1, len(travday1)+1)
pyplot.bar(x-widths, travday1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, travday2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, travday3, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('travday')
pyplot.figure(17)

x = np.arange(1, len(urban1)+1)
pyplot.bar(x-widths, urban1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, urban2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, urban3, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('urban')
pyplot.figure(18)

x = np.arange(1, len(urbansize1)+1)
pyplot.bar(x-widths, urbansize1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, urbansize2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, urbansize3, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('urbansize')
pyplot.figure(19)

x = np.arange(1, len(urbrur1)+1)
pyplot.bar(x-widths, urbrur1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, urbrur2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, urbrur3, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('urbrur')
pyplot.figure(20)

x = np.arange(1, len(ppt5171)+1)
pyplot.bar(x-widths, ppt5171, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, ppt5172, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, ppt5173, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('ppt517')
pyplot.figure(21)

x = np.arange(1, len(youngchild1)+1)
pyplot.bar(x-widths, youngchild1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, youngchild2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, youngchild3, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()

pyplot.title('youngchild')
pyplot.figure(22)

x = np.arange(1, len(resp_cnt1)+1)
pyplot.bar(x-widths, resp_cnt1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, resp_cnt2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, resp_cnt3, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('resp_cnt')
pyplot.figure(23)

x = np.arange(1, len(urbrur_20101)+1)
pyplot.bar(x-widths, urbrur_20101, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, urbrur_20102, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, urbrur_20103, label = 'non-plug hybrids', color = 'g',width=0.1)

pyplot.legend()
pyplot.title('urbrur_2010')
pyplot.figure(24)

x = np.arange(1, len(wrkcount1)+1)
pyplot.bar(x-widths, wrkcount1, label = 'evs', color = 'r',width=0.1)
pyplot.bar(x, wrkcount2, label = 'plug in hybrids', color = 'b',width=0.1)
pyplot.bar(x+widths, wrkcount3, label = 'non-plug hybrids', color = 'g',width=0.1)


pyplot.legend()
pyplot.title('wrkcount')

pyplot.show()


"""
for i in rural:
    totalrural += hhweight[i]
for i in urban:
    totalurban += hhweight[i]
print("total rural: ", totalrural)
print("total urban: ", totalurban)
print(totalurban + totalrural)





print("total electric vehicles: ", int(totalveh))
print("number of electric vehicles given income: ", sum(numvehgiveninc))
print(unique_houses_with_evs)

#homeown, hometype, census_d, census_r, hh_hisp, drvrcnt, cnttdhh, cdivmsar, flag100, hhinc, hhrace, hhsize, hhvehcnt, hhrelatd, lif_cyc, msasize, travday, urban, urbansize, urbrur, ppt517, youngchild, resp_cnt, urbrur_2010, wrkcount






with open('evhouses4.csv', 'w+',newline = '') as f:
    writer = csv.writer(f)
    for i in data2:
        if i[0] in unique_houses_with_evs:
            for j in data:
                if j[0] == i[0]:
                    i = np.append(i, j[3])
                    
            writer.writerow(i)
count = 0

with open('logreg.csv', 'w+' , newline = '') as f:
    writer = csv.writer(f)
    for i in data2:
        #print(i[0])
        if i[0] in unique_houses_with_evs:
            count += 1
            i = np.append([1], i[1:] )
        else:
            i = np.append([0], i[1:])
                        
        writer.writerow(i)
            

test = np.genfromtxt('evhouses4.csv', delimiter=',', skip_header=1)
#use first column as the label
from sklearn.preprocessing import StandardScaler
X = test[:, 1:]
y = test[:, 0]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))
"""