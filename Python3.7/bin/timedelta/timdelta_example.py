import datetime


if __name__ == "__main__":
    print(datetime.timedelta(milliseconds=1, microseconds=1000))

    td = datetime.timedelta(weeks=1, minutes=2, milliseconds=5500)

    print(td)
    print(td.days)
    print(td.seconds)
    print(td.microseconds)
    print(str(td))
    print(repr(td))

    a = datetime.datetime(year=2019, month=5, day=8, hour=14, minute=22)
    b = datetime.datetime(year=2019, month=3, day=14, hour=12, minute=9)
    d = a - b

    print(d)
    print(d.total_seconds())
    print(datetime.date.today() + datetime.timedelta(weeks=1) * 3)
