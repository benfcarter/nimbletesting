import random

from diceroller import DiceRoller

class NimbleDiceRoller(DiceRoller):
    def roll(self, dice_str, advantage=0, print_results=False):
        try:
            # Split the input string into number of dice and number of faces
            num_dice, num_faces = map(int, dice_str.split('d'))

            if print_results:
                print(f'Rolling {dice_str}...')
            
            num_advantage_stacks = abs(advantage)
            num_dice += num_advantage_stacks

            results = [random.randint(1, num_faces) for _ in range(num_dice)]

            if print_results:
                print(f'Original roll: {results}')
                
            for _ in range(num_advantage_stacks):
                if advantage > 0:
                    results.remove(min(results))
                else:
                    results.remove(max(results))

            if print_results:
                print(f'After advantage: {results}')

            is_crit = results[0] == num_faces
            while is_crit:
                results.append(random.randint(1, num_faces))
                is_crit = results[-1] == num_faces
    
            if print_results:
                print(f'After exploding: {results}')

            return results
        
        except ValueError:
            # Handle the case where the input values are not valid
            return "Invalid input values. Please use integers for num_dice and num_faces."

    def roll_as_modifier(self, dice_str, print_results=False):
        try:
            # Split the input string into number of dice and number of faces
            num_dice, num_faces = map(int, dice_str.split('d'))

            if print_results:
                print(f'Rolling {dice_str} as modifier...')

            results = [random.randint(1, num_faces) for _ in range(num_dice)]

            if print_results:
                print(f'Rolled: {results}')

            return results
        
        except ValueError:
            # Handle the case where the input values are not valid
            return "Invalid input values. Please use integers for num_dice and num_faces."
