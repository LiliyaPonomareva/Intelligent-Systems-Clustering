import xml.etree.ElementTree as ET

tree = ET.parse('objects.xml')
root = tree.getroot()

obj1 = []
for row in range(10):
    obj1.append([])
    for column in range(19):
        if column % 2 == 0:
            obj1[row].append(int(root[0][row].text[column]))

obj2 = []
for row in range(10):
    obj2.append([])
    for column in range(19):
        if column % 2 == 0:
            obj2[row].append(int(root[1][row].text[column]))
obj3 = []
for row in range(10):
    obj3.append([])
    for column in range(19):
        if column % 2 == 0:
            obj3[row].append(int(root[2][row].text[column]))

obj4 = []
for row in range(10):
    obj4.append([])
    for column in range(19):
        if column % 2 == 0:
            obj4[row].append(int(root[3][row].text[column]))

obj5 = []
for row in range(10):
    obj5.append([])
    for column in range(19):
        if column % 2 == 0:
            obj5[row].append(int(root[4][row].text[column]))

obj6 = []
for row in range(10):
    obj6.append([])
    for column in range(19):
        if column % 2 == 0:
            obj6[row].append(int(root[5][row].text[column]))

obj7 = []
for row in range(10):
    obj7.append([])
    for column in range(19):
        if column % 2 == 0:
            obj7[row].append(int(root[6][row].text[column]))

obj8 = []
for row in range(10):
    obj8.append([])
    for column in range(19):
        if column % 2 == 0:
            obj8[row].append(int(root[7][row].text[column]))

obj9 = []
for row in range(10):
    obj9.append([])
    for column in range(19):
        if column % 2 == 0:
            obj9[row].append(int(root[8][row].text[column]))

obj10 = []
for row in range(10):
    obj10.append([])
    for column in range(19):
        if column % 2 == 0:
            obj10[row].append(int(root[9][row].text[column]))

obj11 = []
for row in range(10):
    obj11.append([])
    for column in range(19):
        if column % 2 == 0:
            obj11[row].append(int(root[10][row].text[column]))

obj12 = []
for row in range(10):
    obj12.append([])
    for column in range(19):
        if column % 2 == 0:
            obj12[row].append(int(root[11][row].text[column]))

obj13 = []
for row in range(10):
    obj13.append([])
    for column in range(19):
        if column % 2 == 0:
            obj13[row].append(int(root[12][row].text[column]))

obj14 = []
for row in range(10):
    obj14.append([])
    for column in range(19):
        if column % 2 == 0:
            obj14[row].append(int(root[13][row].text[column]))

obj15 = []
for row in range(10):
    obj15.append([])
    for column in range(19):
        if column % 2 == 0:
            obj15[row].append(int(root[14][row].text[column]))

obj16 = []
for row in range(10):
    obj16.append([])
    for column in range(19):
        if column % 2 == 0:
            obj16[row].append(int(root[15][row].text[column]))
