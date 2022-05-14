digits = {10: "A",
          11: "B",
          12: "C",
          13: "D",
          14: "E",
          15: "F",
          16: "G",
          17: "H",
          18: "I",
          19: "J",
          20: "K",
          21: "L",
          22: "M",
          23: "N",
          24: "O",
          25: "P",
          26: "Q",
          27: "R",
          28: "S",
          29: "T",
          30: "U",
          31: "V",
          32: "W",
          33: "X",
          34: "Y",
          35: "Z"
          }

letters = {"A": 10,
           "B": 11,
           "C": 12,
           "D": 13,
           "E": 14,
           "F": 15,
           "G": 16,
           "H": 17,
           "I": 18,
           "J": 19,
           "K": 20,
           "L": 21,
           "M": 22,
           "N": 23,
           "O": 24,
           "P": 25,
           "Q": 26,
           "R": 27,
           "S": 28,
           "T": 29,
           "U": 30,
           "V": 31,
           "W": 32,
           "X": 33,
           "Y": 34,
           "Z": 35}


def from10ToBase(number: int, base: int):
    """Перевод десятичного числа в выбранную пользователем систему счисления"""
    new_number = ""
    while number > 0:
        add_digit = number % base
        if add_digit > 9:
            new_number += digits[add_digit]
        else:
            new_number += str(number % base)
        number //= base
    return new_number[::-1]


def fromBaseTo10(number: str, base: int):
    """Перевод числа из данной системы счисления в десятичную"""
    new_number = 0
    for i in range(len(number)):
        cut_digit = number[-1]
        if cut_digit not in "0123456789":
            new_number += int(letters[cut_digit] * (base ** i))
        else:
            new_number += int(cut_digit) * (base ** i)
        number = number[:-1]
    return new_number

def fromBaseToBase(number: str, fromBase: int, toBase: int):
    if fromBase > 36 or toBase > 36:
        print("Too big base")
        return None
    dec_number = fromBaseTo10(number, fromBase)
    new_number = from10ToBase(dec_number, toBase)
    return new_number

if __name__ == "__main__":
    pass
