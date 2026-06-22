from incomplete_main import tournament_rankings

TestCase = tuple[list[str], list[str]]

run_case: list[TestCase] = [
    (
        ["Gandalf", "bilbo baggins", "frodo baggins", "Sauron"],
        [
            "Rank: 1, Name: Gandalf",
            "Rank: 2, Name: bilbo baggins",
            "Rank: 3, Name: frodo baggins",
            "Rank: 4, Name: Sauron",
        ],
    ),
    (["Frodo"], ["Rank: 1, Name: Frodo"]),
]

submit_cases: list[TestCase] = run_case + [
    ([], []),
    (
        ["Fili", "Kili", "Thorin"],
        ["Rank: 1, Name: Fili", "Rank: 2, Name: Kili", "Rank: 3, Name: Thorin"],
    ),
]


def test(names: list[str], expected: list[str]) -> bool:
    print("---------------------------------")
    print(f"Input: {names}")
    print("")
    result = tournament_rankings(names)
    print(f"Expected: {expected}")
    print(f"Actual: {result}")
    if result == expected:
        return True
    return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_case

main()
