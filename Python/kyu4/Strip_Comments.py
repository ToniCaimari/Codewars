def solution(string, markers):
    solution = ""
    alert = False
    for i in string:
        if alert == False:
            if i not in markers:
                solution += i
            else:
                alert = True
            continue
        elif i == "\n":
            alert = False
            solution = solution[:-1] + i

    return solution[:-1]


assert(solution("apples, pears # and bananas\ngrapes\nbananas !apples",
                ["#", "!"]), "apples, pears\ngrapes\nbananas")
assert(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
