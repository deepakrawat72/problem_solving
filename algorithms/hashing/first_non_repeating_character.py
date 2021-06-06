def first_non_repeating_character(s):
    frequency_dict = {}
    indx = 1000000000
    # code here

    for i in range(0, len(s)):
        item = s[i]
        if item in frequency_dict:
            prev_count = frequency_dict[item][0]
            prev_indexes = frequency_dict[item][1]
            prev_indexes.append(i)
            frequency_dict[item] = [prev_count + 1, prev_indexes]
        else:
            frequency_dict[item] = [1, [i]]

    for k, v in frequency_dict.items():
        if v[0] == 1 and v[1][0] < indx:
            indx = v[1][0]

    if indx == 1000000000:
        return '$'
    else:
        return s[indx]


if __name__ == '__main__':
    string = 'hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs'
    print(first_non_repeating_character(string))
