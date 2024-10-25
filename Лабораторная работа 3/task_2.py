# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, separator = ","):
    str_1 = set(str_1.split(separator))
    str_2 = set(str_2.split(separator))
    result = sorted(list(str_1.intersection(str_2)))
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

a = find_common_participants(participants_first_group, participants_second_group, separator = "|")
print(a)
# TODO Провеьте работу функции с разделителем отличным от запятой
