def average(L):
    if not L:
        return None
    return sum(L)//len(L)

if __name__ == "__main__":
    L = [1,2,3,4,5]
    result = average(L)
    expected_result = 3
    if result == expected_result:
        print(average(L))
    else:
        print("test failed! Received",result,"expected:", expected_result)

if __name__ == "__main__":
    L = [1,2,3,4,5]

    expected_result = 3
    assert average(L) == expected_result
    print(average(L) )


if __name__ == "__main__":
    L = [1,2,3,4,5]


    assert average(L) == 3
    print(average(L) )