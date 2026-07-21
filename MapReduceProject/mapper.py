def map_function(file):
    mapped = []

    with open(file, 'r') as f:
        for line in f:
            parts = line.strip().split(",")

            subject = parts[2]   # Maths / Science / English

            mapped.append((subject, 1))

    return mapped