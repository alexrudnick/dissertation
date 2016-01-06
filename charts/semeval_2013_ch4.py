#!/usr/bin/env python3
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 2

mfsScores = (23.23, 53.07)
chipaScores = (28.97, 58.73)
hltdiScores = (29.36, 62.61)
xlingScores = (19.59, 44.83)
limsiScores = (24.70, 49.01)
nrcScores = (32.16, 41.65)
wsd2Scores = (28.65, 58.23)
psScores = (31.72, 0.0)

ind = np.arange(N)  # the x locations for the groups
width = 0.12       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind + 0 * width, mfsScores, width, color='b')
rects2 = ax.bar(ind + 1 * width, chipaScores, width, color='g')
rects3 = ax.bar(ind + 2 * width, hltdiScores, width, color='r')
rects4 = ax.bar(ind + 3 * width, xlingScores, width, color='c')
rects5 = ax.bar(ind + 4 * width, limsiScores, width, color='m')
rects6 = ax.bar(ind + 5 * width, nrcScores, width, color='y')
rects7 = ax.bar(ind + 6 * width, wsd2Scores, width, color='#FF6666')
rects8 = ax.bar(ind + 7 * width, psScores, width, color='#6666FF')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('SemEval Precision scores: 2013 task')
ax.set_xticks(ind + width * 4.0)
ax.set_xticklabels(('best', 'oof'))

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0], 
           rects7[0], rects8[0]),
          ('mfs', 'chipa', 'hltdi', 'xling', 'limsi', 'nrc', 'wsd2', 'ps'),
          loc='upper left')

## based on autolabel by Lindsey Kuper
## http://composition.al/blog/2015/11/29/a-better-way-to-add-labels-to-bar-charts-with-matplotlib/
def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()

        # Fraction of axis height taken up by this rectangle
        p_height = (height / y_height)

        # If we can fit the label above the column, do that;
        # otherwise, put it inside the column.
        if p_height > 0.95: # arbitrary; 95% looked good to me.
            label_position = height - (y_height * 0.05)
        else:
            label_position = height + (y_height * 0.01)

        ax.text(rect.get_x() + rect.get_width()/2., label_position,
                '%0.1f' % height,
                ha='center', va='bottom')

autolabel(rects1, ax)
autolabel(rects2, ax)
autolabel(rects3, ax)
autolabel(rects4, ax)
autolabel(rects5, ax)
autolabel(rects6, ax)
autolabel(rects7, ax)
autolabel(rects8, ax)

plt.show()
