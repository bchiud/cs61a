"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
MAX_ROLLS = 10

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    rolled_values = [dice() for x in range(num_rolls)]
    if 1 in rolled_values:
        return 1
    return sum(rolled_values)
    # END PROBLEM 1


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    cur_num = score ** 3
    cur_sum = 0
    m = -1 if len(str(cur_num)) % 2 == 0 else 1
    while cur_num > 0:
        cur_sum = cur_sum + m * ( cur_num % 10 )
        cur_num = cur_num // 10
        m = m * -1
    return 1 + abs(cur_sum)
    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= MAX_ROLLS, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if(num_rolls == 0):
        return free_bacon(opponent_score)
    return roll_dice(num_rolls, dice = dice)
    # END PROBLEM 3


def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    swap_num = 3 ** ( player_score + opponent_score )
    return swap_num // ( 10 ** ( len(str(swap_num)) - 1 ) ) == swap_num % 10
    # END PROBLEM 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence, feral_hogs=True):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    feral_hogs: A boolean indicating whether the feral hogs rule should be active.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    announcer = say
    previous_points0, previous_points1 = [0], [0]
    def ferral_bonus(cur_roll, last_score):
        return 3 if abs(last_score -  cur_roll) == 2 else 0
    while max(score0, score1) < goal:
        if who == 0:
            num_rolls = strategy0(score0, score1)
            if feral_hogs and abs(previous_points0[-1] - num_rolls) == 2:
                score0 += 3
            previous_points0.append(take_turn(num_rolls, score1, dice))
            score0 += previous_points0[-1]
        elif who == 1:
            num_rolls = strategy1(score1, score0)
            if feral_hogs and abs(previous_points1[-1] - num_rolls) == 2:
                score1 += 3
            previous_points1.append(take_turn(num_rolls, score0, dice))
            score1 += previous_points1[-1]
        if is_swap(score0, score1):
            score0, score1 = score1, score0
        who = abs(who - 1)
        announcer = announcer(score0, score1)
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    # END PROBLEM 6
    return score0, score1


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores

