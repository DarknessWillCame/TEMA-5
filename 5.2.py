results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

best_results = []
best_search_copied_list = results.copy()
for x in range(3):
    best_result = min(best_search_copied_list)
    best_results.append(best_result)
    best_search_copied_list.remove(best_result)
print('Три лучших результата:', best_results)

worst_results = []
worst_search_copied_list = results.copy()
for x in range(3):
    worst_result = max(worst_search_copied_list)
    worst_results.append(worst_result)
    worst_search_copied_list.remove(worst_result)
print('Три худших результата:', worst_results)

more_than_or_equal_10 = []
for x in results:
    if x >= 10: more_than_or_equal_10.append(x)
print('Все результаты начиная с 10:', more_than_or_equal_10)
