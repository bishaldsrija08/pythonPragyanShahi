import os
print(os.listdir())

print(os.path.exists("text2.txt"))

print(os.makedirs("osfolder", exist_ok=True))

print(os.rename("text.txt", "text2.txt"))