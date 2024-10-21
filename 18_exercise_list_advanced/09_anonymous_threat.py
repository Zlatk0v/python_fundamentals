data_list = input().strip().split()

while True:
    command = input().strip()

    if command == "":
        break

    parts = command.split()
    action = parts[0]

    if action == "merge":
        start_index = int(parts[1])
        end_index = int(parts[2])

        start_index = max(0, start_index)
        end_index = min(len(data_list) - 1, end_index)

        if start_index < end_index:
            merged_string = ''.join(data_list[start_index:end_index + 1])
            data_list[start_index:end_index + 1] = [merged_string]

    elif action == "divide":
        index = int(parts[1])
        partitions = int(parts[2])

        if partitions > 0:
            element = data_list[index]
            part_size = len(element) // partitions
            remainder = len(element) % partitions
            divided_parts = []
            start = 0

            for i in range(partitions):
                extra = 1 if i < remainder else 0
                divided_parts.append(element[start:start + part_size + extra])
                start += part_size + extra

            data_list[index:index + 1] = divided_parts

print(' '.join(data_list))
