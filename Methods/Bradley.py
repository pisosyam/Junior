def Bradley_threshold(src, width, height):
    s = width / 8
    s2 = s // 2
    t = 0.15
    count = 0
    res = [0] * width * height

    # рассчитываем интегральное изображение
    integral_image = [0] * width * height

    for i in range(width):
        sum = 0
        for j in range(height):
            index = j * width + i
            sum += src[index]
            if i == 0:
                integral_image[index] = sum
            else:
                integral_image[index] = integral_image[index - 1] + sum

    # находим границы для локальных областей
    for i in range(width):
        for j in range(height):
            index = j * width + i

            x1 = i - s2
            x2 = i + s2
            y1 = j - s2
            y2 = j + s2

            if x1 < 0:
                x1 = 0
            if x2 >= width:
                x2 = width - 1
            if y1 < 0:
                y1 = 0
            if y2 >= height:
                y2 = height - 1

            count = (x2 - x1) * (y2 - y1)

            sum = (integral_image[y2 * width + x2] - integral_image[y1 * width + x2]
                   - integral_image[y2 * width + x1] + integral_image[y1 * width + x1])
            if src[index] * count < sum * (1 - t):
                res[index] = 0
            else:
                res[index] = 255
    return res
