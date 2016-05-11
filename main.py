# -*- coding: utf-8 -*-
import urllib2
import datetime
import pandas as pd
import os
import matplotlib.pyplot as plt



def download(index):


    if index < 10:
        index = "0"+str(index)
    else:
        index = str(index)
    regions = {1: "Vinnytsya", 2: "Volyn", 3:"Dnipropetrovs'k", 4:"Donets'k", 5:"Zhytomyr", 6:"Zacarpathia", 7:"Zaporizhzhya",
           8:"Ivano-Frankivs'k", 9:"Kiev", 10:"Kirovohrad", 11:"Luhans'k", 12:"L'viv", 13:"Mykolayiv", 14:"Odessa", 15:"Poltava",
           16:"Rivne", 17:"Sumy", 18:"Ternopil'", 19:"Kharkiv", 20:"Kherson", 21:"Khmel'nits'kyy", 22:"Cherkasy", 23:"Chernivtsi",
           24:"Chernihiv", 25:"Crimea"}
    index1 = Reindex(int(index))
    url = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+index1+".txt"
    vhi_url = urllib2.urlopen(url)
    name = "vhi_id_%s %s %s.csv" % (index1, regions[int(index)], datetime.datetime.now().strftime('%d %b %Y %H-%M-%S'))
    out = open(name,'wb')
    out.write(vhi_url.read())
    out.close()
    print ("VHI is successfully downloaded...")

def RegionSelect():
    print("You can download data for some region:")
    regions = {1: "Vinnytsya", 2: "Volyn", 3:"Dnipropetrovs'k", 4:"Donets'k", 5:"Zhytomyr", 6:"Zacarpathia", 7:"Zaporizhzhya",
           8:"Ivano-Frankivs'k", 9:"Kiev", 10:"Kirovohrad", 11:"Luhans'k", 12:"L'viv", 13:"Mykolayiv", 14:"Odessa", 15:"Poltava",
           16:"Rivne", 17:"Sumy", 18:"Ternopil'", 19:"Kharkiv", 20:"Kherson", 21:"Khmel'nits'kyy", 22:"Cherkasy", 23:"Chernivtsi",
           24:"Chernihiv", 25:"Crimea"}
    i = 1
    while i < 25:
        print(i, regions[i])
        i+=1
    print("\nPlease enter the index of the region.")
    index = 0
    flag = True
    while flag:
        try:
            index = int(input())
        except ValueError:
            print("Please enter the number in range from 1 to 25.")
        else:
            if index < 1 or index > 27:
                print("Please enter the number in range from 1 to 25.")
            else:
                flag = False
    return index

def FileSelect():
    files = []
    i = 0
    for file in os.listdir(os.getcwd()):
        if file.endswith(".csv"):
            i += 1
            files.append(file)
            print i,")",file
    choise = int(input("Select the file from the list above: "))
    df = pd.read_csv(files[choise-1],index_col=False, header=1)
    return df

def Reindex(i):
    arr = {1:"24", 2: "25", 3: "05",4: "06", 5: "27", 6:"23", 7:"26", 8:"07", 9:"11", 10:"13", 11:"14", 12:"15", 13:"16", 14:"17", 15:"18",
           16:"19", 17:"21", 18:"22", 19:"08", 20:"09", 21:"10", 22:"01", 23:"03", 24:"02", 25:"04"}
    return arr[i]

def read():
    print FileSelect().to_string(index=False)

def minMax():
    df = FileSelect()
    year =input("Enter the year to determine Max и Min values VHI: ")
    print "Max: ", df[df["year"] == year]["VHI"].max()
    print "Min: ", df[df["year"] == year]["VHI"].min()


def extreme():
    df = FileSelect()
    print "All extreme drought by year:"
    print df[df["VHI"] < 15][df["VHI"] != -1][["year","VHI"]]
    proc = input("Enter the percentage of the territory: ")
    print df[df["VHI"] < 15][df["%Area_VHI_LESS_15"] > proc][["year","week","VHI","%Area_VHI_LESS_15"]].to_string(index=False)

def moderate():
    df = FileSelect()
    print "Moderate drought for years:"
    print df[df["VHI"] < 35][df["VHI"] != -1][["year","VHI"]].to_string(index=False)
    proc = input("Enter the percentage of the territory: ")
    print df[df["VHI"] < 35][df["%Area_VHI_LESS_35"] > proc][["year","week","VHI","%Area_VHI_LESS_35"]].to_string(index=False)
def plot():
    df = FileSelect()
    year =input("Enter year: ")
    plt.figure(1)
    plt.plot(df[df["year"] == year]["week"], df[df["year"] == year]["VHI"] , label = year)
    plt.legend()
    plt.title("Plot for %s year" % (str(year)))
    plt.grid(True)
    plt.show()

while (True):
    print ("1. Download CSV")
    print ("2. View CSV")
    print ("3. Max & Min VHI")
    print ("4. Extreme drought")
    print ("5. Moderate drought")
    print ("6. Plot")
    print ("0. Exit")

    choice = int(input('Choose 0 of 6 : '))

    if choice == 1:
        download(RegionSelect())
    elif choice == 2:
        read()
    elif choice == 3:
        minMax()
    elif choice == 4:
        extreme()
    elif choice == 5:
        moderate()
    elif choice == 6:
        plot()
    elif choice == 0:
        break
    else:
        print ("Try again!(0-6)")
