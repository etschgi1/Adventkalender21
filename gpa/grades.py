noten = [1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 1, 1]  # sem
ects = [7, 7, 7, 3, 1.5, 2.5, 1.5, 4, 1.5, 7, 10, 1]  # sem
notenp = [1, 1, 1, 2, 2, 1, 1, 4, 1, 1]
ectsp = [10, 12.5, 9, 3, 3.5, 6, 3.5, 4.5, 3, 3]
points = {1: 4, 2: 3, 3: 2, 4: 1}
sum_ = 0
sum_p = 0
for c, n in enumerate(noten):
    sum_ += ects[c]*points[n]
for c, n in enumerate(notenp):
    sum_p += ectsp[c]*points[n]
print(f"sem {sum_/sum(ects)}")
print(f"ph {sum_p/sum(ectsp)}")
