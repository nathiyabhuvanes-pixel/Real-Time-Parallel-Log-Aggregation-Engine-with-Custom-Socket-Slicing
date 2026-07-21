import os

def split_file(input_file, output_dir, num_splits=3):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_splits

    for i in range(num_splits):
        start = i * chunk_size
        end = None if i == num_splits - 1 else (i + 1) * chunk_size

        with open(f"{output_dir}/part-{i}.txt", "w") as out:
            out.writelines(lines[start:end])