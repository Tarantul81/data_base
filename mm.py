import matplotlib.pyplot as plt

from data_base.db_operations import q, w
from collections import Counter
from numpy import arange

def histogram(q):
    data = [i[0] for i in q()]
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
    plt.savefig("rampage_countries.jpg")
    plt.show()

data_country = []
data_time = []

for i in w():
    data_country.append(i[0])
    data_time.append(i[1])

summ = {}
for j in range(len(data_country)):
    if data_country[j] in summ:
        summ[data_country[j]] += data_time[j]
    else:
        summ[data_country[j]] = data_time[j]
countries = list(summ.keys())
times = list(summ.values())

plt.pie(times[:20], labels=countries[:20], autopct='%1.1f%%')
# plt.figure(figsize=(20, 20))
plt.savefig("rampage_countries.jpg")
plt.show()
