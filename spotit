"""
Code to implement the game of Spot it!
http://www.blueorangegames.com/spotit/
"""

import comp140_module2 as spotit

def equivalent(point1, point2, mod):
    """
    Determines if the two given points are equivalent in the projective
    geometric space in the finite field with the given modulus.

    Each input point, point1 and point2, must be valid within the
    finite field with the given modulus.

    inputs:
        - point1: a tuple of 3 integers representing the first point
        - point2: a tuple of 3 integers representing the second point
        - mod: an integer representing the modulus

    returns: a boolean indicating whether or not the points are equivalent
    """
    cross_prod = [((point1[1]*point2[2])-(point1[2]*point2[1]))%mod,\
                  ((point1[2]*point2[0])-(point1[0]*point2[2]))%mod,\
                  ((point1[0]*point2[1])-(point1[1]*point2[0]))%mod]
    return (cross_prod == [0,0,0])

    
def incident(point, line, mod):
    """
    Determines if a point lies on a line in the projective
    geometric space in the finite field with the given modulus.

    The inputs point and line must be valid within the finite field
    with the given modulus.

    inputs:
        - point: a tuple of 3 integers representing a point
        - line: a tuple of 3 integers representing a line
        - mod: an integer representing the modulus

    returns: a boolean indicating whether or not the point lies on the line
    """
    return (((line[0]*point[0])+(line[1]*point[1])+(line[2]*point[2])) % mod == 0)


def possible_points(mod):
    """
    Generate all possible points with the given modulus.
    
    inputs:
        - mod: an integer representing the modulus
    
    returns: a list of possible points, each is a tuple of 3 elements
    """
    possible = []
    for elem1 in range(mod):
        for elem2 in range(mod):
            for elem3 in range(mod):
                current = (elem1, elem2, elem3)
                possible.append(current)
    return possible


def generate_all_points(mod):
    """
    Generate all unique points in the projective geometric space in
    the finite field with the given modulus.

    inputs:
        - mod: an integer representing the modulus

    returns: a list of unique points, each is a tuple of 3 elements
    """
    
    points = []
    for current in possible_points(mod):
        if current != (0,0,0):
            if len(points) == 0:
                points.append(current)
            else:
                unique = True
                for point in points:
                    if equivalent(current,point,mod):
                        unique = False
                        break
                if unique:
                    points.append(current)
    return points

generate_all_points(3)


def create_cards(points, lines, mod):
    """
    Create a list of unique cards.

    Each point and line within the inputs, points and lines, must be
    valid within the finite field with the given modulus.

    inputs:
        - points: a list of unique points, each represented as a tuple of 3 integers
        - lines: a list of unique lines, each represented as a tuple of 3 integers
        - mod: an integer representing the modulus

    returns: a list of lists of integers, where each nested list represents a card.
    """
    cards = []
    for line in lines:
        card = []
        for point in points:
            if incident(point,line,mod):
                card.append(points.index(point))
        cards.append(card)
    return cards

def run():
    """
    Create the deck and play the game.
    """
    # Prime modulus
    # Set to 2 or 3 during development
    # Set to 7 for the actual game
    #modulus = 7

    # Generate all unique points for the given modulus
    #points = generate_all_points(modulus)

    # Lines are the same as points, so make a copy
    #lines = points[:]

    # Generate a deck of cards given the points and lines
    #deck = create_cards(points, lines, modulus)

    # Run GUI - uncomment the line below after you have implemented
    #           everything and you can play your game.  The GUI does
    #           not work if the modulus is larger than 7.

    #spotit.start(deck)

# Uncomment the following line to run your game (once you have
# implemented the run function.)

run()
