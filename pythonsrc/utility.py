import steepestGradientDescent as SGD
import conjugateGradient as CG
import numpy as np
import normFunction as nf
import matplotlib.pyplot as plt
import os


def readMatrix(type, number):
    raw = []
    with open('../Matrices/Matrix' + type + '/matrix' + type + str(number) + '.txt', 'r') as f:
        for line in f:
            raw.append(line.split())
    A = np.array(raw, dtype=float)
    return A


# we created this two functions so we can calculate
# the norm as a call froma an API
def normCG(A):
    f = nf.normFunction(A)
    CGoptimizer = CG.conjugateGradient(f)
    return CGoptimizer.ConjugateGradientTIME()


def normSDG(A):
    f = nf.normFunction(A)
    SGDoptimizer = SGD.steepestGradientDescent(f)
    return SGDoptimizer.steepestGradientDescentTIME()


def density(type):
    if type == 'A':
        return 1
    elif type == 'B':
        return 1
    elif type == 'C':
        return 1
    elif type == 'D':
        return 0.5
    elif type == 'E':
        return 0.5
    elif type == 'F':
        return 0.25
    elif type == 'G':
        return 0.25
    elif type == 'H':
        return 'Random'


def printPlot(errorsSGD=None, relerrorsSGD=None, gradientsSGD=None, errorsCG=None, relerrorsCG=None, gradientsCG=None,
              A=None, type=None, num=None):
    yLabel1 = 'Absolute Error'
    yLabel2 = 'Relative Error'
    yLabel3 = 'Norms Gradient'
    xLabel1 = 'Iterations'

    fig, [errPlot, relErrPlot, gradPlot] = plt.subplots(3, 2, sharex=False, sharey=False)
    fig.set_size_inches(18.5, 10.5)
    m, n = np.shape(A)

    errPlot[0].set_title(
        'Steepest Gradient Descent \n Type ' + type + '     Density =  ' + str(density(type)) + '    M = ' + str(
            m) + ' N = ' + str(n))
    errPlot[0].set(ylabel=yLabel1)
    errPlot[0].set_yscale('log')
    errPlot[0].plot(errorsSGD)

    relErrPlot[0].plot(relerrorsSGD)
    relErrPlot[0].set_yscale('log')
    relErrPlot[0].set(ylabel=yLabel2)

    gradPlot[0].set(ylabel=yLabel3)
    gradPlot[0].set(xlabel=xLabel1)
    gradPlot[0].set_yscale('log')
    gradPlot[0].plot(gradientsSGD)

    errPlot[1].set_title(
        'Conjugate Gradient \n Type ' + type + '     Density =  ' + str(density(type)) + '    M = ' + str(
            m) + ' N = ' + str(n))
    errPlot[1].set_yscale('log')
    errPlot[1].plot(errorsCG, "C1")

    relErrPlot[1].plot(relerrorsCG, 'C1')
    relErrPlot[1].set_yscale('log')

    gradPlot[1].set(xlabel=xLabel1)
    gradPlot[1].set_yscale('log')
    gradPlot[1].plot(gradientsCG, 'C1')
    plt.show()

    savePlot(type, num, fig)


def savePlot(type, num, fig):

    directory = "../Plot/"
    if num == "0":
        file = "AVG" + type + num + ".png"
    else:
        file = type + num + ".png"
    if not os.path.exists(directory):
        os.makedirs(directory)
    fig.savefig(directory + file)
