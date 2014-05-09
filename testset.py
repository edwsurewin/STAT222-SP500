# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
from __future__ import division
from nose.tools import eq_,ok_,nottest
import re

def test_sum():
    eq_(2+2,4)

## input: a dictionary
def FindNor(y): 
    list0=y.values()
    S=sum(list0)
    Dic1=y.keys()
    Dic2=map(lambda x: (x/S), list0)
    Dic3=dict(zip(Dic1,Dic2))
    return(Dic3)
## D3 is the normalized freq
###

test={'a':1,'b':1}
def test_FindNor_1():
    assert FindNor(test)=={'a':0.5,'b':0.5}


test1={'a':0,'b':1}
def test_FindNor_2():
    assert FindNor(test1)=={'a':0,'b':1}

#test={'a':0,'b':0}
#    ok_(FindNor(test)=={'a':0.5,'b':0.5},'expected failure')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#### This function is used to count the number of documents that contains a particular word.
# input: a dictionary
def findDoc(Term):
    W=int()
    for i in test:
        # test is the file after i load in the pickle
        if Term in i:
            W=W+1
    return(W)
#output: a number
def test_findDoc():
    assert findDoc('a')==1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## input: two dictionaries:
def FindSharedKey(dic1,dic2):
    ABkey=dic1.viewkeys()&dic2.viewkeys()
    leng=min(len(dic1),len(dic2))
    prop=len(ABkey)/(leng+1)
    return(prop)
#output: a fraction.
    
d1={'a':0,'b':0}
d2 = {'c':0,'d':0}
d3={'f':0,'g':0}
d4={'a':0,'b':0}
def test_FindSharedKey_1():
    assert FindSharedKey(d1,d2) == 0

def test_FindSharedKey_2():
    assert FindSharedKey(d1,d4) == (2/3)
## note d1==d4. the value is not 1 because i purposely added 1 so that I will not run into the problem of dividing by 0.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# input: two dictionaries. One small, one big (the reference dictionary)
def PropWordShared(dic1,test):
    propShared=map(lambda x: FindSharedKey(dic1,x),test)
    return(propShared)
#output: a list of fraction    
def test_PropWord_1():
    assert PropWordShared(test,[d2,d3])==[0,0]

def test_PropWord_2():
    assert PropWordShared(test,[test,test])==[2/3,2/3]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## removes all the numeric numbers in the title
# input: a character
def remNum(x):
    y=re.sub('[0-9]',"",x)
    return(y)
# output: the same character vector w/o any numeric in it
def test_remNum_1():
    assert remNum('a')=='a'

def test_remNum_2():
    assert remNum('10')==''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# input character vector
def sliceup(x):
    leng=len(x)-2
    y=range(leng)
    z=map(lambda a: x[0:a+3], y)
    # can make the match more harsh by increasing th size of the sub segment.
    return(z)

# Use the strings to compare two words
def FindCommon(word,slices):
    L=len(slices)
    f=map(lambda x:(int(bool(re.search(x,word)))/L),slices)
    return(sum(f))

#Assign a score to the two titles base on how similar they are
#input character vector, and a list of character vectors (the reference list)
def SimiTitle(word, Title):
    # compares a particular word to the each elements in the title.
    g=sliceup(word)
    h=map(lambda x:FindCommon(x,g) ,Title)
    return(h)
# output: a list of fraction

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Title=['aaaa','bbbb']
#title needs to have more than 4 charactesrs in length
def test_SimiTitle_1():
    assert SimiTitle('aaaa',Title)==[1,0]

def test_SimiTitle_2():
    assert SimiTitle('cccc',Title)==[0,0]

def test_SimiTitle_3():
    assert SimiTitle('aa',Title)==[0,0]

def test_SimiTitle_4():
    assert SimiTitle('aaaaa',Title)==[2/3,0]

