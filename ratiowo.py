import sys
import configparser
import re
import math
from collections import Counter


class Calculator:
    def __init__(self):
        # Maps names of ingredients to their Ingredient
        self.entries = {}

    def add(self, ingredient):
        self.entries[ingredient.name] = ingredient

    # Given the name of an ingredient and how much you want per second, say the number of machines needed.
    def calculate(self, wanted_name, wanted_rate):
        # Maps each ingredient name to an array: [machine count, ingredient].
        # This is not a tuple because tuples are immutable.
        results = {}

        def helper(ingredient, required_amount, required_time):
            # This writes the number of machines producing this ingredient that are required
            # to `results`.
            # If there's something already in there then it's added to it.
            # (For example if I already need 2 cobble/second and this ends up needing 3 cobble/second,
            # it adds up to 5 cobble/second)
            # Then it recursively calls this on its sub-ingredients.
            num_machines = (required_amount / required_time) / \
                (ingredient.units / ingredient.time)
            if ingredient.name in results:
                # we require this ingredient elsewhere
                results[ingredient.name][0] += num_machines
            else:
                # Brand spanking new
                results[ingredient.name] = [num_machines, ingredient]

            for sub_ingredient, sub_amount in ingredient.requires.items():
                helper(self.entries[sub_ingredient],
                       sub_amount * required_amount / ingredient.units, ingredient.time * required_time)

        root_ingredient = self.entries[wanted_name]
        # Calculare the required amount for the first one
        required_amount = wanted_rate * root_ingredient.time
        # and do recursion
        helper(root_ingredient, required_amount, root_ingredient.time)

        # Let's also calculate how many of each machine is needed
        machine_counts = Counter()
        for [machine_count, ingredient] in results.values():
            machine_counts[ingredient.machine] += math.ceil(machine_count)
        machine_counts = sorted([tup  # short for tuple
                                 for tup in machine_counts.items()], key=lambda a: a[1], reverse=True)

        # and send it out:
        print("Youwu will need:")
        for [machine_count, ingredient] in results.values():
            print(
                f"- {math.ceil(machine_count)}x {ingredient.machine} making {ingredient.name} ({machine_count:.2f} unrounded)")
        print("Machinewy needed:")
        for (machine, count) in machine_counts:
            print(f"- {count}x {machine}")

        # print a newline to make reading it easier
        print()

    def __call__(self, wanted_name, wanted_rate):
        self.calculate(wanted_name, wanted_rate)


class Ingredient:
    def __init__(self, name, units, time, machine='<unknown>', requires={}):
        # Name of this ingredient
        self.name = name
        # How many units (items or mB) this produces
        self.units = units
        # How often the production happens in seconds
        self.time = time
        # The machine this is made in
        self.machine = machine
        # Maps names of ingredients to the amount required
        # For example, if `self` is planks, this would be {'Log': 1}.
        # If `self` is stone pickaxe, this would be {'Cobblestone': 3, 'Stick': 2}.
        # If this is empty, it requires nothing (like an apiary or a pump)
        self.requires = requires


numberize_regex = re.compile(r"[\d\.]+")


def numberize(input):
    """Get a number out of a string like `3x` -> 3 or `150mb` -> 3"""
    return float(numberize_regex.match(input)[0])


ratiowo_chan = r"""
   ^---^
 / O   O \ -- I'm Ratiowo-chan! I cawucuwated {} ingwedients fow u~~
 \ >///< /    P-pwease wun `ratiowo(item, rate)` to calcuwate!
  -------
"""


if __name__ == '__main__':
    # Main!

    # Open up the given config file
    config = configparser.ConfigParser()
    config.optionxform = lambda x: x  # Turn off fixing the case on keys
    config.read(sys.argv[1])

    # Populate the calculator
    ratiowo = Calculator()
    for (name, ingredient) in config.items():
        if name == 'DEFAULT':
            continue

        units = numberize(ingredient['Units'])
        time = numberize(ingredient['Time'])
        machine = ingredient.get('Machine', '<unknown>')
        # Get the required sub-ingredients
        reqs = {name: numberize(count) for (name, count) in ingredient.items() if (name not in [
            'Units', 'Time', 'Machine'])}
        # and add it to the calculator
        ratiowo.add(Ingredient(name, units, time, machine, reqs))

    print(ratiowo_chan.format(len(ratiowo.entries)))
