_data = {
    "p_name": "Ivan",
    "p_last_name": "Ivanov",
    "p_second_name": "Ivanovich",
}

p_name = _data["p_name"]
p_last_name = _data["p_last_name"]
p_second_name = _data["p_second_name"]

result = f'{p_last_name} {p_name} {p_second_name}'
print(result)