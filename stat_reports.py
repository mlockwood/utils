#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Lockwood'
__github__ = 'mlockwood'
__email__ = 'lockwm@uw.edu'


def accuracy(acc, file):
    writer = open('{}.acc'.format(file), 'w')
    # New sorted acc
    sorted_acc = {}
    # Store correct and incorrect results
    acc_total = [0, 0]

    # Store labels and sort them
    for label in acc.keys():
        values = []
        for key in acc[label]:
            index = 0 if (key == label or key == '<correct>' or key == 'standard') else 1
            acc_total[index] += acc[label][key]
            values.append((key, acc[label][key]))
        values = sorted(values, key=lambda x: x[1], reverse=True)
        sorted_acc[label] = values

    # Print out accuracy results
    writer.write('Accuracy: ' + str(0.0 if sum(acc_total) else acc_total[0] / sum(acc_total)) + '\n\n')

    # Process for each label
    for label in sorted(sorted_acc.keys()):
        writer.write(str(label) + '\n')
        for value in sorted_acc[label]:
            writer.write('\t{0:20s}\t{1:8d}'.format(value[0], value[1]) + '\n')
        writer.write('\n')
    writer.close()


def out_evaluation(correct_total, n, incorrect_list, correct_list, file):
    # Write results to file
    writer = open('{}.out'.format(file), 'w')
    writer.write('Accuracy: {}\n'.format(correct_total / float(n)))
    writer.write('Correct: {}; Total: {}\n\n'.format(correct_total, n))

    # Write incorrect_list
    writer.write('Incorrect pairs\n')
    [writer.write('{0:56s} Gold: {1:20s} System: {2:20s}\n'.format(*entry)) for entry in incorrect_list]

    # Write correct list
    writer.write('\nCorrect pairs\n')
    [writer.write('{0:56} Gold: {1:20s} System: {2:20s}\n'.format(*entry)) for entry in correct_list]