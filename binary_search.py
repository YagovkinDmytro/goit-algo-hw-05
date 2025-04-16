def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_border = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
        # інакше x присутній на позиції і повертаємо його
        else:
            upper_border = arr[mid + 1]
            return (iterations, upper_border)
    # якщо елемент не знайдений
    return -1

arr = [0.1, 0.2, 0.45, 0.59, 1.3, 2.1, 2.4, 3.0, 3.2, 4.5, 4.9, 10.9, 40.5]
x = 2.0
result = binary_search(arr, x)
if result != -1:
    print(f"Element found in '{result[0]}' iterations, upper bound '{result[1]}'")
else:
    print("Element is not present in array")