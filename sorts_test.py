from sorts import *

def test():
    import random

    assert bubble_sort([]) == quick_sort([]) == []

    for i in range(10):
        arr = [random.randrange(1, 100) for _ in range(random.randrange(1, 20))]
        print("unsorted")
        print(arr)
        q_s = quick_sort(arr)
        print("q s:", q_s)
        b_s = bubble_sort(arr)
        print("b s:", b_s)
        p_s = sorted(arr)
        assert b_s == q_s == p_s

if __name__ == "__main__":
    test()
    print("Tests passed!")