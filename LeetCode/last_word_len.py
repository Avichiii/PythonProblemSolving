def lengthOfLastWord( string):
    string = str(string).strip().split(' ')
    return string[-1]

print(lengthOfLastWord("   fly me   to   the moon  "))