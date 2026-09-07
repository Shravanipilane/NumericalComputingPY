from Interpolator import LagrangeInterpolation


def read_questions(filename):
    """Very simple parser for our Input.txt format."""
    questions = []
    current = None
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("QUESTION"):
                if current:
                    questions.append(current)
                current = {"id": line, "x": [], "y": [], "estimate": []}
            elif line.startswith("X:"):
                current["x"] = [float(v) for v in line[2:].split()]
            elif line.startswith("Y:"):
                current["y"] = [float(v) for v in line[2:].split()]
            elif line.startswith("ESTIMATE:"):
                current["estimate"] = [float(v) for v in line[9:].split()]
    if current:
        questions.append(current)
    return questions


def solve_question(q, out):
    """Solve one question and write just the data + the answer(s)."""

    out.write(f"\n===== {q['id']} =====\n")
    out.write(f"X data: {q['x']}\n")
    out.write(f"Y data: {q['y']}\n")

    # This one line uses our whole class chain:
    # Matrix -> Interpolator -> LagrangeInterpolation
    interp = LagrangeInterpolation(q["x"], q["y"])

    # Estimate f(x) at each requested point
    for point in q["estimate"]: 
        value = interp.estimate(point)
        out.write(f"Estimate f({point}) = {round(value, 4)}\n")

    # Question 5 specifically asks for the degree of the polynomial
    if q["id"] == "QUESTION 5":
        out.write(f"Degree of the resulting polynomial = {interp.find_degree()}\n")


if __name__ == "__main__":
    questions = read_questions("Input.txt")

    with open("output.txt", "w") as out:
        for q in questions:
            solve_question(q, out)

    print("Done. Results written to output.txt")