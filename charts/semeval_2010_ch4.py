#!/usr/bin/env python3
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 2

mfsScores = (18.36, 48.41)
chipaScores = (22.36, 59.11)
uvtScores = (23.42, 43.12)
t3Scores = (19.78, 35.84)
uhdScores = (20.48, 38.78)
fccScores = (15.09, 40.76)

ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind + 0 * width, mfsScores, width, color='b')
rects2 = ax.bar(ind + 1 * width, chipaScores, width, color='g')
rects3 = ax.bar(ind + 2 * width, uvtScores, width, color='r')
rects4 = ax.bar(ind + 3 * width, t3Scores, width, color='c')
rects5 = ax.bar(ind + 4 * width, uhdScores, width, color='m')
rects6 = ax.bar(ind + 5 * width, fccScores, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('SemEval Precision scores: 2010 task')
ax.set_xticks(ind + width * 3.0)
ax.set_xticklabels(('best', 'oof'))

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0]),
          ('mfs', 'chipa', 'uvt', 't3', 'uhd', 'fcc'),
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

plt.show()
