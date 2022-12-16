myfile = open("input.txt")
content = myfile.read()

scan_info = {}
for line in content.splitlines():
  line = line.split(':')
  scan_info[line[0]] = int(line[1])

myfile = open("input2.txt")
content = myfile.read()

sue_infos = []
for i, line in enumerate(content.splitlines()):
  infos = {}
  line = line.replace(str(i+1)+":", "")
  line = line.replace("Sue ", "")
  for info in line.split(','):
    info = info.strip()
    info = info.split(':')
    infos[info[0]] = int(info[1])
  infos["sue_number"] = i+1
  sue_infos.append(infos)

def filter_sue(sue_info):
  for key, value in sue_info.items():
    if key == "sue_number": continue
    if scan_info[key] != value:
      return False
  return True

print(list(filter(filter_sue, sue_infos)))
