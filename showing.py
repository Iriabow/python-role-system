import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

import dice_box

number_of_dice = 5
number_of_face = 20


value_counting = {}
for i in range(0,1000000):
    dice_roll_sum = dice_box.sum_n_d(number_of_dice, number_of_face)
    if value_counting.get(dice_roll_sum):
        value_counting[dice_roll_sum] += 1
    else:
        value_counting[dice_roll_sum] = 1

objects = tuple(range(number_of_dice,number_of_dice*number_of_face+1))
y_pos = np.arange(len(objects))
print(objects)
print(value_counting)
ocurrences = []
for o in objects:
    count = value_counting.get(o) 
    if count:
        ocurrences.append(count)
    else:
        ocurrences.append(0)


plt.bar(y_pos, ocurrences, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Total dice sum')
plt.title('Central Limit Theorem Test')
plt.show()