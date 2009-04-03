from util import memo

def score_ch(ch):
    try:
        return 'abcdefghijklmnopqrstuvwxyz'.index(ch) + 1
    except:
        return 0

def score(name):
    return sum(score_ch(ch) for ch in name.lower())

# print score('COLIN'), score('coLin')

ord = 1
total = 0
for name in open('alpha_names.txt').readlines():
    name.strip()
    total += ord * score(name)
    ord += 1

print total