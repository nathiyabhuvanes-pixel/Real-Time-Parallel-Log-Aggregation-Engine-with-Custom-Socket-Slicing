import os
import hashlib

def partition(mapped_data, num_reducers):
    if not os.path.exists("partitions"):
        os.makedirs("partitions")

    parts = [[] for _ in range(num_reducers)]

    for key, value in mapped_data:
        index = int(hashlib.md5(key.encode()).hexdigest(), 16) % num_reducers
        parts[index].append((key, value))

    for i, part in enumerate(parts):
        with open(f"partitions/part-{i}.txt", "w") as f:
            for k, v in part:
                f.write(f"{k},{v}\n")