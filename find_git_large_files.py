import os
import subprocess

print("Scanning Git repo for large files...")

# Get all git object hashes with paths
output = subprocess.check_output(["git", "rev-list", "--objects", "--all"], text=True)
entries = output.splitlines()

sizes = []
for entry in entries:
    try:
        sha, path = entry.split(" ", 1)
        size = int(subprocess.check_output(["git", "cat-file", "-s", sha]))
        sizes.append((size, path))
    except:
        continue

# Sort by size descending
sizes.sort(reverse=True)

for size, path in sizes[:20]:  # Show top 20 large files
    print(f"{round(size/1024/1024, 2)} MB\t{path}")
