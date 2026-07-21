def reduce_file(file, output_file):
    result = {}

    with open(file, 'r') as f:
        for line in f:
            key, value = line.strip().split(",")
            value = int(value)

            result[key] = result.get(key, 0) + value

    with open(output_file, 'a') as out:
        for k, v in result.items():
            out.write(f"{k} : {v}\n")