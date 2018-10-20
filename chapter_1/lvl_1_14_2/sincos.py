# 3sin2alphacos3beta

import math


def sin_cos(alpha, beta):
    result = (3 * math.sin(2 * int(alpha)) * math.cos(3 * int(beta)))
    return round(result, 2)
