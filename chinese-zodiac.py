# http://www.codewars.com/kata/chinese-zodiac

def chinese_zodiac(year):
    animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']

    return '{} {}'.format(elements[(year - 1984) // 2 % 5], animals[(year - 1984) % 12])
