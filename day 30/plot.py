import matplotlib.pyplot as plt


months= [1,2,3,4,5,6,7,8,9, 10, 11, 12]
sales = [100, 150, 200, 250, 300, 200, 400, 450, 500, 550, 600, 100]

plt.plot(months, sales, marker='o', ms = 10)
plt.xlabel('Months')
plt.title('Sales Data')
plt.ylabel('Sales')
plt.show()