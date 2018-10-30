import matplotlib.pyplot as plt

#x cordinates on left side of bars
left = [1,2,3,4,5]

#height of bars
height = [10,24,36,40,5]

#labels for bars
tick_label = ['one','two','three','four','five']

#plotting as bar graph
plt.bar(left, height, tick_label = tick_label,
		 width = 0.8,color = ['red','blue'])

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('my bar chart')
plt.show()