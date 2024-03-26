import matplotlib.pyplot as plt
import csv


x = []
y = []
z = []


with open('data1.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=';')
    
    for rows in plotting:
        x.append(float(rows[0]))
        y.append(float(rows[3]))
        z.append(float(rows[4]))
        
        
plt.plot(x, y)
plt.plot(x, z)
plt.title('Графики')
plt.xlabel('time,sec')
plt.ylabel('Положение заслонки(%) и обороты(об/мин)')
plt.legend(['Положение дроссельной заслонки(%) ', 'Обороты двигателя(об/сек)'])
plt.show()


