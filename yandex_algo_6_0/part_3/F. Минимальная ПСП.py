with open("input.txt") as file:
    n = int(file.readline())
    lex_order_dict = {bracket: index for index, bracket in enumerate(file.readline().strip())} 
    s_begin = file.readline().strip()

BRACKETS_PAIRS_DCT = {'(': ')', '[': ']'}

def build_min_lex_order_valid_brackets_chain(n, bracket_pairs, lex_order_dict, s):
    opening_brackets = set(bracket_pairs.keys())
    closing_brackets = set(bracket_pairs.values())
    minimal_opening_bracket = min(opening_brackets, key=lambda b: lex_order_dict[b])

    # Initialize answer and stack
    ans = s
    stack = []
    for c in s:
        if c in opening_brackets:
            stack.append(c)
        elif c in closing_brackets:
            if stack and bracket_pairs[stack[-1]] == c:
                stack.pop()
            else:
                # The starting string s must be a prefix of a valid CBS
                # Since the problem guarantees an answer exists, we proceed
                pass
        else:
            # Invalid character, but problem says s consists of brackets
            pass

    pos = len(s)
    while pos < n:
        positions_left = n - pos
        if positions_left == len(stack):
            # Must close brackets to ensure we can close all open brackets
            closing_bracket = bracket_pairs[stack[-1]]
            ans += closing_bracket
            stack.pop()
        else:
            if stack:
                # Can choose to close or open a bracket
                closing_bracket = bracket_pairs[stack[-1]]
                closing_bracket_lex_order = lex_order_dict[closing_bracket]
                # Minimal opening bracket
                opening_bracket = minimal_opening_bracket
                opening_bracket_lex_order = lex_order_dict[opening_bracket]
                if closing_bracket_lex_order <= opening_bracket_lex_order:
                    # Close the last open bracket
                    ans += closing_bracket
                    stack.pop()
                else:
                    # Open a new bracket
                    ans += opening_bracket
                    stack.append(opening_bracket)
            else:
                # Stack is empty, must open a new bracket
                ans += minimal_opening_bracket
                stack.append(minimal_opening_bracket)
        pos += 1
    return ans

ans = build_min_lex_order_valid_brackets_chain(n, BRACKETS_PAIRS_DCT, lex_order_dict, s_begin)

with open("output.txt", "w") as file:
    file.write(ans)
