# Codewars - Clock in Mirror
# https://www.codewars.com/kata/56548dad6dae7b8756000037/train/python


def what_is_the_time(time_in_mirror):
    # return ":".join(time_in_mirror.split(":"))
    if int(time_in_mirror.split(":")[0]) == 12 or 0 or 6:
        h = str(int(time_in_mirror.split(":")[0])).zfill(2)
    else:
        h = str(11 - int(time_in_mirror.split(":")[0])).zfill(2)

    if int(time_in_mirror.split(":")[1]) == 0:
        m = "00"
    else:
        m = str(60 - int(time_in_mirror.split(":")[1])).zfill(2)
    return h + ":" + m


print(what_is_the_time("06:35"))
print(what_is_the_time("11:59"))

print(what_is_the_time("06:35"), "05:25")
print(what_is_the_time("11:59"), "12:01")
print(what_is_the_time("12:02"), "11:58")
print(what_is_the_time("04:00"), "08:00")
print(what_is_the_time("06:00"), "06:00")
print(what_is_the_time("12:00"), "12:00")
print(what_is_the_time("00:10"))