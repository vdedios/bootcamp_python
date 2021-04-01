#!/usr/bin/env python3

import pprint

cookbook = {
    'sandwich' : {
        'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal' : 'lunch',
        'prep_time' : '10 minutes'
    },
    'cake' : {
        'ingredients' : ['flour', 'sugar', 'eggs'],
        'meal' : 'dessert',
        'prep_time' : '60 minutes'
    },
    'salad' : {
        'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal' : 'lunch',
        'prep_time' : '15 minutes'
    }
}

def output_recipe(name):
    recipe = cookbook[name]
    print(f'Recipe for {name}:')
    print(f'Ingredients list: [', end = '')
    for ingredient in recipe['ingredients'][:-1]:
        print(f"'{ingredient}', ", end = '')
    print(f"'{recipe['ingredients'][-1]}']")
    print(f"To be eaten for {recipe['meal']}.")
    print(f"Takes {recipe['prep_time']} of cooking.")
    print('')

def print_recipe():
    name = input('Please, enter recipe name to read: ')
    if (name in cookbook.keys()) == False:
        print(f'{name} does not exists in cookbook')
    else:
        output_recipe(name)

def print_recipes():
    for recipe in cookbook:
        output_recipe(recipe)

def delete_recipe():
    name = input('Please, enter recipe name to delete: ')
    if (name in cookbook.keys()) == False:
        print(f'{name} does not exists in cookbook')
    else:
        del cookbook[name]
        print(f'{name} successfully deleted!')

def add_recipe():
    name = input('Recipe name: ')
    ingredients = input('Ingredients separated by commas: ').split(',')
    for i in range(len(ingredients)):
        ingredients[i] = ingredients[i].strip()
    meal = input('Type of meal: ')
    prep_time = input('Preparation time: ')
    cookbook[name] = {
        'ingredients' : ingredients,
        'meal' : meal,
        'prep_time' : prep_time
    }

def main():
    while True:
        print('\n')
        print('Please select an option by typing the corresponding number:')
        print('1: Add a recipe')
        print('2: Delete a recipe')
        print('3: Print a recipe')
        print('4: Print the cookbook')
        print('5: Quit\n')
        option = input()
        if option == '1': add_recipe()
        elif option == '2': delete_recipe()
        elif option == '3': print_recipe()
        elif option == '4': print_recipes()
        elif option == '5': break
        else: print('This option does not exist, please type the corresponding number.\nTo exit, enter 5.')

if __name__ == "__main__":
    main()