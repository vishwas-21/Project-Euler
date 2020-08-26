import time

start = time.time()
n = 50
ans = n * n * 3     # These are solutions when both the other points are on axes
for a in range(1, n + 1):   # And Here we are choosing a point and finding integer solutions to line perpendicular to
    for b in range(1, n + 1):   # the line passing through origin and selected point
        x = (a * a + b * b) // a
        while x >= 0:
            y = (a * a + b * b - a * x) / b
            if y.is_integer() and y <= n and (a != x or b != y) and x <= n:
                ans += 1
            x -= 1
print(ans)
print(time.time() - start)