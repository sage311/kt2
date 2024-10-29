import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.3, 100)
categories = ['E', 'F', 'G', 'H']
values = np.random.randint(10, 80, size=4) 

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), label='Синус', color='orange') 
plt.scatter(x, y, color='cyan', s=15, alpha=0.7, label='Шум')  
plt.title('График синуса')
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.legend()

plt.subplot(2, 2, 2)
plt.hist(np.random.rand(1000), bins=25, color='lightblue', edgecolor='black') 
plt.title('Гистограмма случайных данных')
plt.xlabel('Данные')
plt.ylabel('Частота')

plt.subplot(2, 2, 3)
plt.scatter(x, y, color='magenta', alpha=0.8)
plt.title('График разброса')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 4)
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])  # Изменили цвета
plt.title('Круговая диаграмма категорий')

plt.tight_layout()
plt.show()
