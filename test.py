# invalid = [1111,2222,3333,4444,5555,6666,7777,8888,9999]
# dic = {}
# count = 1
# for num in range(1001, 10000):
#     if num not in invalid:
#         print(num)
#         res = int("".join(sorted(list(str(num)), reverse=True))) - int("".join(sorted(list(str(num)))))
#         print(f'{int("".join(sorted(list(str(num)), reverse=True)))} - {int("".join(sorted(list(str(num)))))} = {res}')
#         if res == 999:
#             dic[str(count)] = f"gave 999 at {count}"
#         else:
#             while res != 6174:
#                 count+=1
#                 res = int("".join(sorted(list(str(res)), reverse=True))) - int("".join(sorted(list(str(res)))))
#                 print(f'{int("".join(sorted(list(str(res)), reverse=True)))} - {int("".join(sorted(list(str(res)))))} = {res}')
#             dic[str(num)] = count
#             print(count, " times")
#             count = 1
#             res = 0

# print(dic)

import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, 'test.json')

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data['1232'])

rank = {}

for v in data:
    if(str(data[v]) in rank.keys()):
        rank[str(data[v])] += 1
        # print("here")
    else:
        rank[str(data[v])] = 1

print(rank)