
next_player = None

sides = [[4 for i in range(6)] + [0] for i in range(2)]
result = sides[0] + sides[1]

# 12 max
action = 9

idx = 1

for ln in range(result[action]):
    if action + idx >= len(result):
        idx = -action

    result[action + idx] += 1

    if ln + 1 == result[action] and action + idx in [6, 13]:
        next_player = 1

    idx += 1

result[action] = 0

print(result, next_player)