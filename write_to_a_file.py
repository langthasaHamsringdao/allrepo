import import_file

with open('data.txt') as f:
    data = f.readlines()

with open('write_data.txt', 'w') as f:
    for line in data:
        f.write(line)