#!/usr/bin/env python3
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 2

mfsScores =          (45.58, 49.76)
linearsvcScores =    (45.32, 50.90)
maxent_l1Scores =    (46.99, 51.56)
maxent_l2Scores =    (48.31, 53.23)
randomforestScores = (48.26, 52.17)

# 2016-01-06-13-47-es-gn-MFS-default-regular
# accuracy: 0.4558
# 2016-01-06-13-47-es-gn-linearsvc-l2-c1-default-regular
# accuracy: 0.4532
# 2016-01-06-13-47-es-gn-maxent-l1-c1-default-regular
# accuracy: 0.4699
# 2016-01-06-13-47-es-gn-maxent-l2-c1-default-regular
# accuracy: 0.4831
# 2016-01-06-13-47-es-gn-random-forest-default-default-regular
# accuracy: 0.4826

# 2016-01-06-13-47-es-gn-MFS-default-nonnull
# accuracy: 0.4976
# 2016-01-06-13-47-es-gn-linearsvc-l2-c1-default-nonnull
# accuracy: 0.5090
# 2016-01-06-13-47-es-gn-maxent-l1-c1-default-nonnull
# accuracy: 0.5156
# 2016-01-06-13-47-es-gn-maxent-l2-c1-default-nonnull
# accuracy: 0.5323
# 2016-01-06-13-47-es-gn-random-forest-default-default-nonnull
# accuracy: 0.5217

ind = np.arange(N)  # the x locations for the groups
width = 0.18       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind + 0 * width, mfsScores, width, color='b')
rects2 = ax.bar(ind + 1 * width, linearsvcScores, width, color='g')
rects3 = ax.bar(ind + 2 * width, maxent_l1Scores, width, color='r')
rects4 = ax.bar(ind + 3 * width, maxent_l2Scores, width, color='c')
rects5 = ax.bar(ind + 4 * width, randomforestScores, width, color='m')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Spanish-Guarani classification accuracy')
ax.set_xticks(ind + width * 2.5)
ax.set_xticklabels(('regular', 'nonnull'))

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]),
          ('mfs', 'linearsvc', 'maxent_l1', 'maxent_l2', 'randomforest'),
          loc='lower right')

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

plt.show()
