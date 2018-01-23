# GrowMaze
Experimentation in creating mazes with python.\
Also see: [FriesW/MutateMaze](https://github.com/FriesW/MutateMaze)\
Also see: [FriesW/ConnectMaze](https://github.com/FriesW/ConnectMaze)

## Use
Created in Python 2.7. To use, simply invoke Run.py. To make mazes in other pieces of software, import make_maze from Maze.py.

## A maze!
This looks okay in a desktop browser, but might not look right on mobile. Apparently mobile GitHub code blocks don't use a monospace font.
```
Maze Hash: ge3hymjtpq3xy2rtinmu2n2gi5ati
Dimensions: 16x13
Starting points: 7
███████████████████████████████████████████████████████████████████████████████████████████████████
███                                                         ███   ███         ███   ███   ███   ███
███   █████████   █████████   █████████   ███   ███████████████   ███   █████████   ███   ███   ███
███   ███         ███               ███   ███               ███                           ███   ███
███   █████████████████████   █████████   █████████   ███   █████████   ███████████████   ███   ███
███   ███                           ███         ███   ███   ███         ███                     ███
███████████████   █████████   ███████████████████████████████████████████████████   ███   ███   ███
███   ███               ███                     ███   ███                           ███   ███   ███
███   █████████   █████████   ███   ███   █████████   ███   ███   ███   ███   ███   ███   ███   ███
███   ███         ███         ███   ███   ███   ███   ███   ███   ███   ███   ███   ███   ███   ███
███   ███████████████████████████   █████████   ███   ███████████████   ███   ███   ███   █████████
███   ███         ███   ███                     ███   ███   ███         ███   ███   ███         ███
███   █████████   ███   ███████████████   █████████   ███   ███   █████████   ███   ███   ███   ███
███   ███   ███                           ███               ███   ███         ███   ███   ███   ███
███   ███   ███████████████   █████████   █████████   ███████████████   █████████   ███████████████
███         ███   ███   ███   ███                           ███   ███         ███   ███   ███   ███
███   ███   ███   ███   █████████   ███████████████   █████████   ███   ███   █████████   ███   ███
███   ███   ███         ███   ███   ███               ███   ███         ███   ███   ███         ███
███   █████████   █████████   █████████████████████   ███   ███   ███████████████   █████████   ███
███                                                                     ███         ███         ███
███   ███   ███   ███   █████████   ███   ███   ███   ███   █████████████████████   █████████   ███
███   ███   ███   ███         ███   ███   ███   ███   ███         ███               ███         ███
███   █████████   ███████████████████████████   ███   █████████   ███████████████   ███   █████████
███         ███               ███   ███         ███   ███   ███   ███               ███         ███
███   ███████████████████████████   █████████   █████████   ███   ███████████████   ███   █████████
███                                 ███               ███                                       ███
███████████████████████████████████████████████████████████████████████████████████████████████████
```

## How it works
A grid is created, which is essentially a 2D doubly-linked list. Seed starting locations are picked at random. These locations are randomly picked for growth. Growth is the connection of two nodes. Each collection of connected nodes is randomly selected and randomly grown until the entire grid is consumed. If a collection of nodes is grown/connected into another collection of nodes, the two are combined.

Part of the reason for this code was to experiment with how the number of starting locations effects the appearance of the maze. That is why the number of seed locations can be changed as a parameter. Much simpler code would have assumed that there was only one set of connected nodes, which all grew from one seed.
