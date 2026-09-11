# Example 2.5 - THE LOOP2.PY PROGRAM
# Nested for loop (loop di dalam loop)

for i in range(5):
    for j in range(5):
        x = i * j
        print(x)
    print("Inner Loop Finished")
print("Outer Loop Finished")
