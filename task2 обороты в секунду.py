import matplotlib.pyplot as plt
import csv


X = []
Y = []
Z = []
Zsec = []
sec = 60

with open('data1.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=';')
    
    for ROWS in plotting:
        X.append(float(ROWS[0]))
        Y.append(float(ROWS[3]))
        Z.append(float(ROWS[4]))
        
Zsec = [num / sec for num in Z]
        

plt.plot(X, Y)
plt.plot(X, Zsec)
plt.title('Графики')
plt.xlabel('time,sec')
plt.ylabel('Положение заслонки(%) и Обороты двигателя(Об/сек)')
plt.legend(['Положение дроссельной заслонки(%) ', 'Обороты двигателя(об/сек)'])
plt.show()



