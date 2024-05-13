def upper_case(s):
    '''делает буквы в строке заглавными'''
    return s.title()


def upper_first_letter(s):
    s = ' '.join(word.capitalize() for word in s.split())
    return s
