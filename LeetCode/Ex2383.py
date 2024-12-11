def minNumberOfHours(initialEnergy, initialExperience, energy, experience):
    hours = 0

    if sum(energy) >= initialEnergy:
        hours += sum(energy) - initialEnergy + 1
        initialEnergy += hours

    for x in experience:
        if x >= initialExperience:
            hours += x-initialExperience + 1
            initialExperience = x + 1

        initialExperience += x

    return hours


initialEnergy = 5
initialExperience = 3
energy = [1, 4]
experience = [2, 5]
print(minNumberOfHours(initialEnergy, initialExperience, energy, experience))
