def average(L):

    if not L:
        return None
    return sum(L)//len(L)

def test():
    L = [1,2,3,4,5]


    assert average(L) == 3

