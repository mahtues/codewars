# http://www.codewars.com/kata/hit-count

def counter_effect(hit_count):
    return [ [ i for i in range(int(c) + 1)  ] for c in hit_count ]
