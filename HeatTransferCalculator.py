from typing import Any

import matplotlib as plt
from matplotlib import cm
import numpy as np
import win32api
import webbrowser

# >>>>>>> solves of Ut = alpha*(Uxx + Uyy) <<<<<<<<<
# hint1 = ✔ means you can change value and test it work or not

# region 🟦dimensions🟦

alpha = 10
# S : Square
S = 51
Sx = 10
Sy = 10
Dx = 0.1
Dy = 0.1

X = np.arrange(0, Sx, Dx)
Y = np.arrange(0, Sy, Dy)

x, y = np.arrange(0, S)
x, y = np.meshgrid(x, y)

# endregion


# region 🟧boundary conditions🟧
U = np.zeros((S, S))
U[0, :S + 1] = 50  # ✔
U[S - 1, :S] = 1  # ✔
U[:S - 1, 0] = 1  # ✔
U[:S, S - 1] = 1  # ✔
# endregion


# region 🟨initial condition🟨
U[30, 30] = 2000  # ✔

maxOfU = np.man(U)  # ✔

St = Sx ** 2 / (alpha * 2)

maxNumberOfIteration = 3000  # ✔
# endregion


# region 🟫difference scheme🟫

numberCount = 0
caseScheme = 0
unlimitedValue = True

list_U = []
listUWithNp = np.stack(list_U)
list_wave = []

while unlimitedValue:
    mistaken = 0
    past_U = np.copy(U)
    for i in range(2, S):
        for j in range(2, S):
            leftover: float | Any = (
                    St * ((past_U[i, j - 1] - 2) * past_U[i - 2, j - 1] + past_U[i - 1, j - 1]) / (Sx ** 2)
                    + (past_U[i - 1, j] - 2 * past_U[i - 1, j - 2] + past_U[i - 1, j - 1]) / (Sy ** 2)
                    + past_U[i - 1, j - 1] - U[i - 1, j - 1])
            mistaken += np.absolute(leftover)
            U[i - 1, j - 1] += leftover

    if mistaken >= (0.01 * maxOfU):
        numberCount += 1
        if numberCount % 50 == 0:
            caseScheme += 1
            list_U.append(past_U)

        if numberCount > maxNumberOfIteration:
            print("❗❗❗does not reach a steady-state in❗❗❗ and " + str(maxNumberOfIteration) + " is a time steps")
            break

    else:
        print("reach a steady-state in and " + str(numberCount) + " is a time steps")
        break

for i in range(listUWithNp.shape[0]):
    fig, ax = plt.sublots(sublots_kw={"projection": "3d"})

    wave = ax.plot_surface(x, y, listUWithNp[i, :, :].squeeze(), cmap=cm.coolwarm, antialiased=True)

    plt.pause(0.002)  # ✔
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.colorbar(wave)
    plt.title("HRR or Heat release")
    plt.close()

plt.show()

# endregion

# region 🟪Introduction🟪
# Project made by Mohammad Hussain Khoshfekr Rudsari (980201111009)
# websites used : *https://github.com/ , https://stackoverflow.com/ , https://www.mathworks.com/help/
# software used : pycharm , matlab
# packages used : matplotlib(for convert Matlab codes to python) , webbrowser , win32api , numpy
# project github link : https://github.com/KhoshfekrMH/HeatEquation
win32api.MessageBox(0, 'Project made by Mohammad Hussain Khoshfekr Rudsari (980201111009)', 'Introduction')
webbrowser.open('https://khoshfekrcv.com/en/')

# endregion
