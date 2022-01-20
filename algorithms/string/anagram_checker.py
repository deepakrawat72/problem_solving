# Note : Two strings are called anagram if all the characters in str1 exists in str2 and same no. of times.
def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    count = [0] * 256  # create an array of size 256 as no. of ascii characters are only 256.

    for i in range(0, len(str1)):
        count[ord(str1[i])] += 1  # increment the value at ASCII position(derived from character ascii value) by 1
        count[ord(str2[i])] -= 1  # decrement the value at ASCII position(derived from character ascii value) by 1

    # each occurrence of a character in str1 will cancel out the occurrence of a character in str2. This way if both the
    # strings are anagram then they will both cancel out each other and the count array should hold all 0's.
    for item in count:
        if item != 0:
            return False
    return True


if __name__ == '__main__':
    print(check_anagram("abca", "bcaa"))
