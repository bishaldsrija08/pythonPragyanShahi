import shutil

print(shutil.copy("text2.txt", "text3.txt"))
print(shutil.move("text3.txt", "osfolder/text3.txt"))

print(shutil.rmtree("osfolder"))