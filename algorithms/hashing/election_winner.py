from collections import Counter


def winner(arr):
    # Your code here
    # return the name of the winning candidate and the votes he recieved

    max_vote_count = 0
    election_winner = ""
    frequency = Counter(arr)

    for k, v in frequency.items():
        if v > max_vote_count:
            max_vote_count = v
            election_winner = k

        elif v == max_vote_count and (len(election_winner) == 0 or k < election_winner):
            election_winner = k

    return election_winner


if __name__ == '__main__':
    votes = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie',
             'johnny', 'john']

    print(winner(votes))
