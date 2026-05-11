import os

folder = "file handling"   # 👈 space here

if not os.path.exists(folder):
    os.mkdir(folder)

for i in range(1, 11):
    file_path = os.path.join(folder, f"{i}.py")
    
    with open(file_path, "w") as f:
        f.write(f"# This is file {i}\n")

print("Files created successfully!")