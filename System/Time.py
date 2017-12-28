from datetime import date, time, datetime, timedelta


class Time:
    def __init__(self):
        d = date(680, 1, 3)
        t = time(12, 00)
        self._dt = datetime.combine(d, t)

    def advance(self, hour, minute):
        t = timedelta(hours=hour, minutes=minute)
        self._dt += t

    def get_time(self):
        return self.get_hour() + ":" + self.get_minute()

    def get_month(self):
        return self._dt.strftime("%B")

    def get_weekday(self):
        return self._dt.strftime("%A")

    def get_month_day(self):
        return self._dt.strftime("%d")

    def get_year(self):
        return self._dt.strftime("%Y")

    def get_hour(self):
        return self._dt.strftime("%H")

    def get_minute(self):
        return self._dt.strftime("%M")


def main():
    time_object = Time()
    print(time_object.get_time())
    print(time_object.get_weekday())
    time_object.advance(13, 0)
    print(time_object.get_time())
    print(time_object.get_weekday())


if __name__ == "__main__":
    main()
