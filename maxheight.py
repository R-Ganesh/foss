def max_area(height):
    n = len(height)
    max_water = 0

    for i in range(n):
        for j in range(i + 1, n):
            h = min(height[i], height[j])
            w = j - i
            max_water = max(max_water, h * w)

    return max_water
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(height)
print(result)