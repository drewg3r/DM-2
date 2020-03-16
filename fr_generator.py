"""
Generates random possible connection between the components of two given sets
ASB, if A is the father of B
"""
import random
import core


def generate(A, B, s_possibility, r_possibility):
    A = list(A)
    B = list(B)
    S = set()
    R = set()
    used_children = []
    fathers_wd = set()
    used_boys = set()
    used_fathers = set()
    for a in A:
        for b in B:
            if a in core.men_names:
                if b not in used_children:
                    if random.randint(1, s_possibility) == 1:
                        S.add((a, b))
                        used_children.append(b)
                        if b in core.women_names:
                            fathers_wd.add(a)

    for f in fathers_wd:
        for b in B:
            if b in core.men_names:
                if (f, b) not in S:
                    if b not in used_boys:
                        if f not in used_fathers:
                            if random.randint(1, r_possibility) == 1:
                                R.add((f, b))
                                used_fathers.add(f)
                                used_boys.add(b)

    return S, R
