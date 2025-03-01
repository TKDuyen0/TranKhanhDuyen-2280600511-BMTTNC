def taoTupleTuList(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = taoTupleTuList(numbers)

print("List: ",numbers)
print("Tuple từ List: ", my_tuple)