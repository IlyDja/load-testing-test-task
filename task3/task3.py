import json

path1, path2, path3 = input(), input(), input()
with open(path1) as values, open(path2) as tests, open(path3, 'w') as report:
    tests = json.load(tests)
    values = json.load(values)['values']
    values = dict(map(lambda d: (list(d.items())[0][1], list(d.items())[1][1]), values))
    to_dump = tests.copy()

    def parse_d(d):
        id = d['id']
        if 'value' in d:
            d['value'] = values[id]
        if 'values' in d:
            for d_inner in d['values']:
                parse_d(d_inner)

    for d in to_dump['tests']:
        parse_d(d)

    json.dump(to_dump, report)
