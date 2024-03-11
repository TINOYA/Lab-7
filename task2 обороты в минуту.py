import matplotlib.pyplot as plt
import csv


X = []
Y = []
Z = []


with open('data1.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=';')
    
    for ROWS in plotting:
        X.append(float(ROWS[0]))
        Y.append(float(ROWS[3]))
        Z.append(float(ROWS[4]))
        
        
plt.plot(X, Y)
plt.plot(X, Z)
plt.title('Графики')
plt.xlabel('time,sec')
plt.ylabel('Положение заслонки(%) и обороты(об/мин)')
plt.legend(['Положение дроссельной заслонки(%) ', 'Обороты двигателя(об/сек)'])
plt.show()


