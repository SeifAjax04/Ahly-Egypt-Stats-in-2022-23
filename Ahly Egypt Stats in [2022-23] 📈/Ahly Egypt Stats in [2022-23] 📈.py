# -*- coding: utf-8 -*-

# -- Sheet --

!pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Data for different championships
championships = ['Egyptian Premier League', 'CAF Champions League', 'FIFA Club World Cup']

epl_stats = {
    'App': 34,
    'Goals': 63,
    'Goals conceded': 13,
    'Assists': 40
}

caf_stats = {
    'App': 12,
    'Goals': 23,
    'Goals conceded': 10,
    'Assists': 23
}

fifa_stats = {
    'App': 4,
    'Goals scored': 7,
    'Goals conceded': 8,
    'Assists': 4
}

stats_keys = list(epl_stats.keys())

epl_values = list(epl_stats.values())
caf_values = list(caf_stats.values())
fifa_values = list(fifa_stats.values())

bar_width = 0.25
index = np.arange(len(stats_keys))

plt.figure(figsize=(12, 6))
bars1 = plt.bar(index, epl_values, bar_width, label='Egyptian Premier League')
bars2 = plt.bar(index + bar_width, caf_values, bar_width, label='CAF Champions League')
bars3 = plt.bar(index + bar_width * 2, fifa_values, bar_width, label='FIFA Club World Cup')

plt.xlabel('Statistics')
plt.ylabel('Values')
plt.title('Al-Ahly Egypt Statistics [2022/2023]', fontweight='bold', color='red')  # Set title properties
plt.xticks(index + bar_width, stats_keys)
plt.legend()

# Add values on top of the bars
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        plt.annotate('{}'.format(height),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')

autolabel(bars1)
autolabel(bars2)
autolabel(bars3)

# Add your credit, Twitter account, and website
plt.text(0.5, -0.2, "Created by @SeifAjax04\nseifkhaled.me", ha='center', fontsize=10, transform=plt.gca().transAxes)
# Add the source information on the left
plt.text(0.02, -0.1, "Source: @SofascoreARB", color='red', ha='left', fontsize=10, transform=plt.gca().transAxes)
plt.tight_layout()

# save the plot as a PNG image in Datlore workspace
plt.savefig('Ahly Stats in 22-23.png', dpi=300)

# show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data for different championships
championships = ['Egyptian Premier League', 'CAF Champions League', 'FIFA Club World Cup']

epl_stats = {
    'App': 34,
    'Goals': 63,
    'Goals conceded': 13,
    'Assists': 40
}

caf_stats = {
    'App': 12,
    'Goals': 23,
    'Goals conceded': 10,
    'Assists': 23
}

fifa_stats = {
    'App': 4,
    'Goals scored': 7,
    'Goals conceded': 8,
    'Assists': 4
}

stats_keys = list(epl_stats.keys())

epl_values = list(epl_stats.values())
caf_values = list(caf_stats.values())
fifa_values = list(fifa_stats.values())

bar_width = 0.25
index = np.arange(len(stats_keys))

plt.figure(figsize=(12, 6))
bars1 = plt.bar(index, epl_values, bar_width, label='Egyptian Premier League')
bars2 = plt.bar(index + bar_width, caf_values, bar_width, label='CAF Champions League')
bars3 = plt.bar(index + bar_width * 2, fifa_values, bar_width, label='FIFA Club World Cup')

plt.xlabel('Statistics')
plt.ylabel('Values')
plt.title('Al-Ahly Club Statistics in Different Championships')
plt.xticks(index + bar_width, stats_keys)
plt.legend()

# Add values on top of the bars
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        plt.annotate('{}'.format(height),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')

autolabel(bars1)
autolabel(bars2)
autolabel(bars3)

# Add a grid to the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data for different championships
championships = ['Egyptian Premier League', 'CAF Champions League', 'FIFA Club World Cup']

epl_stats = {
    'App': 34,
    'Goals': 63,
    'Goals conceded': 13,
    'Assists': 40
}

caf_stats = {
    'App': 12,
    'Goals': 23,
    'Goals conceded': 10,
    'Assists': 23
}

fifa_stats = {
    'App': 4,
    'Goals scored': 7,
    'Goals conceded': 8,
    'Assists': 4
}

stats_keys = list(epl_stats.keys())

epl_values = list(epl_stats.values())
caf_values = list(caf_stats.values())
fifa_values = list(fifa_stats.values())

bar_width = 0.25
index = np.arange(len(stats_keys))

plt.figure(figsize=(12, 6))
bars1 = plt.bar(index, epl_values, bar_width, label='Egyptian Premier League')
bars2 = plt.bar(index + bar_width, caf_values, bar_width, label='CAF Champions League')
bars3 = plt.bar(index + bar_width * 2, fifa_values, bar_width, label='FIFA Club World Cup')

plt.xlabel('Statistics')
plt.ylabel('Values')
plt.title('Al-Ahly Egypt Statistics [2022/2023]', fontweight='bold', color='red')  # Set title properties
plt.xticks(index + bar_width, stats_keys)
plt.legend()

# Add values on top of the bars
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        plt.annotate('{}'.format(height),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')

autolabel(bars1)
autolabel(bars2)
autolabel(bars3)

# Add your credit, Twitter account, and website
plt.text(0.5, -0.2, "Created by @SeifAjax04\nseifkhaled.me", ha='center', fontsize=10, transform=plt.gca().transAxes)
# Add the source information on the left
plt.text(0.02, -0.1, "Source: @SofascoreARB", color='red', ha='left', fontsize=10, transform=plt.gca().transAxes)
plt.tight_layout()

# save the plot as a PNG image in Datlore workspace
plt.savefig('Ahly Stats in 22-23.png', dpi=300)

# show the plot
plt.show()

