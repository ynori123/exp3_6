import random

year = "2015"
month = "Aug"

record_style = "{0}/{1}/{2:02d} {3:2.3f}"

outfile = open('temperature.dat', "w", encoding="utf8")
#header
outfile.write("  年/月/日      気温［℃］\n")

for day in range(1,32) :
    random.seed()
    temperature = random.uniform(30.0, 40.0)

    outfile.write(record_style.format(year, month, day, temperature))
    outfile.write("\n")
    day += 1