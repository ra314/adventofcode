myfile = open("input2.txt")
content = myfile.read()

print(content.count("(") - content.count(")"))
