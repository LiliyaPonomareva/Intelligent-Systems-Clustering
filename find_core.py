from create_obj import *

core1 = []
core2 = []
core3 = []
core4 = []

for i in range(10):
    core1.append([])
    for j in range(10):
        core1[i].append(float(obj1[i][j] + obj2[i][j] + obj3[i][j])/3)

for i in range(10):
    core2.append([])
    for j in range(10):
        core2[i].append(float(obj4[i][j] + obj5[i][j] + obj6[i][j])/3)

for i in range(10):
    core3.append([])
    for j in range(10):
        core3[i].append(float(obj7[i][j] + obj8[i][j] + obj9[i][j])/3)

for i in range(10):
    core4.append([])
    for j in range(10):
        core4[i].append(float(obj10[i][j] + obj11[i][j] + obj12[i][j])/3)

