import matplotlib.pyplot as plt

# Example data
categories = ['Category A', 'Category B', 'Category C']
frequency = [10, 15, 7]

# Create bar plot
plt.bar(categories, frequency)
plt.xlabel('Categories')
plt.ylabel('Frequency')
plt.title('Frequency Distribution')
plt.show()
