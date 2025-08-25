import array as arr

array_num = arr.array('i', [1, 4, 2, 4, 8, 7])
print("Original array: " + str(array_num))
print("Number of occurence of the number 4 in the said array: " + str(array_num.count(4)))

array_num.reverse()
print("The reverse order of the items is:: " + str(array_num))