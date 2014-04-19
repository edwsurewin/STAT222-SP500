
import os
import scipy.stats as stats
os.chdir("/Users/edwsurewin/Dropbox/Berkeley MA/222/STAT222-SP500") # or elsewhere at which "SP500.csv" is stored

import pandas as pd
SP500 = pd.read_csv("SP500.csv")

#print(SP500.tail()) = 0 to 16146
#len(SP500['Day']) = 16147

rate = [None]*(len(SP500['Open'])-1)

def compute_rate(SP500, rate):
    for i in range(0, len(SP500['Open'])-1):
        rate[i] = SP500['Open'][i]/SP500['Adj Close'][i+1]
    return rate

rate = compute_rate(SP500, rate)

##############################################
################ TEST SUITE ##################
##############################################

def test_1(): # if index 1 is correct
    abc = [None]*(len(SP500['Open'])-1)
    result = round(compute_rate(SP500, abc)[1], 7)
    assert result == round(1.0000747101,7)

def test_2(): # if index 88 is correct
    abc = [None]*(len(SP500['Open'])-1)
    result = round(compute_rate(SP500, abc)[88], 7)
    assert result == round(0.999801110372,7)

def test_3(): # if index 777 is correct
    abc = [None]*(len(SP500['Open'])-1)
    result = round(compute_rate(SP500, abc)[777], 7)
    assert result == round(1.00234814792,7)