#Beautiful Binary String
def beautiful_binary_string(str):
    moves = 0
    lst = list(str)
    for i in range(0, len(lst)-1):
        if lst[i] == '0' and lst[i+1] == '1' and lst[i+2] == '0':
            lst[i+2] = '1'
            moves += 1
            i += 3
        else: 
            i+=1
    str = "".join(lst)
    return moves

if __name__ == '__main__':
    str = input('input a binary string: ')
    print ('Required moves: ', end = ' ' )
    print(beautiful_binary_string(str))