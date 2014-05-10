def calc_len(maxprice):
    highmaxprice = range(0)
    for i in range(len(maxprice)):
	if maxprice[i] > 1000:
		highmaxprice = highmaxprice + [maxprice[i]]
    return highmaxprice

def test_1():
    result = calc_len([25.682, 25.681, 47.705, 58.268, 70.173, 91.905, 91.904, 102.997, 114.752, 103.464, 133.155, 133.148, 166.107, 166.107, 309.770, 467.390, 467.385, 1465.450, 1465.411, 1506.617, 1317.946, 1317.928, 1814.799, 1814.949])
    print 'hello, this is a test; the value of result is', len(result)
    assert len(result) < 10