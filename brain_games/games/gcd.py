def gcd_randoms():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    question = f"{first} {second}"
    randoms = [first, second]
    randoms.sort()
    first = randoms[0]
    second = randoms[1]
    n = first
    while True:
        if second % n == 0 and first % n == 0:
            return [question, n]
        else:
            n -= 1
