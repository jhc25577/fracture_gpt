import pandas as pd
import seaborn
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import metrics


data_melanoma = pd.read_csv('../bone_fracture_results/bone_fracture_frac_1.csv')
data_normal = pd.read_csv('../bone_fracture_results/bone_fracture_nofrac_1.csv')

data_melanoma = data_melanoma.assign(truth = np.ones(len(data_melanoma['filename'])))
data_normal = data_normal.assign(truth = np.zeros(len(data_normal['filename'])))

data_list = [data_melanoma, data_normal]

data = pd.concat(data_list, ignore_index=True)

data['result'].replace(['B.','A.'], [0,1], inplace=True)
data['result'].replace(['B','A'], [0,1], inplace=True)
data['result'].replace(['B)','A)'], [0,1], inplace=True)
data = data.drop(['filename'], axis=1)

for x in data['result']:
    if x != 0 and x != 1:
        data['result'].replace([x], [None], inplace=True)
data = data.dropna()

data = data.astype(int)

for x in data['truth']:
    if type(x) != int:
        print(x)

confusion_matrix = metrics.confusion_matrix(data['truth'], data['result'])
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ["not fracture", "fracture"])

F1 = metrics.f1_score(data['truth'],data['result'], average='binary')
recall = metrics.recall_score(data['truth'],data['result'], average='binary')
precision = metrics.precision_score(data['truth'],data['result'], average='binary')
accuracy = metrics.accuracy_score(data['truth'],data['result'])

print("Accuracy: ", accuracy)
print("F1: ", F1)
print("Recall: ", recall)
print("Precision: ", precision)

cm_display.plot(cmap='bone')
plt.show()

data.to_csv('../bone_fracture_results/prep_bone_fracture_1.csv')