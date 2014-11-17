from __future__ import unicode_literals
from collections import OrderedDict

RULES = OrderedDict([
    (3, "Fizz"),
    (5, "Buzz"),
    (7, "Sivv"),
])


def fizz_buzz(num):
    output = ""
    if not (num % 3):
        output += "Fizz"
    if not (num % 5):
        output += "Buzz"
    if not output:
        output = str(num)
    return output


def extensible_fizzbuzz(num):
    output = ""
    for factor in RULES:
        if not (num % factor):
            output += RULES[factor]
    if not output:
        output = str(num)

    return output

if __name__ == '__main__':
    for i in xrange(200):
        print i, fizz_buzz(i), extensible_fizzbuzz(i)
