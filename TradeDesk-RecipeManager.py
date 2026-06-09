import time
from collections import defaultdict

class RecipeManager(object):
    def __init__(self):
        self.recipes = {}                           # name -> dict of recipe data
        self.ingredient_index = defaultdict(set)    # ingredient -> set of recipe names
        self.users = set()                          # set of user_ids

    def create_user(self, user_id):
        self.users.add(user_id)

    def add_recipe(self, user_id, name, ingredients, steps):
        if user_id not in self.users:
            return False # User doesn't exist
        if name in self.recipes:
            return False # Recipe already exists

        # 1. Save to main hash map
        self.recipes[name] = {
            "name": name,
            "ingredients": set(ingredients), # Store as set for fast diffing during updates
            "steps": steps,
            "creator": user_id,
            "last_modifier": user_id,
            "created_time": time.time(),
            "updated_time": time.time(),
            "ingredient_count": len(ingredients)
        }

        # 2. Update inverted index
        for ing in ingredients:
            self.ingredient_index[ing].add(name)
            
        return True

    def get_recipe(self, name):
        return self.recipes.get(name, None)

    def update_recipe(self, user_id, name, new_ingredients=None, new_steps=None):
        recipe = self.recipes.get(name)
        if not recipe:
            return False # Not found
        if recipe["creator"] != user_id:
            return False # Unauthorized

        if new_ingredients is not None:
            old_ingredients = recipe["ingredients"]
            new_ingredients_set = set(new_ingredients)
            
            # Remove ingredients that are no longer in the new version
            for ing in (old_ingredients - new_ingredients_set):
                self.ingredient_index[ing].remove(name)
                
            # Add new ingredients
            for ing in (new_ingredients_set - old_ingredients):
                self.ingredient_index[ing].add(name)
                
            recipe["ingredients"] = new_ingredients_set
            recipe["ingredient_count"] = len(new_ingredients_set)

        if new_steps is not None:
            recipe["steps"] = new_steps

        recipe["last_modifier"] = user_id
        recipe["updated_time"] = time.time()
        return True

    def delete_recipe(self, user_id, name):
        recipe = self.recipes.get(name)
        if not recipe:
            return False # Not found
        if recipe["creator"] != user_id:
            return False # Unauthorized

        # 1. Remove from inverted index
        for ing in recipe["ingredients"]:
            self.ingredient_index[ing].remove(name)

        # 2. Remove from main hash map
        del self.recipes[name]
        return True

    def search_by_ingredient(self, ingredient):
        # Returns a list of recipe names. O(1) lookup.
        return list(self.ingredient_index.get(ingredient, []))

    def list_recipes(self, sort_by="name", order="asc"):
        # In Python 2.7, .values() returns a list directly
        recipes_list = self.recipes.values()
        
        # Sort on the fly. Timsort is O(N log N)
        reverse_order = (order == "desc")
        recipes_list.sort(key=lambda r: r.get(sort_by), reverse=reverse_order)
        
        return recipes_list
