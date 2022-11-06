file = open('OzerovSS_Ub-23_vvod(1variant).txt', encoding='utf-8')

line = file.readlines()

print("Матрица")
A=[]
for element in line:
    matrix = element.replace("\n","   ").split()
    A.append(str(matrix))
print(A)
file.close()
file1 = open('OzerovSS_Ub-23_vivod(1variant).txt', 'w', encoding='utf-8')
print(file1.write(str(A)))
file1.close()




