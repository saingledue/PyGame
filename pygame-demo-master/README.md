# pygame-demo

# Getting familiar pygame and the graphing template

In this lab, you’ll make some fixes to a "video game" that no one thinks is very fun! This code and the pygame library is used extensively for the larger project, so it will be important (and make your life easier) to learn about it. Documentation for pygame is here: <https://https://www.pygame.org/docs/>

Work with your partner and try to practice pair programming. Push your changes to GitHub so we can easily review them.

# Instructions:

1.  Clone this project to your local computer.
2.  Take some time to browse the files associated with this project. In particular, look at the data.py and config.py files to see what they store and how.
3.  When you run the "game" for the first time (main.py), you can see why no one wants to play it! The players move too slowly and you can't see the whole playing surface!
4.  Your first task is to fix the game so it is at least viewable and the players move faster:
5.  Make the screen big enough to show the whole playing field
6.  Make the players move faster (this can be done in many ways, try different settings)
7.  The nodes and their text are not easy to see (they're all black, possibly too big), so try different ways to fix that and make sure the nodes are drawn with             different colors so you can see their borders and unique IDs
8.  Your second task is to add another test graph and have players move along an appropriate test path:
9.  Add a graph with at least 10 nodes to the graph_data, along with edges listed in the adjacency lists so it is possible to go from a start to exit node
10.  Add an appropriate new test path for the new graph
11.  Add another player to the player_data so a second player spawns after the first player exits the game (and find an appropriate image in the images folder)
12.  Add some appropriate functionality to the exit button! <https://www.pygame.org/docs/ref/pygame.html>
