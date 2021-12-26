# 4) Write an efficient method that tells us whether or not an input string brackets ("{", "}",
# "(", ")", "[", "]") opened and closed properly. Example: “{[]}” => true, “{(])}” => false,
# “{([)]}” => false

def check_close_braces(text, open_close_rules={"{":"}","[":"]","(":")"}):
    open_rules = open_close_rules.keys()
    close_rules = open_close_rules.values()
    is_open=False
    for char in text:
        # check if s is a open char
        if char in open_rules:
            open_rule = char # get current open_rule
            close_rule = open_close_rules[open_rule] # get the current close rule
            is_open = True
        elif is_open and char == close_rule:
            is_open = False
        elif is_open and char != close_rule and char in close_rules:
            return False
    if is_open:
        return False
    return True


if __name__ == "__main__":
    asd = "{}{" # false
    qwe = "{[]}" # true
    zxc = "{([)]}" # false
    print( check_close_braces(asd))
    print( check_close_braces(qwe))
    print( check_close_braces(zxc))
