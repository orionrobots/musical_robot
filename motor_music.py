import time
import board
import pwmio

A1_PWM = pwmio.PWMOut(board.GP17, frequency=440, variable_frequency=True)
B1_PWM = pwmio.PWMOut(board.GP18, frequency=440, variable_frequency=True)

# https://en.wikipedia.org/wiki/Piano_key_frequencies
notes = {
    'A4': 440,
    'B4': 494,
    'C4': 523,
    'D5': 587,
    'E5': 659,
    'F5': 698,
    'G5': 784,
    'A5': 880,
    'B5': 988,
    'C6': 1046,
}



tune = [['C4', 'E5'], ['D5', 'F5'], ['E5', 'G5']]
# a, b, duration, rest
tune = [
    ['E5', 'G5', 0.4, 0.2],
    ['F5', 'A5', 0.15, 0.15],
    ['E5', 'G5', 0.3, 0.3],
    ['D5', 'F5', 0.3, 0.3],
    ['C4', 'E5', 0.3, 0.3],
    ['D5', 'F5', 0.3, 0.3],
    ['E5', 'G5', 0.3, 0.3],
]

tone = 440
TONE_ON_DUTY = 2 ** 14
TONE_OFF_DUTY = 0


for a, b, duration, rest in tune:
    A1_PWM.frequency = notes[a]
    B1_PWM.frequency = notes[b]
    A1_PWM.duty_cycle = TONE_ON_DUTY
    B1_PWM.duty_cycle = TONE_ON_DUTY
    time.sleep(duration)
    A1_PWM.duty_cycle = TONE_OFF_DUTY
    B1_PWM.duty_cycle = TONE_OFF_DUTY
    time.sleep(rest)
