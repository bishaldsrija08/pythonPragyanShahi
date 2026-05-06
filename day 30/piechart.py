import matplotlib.pyplot as plt

marks = [80, 90, 70, 85, 95]
labels = ['Math', 'Science', 'English', 'History', 'Art']
colors = ['red', 'blue', 'green', 'orange', 'purple']
myexplode = (0.1, 0.1, 0.1, 0.1, 0.1)  # explode the first slice (Math)
plt.pie(marks, labels=labels, colors=colors, explode=myexplode, autopct='%1.1f%%', shadow=True)
plt.title("Marks Distribution")
plt.legend()
plt.show()