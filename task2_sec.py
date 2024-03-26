import matplotlib.pyplot as plt
import csv


x = []
y = []
z = []
zsec = []
SEC = 60

with open('data1.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=';')
    
    for row in plotting:
        x.append(float(row[0]))
        y.append(float(row[3]))
        z.append(float(row[4]))
        
zsec = [num / SEC for num in z]
        

plt.plot(x, y)
plt.plot(x, zsec)
plt.title('Графики')
plt.xlabel('time,sec')
plt.ylabel('Положение заслонки(%) и Обороты двигателя(Об/сек)')
plt.legend(['Положение дроссельной заслонки(%) ', 'Обороты двигателя(об/сек)'])
plt.show()



