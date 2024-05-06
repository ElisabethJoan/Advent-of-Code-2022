def solution(puzzel_input):
    maxCalories = 0
    currentCalories = 0
    for food in puzzel_input.split('\n'):
        if (food != ''):
            currentCalories = currentCalories + int(food)
        else:
            if (maxCalories < currentCalories):
                maxCalories = currentCalories
            currentCalories = 0
    
    return maxCalories

raw = open('input').read().rstrip()
print(solution(raw))