#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
#   pythoncientifico Project (https://github.com/juniors90/pythoncientifico/).
# Copyright (c) 2021, Juan David Ferreira
# License: MIT
#   Full Text: https://github.com/juniors90/pythoncientifico/blob/main/LICENSE

import matplotlib.pyplot as plt

import numpy as np


def variables(n, jitter_amp):
    """construye datos con ruidos que se representan en el sistema de
    coordenadas cartesianas a través de las variables :math:`x` e :math:`y`,
    donde :math:`y` es el dato ruidoso de :math:`x`.

    :param n: ``int()``
    :param jitter_amp: ``float()``
    :return: ``n`` pares ordenados :math:`(x,y)` con la amplitud
            del ruido ``jitter_amp``.

    * Example

    >>> from pythoncientifico import *
    >>> x, y = variables(50, 4.0)
    >>> plt.plot(x, y, "ok")
    [<matplotlib.lines.Line2D object at 0x052A6E08>]
    >>> plt.show()
    """
    x = np.linspace(0, 10, n)
    jitter = jitter_amp * (np.random.random(n) - 0.5)
    y = x + jitter
    return x, y


x, y = variables(50, 4.0)
plt.plot(x, y, "ok")
plt.grid()
