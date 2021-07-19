#number of good pairs
def number_of_good_pairs(lst):
    nums = 0
    for i in range (0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                print((i, j))
                nums += 1
    return nums 

if __name__ == '__main__':
    test1 = [1,2,3,1,1,3]
    print (number_of_good_pairs(test1))
    test2 = [1,1,1,1]
    print (number_of_good_pairs(test2))
    test3 = [1,2,3]
    print (number_of_good_pairs(test3))

