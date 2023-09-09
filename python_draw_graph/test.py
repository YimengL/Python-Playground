import matplotlib.pyplot as plt
import seaborn as sns
import csv


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

full_data = [kf_apikal, kf_mittel, kf_zervikal,
             fm_apikal, fm_mittel, fm_zervikal,
             hyf_apikal, hyf_mittel, hyf_zervikal]

with open(file_name) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        for index, data in enumerate(full_data):
            full_data[index]['data'].append(float(row[index]))

print("Please verify below data: ")
for r in full_data:
    print("{}: {}".format(r['label'], r['data']))

data_to_plot = list(map(lambda d: d['data'], full_data))

sns.stripplot(data=data_to_plot, palette='dark:black', edgecolor="gray", size=3)

ax = sns.violinplot(data=data_to_plot)
ax.set_title('Custom violinplot 1')
ax.set_xlabel("Feilen-System")
ax.set_ylabel("Kanalstranport")
ax.set_xticklabels(labels=list(map(lambda d: d['label'], full_data)), rotation=45, fontsize=6)
# palette=["#EFE4E8", 'r', 'r', 'g', 'g', 'g', 'b', 'b', 'b']

plt.show()
