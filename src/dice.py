"""Make dice generator."""
import random


def main():
    print("start game")
    type_of_dice_flag = False
    number_of_error = 0
    while type_of_dice_flag is False:
        type_of_dice = int(input("dice choice 6, 12, 24 :\n"))
        if (type_of_dice == 6) or (type_of_dice == 12) or (type_of_dice == 24):
            type_of_dice_flag = True
        else:
            number_of_error = number_of_error + 1
            print(f"try again bro : number_of_error {number_of_error}")
            if number_of_error == 5:
                return 1
    dice_value = dice_roll(type_of_dice)
    print_value(dice_value)
    print("end game")


def dice_roll(type_of_dice: int):
    """ Roll the dice. """
    dice_value = random.randint(1, type_of_dice)
    return dice_value


def print_value(dice_value: int):
    """Printing the dice value."""
    print(f"dice_value: {dice_value}")


if __name__ == '__main__':
    main()