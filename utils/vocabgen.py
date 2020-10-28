"""
Original author: Chris Donahue
Source: https://github.com/chrisdonahue/LakhNES/blob/master/data/tx1_midi.py
"""


def quantize_wait(wait):
    wait = min(wait, 100000)

    if wait > 10000:
        wait = 1000 * int(round(float(wait) / 1000) + 1e-4)
    elif wait > 1000:
        wait = 100 * int(round(float(wait) / 100) + 1e-4)
    elif wait > 100:
        wait = 10 * int(round(float(wait) / 10) + 1e-4)

    return wait


def main():
    vocab = []

    # Add waits
    last_wait = None
    for i in xrange(1, 100001):
        wait = quantize_wait(i)
        if last_wait is None or wait != last_wait:
            vocab.append("WT_{}".format(wait))
            last_wait = wait

    # Add notes
    ins_to_range = {"P1": [33, 108], "P2": [33, 108], "TR": [21, 108], "NO": [1, 16]}
    for ins in ["P1", "P2", "TR", "NO"]:
        vocab.append("{}_NOTEOFF".format(ins))
        lo, hi = ins_to_range[ins]
        for n in range(lo, hi + 1):
            vocab.append("{}_NOTEON_{}".format(ins, n))

    with open("data/vocab.txt", "w") as f:
        f.write("\n".join(vocab))


if __name__ == "__main__":
    main()