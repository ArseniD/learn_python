import datetime


if __name__ == "__main__":
    print(datetime.time(3))
    print(datetime.time(3, 1))
    print(datetime.time(3, 1, 2))
    print(datetime.time(3, 1, 2, 232))

    print(datetime.time(hour=23, minute=59, second=59, microsecond=9999))

    t = datetime.time(10, 32, 47, 675623)
    print(t.hour)
    print(t.minute)
    print(t.second)
    print(t.microsecond)

    print(t.isoformat())
    print(t.strftime('%Hh%Mm%Ss'))

    # Besy pythonic way to display the time
    print("{t.hour}h{t.minute}m{t.second}s".format(t=t))

    print(datetime.time.min)
    print(datetime.time.max)
    print(datetime.time.resolution)
