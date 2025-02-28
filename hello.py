import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

kelas = ["kelas"]
Polychaeta=22 
Enoplea=15 
Insecta=13 
Hexanauplia=10 
Arachnida=6 
Bacillariophyceae=5 
Gastropoda=4 
Coscinodiscophyceae=4 
Malacostraca=4 
Rhabditophora=2 
Clitellata=2 
Hydrozoa=2 
Mediophyceae=2 
Actinopteri=2 
Peronosporales=1 
Flabellinia=1 
Chromadorea=1 
Florideophyceae=1 
Aves=1 
Pythiales=1 


fig, ax = plt.subplots()
ax.bar(kelas, Polychaeta)
ax.bar(kelas, Enoplea, bottom=Polychaeta)
ax.bar(kelas, Insecta, bottom=Polychaeta)
ax.bar(kelas, Hexanauplia, bottom=Polychaeta)
ax.bar(kelas, Arachnida, bottom=Polychaeta)
ax.bar(kelas, Bacillariophyceae, bottom=Polychaeta)
ax.bar(kelas, Gastropoda, bottom=Polychaeta)
ax.bar(kelas, Coscinodiscophyceae, bottom=Polychaeta)
ax.bar(kelas, Malacostraca, bottom=Polychaeta)
ax.bar(kelas, Rhabditophora, bottom=Polychaeta)
ax.bar(kelas, Clitellata, bottom=Polychaeta)
ax.bar(kelas, Hydrozoa, bottom=Polychaeta)
ax.bar(kelas, Mediophyceae, bottom=Polychaeta)
ax.bar(kelas, Actinopteri, bottom=Polychaeta)
ax.bar(kelas, Peronosporales, bottom=Polychaeta)
ax.bar(kelas, Flabellinia, bottom=Polychaeta)
ax.bar(kelas, Chromadorea, bottom=Polychaeta)
ax.bar(kelas, Florideophyceae, bottom=Polychaeta)
ax.bar(kelas, Aves, bottom=Polychaeta)
ax.bar(kelas, Pythiales, bottom=Polychaeta)

kelas_labels = [
    'Polychaeta', 'Enoplea', 'Insecta', 'Hexanauplia', 'Arachnida', 'Bacillariophyceae', 'Gastropoda', 'Coscinodiscophyceae', 'Malacostraca', 'Rhabditophora', 'Clitellata', 'Hydrozoa', 'Mediophyceae', 'Actinopteri', 'Peronosporales', 'Flabellinia', 'Chromadorea', 'Florideophyceae', 'Aves', 'Pythiales'
]

values = [
    Polychaeta, Enoplea, Insecta, Hexanauplia, Arachnida, Bacillariophyceae, Gastropoda, Coscinodiscophyceae, Malacostraca, Rhabditophora, Clitellata, Hydrozoa, Mediophyceae, Actinopteri, Peronosporales, Flabellinia, Chromadorea, Florideophyceae, Aves, Pythiales
]

total = sum(values)
bottom = 0
for label, value in zip(kelas_labels, values):
    percentage = (value / total) * 100
    ax.bar(kelas, percentage, label=label, bottom=bottom)
    bottom += percentage

ax.set_ylabel('Percentage')
ax.set_xlabel('kelas SP2')
ax.set_title('Percentage of Each kelas')

# Add percentage labels to each bar
bottom = 0
for label, value in zip(kelas_labels, values):
    percentage = (value / total) * 100
    colors = plt.cm.tab20(np.linspace(0, 1, len(kelas_labels)))
    ax.bar(kelas, percentage, label=label, bottom=bottom, color=colors[kelas_labels.index(label)])
    bottom += percentage
ax.set_xticks([])

handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles[:len(kelas_labels)], labels[:len(kelas_labels)], loc='center left', bbox_to_anchor=(1, 0.5))
for handle, color in zip(legend.legendHandles, colors):
    handle.set_color(color)
plt.show()

