import matplotlib.pyplot as plt

# Read data from file
with open('data.txt', 'r') as file:
    data = [tuple(map(int, line.split())) for line in file]

# Extract x and y values
x_values, y_values = zip(*data)

# Plot stem plot
plt.stem(x_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Stem Plot for x(n) = 20 - n')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('f2.png')
plt.show()
