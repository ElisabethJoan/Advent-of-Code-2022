def solution(puzzel_input):
    # A, X = Rock - B, Y = Paper - C, Z = Scissors 
    choice = { 'X': 2, 'Y': 1, 'Z': 3 }
    result = { 'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3 }
    score = 0
    for game in puzzel_input.split('\n'):
        score = score + choice[game[2]]
        score = score + result[''.join(game.split(' '))]
    return score


raw = open('input').read().rstrip()
print(solution(raw))