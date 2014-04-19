
import os
import scipy.stats as stats
os.chdir("/Users/edwsurewin/Dropbox/Berkeley MA/222/STAT222-SP500")

import pandas as pd

SP500 = pd.read_csv("SP500.csv")
SP500['Day'] = "null"

import datetime

for i in range(0, len(SP500['Day'])):
    SP500['Day'][i] = datetime.date(int(SP500['Date'][i][0:4]), int(SP500['Date'][i][5:7]), int(SP500['Date'][i][8:10])).isoweekday()

rate = [None]*(len(SP500['Day'])-1)

def compute_rate(SP500, rate):
    for i in range(0, len(SP500['Day'])-1):
        rate[i] = SP500['Open'][i]/SP500['Adj Close'][i+1]
    return rate

rate = compute_rate(SP500, rate)

Monday = []       # dynamic list
Tuesday = []      # create daily rate, in reference to "close adj" day
Wednesday = []    # thus, control group is Friday, i.e. 5
Thursday = []     # if the subsequent Monday is a holiday, then (Tue's open / Friday's close) = raw rate
Friday = []       

for i in range(1, len(SP500['Day'])):
    if SP500['Day'][i] == 1:
        Monday.append(rate[i-1])
    else:
        if SP500['Day'][i] == 2:
            Tuesday.append(rate[i-1])
        else:
            if SP500['Day'][i] == 3:
                Wednesday.append(rate[i-1])
            else:
                if SP500['Day'][i] == 4:
                    Thursday.append(rate[i-1])
                else:
                    if SP500['Day'][i] == 5:
                        Friday.append(rate[i-1])   
                        
NonFri = Monday + Tuesday + Wednesday + Thursday

from sklearn.neighbors import KernelDensity
kde = KernelDensity(bandwidth=.001, algorithm='auto', kernel='tophat', metric='euclidean', atol=0, rtol=0, breadth_first=True, leaf_size=40, metric_params=None)
# kernel estimation with tophat as spike-like histogram


kde.fit(Friday+NonFri)
ker100 = kde.sample(n_samples=100, random_state=None)

sample = []
for i in range(0, len(ker100)):
    sample = sample + ker100.tolist()[0]
    
MonteCarloBoot = kde.sample(n_samples=1000, random_state=None)
    
BootMean = [None]*len(MonteCarloBoot)
def bootMean(MonteCarloBoot, BootMean):
    for i in range(0, len(MonteCarloBoot)):
        BootMean[i] = MonteCarloBoot[i].mean()
    return(BootMean)

BootMean = bootMean(MonteCarloBoot, BootMean)

# Bootstrapping with T = mean(obs)
# v_boot = 1/B * B_sum(T - mean(T))^2


##############################################
################ TEST SUITE ##################
##############################################

def test_4(): # if index 1 is correct
    BootMean = [None]*len(MonteCarloBoot)
    result = bootMean(MonteCarloBoot, BootMean)[1]
    assert result == MonteCarloBoot[1].mean()
    
def test_5(): # if index 10 is correct
    BootMean = [None]*len(MonteCarloBoot)
    result = bootMean(MonteCarloBoot, BootMean)[10]
    assert result == MonteCarloBoot[10].mean()
    
def test_6(): # if index 100 is correct
    BootMean = [None]*len(MonteCarloBoot)
    result = bootMean(MonteCarloBoot, BootMean)[100]
    assert result == MonteCarloBoot[100].mean()