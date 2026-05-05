import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [3.1, 2.5, 4.0, 5.2, 6.8, 7.5, 8.0, 7.2, 6.0, 4.5, 3.8, 2.9]

plt.barh(months, rainfall, color='blue')
plt.ylabel('Months')
plt.xlabel('Rainfall (inches)')
plt.title('Average Monthly Rainfall')
plt.show()