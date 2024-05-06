def split_rucksack(rucksack):
    x = len(rucksack) // 2
    return rucksack[:x], rucksack[x:]

def solution(puzzel_input):
    lower = 96
    upper = 38

    rucksacks = [x for x in puzzel_input.split('\n')]

    priority_sum = 0
    for rucksack in rucksacks:
        l, r = split_rucksack(rucksack)

raw = open('testinput').read().rstrip()
print(solution(raw))


