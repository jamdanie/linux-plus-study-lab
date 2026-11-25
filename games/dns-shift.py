"""Classify four simulated DNS lookups. No network requests are made."""
import argparse
from pathlib import Path
import random

CASES = [
    [
        "rack-a",
        "IPv4 answer returned",
        "The A record supplies an IPv4 address. Test the intended application separately."
    ],
    [
        "rack-b",
        "Requested record type absent",
        "The name exists. This negative answer concerns AAAA, which carries an IPv6 address."
    ],
    [
        "rack-c",
        "Name reported nonexistent",
        "This resolver reports that the queried name does not exist. Compare the spelling and intended zone."
    ],
    [
        "rack-d",
        "No DNS reply observed",
        "A timeout gives no response code. Check resolver selection and reachability before drawing conclusions about the record."
    ]
]
CAPTURES = Path(__file__).resolve().parents[1] / "fixtures" / "dns-shift"


def play(seed):
    rng = random.Random(seed)
    rounds = list(CASES)
    rng.shuffle(rounds)
    score = 0
    for number, (host, answer, explanation) in enumerate(rounds, 1):
        print(f"\nTicket {number}/{len(rounds)}")
        print((CAPTURES / (host + ".txt")).read_text(encoding="utf-8").strip())
        choices = [entry[1] for entry in CASES]
        rng.shuffle(choices)
        for index, label in enumerate(choices, 1):
            print(f"{index}. {label}")
        while True:
            choice = input("Diagnosis (1–4, q to quit): ").strip().lower()
            if choice == "q":
                print(f"Completed {number - 1} tickets with {score} correct.")
                return
            if choice in {"1", "2", "3", "4"}:
                break
            print("Enter a listed number or q.")
        if choices[int(choice) - 1] == answer:
            score += 1
            print("Correct.")
        else:
            print(f"Answer: {answer}.")
        print(explanation)
    print(f"Final score: {score}/{len(rounds)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, help="Repeat a particular round order.")
    try:
        play(parser.parse_args().seed)
    except (EOFError, KeyboardInterrupt):
        print("\nShift ended.")
