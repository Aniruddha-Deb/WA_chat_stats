import sys
import re
import csv
import matplotlib.pyplot as plt

regex = re.compile("\[([0-3][0-9]/[0-1][0-9]/2[0-1]), (\d*:\d\d:\d\d [AP]M)\] ([^:]*):(.*)")

count = {}

ctr = 0;
with open(sys.argv[1], "r") as chat:
	out = open('stats.csv', 'w', newline='')
	outwriter = csv.writer(out)
	line = chat.readline()
	while line:
		data = regex.match(line)
		if data:
			date = data[1]
			time = data[2]
			person = data[3].strip().encode("ascii", "ignore").decode()
			if "changed the subject to" in person:
				line = chat.readline()
				continue
			if person in count:
				count[person] += 1
			else:
				count[person] = 1
			text = data[4].strip()
			ctr += 1
			outwriter.writerow([date, time, person, text])
			if ctr % 1000 == 0:
				print(".", end="", flush=True)
			if ctr % 10000 == 0:
				print("")
		line = chat.readline()

print("Done with reading")
sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=False))
fig, ax = plt.subplots()
ax.xaxis.tick_top()
plt.title("Cult stats as of 10/05/21 12:43:56 PM")
plt.barh(*zip(*sorted_count.items()))
plt.tight_layout()
plt.show()
