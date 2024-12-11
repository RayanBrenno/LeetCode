def checkRecord(s):
    return True if s.count("A") < 2 and s.count("LLL") == 0 else False

s = "PPALLP"
print(checkRecord(s))