import calendar

years = int(input())

if (calendar.isleap(years)):
  print("Leap Year")
else:
  print("Not a Leap Year")
