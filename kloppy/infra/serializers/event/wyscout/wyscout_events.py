from typing import List


class DUEL:
    EVENT = 1

    GROUND_ATTACKING = 11
    GROUND_DEFENDING = 12
    GROUND_LOOSE_BALL = 13


class FOUL:
    EVENT = 2

    FOUL = 20
    HAND = 21
    LATE_CARD = 22
    OUT_OF_GAME = 23
    PROTEST = 24
    SIMULATION = 25
    TIME_LOST = 26
    VIOLENT = 27


class FREE_KICK:
    EVENT = 3

    CORNER = 30
    FREE_KICK = 31
    FREE_KICK_CROSS = 32
    FREE_KICK_SHOT = 33
    GOAL_KICK = 34
    PENALTY = 35
    THROW_IN = 36

    PASS_TYPES = [CORNER, FREE_KICK, FREE_KICK_CROSS, GOAL_KICK, THROW_IN]
    SHOT_TYPES = [FREE_KICK_SHOT, PENALTY]


class GOALKEEPER:
    EVENT = 4

    LEAVING_LINE = 40


class INTERRUPTION:
    EVENT = 5

    BALL_OUT = 50
    WHISTLE = 51


class OFFSIDE:
    EVENT = 6

    OFFSIDE = 6


class OTHERS_ON_BALL:
    EVENT = 7

    ACCELERATION = 70
    CLEARANCE = 71
    TOUCH = 72


class PASS:
    EVENT = 8

    CROSS = 80
    HAND = 81
    HEAD = 82
    HIGH = 83
    LAUNCH = 84
    SIMPLE = 85
    SMART = 86


class SAVE:
    EVENT = 9

    REFLEXES = 90
    SAVE_ATTEMPT = 91


class SHOT:
    EVENT = 10

    SHOT = 100