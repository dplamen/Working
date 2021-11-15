text = input()

parentheses = []
balanced = True
for ch in text:
    if ch in '({[':
        parentheses.append(ch)
    elif parentheses and parentheses[-1] + ch in ('()', '{}', '[]'):
        parentheses.pop()
    else:
        balanced = False
        break

if balanced:
    print('YES')
else:
    print('NO')
