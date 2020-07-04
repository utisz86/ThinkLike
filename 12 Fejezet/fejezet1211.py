import calendar
naptar = calendar.TextCalendar() # Hozd létre egy példányát!
naptar.pryear(2017)            # Mi történik itt?

print()

d = calendar.LocaleTextCalendar(6, "HUNGARIAN")
d.pryear(2017)

for year in range(2010, 2020):
    print(calendar.isleap(year))