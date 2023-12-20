from read_midi import midi_to_vec
import matplotlib.pyplot as plt
import numpy as np
import sys


def main():

    if len(sys.argv )!= 2:
        print('Usage: python midi-svg.py [path-to-midi-file] [number-of-measures]')
    midi_path = sys.argv[1]
    n_measures = int(sys.argv[2])
    vec = midi_to_vec(midi_path)

    # TODO: guard against divide by zero and negative sizes
    size_of_measure = int(len(vec) / n_measures)
    size_of_vec = size_of_measure * n_measures

    A = np.array(vec[0:size_of_vec]).reshape(n_measures, size_of_measure).transpose()
    B, D, Q = np.linalg.svd(A, full_matrices = False)
    C = np.diag(D) @ Q

    B = B[:, 0:2]
    C = C[0:2, :]

    for i in range(len(C[0])):
        x = C[0, i]
        y = C[1, i]
        norm = np.sqrt(x*x + y*y)
        x /= norm
        y /= norm
        C[0, i] = x
        C[1, i] = y

    xvals = C[:1, :]
    yvals = C[1:, :]

    fig, ax = plt.subplots()
    ax.scatter(xvals[0], yvals[0])
    for i in range(len(xvals[0])):
        ax.annotate(i+1, (xvals[0, i], yvals[0, i])) 
    plt.show()


        
if __name__ == '__main__':
    main()
