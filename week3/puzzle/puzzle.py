"""
хіхі хаха
"""
##################################
# BEFORE
##################################


# def validate_board(board:list)->bool:
#     """
#     return True if the board is correct due to the rules
#     return False if the board if board isn't 
#     >>> validate_board(["**** ****","***1 ****","**8 3****","* 4 1****",\
# "     9 5 "," 6  83  *","3   7  **","  8  2***","  2  ****"])
#     False
#     """
    # def norepeat_in_list(lst:list)->bool:
    #     """
    #     return False if elements in lst appear more than once
    #     return True if their appearance is unique
    #     >>> norepeat_in_list([9, 1, 3, 5, 3])
    #     False
    #     >>> norepeat_in_list([9, 1, 3, 5])
    #     True
    #     """
    #     for i in range(10):
    #         if lst.count(i)>1:
    #             return False
    #     return True
#     if len(board)!=9:
#         return False
#     for i in board:
#         if len(i)!=9:
#             return False
#     for i in board:
#         lines=[]
#         for j in i:
#             if j.isnumeric():
#                 lines.append(int(j))
#             if not norepeat_in_list(lines):
#                 return False
#     for i in range(9):
#         columns=[]
#         for j in range(9):
#             if board[j][i].isnumeric():
#                 columns.append(int(board[j][i]))
#             if not norepeat_in_list(columns):
#                 return False
#     for i in range(5):
#         figures=[]
#         for j in range(i,i+5):
#             if board[8-i][j].isnumeric():
#                 figures.append(int(board[8-i][j]))
#             if board[8-j][i].isnumeric():
#                 figures.append(int(board[8-j][i]))
#             if not norepeat_in_list(figures):
#                 return False
#     return True

# # if __name__ == "__main__":
# #     import doctest
# #     print(doctest.testmod())


##################################
# AFTER
##################################
def validate_board(board:list)->bool:
    """
    return True if the board is correct due to the rules
    return False if the board if board isn't 
    >>> validate_board(["**** ****","***1 ****","**8 3****","* 4 1****",\
"     9 5 "," 6  83  *","3   7  **","  8  2***","  2  ****"])
    False
    """
    def norepeat_in_list(lst:list)->bool:
        """
        return False if elements in lst appear more than once
        return True if their appearance is unique
        >>> norepeat_in_list([9, 1, 3, 5, 3])
        False
        >>> norepeat_in_list([9, 1, 3, 5])
        True
        """
        for i in lst:
            if lst.count(i)>1:
                return False
        return True
    if len(board)!=9:
        return False
    for i in board:
        if len(i)!=9:
            return False
    for i in board:
        lines=[]
        for j in i:
            if j.isnumeric():
                lines.append(int(j))
            elif j!=' ' and j!='*':
                return False
        if lines and not norepeat_in_list(lines):
            return False
    for i in range(9):
        columns=[]
        for j in range(9):
            if board[j][i].isnumeric():
                columns.append(int(board[j][i]))
        if columns and not norepeat_in_list(columns):
            return False
    for i in range(5):
        figures=[]
        for j in range(i,i+5):
            if board[8-i][j].isnumeric():
                figures.append(int(board[8-i][j]))
            if board[8-j][i].isnumeric() and 8-j!=8-i:
                figures.append(int(board[8-j][i]))
        if figures and not norepeat_in_list(figures):
            return False
    return True

# if __name__ == "__main__":
#     import doctest
#     print(doctest.testmod())
