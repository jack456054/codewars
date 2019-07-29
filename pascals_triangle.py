def pascals_triangle(n):
    result, current_layer = [1], [1]
    if n == 1:
        return current_layer
    for i in range(0, n - 1):
        last_layer = current_layer.copy()
        # for j in range(1, len(last_layer)):
        #     current_layer[j] = last_layer[j] + last_layer[j - 1]
        current_layer = [last_layer[j] + last_layer[j - 1] if j > 0 else 1 for j in range(0, len(last_layer))]
        current_layer.append(1)
        result.extend(current_layer)
    return result


if __name__ == '__main__':
    print(pascals_triangle(1))
    print(pascals_triangle(2))
    print(pascals_triangle(3))
    print(pascals_triangle(4))
