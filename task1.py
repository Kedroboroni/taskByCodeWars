def strip_comments(string, markers):
    return "\n".join( [ str(  strings[:strings.find(mark)].rstrip() ) for mark in markers for strings in string.splitlines( ) ] )


l = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(l)