def all_variants(text):
    text = str(text)
    for i in range(len(text)):
        for r in range(len(text) - i):
            yield text[r:r + i + 1]

a = all_variants("abc")

for i in a:
    print(i)