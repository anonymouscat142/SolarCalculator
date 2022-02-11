input = []
i=0
with open('SolarCalculations.txt') as f:
    lines = f.readlines()
count = 0
for line in lines:
    count += 1    
print(lines)

def hoursMinutesSeconds(lines):
    i=0
    while(i<len(lines)):
        var1 = lines[i]
        var2 = var1.replace(':','')
        hours = int(var2[0])
        minutes = int(var2[1:3])
        seconds = int(var2[3:5])
        y = (hours + (minutes * .016) + (seconds * .00027))
        lines[i] = "(" + str(i) + "," + str(y) + "),"
        i += 1
    i=0
    out=""
    while(i<len(lines)):
        out = out + lines[i]
        i+=1
    return out

def Minutes(lines):
    i=0
    while(i<len(lines)):
        var = lines[i]
        var2 = float(var[:6]) * 0.0166667
        lines[i] = "(" + str(i) + "," + str(var2) + "),"
        i+=1
    i=0
    out=""
    while(i<len(lines)):
        out = out + lines[i]
        i+=1
    return out

def newLines(out):
    out = '\n'.join(map(str, out))
    return out

out = Minutes(lines)
print(out)