class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredient_to_recipe = defaultdict(list)
        in_degree = {}

        for recipe, needed in zip(recipes, ingredients):
            for ingredient in needed:
                ingredient_to_recipe[ingredient].append(recipe)
            in_degree[recipe] = len(needed)

        can_create = []
        while supplies:
            ingredient = supplies.pop()
            for recipe in ingredient_to_recipe[ingredient]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    can_create.append(recipe)
                    supplies.append(recipe)
        return can_create
