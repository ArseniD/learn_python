def fizzbuzz(n, additional_rules=None):
    """

    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(1)
    '1'
    >>> fizzbuzz(25)
    'Buzz'
    >>> fizzbuzz(33, {3: "sdfd"})
    'sdfd'
    >>> fizzbuzz(15)
    'FizzBuzz'

    """
    answer = ""
    rules = {3: "Fizz", 5: "Buzz"}
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
        answer = str(n)
    return answer
