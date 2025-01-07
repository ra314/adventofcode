import sys

def read() -> str:
  if len(sys.argv) != 2:
    assert(False)
  filename: str
  match sys.argv[1]:
    case "-1":
      filename = "1in.txt"
    case "-2":
      filename = "2in.txt"
    case _:
      print("File number arg not provided", file=sys.stderr)
      assert(False)
  content = open(filename, "r").read()
  if not content:
    print("File is empty or not found", file=sys.stderr)
  return content
