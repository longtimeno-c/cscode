# (a)(i) Declare the class EventItem
class EventItem:
    def __init__(self, EventName, Type, Difficulty):
        # Private attributes with suitable data types
        self._EventName = str(EventName)  # String: Name of the event
        self._Type = str(Type)            # String: Type of event (e.g., Jump, Swim)
        self._Difficulty = int(Difficulty) # Integer: Difficulty level of the event

    # (a)(ii) Getter methods
    def GetName(self):
        return self._EventName  # Returns event name

    def GetDifficulty(self):
        return self._Difficulty  # Returns event difficulty

    def GetEventType(self):
        return self._Type  # Returns event type


# (b)(i) Declare a 1D array ‘Group’ with at least 5 elements of type EventItem
# The array will store EventItem objects
Group = []  # List to store EventItem objects

# (b)(ii) Instantiate and store the five events in the main program
# Example events: (EventName, Type, Difficulty)
Group.append(EventItem("High Jump", "Jump", 5))
Group.append(EventItem("Freestyle Swim", "Swim", 7))
Group.append(EventItem("Sprint", "Run", 6))
Group.append(EventItem("Off-road Driving", "Drive", 8))
Group.append(EventItem("Diving", "Swim", 9))


# (c)(i) Define the Character class
class Character:
    def __init__(self, CharacterName, Jump, Swim, Run, Drive):
        # Private attributes with appropriate names
        self._CharacterName = str(CharacterName)  # String: Character name
        self._Jump = int(Jump)    # Integer: Skill level in Jump
        self._Swim = int(Swim)    # Integer: Skill level in Swim
        self._Run = int(Run)      # Integer: Skill level in Run
        self._Drive = int(Drive)  # Integer: Skill level in Drive

    # (c)(ii) GetName method to return the character's name
    def GetName(self):
        return self._CharacterName  # Returns character name

    # (c)(iii) CalculateScore method
    def CalculateScore(self, eventType, difficulty):
        # Determine the skill level based on event type
        if eventType == "Jump":
            skill_level = self._Jump
        elif eventType == "Swim":
            skill_level = self._Swim
        elif eventType == "Run":
            skill_level = self._Run
        elif eventType == "Drive":
            skill_level = self._Drive
        else:
            return 0  # Return 0 if event type is unknown

        # Calculate success chance as a percentage
        if difficulty > 0:  # Avoid division by zero
            chance = (skill_level / difficulty) * 100
        else:
            chance = 0  # If difficulty is 0, assume no chance of success

        return round(chance, 2)  # Return percentage rounded to 2 decimal places


# Example Usage:
# Creating a character
char1 = Character("Alex", 8, 6, 7, 9)

# Testing CalculateScore method
event = Group[0]  # High Jump event
print(f"{char1.GetName()} has a {char1.CalculateScore(event.GetEventType(), event.GetDifficulty())}% chance of completing {event.GetName()}.")