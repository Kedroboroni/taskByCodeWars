def strip_comments(string, markers):
    return "\n".join( [ str(min( [ str(  strings[:strings.find(mark)] ).rstrip() for mark in markers] ) ) for strings in string.splitlines( ) ] )