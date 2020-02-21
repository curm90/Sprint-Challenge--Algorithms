'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # a place to store the count
    count = 0
    # if len word < 1 return 0
    if len(word) < 1:
        return 0
    # else
    else:
        # slice arr with first 2 indeces and check if if == to 'th'
        if word[:2] == 'th':
            # if yes increment count
            count += 1
    # return count + count_th with next arr
    return count + count_th(word[1:])
