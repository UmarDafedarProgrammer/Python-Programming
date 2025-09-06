# Read the file content and display
FilePath = "C:/Users/umard/OneDrive/Desktop/Repo/GenerativeAI/virt_env_dev/Repo/Python-Programming/DataFolder"
FileName = "Sample.txt"

with open(f"{FilePath}/{FileName}", "r") as file:
    content = file.read()
    print(content)

with open(f"{FilePath}/{FileName}", "r") as file:
    for line in file:
        print(line.strip())