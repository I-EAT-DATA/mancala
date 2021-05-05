

in_one = "ello there"
in_two = " "

def diff(in_one, in_two):
    final = ""

    longer = in_one if len(in_one) > len(in_two) else in_two

    for idx in range(len(longer)):
        char_one = in_one[idx] if idx < len(in_one) else ""
        char_two = in_two[idx] if idx < len(in_two) else ""

        # if char_one == " " or char_two == " ":
        #     continue
        
        if char_one == "":
            final += f"{{{char_two}}}"
        elif char_two == "":
            final += f"{{{char_one}}}"
        elif char_one != char_two:
            final += f"({char_one}/{char_two})"

        else:
            final += longer[idx]


    # for char_one in in_one:
    #     for char_two in in_two:
    #         if char_one != char_two:
    #             final += f"({char_one}/{char_two})"
    #         else:
    #             final += char_one

    print(final)
    # for char_idx, char in enumerate(in_one):
        

diff(in_one, in_two)


