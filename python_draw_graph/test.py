import matplotlib.pyplot as plt
import seaborn as sns
import csv

# Start - Configuration

file_name = 'data.csv'  # 文件位置

kf_apikal = {'label': 'KF-Apikal', 'data': []}
kf_mittel = {'label': 'KF-Mittel', 'data': []}
kf_zervikal = {'label': 'KF-Zertikal', 'data': []}
fm_apikal = {'label': 'FM-Apikal', 'data': []}
fm_mittel = {'label': 'FM-Mittel', 'data': []}
fm_zervikal = {'label': 'FM-Zertikal', 'data': []}
hyf_apikal = {'label': 'HyF-Apikal', 'data': []}
hyf_mittel = {'label': 'HyF-Mittel', 'data': []}
hyf_zervikal = {'label': 'HyF-Zertikal', 'data': []}

# End Configuration

full_data = [kf_apikal, kf_mittel, kf_zervikal,
             fm_apikal, fm_mittel, fm_zervikal,
             hyf_apikal, hyf_mittel, hyf_zervikal]

color1 = "#EFE4E8"

with open(file_name) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        for index, data in enumerate(full_data):
            full_data[index]['data'].append(float(row[index]))

print("Please verify below data: ")
for r in full_data:
    print("{}: {}".format(r['label'], r['data']))

assert (len(full_data) == 9), "full data"

data_to_plot = list(map(lambda d: d['data'], full_data))

fs = 10
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create a figure instance
# fig = plt.figure();
# ax = fig.add_axes([0, 0, 1, 1])

# ax.violinplot(data_to_plot, pos, points=20, widths=0.3,
#                      showmeans=True, showextrema=True, showmedians=True)
# ax.set_title('Custom violinplot 1', fontsize=fs)
# # plt.show()


plt.figure(dpi=120)
plt.xlabel("Feilen-System", {"size": 10})
plt.ylabel("Kanalstranport", {"size": 10})
plt.yticks(fontsize=12)

g = sns.violinplot(data_to_plot, palette=["#EFE4E8", 'r', 'r', 'g', 'g', 'g', 'b', 'b', 'b'])
g.set_xticklabels(labels=list(map(lambda d: d['label'], full_data)), rotation=45)

plt.show()
