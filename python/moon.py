
''' moon_phases.py
determine the moon phase at a given date
(mildly off on moon's light intensity)
checked with http://aa.usno.navy.mil/data/docs/RS_OneDay.html
tested with Python274 and Python331  by  vegaseat  02may2013
'''
def moon_phase(month, day, year):
    ages = [18, 0, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7]
    offsets = [-1, 1, 0, 1, 2, 3, 4, 5, 7, 7, 9, 9]
    description = ["new (totally dark)",
      "waxing crescent (increasing to full)",
      "in its first quarter (increasing to full)",
      "waxing gibbous (increasing to full)",
      "full (full light)",
      "waning gibbous (decreasing from full)",
      "in its last quarter (decreasing from full)",
      "waning crescent (decreasing from full)"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if day == 31:
        day = 1
    days_into_phase = ((ages[(year + 1) % 19] +
                        ((day + offsets[month-1]) % 30) +
                        (year < 1900)) % 30)
    index = int((days_into_phase + 2) * 16/59.0)
    #print(index)  # test
    if index > 7:
        index = 7
    status = description[index]
    # light should be 100% 15 days into phase
    light = int(2 * days_into_phase * 100/29)
    if light > 100:
        light = abs(light - 200);
    date = "%d%s%d" % (day, months[month-1], year)
    return date, status, light


# put in a date you want ...
# 26jan2009 is the start of the Chinese New Year for 2009
# the moon is at its lowest intensity
month = 12
day = 17
year = 1945  # use yyyy format
date, status, light = moon_phase(month, day, year)
print("moon phase on %s is %s, light = %d%s" % (date, status, light, '%'))
''' result ...
moon phase on 26Jan2009 is waning crescent (decreasing from full), light = 0%
'''



