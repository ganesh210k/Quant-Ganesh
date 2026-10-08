# Solutions for practice.py - only peek after a real attempt!
# Running this file runs the same checker against these answers.

def ohms_law_current(v, r):
    return v / r


def power(v, i):
    return v * i


def format_reading(value, unit):
    return f"{value:.2f} {unit}"


def regulator_voltage(part_number):
    return int(part_number[-2:])


def battery_status(volts):
    if volts >= 4.1:
        return "FULL"
    elif volts >= 3.5:
        return "OK"
    else:
        return "LOW"


def series_resistance(resistors):
    total = 0
    for r in resistors:
        total += r
    return total


def count_over_limit(readings, limit):
    count = 0
    for x in readings:
        if x > limit:
            count += 1
    return count


def to_milliamps(currents_a):
    return [i * 1000 for i in currents_a]


def average(values):
    return sum(values) / len(values)


COLOURS = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
           "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}


def colour_to_digit(colour):
    return COLOURS[colour]


def parallel_resistance(r1, r2):
    return r1 * r2 / (r1 + r2)


def voltage_divider(vin, r1, r2=10_000):
    return vin * r2 / (r1 + r2)


def safe_float(text):
    try:
        return float(text)
    except ValueError:
        return None


if __name__ == "__main__":
    import practice
    # Swap the solutions into the practice module, then run its checker.
    for name, obj in list(globals().items()):
        if callable(obj) and not name.startswith("_"):
            setattr(practice, name, obj)
    practice._check()
