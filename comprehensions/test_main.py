from incomplete_main import comprehension

TestCase = tuple[int, list[int]]

run_case: list[TestCase] = [(5, [0, 1, 2, 3, 4, 5]), (1, [0, 1])]

submit_cases: list[TestCase] = run_case + [
    (0, [0]),
    (3, [0, 1, 2, 3]),
    (10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
]


def test(n: int, expected: list[int]) -> bool:
    print("---------------------------------")
    print(f"Input: {n}")
    print("")
    result = comprehension(n)
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
