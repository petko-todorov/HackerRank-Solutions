def return_book():
    if m1 == m2 and y1 == y2 and d1 > d2:
        fine = 15 * (d1 - d2)
        return fine
    elif m1 > m2 and y1 == y2:
        fine = 500 * (m1 - m2)
        return fine
    elif y1 > y2:
        return 10_000

    return 0


d1, m1, y1 = [int(x) for x in input().split()]  # returned
d2, m2, y2 = [int(x) for x in input().split()]  # expected to be returned

returned = int(f'{d1:02d}{m1:02d}{y1:02d}')
expected = int(f'{d2:02d}{m2:02d}{y2:02d}')

print(return_book())
