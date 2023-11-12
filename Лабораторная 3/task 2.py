def find_common_participants(first_group, second_group, sep=","):
    first_set = set(first_group.split(sep))
    second_set = set(second_group.split(sep))
    group = list(second_set.intersection(first_set))
    group.sort()
    return group
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, sep="|")
print(result)