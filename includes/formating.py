# import standard modules
import pytz
import datetime


def s_to_hms(seconds, max_hours=24):
    time = float(seconds)
    hours = int(time // 3600)
    time %= 3600
    minutes = int(time // 60)
    time %= 60
    seconds = int(time)

    return "{:02d}hrs {:02d}mins {:02d}s".format(hours, minutes, seconds)

def s_to_ms(seconds):
    time = float(seconds)
    minutes = int(time // 60)
    time %= 60
    seconds = int(time)

    return "{:02d}mins {:02d}s".format(minutes, seconds)


def s_to_hm(seconds, max_hours=24):
    time = float(seconds)
    days = int(float(seconds) // (24 * 3600))
    time %= (24 * 3600)
    hours = int(time // 3600) + 24 * days
    time %= 3600
    minutes = int(time // 60)

    str_max_hours = ">{} hours".format(max_hours)
    return "{: >9}".format(str_max_hours) if hours > max_hours else "{: >2}h {: >2}min".format(hours, minutes)


def s_to_dhm(seconds, max_days=99):
    time = float(seconds)
    days = int(float(seconds) // (24 * 3600))
    time %= (24 * 3600)
    hours = int(time // 3600)
    time %= 3600
    minutes = int(time // 60)

    str_max_days = "> {} days".format(max_days)
    return "{: >13}".format(str_max_days) if days > max_days else "{: >2}d {: >2}h {: >2}min".format(days, hours, minutes)


def ts_to_date(timestamp):
    return datetime.date.fromtimestamp(timestamp, tz=pytz.UTC)


def ts_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, tz=pytz.UTC)
