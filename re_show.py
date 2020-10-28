import re

text = """In September 1769 she reached New
Zealand, the first European vessel to visit
in 127 years."""

# print(text)

# not correct word spit
# for n, word in enumerate(text.split(" ")):
#     print(n, "=>", word)

# 1 Correct
# for n, word in enumerate(re.split('\W+', text)):
#     print(n, "=>", word)

# 2 Correct
# for n, word in enumerate(re.findall(r'\w+', text)):
#     print(n, "=>", word)


# for n, word in enumerate(re.findall(r'[A-Z]\w+\W(\w+)', text)):
#     print(n, "=>", word)

for n, word in enumerate(re.findall(r'(\w{3})\w+', text)):
    print(n, "=>", word)
