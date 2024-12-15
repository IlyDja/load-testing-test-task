n, m = int(input()), int(input())
circular_array = list(range(1, n + 1))
first_el_array = circular_array[0]
last_el_array = circular_array[-1]

if m > n:
    circular_array *= m // n + 1

intervals = [circular_array[:m]]
len_int = len(intervals[-1])
while True:
    last_el_intervals = intervals[-1][-1]
    if last_el_intervals != first_el_array:
        start = last_el_intervals
        new_interval = []
        for _ in range(len_int):
            new_interval.append(start)
            start += 1
            if start > last_el_array:
                start = 1
        intervals.append(new_interval)
    else:
        break

firsts = ''.join([str(interval[0]) for interval in intervals])
# intervals = ', '.join(map(lambda l: ''.join(map(str, l)), intervals))
# print('Круговой массив: ', *circular_array[:n], '.', sep='')
# print(f'При длине обхода {m} получаем интервалы: {intervals}.')
# print(f'Полученный путь: {firsts}.')
print(firsts)
