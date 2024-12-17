from itertools import combinations

def is_special_sum_set(s):
    n = len(s)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                for subset_a in combinations(s, i):
                    for subset_b in combinations(s, j):
                        if set(subset_a).isdisjoint(set(subset_b)):
                            sum_a, sum_b = sum(subset_a), sum(subset_b)
                            if (i > j and sum_a <= sum_b) or (i < j and sum_a >= sum_b):
                                return False

    subset_sums = {}
    for i in range(1, n):
        for subset in combinations(s, i):
            subset_sum = sum(subset)
            if subset_sum in subset_sums:
                if set(subset_sums[subset_sum]).isdisjoint(set(subset)):
                    return False
            subset_sums[subset_sum] = subset
    return True

def generate_next_set(previous_set):
    b = previous_set[len(previous_set) // 2]
    next_set = [b]
    for elem in previous_set:
        next_set.append(b + elem)
    return next_set

def main():
    sets = [[1],[1, 2],[2, 3, 4],[3, 5, 6, 7], [6, 9, 11, 12, 13],[11, 18, 19, 20, 22, 25]]

    previous_set = sets[-1]
    next_set = generate_next_set(previous_set)

    if is_special_sum_set(next_set):
        print("The generated set satisfies the special sum set conditions!")
    else:
        print("The generated set does NOT satisfy the special sum set conditions!")

    print("Generated Set for n=7:", next_set)
    print("Corresponding Set String:", ''.join(map(str, next_set)))

if __name__ == "__main__":
    main()
