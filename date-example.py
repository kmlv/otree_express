"""
    date-example.py
    Examples of loading different dates
"""

import datetime
import dateutil.parser
import calendar

# Case 1: otree date
ex = "2016-10-29 00:01:09.466406+00:00"
a = dateutil.parser.parse(ex)
print(a.isoformat())

# Case 2: ISO String, AKA js date string
ex = "2016-10-29T00:01:10.005Z"
b = dateutil.parser.parse(ex)
stamp = calendar.timegm(b.timetuple())
print(b.isoformat())

# Case 3: UNIX timestamp with decimal, Shimmer sensor
ex = 1479773262604.13
c = datetime.datetime.utcfromtimestamp(ex/1000)
print(c.isoformat())

# Case 4: UNIX timestamp without decimal
ex = 1479774225986
d = datetime.datetime.utcfromtimestamp(ex/1000)
print(d.isoformat())
