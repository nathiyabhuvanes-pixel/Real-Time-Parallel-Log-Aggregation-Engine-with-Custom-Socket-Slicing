import os
from splitter import split_file
from mapper import map_function
from partitioner import partition
from sorter import sort_file
from reducer import reduce_file

INPUT = "input/input.txt"
INTERMEDIATE = "intermediate"
OUTPUT = "output/result.txt"
REDUCERS = 3

# STEP 1: Split
split_file(INPUT, INTERMEDIATE)

# STEP 2: Map
mapped = []
for file in os.listdir(INTERMEDIATE):
    path = os.path.join(INTERMEDIATE, file)
    mapped.extend(map_function(path))

# STEP 3: Partition
partition(mapped, REDUCERS)

# STEP 4: Sort
for file in os.listdir("partitions"):
    sort_file(os.path.join("partitions", file))

# STEP 5: Reduce
if os.path.exists(OUTPUT):
    os.remove(OUTPUT)

for file in os.listdir("partitions"):
    reduce_file(os.path.join("partitions", file), OUTPUT)

print("✅ Completed! Check output/result.txt")