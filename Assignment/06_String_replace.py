import re

a = "the movie is not that poor"
k = re.sub(r"not\s+\w+\s+poor", "good", a)
print(k)

