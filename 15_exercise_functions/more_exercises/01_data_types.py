def process_input(def_data_type: str, max_value):
    if def_data_type == "int":
        max_result = max_value * 2
    elif def_data_type == "real":
        max_result = format(max_value * 1.5, '.2f')
    elif def_data_type == "string":
        max_result = f"${max_value}$"
    return max_result


data_type = input().strip().lower()
value_input = input()

if data_type == "int":
    value = int(value_input)
elif data_type == "real":
    value = float(value_input)
elif data_type == "string":
    value = value_input

result = process_input(data_type, value)
print(result)
