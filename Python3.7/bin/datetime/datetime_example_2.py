import datetime


if __name__ == "__main__":
    print(datetime.datetime(2003, 5, 12, 14, 33, 22, 245323))
    print(datetime.datetime.today())
    print(datetime.datetime.now())
    print(datetime.datetime.utcnow())
    print(datetime.datetime.fromordinal(5))
    print(datetime.datetime.fromtimestamp(3635352))
    print(datetime.datetime.utcfromtimestamp(3635352))

    d = datetime.date.today()
    t = datetime.time(8, 15)
    print(datetime.datetime.combine(d, t))
    dt = datetime.datetime.strptime("Monday 6 January 2019, 12:13:31",
                                    "%A %d %B %Y, %H:%M:%S")
    print(dt)
    print(dt.date())
    print(dt.time())
    print(dt.day)
    print(dt.isoformat())
