# Plotting
labels = ['Monica', 'Adrian', 'Jared']
num = [230, 100, 98] # Note that this does not need to be percentages

import matplotlib.pyplot as plt
plt.pie(num, labels=labels, autopct='%4.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])

plt.title('Voting Results: Club President', fontdict={'fontsize': 20})
# plt.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])
plt.show()
