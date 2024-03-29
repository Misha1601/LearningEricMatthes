import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]

plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Squares Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()
