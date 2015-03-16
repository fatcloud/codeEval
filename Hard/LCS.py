str1 = ""
str2 = ""
def LCS( a, b ):
	#check if a or b is too large
	if( a >= len(str1) or b >= len(str2) ):
		return ""
		
	#if the two substrings shares identical initial character
	if( str1[a] == str2[b] ):
		return str1[a] + LCS( a + 1, b + 1 )
	
	#compare two possible result: take str1[a] or not
	pos = str2.find( str1[a], b )
	if( pos is not -1 ):
		str11 = LCS( a , pos )
	else:
		str11 = ""
	str12 = LCS( a + 1, b )
	
	if( len( str11 ) > len( str12 ) ):
		return str11
	else:
		return str12
	
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	if( test is '\n' ):
		continue
	str1, str2 = test.split( ";")
	print( LCS( 0, 0 ) )

test_cases.close()