import matplotlib.pyplot as plt
import seaborn as sns
import csv

# Start - Configuration

file_name = 'data.csv'   # 文件位置

# End Configuration

kf_apikal = {'label': 'KF-Apikal', 'data': []}
kf_mittel = {'label': 'KF-Mittel', 'data': []}
kf_zervikal = {'label': 'KF-Zertikal', 'data': []}
fm_apikal = []
fm_mittel = []
fm_zervikal = []
hyf_apikal = []
hyf_mittel = []
hyf_zervikal = []

full_data = [kf_apikal, kf_mittel, kf_zervikal]

color1 = "#EFE4E8"

with open(file_name) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        kf_apikal['data'].append(int(row[0]))
        kf_mittel['data'].append(int(row[1]))
        kf_zervikal['data'].append(int(row[2]))
        fm_apikal.append(int(row[3]))
        fm_mittel.append(int(row[4]))
        fm_zervikal.append(int(row[5]))
        hyf_apikal.append(int(row[6]))
        hyf_mittel.append(int(row[7]))
        hyf_zervikal.append(int(row[8]))

print("Print Out All data: ")
for r in full_data:
    print("{}: {}".format(r['label'], r['data']))

data_to_plot = [kf_apikal['data'], kf_mittel['data'], kf_zervikal['data'], fm_apikal, fm_mittel,
                fm_zervikal, hyf_apikal, hyf_mittel, hyf_zervikal]

data_to_plot = list(map(lambda d : d['data'], full_data))

print("Data to Plot: {}".format(data_to_plot))

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
labels = ['KF-Apikal', 'KF-Mittel', 'KF-Zertikal',
          'FM-Apikal', 'FM-Mittel', 'FM-Zertikal',
          'HyF-Apikal', 'HyF-Mittel', 'HyF-Zertikal']
plt.xlabel("Feilen-System", {"size": 10})
plt.ylabel("Kanalstranport", {"size": 10})
plt.yticks(fontsize = 12)

g = sns.violinplot(data_to_plot, palette=[color1, 'r', 'r', 'g', 'g', 'g', 'b', 'b', 'b'])
g.set_xticklabels(labels=labels, rotation=45)


plt.show()
