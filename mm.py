import matplotlib.pyplot as plt

from data_base.db_operations import x
from collections import Counter
from numpy import arange


data = [i[0] for i in x()]
country_stats = Counter(data)
x, y = list(country_stats.keys()), list(country_stats.values())
minn, maxx = min(y), max(y)
values = arange(0, 100, 10)
plt.figure(figsize=(100, 100))
bars = plt.bar(x, y)
bars[y.index(maxx)].set_color('m')
bars[y.index(minn)].set_color('0')
plt.title("Top 10 Countries by Number of Rampages")
plt.xlabel("Country")
plt.ylabel("Number of People")
plt.xticks(rotation=90, fontsize=14)
plt.yticks(values, [str(val) for val in values])
plt.tight_layout()
# plt.text(x[y.index(maxx)], maxx, '', color='0')
# plt.text(x[y.index(minn)], minn, '', color='m')
plt.savefig("rampage_countries.jpg")

plt.show()