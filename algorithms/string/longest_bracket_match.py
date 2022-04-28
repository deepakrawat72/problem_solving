def find_longest_match(str):
    open_bkt_count = 0
    longest_bkt_length = 0
    for c in str:
        if c == ')' and open_bkt_count > 0 :
            open_bkt_count -=1
            longest_bkt_length +=2
        elif c == '(':
            open_bkt_count +=1

    return longest_bkt_length


if __name__ == '__main__':
    print(find_longest_match("()()()())))"))
    print(find_longest_match(")()()(()"))


