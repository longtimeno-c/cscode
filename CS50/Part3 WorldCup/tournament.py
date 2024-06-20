import sys
import time
import random

# Number of simulations to run
N = 1000

def generate_matchups(teams):
    # Generate matchups by pairing each team with the next one in the list
    matchups = []
    for i in range(0, len(teams), 2):
        matchups.append((teams[i], teams[i+1]))
    return matchups

def simulate_tournament(matchups):
    # Simulate a single tournament
    winners = []
    for match in matchups:
        team1, rating1 = match[0]
        team2, rating2 = match[1]
        
        # Calculate probability of winning based on ratings
        total_rating = rating1 + rating2
        prob_team1 = rating1 / total_rating
        prob_team2 = rating2 / total_rating
        
        # Simulate the match
        rand_num = random.random()
        if rand_num < prob_team1:
            winners.append(team1)
        else:
            winners.append(team2)
            
    return winners

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

    # Print the teams array for demo
    print("Teams Array:")
    print(teams)
    time.sleep(2)  # Pause for 2 seconds for demo of team fetch from file
    print("\n\n")

    # Generate tournament bracket
    # Generate matchups
    matchups = generate_matchups(teams)

    # Print the matchups for demo
    print("Matchups:")
    for i, match in enumerate(matchups):
        print(f"Pair {i+1}: {match[0][0]} ({match[0][1]}) vs {match[1][0]} ({match[1][1]})")
    
    print()
    time.sleep(2)
    print("Probability of Winning Tournament:")
    time.sleep(1)
    counts = {}
    # Simulate N tournaments and keep track of win counts
    for _ in range(N):
        # Simulate a tournament
        winners = simulate_tournament(matchups)
        # Count the wins for each team
        for team in winners:
            team_name, _ = team
            counts[team_name] = counts.get(team_name, 0) + 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")

if __name__ == "__main__":
    main()
