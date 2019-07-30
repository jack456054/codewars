def race(v1, v2, g):
    if v1 >= v2:
        return None
    result = int(g / (v2 - v1) * 3600)
    return [result // 3600, result // 60 % 60, result % 60]


if __name__ == '__main__':
    print(race(720, 850, 70))
    print(race(80, 91, 37))
    print(race(80, 100, 40))
