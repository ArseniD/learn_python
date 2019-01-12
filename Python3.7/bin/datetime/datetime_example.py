import datetime


if __name__ == "__main__":
    print(datetime.date(2019, 1, 6))
    print(datetime.date(year=2019, month=1, day=6))
    print(datetime.date.today())
    print(datetime.date.fromtimestamp(1000000000))
    print(datetime.date.fromordinal(62555))

    d = datetime.date.today()
    print(d.year)
    print(d.month)
    print(d.day)
    print(d.weekday())  # day of the week starts from 0
    print(d.isoweekday())  # day of the week starts from 1
    print(d.isoformat())  # ISO representation of dates amd times

    print(d.strftime('%A %d %B %Y'))
    print("The date is {:%A %d %B %Y}".format(d))

    e = datetime.date(2019, 1, 5)
    print(e.strftime('%A %-d %B %Y'))  # truncate 0 from date

    # Best pythonic way to extract the date
    print("{date:%A} {date.day} {date:%B} {date.year}".format(date=e))

    print(datetime.date.min)
    print(datetime.date.max)
    print(datetime.date.resolution)

