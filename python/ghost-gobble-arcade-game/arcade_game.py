"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    """
    can_eat = False

    if(power_pellet_active and touching_ghost):
        can_eat = True

    return can_eat

def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    
    can_score = False

    if(touching_power_pellet or touching_dot):
        can_score =True

    return can_score

def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    game_over = False

    if(not power_pellet_active and touching_ghost):
        game_over = True

    return game_over

def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """

    has_won = False

    if(has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)):
        has_won = True
            
    return has_won
