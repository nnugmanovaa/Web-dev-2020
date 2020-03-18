# Given a non-empty string like "Code" return a string like "CCoCodCode".
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'


def string_splosion(str):
    new_str = ''
    for i in range(1, len(str)+1):
        new_str += str[:i]

    return new_str


