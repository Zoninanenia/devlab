score = int(input())
if score >= 0 and score <= 100 :
  if score >= 80 and score <= 100 :
    print("A")
  if score >= 70 and score <= 79 :
    print("B")
  if score >= 60 and score <= 69 :
    print("C")
  if score >= 50 and score <= 59 :
    print("D")
  if score < 50 :
    print("F")
else:print("ERROR")
