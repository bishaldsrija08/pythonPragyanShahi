f= open("test.txt", "r")
for line in f:
    name, lname, eng, sci = line.split() #split the line into 4 parts and assign to variables
    avg = (int(eng)+int(sci))/2
    print(f"{name} average is {avg}")