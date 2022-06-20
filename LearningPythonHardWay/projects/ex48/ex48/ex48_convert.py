def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

num = convert_number(123)
wor = convert_number('apple')

print(num)
print(wor)