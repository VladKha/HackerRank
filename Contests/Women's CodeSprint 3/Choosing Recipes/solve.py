import itertools
import copy

inf = float('inf')

if __name__ == '__main__':
    def count_ready_recipes(pantry):
        ready_recipes = 0

        for recipe in recipes:
            if all(j in pantry for j in range(p) if recipe[j] == 1):
                ready_recipes += 1

        return ready_recipes

    q = int(input())

    for _ in range(q):
        r, p, n, m = map(int, input().split())
        pantry = set(map(int, input().split()))
        cost = list(map(int, input().split()))

        recipes = [
            list(map(int, input().split())) for _ in range(r)
        ]

        ready_recipes = count_ready_recipes(pantry)
        if ready_recipes < n:
            # get all not present ingredients
            needed_ingredients = set()
            for i in range(r):
                for j in range(p):
                    if recipes[i][j] == 1 and j not in pantry:
                        needed_ingredients.add(j)

            # get all combinations of not present ingredients
            combinations = []
            for i in range(1, len(needed_ingredients) + 1):
                combinations += list(itertools.combinations(needed_ingredients, i))

            min_cost = inf
            for combination in combinations:
                tmp = copy.deepcopy(pantry)
                tmp = tmp.union(set(combination))
                ready_recipes = count_ready_recipes(tmp)

                if ready_recipes >= n:
                    tmp_cost = sum(cost[j] for j in combination)
                    min_cost = min(min_cost, tmp_cost)

            print(min_cost)
        else:
            print(0)
