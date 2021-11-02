# # 행 열
# n, m = map(int, input().split())
#
# array = []
#
# # 3 1 2
# # 2 1 4
# for i in range(n):
#     array.append(list(map(int, input().split())))
#
# drawing = []
#
# for i in range(n):
#     drawing.append(min(array[i]))
#
# print(max(drawing))
#
# # O(2n)
#
# #################################################################
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
#
# print(result)
#
# # O(n)
#
# ##########################################################
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = 10001
#     for j in data:
#         min_value = min(min_value, j)
#     result = max(result, min_value)
#
# print(result)

###
# 행 열
n, m = map(int, input().split())


result = 0
min_array = []
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    min_array.append(min_value)

print(max(min_array))

