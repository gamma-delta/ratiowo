# ratiowo

*notices ur idle machines* owo wuts this?

Ratiowo is a ratio calculator and recipe planner. I designed it for use in the FTB Interactions modpack, but it should work for anything where:

* You have something you would like to make
* The thing is made up of other things
* You know how fast everything can be made

# How to Use

To use Ratiowo, simply run `python -i ratiowo.py path/to/recipes.owo`. It will drop you into an interactive shell.

Query Ratiowo by running `ratiowo(item, rate)`.

For example:

```
> python -i ratiowo.py examples/example.owo

   ^---^
 / O   O \ -- I'm Ratiowo-chan! I cawucuwated 5 ingwedients fow u~~
 \ >///< /    P-pwease wun `ratiowo(item, rate)` to calcuwate!
  -------

# This is asking Ratiowo-chan: what do I need in order to get 1 stone pickaxe every 1 second?
>>> ratiowo('Stone Pickaxe', 1/1)
Youwu will need:
- 1x Crafter making Stone Pickaxe (1.00 unrounded)
- 3x Cobblestone Generator making Cobblestone (3.00 unrounded)
- 1x Crafter making Stick (0.50 unrounded)
- 2x Water-powered Saw making Plank (1.25 unrounded)
- 1x Tree Farm making Log (0.05 unrounded)
Machinewy needed:
- 3x Cobblestone Generator
- 2x Crafter
- 2x Water-powered Saw
- 1x Tree Farm

# What if I want two pickaxes per second?
>>> ratiowo('Stone Pickaxe', 2/1)
Youwu will need:
- 2x Crafter making Stone Pickaxe (2.00 unrounded)
- 6x Cobblestone Generator making Cobblestone (6.00 unrounded)
- 1x Crafter making Stick (1.00 unrounded)
- 3x Water-powered Saw making Plank (2.50 unrounded)
- 1x Tree Farm making Log (0.09 unrounded)
Machinewy needed:
- 6x Cobblestone Generator
- 3x Crafter
- 3x Water-powered Saw
- 1x Tree Farm

# What if I want a stack of pickaxes every minute (60 seconds)?
>>> ratiowo('Stone Pickaxe', 64/60)
Youwu will need:
- 2x Crafter making Stone Pickaxe (1.07 unrounded)
- 4x Cobblestone Generator making Cobblestone (3.20 unrounded)
- 1x Crafter making Stick (0.53 unrounded)
- 2x Water-powered Saw making Plank (1.33 unrounded)
- 1x Tree Farm making Log (0.05 unrounded)
Machinewy needed:
- 4x Cobblestone Generator
- 3x Crafter
- 2x Water-powered Saw
- 1x Tree Farm
```

# How to write your own `.owo` files

An `.owo` file has the same general syntax as a `.cfg` or `.ini` file. (Specifically, it uses the [`configparser` Python library.](https://docs.python.org/3/library/configparser.html))

I've included some example files that should help you get started.