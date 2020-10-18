from covariance import *

def distance(obj, core, S):
    #преобразуем объект, ядро и матрицу ковариаций в массивы, чтобы использовать numpy
    core = numpy.array(core, dtype=float)
    obj = numpy.array(obj, dtype=float)
    S = numpy.array(S, dtype=float)

    #найдем разность между элементами объекта и ядра
    diff = obj - core

    #транспонируем разность
    diff_transp = diff.transpose()

    # сделаем списком разность
    diff = diff.flatten().tolist()

    # сделаем списком транспонированную разность
    diff_transp = diff_transp.flatten().tolist()

    #заведем единичную матрицу 10х10
    E = numpy.eye(100)

    #сумма матрицы ковариаций и единичной матрицы
    SE = S + E

    #найдем обратную ей
    SE_inverse = numpy.linalg.inv(SE)

    #найдем расстояние Евклида-Махаланобиса
    D = numpy.dot(diff_transp, SE_inverse)
    D = numpy.dot(D, diff)
    return(D)
