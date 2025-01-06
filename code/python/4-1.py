rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

print(rainbow[2])

sorted_rainbow = rainbow.copy()
sorted_rainbow.sort()
# print(sorted_rainbow)

another_sorted_rainbow = sorted(rainbow)
# print(another_sorted_rainbow)

appended_rainbow = rainbow.copy()
appended_rainbow.append('crimson')
# print(appended_rainbow)

deleted_rainbow = [rainbow[0], rainbow[1], rainbow[6]]
print(deleted_rainbow)

del_rainbow = rainbow.copy()
del del_rainbow[2:6]
print(del_rainbow)