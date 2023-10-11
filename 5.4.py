example_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
example_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
example_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def rewrite_grade(results):
    new_result = []
    for x in results:
        if x == 2: continue
        if x == 3:
            new_result.append(4)
            continue
        new_result.append(x)
    return new_result

print('Список оценок 1:', rewrite_grade(example_1))
print('Список оценок 2:', rewrite_grade(example_2))
print('Список оценок 3:', rewrite_grade(example_3))