def announce_lead_changes(prev_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != prev_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say

def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 6)
    Player 0 now has 10 and Player 1 now has 6
    >>> h3 = h2(6, 17)
    Player 0 now has 6 and Player 1 now has 17
    Player 1 takes the lead by 11
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def announce_highest(who, prev_high=0, prev_score=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 11)
    11 point(s)! That's the biggest gain yet for Player 1
    >>> f3 = f2(20, 11)
    >>> f4 = f3(13, 20)
    >>> f5 = f4(20, 35)
    15 point(s)! That's the biggest gain yet for Player 1
    >>> f6 = f5(20, 47) # Player 1 gets 12 points; not enough for a new high
    >>> f7 = f6(21, 47)
    >>> f8 = f7(21, 77)
    30 point(s)! That's the biggest gain yet for Player 1
    >>> f9 = f8(77, 22) # Swap!
    >>> f10 = f9(33, 77) # Swap!
    55 point(s)! That's the biggest gain yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    def say(score0, score1):
        who_scores = {
            0 : score0,
            1 : score1,
        }
        cur_score = who_scores[who]
        cur_increment = cur_score - prev_score
        if cur_increment > prev_high:
            print('{pts} point(s)! That\'s the biggest gain yet for Player {plyr}'.format(pts=cur_increment, plyr=who))
            return announce_highest(who, prev_high = cur_increment, prev_score = cur_score)
        else:
            return announce_highest(who, prev_high = prev_high, prev_score = cur_score)
    return say
    # END PROBLEM 7


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(g, num_samples=1000):
    """Return a function that returns the average value of G when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def get_avg(*args):
        rolls = [g(*args) for x in range(num_samples)]
        avg = sum(rolls) / len(rolls)
        return avg
    return get_avg
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    cur_max_scoring_rolls, cur_max_avg = 0, 0
    for cur_rolls in range(1, MAX_ROLLS + 1):
        avg_func = make_averaged(roll_dice, num_samples=num_samples)
        cur_avg = avg_func(cur_rolls, dice)
        if cur_avg > cur_max_avg:
            cur_max_scoring_rolls, cur_max_avg = cur_rolls, cur_avg
    return cur_max_scoring_rolls
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"



def bacon_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least MARGIN points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    if free_bacon(opponent_score) >= margin:
        return 0
    return num_rolls
    # END PROBLEM 10


def swap_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points and does not trigger a
    non-beneficial swap. Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11

    free_bacon_points = free_bacon(opponent_score)
    new_score = score + free_bacon_points

    if is_swap(new_score, opponent_score) and new_score < opponent_score:
        return 0
    elif free_bacon_points >= margin and not (is_swap(new_score, opponent_score) and new_score > opponent_score):
        return 0
    return num_rolls
    # END PROBLEM 11

# final_strategy(10, 0)
def final_strategy(score, opponent_score, dice=six_sided, goal=GOAL_SCORE, num_samples=1000):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***

    * swap_strategy is a good default strategy to start with.
    * There's no point in scoring more than 100. Check whether you can win by rolling 0, 1 or 2 dice. If you are in the lead, you might take fewer risks.
    * Try to force a beneficial swap rolling more than 0 dice.
    * Choose the num_rolls and margin arguments carefully.
    """
    # BEGIN PROBLEM 12

    # Expected points from rolling dice(s)
    expected_points = {rolls: None for rolls in range(1, MAX_ROLLS + 1)}
    avg_outcome_func = make_averaged(roll_dice, num_samples = num_samples)
    for cur_rolls in expected_points:
        expected_points[cur_rolls] = avg_outcome_func(cur_rolls, dice)

    # Expected points from free bacon
    expected_free_bacon_points = free_bacon(opponent_score)
    expected_points[0] = score + expected_free_bacon_points

    # Update expected points if new score will result in swap
    for cur_rolls in expected_points:
        if is_swap(expected_points[cur_rolls], opponent_score):
            expected_points[cur_rolls] = opponent_score - expected_points[cur_rolls]

    # Find roll which will result in highest score while minimizing excess above goal
    cur_recommended_rolls = 0
    cur_recommended_expected_score = -1000000 # 150
    cur_recommended_excess = 0 # 50
    for cur_rolls in expected_points:
        cur_expected_points = expected_points[cur_rolls]
        cur_expected_score = score + cur_expected_points # 125
        cur_expected_excess = cur_expected_points - goal # 25

        # print('DEBUG:', 'cur_recommended_expected_score', cur_recommended_expected_score, 'cur_expected_score:', cur_expected_score)
        # print('DEBUG:', 'cur_recommended_excess', cur_recommended_excess, 'cur_expected_excess:', cur_expected_excess)

        def update(rolls=cur_rolls, expected_score=cur_expected_score, excess=cur_expected_excess):
            # print('DEBUG:', 'Update is called')
            return rolls, expected_score, excess

        if cur_expected_score >= goal and cur_expected_excess < cur_recommended_excess:
            cur_recommended_rolls, cur_recommended_expected_score, cur_recommended_excess = update()
        elif cur_expected_score >= goal and cur_expected_excess >= cur_recommended_excess:
            continue
        elif cur_expected_score > cur_recommended_expected_score:
            cur_recommended_rolls, cur_recommended_expected_score, cur_recommended_excess = update()

    # print('DEBUG:', 'Recommended Rolls:', int(cur_recommended_rolls), 'Expected New Scores:', int(cur_recommended_expected_score), opponent_score)
    return int(cur_recommended_rolls)






    def best_num_dice_to_roll(score, opponent_score):
        """ Returns the optimal number of dice to roll given score and opponent_score
        assuming it is the beginning of your turn.
        """
        score = score
        opponent_score = opponent_score
        best_probability, best_n = 0, 1
        #Iterate through each number of dice that can be rolled
        for n in range(0, MAX_DICE + 1):
            probability = probability_of_winning_by_rolling_n(score, opponent_score, n)
            if probability > best_probability:
                best_probability, best_n = probability, n
        return best_n


    def probability_of_winning_by_with_n_rolls(score, opponent_score, n):
        """ Returns probability that you will win if you roll n dice assuming it is
        your turn now.
        """
        sides = 6
        #Hog wild
        if hog_wild(score, opponent_score):
            sides = 4
        probability_of_winning = 0
        if n == 0:
            #Free Bacon
            turn_score = free_bacon_score(opponent_score)
            probability_of_winning = probability_of_winning_with_given_scores(
                    score + turn_score, opponent_score)
        else:
            #Iterate over each possible outcome for rolling n dice
            for possible_score in range(1, (sides * n) + 1):
                probability_of_winning += probability_of_scoring(possible_score, n,
                        sides) * probability_of_winning_with_given_scores(
                        score + possible_score, opponent_score)
        return probability_of_winning

    def number_of_ways_to_score(k, n, s):
        """ Returns the number of ways that k can be scored by rolling n
        s sided dice without pigging out.
        
        k: goal score
        n: number of dice to use
        s: number of sides on dice
        
        >>> number_of_ways_to_score(4, 1, 6)
        1
        >>> number_of_ways_to_score(12, 2, 6)
        1
        >>> number_of_ways_to_score(11, 2, 6)
        2
        >>> number_of_ways_to_score(7, 3, 6)
        3
        >>> number_of_ways_to_score(8, 3, 4)
        6
        """
        if k < 0:
            return 0
        if k == 0 and n == 0:
            return 1
        if n == 0:
            return 0
        total = 0
        for i in range(2, s + 1):
            total += number_of_ways_to_score(k - i, n - 1, s)
        return total
        
    def probability_of_scoring(k, n, s):
        """ Returns the chance that at least k will be scored by rolling n s sided
        dice without pigging out.
        
        k: goal score
        n: number of dice to use
        s: number of sides on dice
        
        >>> almost_equal = lambda x, y: abs(x - y) < 1e-10
        >>> almost_equal(probability_of_scoring(4, 1, 6), 1/6)
        True
        >>> almost_equal(probability_of_scoring(7, 3, 6), 3/216)
        True
        >>> almost_equal(probability_of_scoring(1, 2, 6), 11/36)
        True
        >>> almost_equal(probability_of_scoring(2, 3, 6), 0)
        True
        >>> almost_equal(probability_of_scoring(11, 10, 6), 0)
        True
        """
        if k == 1:
            return Decimal(1) - Decimal((pow(s - 1, n) / pow(s, n)))
        return Decimal(number_of_ways_to_score(k, n, s)) / Decimal(pow(s, n))

    def probability_of_winning_with_given_scores(score, opponent_score):
        if is_swap(score, opponent_score):
            score, opponent_score = opponent_score, score
        if score >= GOAL_SCORE:
            return 1
        elif opponent_score >= GOAL_SCORE:
            return 0
        opponent_num_rolls = best_num_dice_to_roll(opponent_score, score)
        probability_of_opponent_winning = probability_of_winning_by_rolling_n(opponent_score, score, opponent_num_rolls)
        return 1 - probability_of_opponent_winning

    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()