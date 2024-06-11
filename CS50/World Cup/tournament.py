# Simulate a sports tournament

import csv
import itertools
import sys
import time
import random

# Number of simluations to run
N = 1000

def generate_matchups(teams):
    # Generate matchups by pairing each team with the next one in the list
    matchups = []
    for i in range(0, len(teams), 2):
        matchups.append((teams[i], teams[i+1]))
    return matchups

def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # Read teams into memory from file
    filename = sys.argv[1]
    with open(filename, "r") as file:
        # Skip the header line
        next(file)
        # Read the content line by line
        for line in file:
            # Split each line by comma and strip whitespace
            team_name, rating = line.strip().split(',')
            # Append the team to the teams array
            teams.append((team_name, int(rating)))

    # Print the teams array for demonstration
    print("Teams:")
    print(teams)
    time.sleep(2)  # Pause for 2 seconds for demonstration of team fetch from file
    print("\n\n")

    # Generate tournament bracket
    # Generate matchups
    matchups = generate_matchups(teams)

    # Print the matchups for demonstration
    print("Matchups:")
    for i, match in enumerate(matchups):
        print(f"Pair {i+1}: {match[0][0]} ({match[0][1]}) vs {match[1][0]} ({match[1][1]})")

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    
    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")  # Fix N or replace with appropriate value


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO


if __name__ == "__main__":
    main()