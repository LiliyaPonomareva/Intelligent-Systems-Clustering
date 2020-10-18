from find_core import *
import numpy

def Matrix_of_Covarience(object1, object2, object3, core):

    object1 = numpy.array(object1, dtype=float)
    object2 = numpy.array(object2, dtype=float)
    object3 = numpy.array(object3, dtype=float)
    core = numpy.array(core, dtype=float)

    object1 = object1.flatten().tolist()
    object2 = object2.flatten().tolist()
    object3 = object3.flatten().tolist()
    core = core.flatten().tolist()

    matrix = []
    for i in range(100):
        matrix.append([])
        for j in range(100):
            a = (object1[i] - core[i]) * (object1[j] - core[j])
            b = (object2[i] - core[i]) * (object2[j] - core[j])
            c = (object3[i] - core[i]) * (object3[j] - core[j])
            matrix[i].append(float(a+b+c)/2)
    return(matrix)

matrix1 = Matrix_of_Covarience(obj1, obj2, obj3, core1)
matrix2 = Matrix_of_Covarience(obj4, obj5, obj6, core2)
matrix3 = Matrix_of_Covarience(obj7, obj8, obj9, core3)
matrix4 = Matrix_of_Covarience(obj10, obj11, obj12, core4)