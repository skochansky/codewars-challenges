def isbn_converter(isbn):
    total_sum = 0
    counter = 1
    isbn = isbn[:-1]
    isbn = "978-" + isbn
    for char in isbn:
        if char.isdigit():
            # alternate from left to right by 1 or 3
            if counter % 2 == 0:
                total_sum += int(char) * 3
            else:
                total_sum += int(char) * 1
            counter += 1
    result = total_sum % 10
    if result == 0:
        return isbn + "0"
    else:
        return isbn + str(10 - result)

