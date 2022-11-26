def updatedRank(names, marks, updates, n):

  x = [[0 for j in range(3)] for i in range(n)]
  for i in range(n):

    x[i][0] = names[i]

    x[i][1] = marks[i] + updates[i]

    x[i][2] = i + 1

  highest = x[0]
  for j in range(1, n):
    if (x[j][1] >= highest[1]):
      highest = x[j]

  print("Name: ", highest[0], ", Jump: ", abs(highest[2] - 1), sep="")


names1 = (input("names: ")).split(",")
marks1 = (input("marks: ")).split(",")
updates1 = (input("updates: ")).split(",")
names = list(names1)
marks = list(marks1)
updates = list(updates1)
n = len(marks)
updatedRank(names, marks, updates, n)
