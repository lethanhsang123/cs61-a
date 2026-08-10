import sys
import doctest

def twenty_twenty_six():
    """Come up with the most creative expression that evaluates to 2026
    using only numbers and the +, *, and - operators (or ** and % if you'd like).

    >>> twenty_twenty_six()
    2026
    """
    return 2026

if __name__ == "__main__":

    tests = {
        "twenty_twenty_six": twenty_twenty_six
    }

    if len(sys.argv) == 2:
        name = sys.argv[1]

        if name in tests:
            doctest.run_docstring_examples(
                tests[name],
                globals(),
                verbose=True
            )
        else:
            print(f"Unknown function: {name}")

    else:
        doctest.testmod(verbose=True)
