'''Runs convergence tests for arguments given'''

def midpnttest(p1,p2,rtol):
    '''
    Checks to see if distance from the average of p1 and p2 is within
    the rtol values, returns a list containing test_bool and
    test_value
    '''
    test_value = abs((p1 - p2)/(p1+p2))
    test_bool = test_value < rtol
    output = (test_value,test_bool)
    return output
