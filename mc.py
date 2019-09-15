#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# make text editors/python happy ^^^

from __future__ import print_function

import sys

# Trick to make character encoding/decoding almost work in py 2.7.
reload(sys)  
sys.setdefaultencoding('UTF8')


# (C) 2018 by Hannu E K Nevalainen, Strängnäs, SWEDEN
# Free under GPL v2 or later
#

atom={
# ITU @ https://en.wikipedia.org/wiki/Morse_code#Development_and_history 
' ':' ', # space -> space in morse
'a':'.-',
'b':'-...',
'c':'-.-.',
'd':'-..',
'e':'.',
'f':'..-.',
'g':'--.',
'h':'....',
'i':'..',
'j':'.---',
'k':'-.-', # Invitation to Transmit
'l':'.-..',
'm':'--',
'n':'-.',
'o':'---',
'p':'.--.',
'q':'--.-',
'r':'.-.',
's':'...',
't':'-',
'u':'..-',
'v':'...-',
'w':'.--',
'x':'-..-',
'y':'-.--',
'z':'--..',
'0':'-----',
'1':'.----',
'2':'..---',
'3':'...--',
'4':'....-',
'5':'.....',
'6':'-....',
'7':'--...',
'8':'---..',
'9':'----.',

# ^- ITU

# punctation, not all part of ITU
'.':'.-.-.-',
',':'--..--',
'?':'..--..',
"'":'.----.',
'!':'-.-.--',# KW-digraph
'/':'-..-.',
'(':'-.--.',
')':'-.--.-',
'&':'.-...', # AS-digraph, "Wait"
':':'---...',
';':'-.-.-.',
'=':'-...-', # sv.wikipedia - "separator"
'+':'.-.-.', # AR-digraph "New Page Signal", sv.wikipedia - "the end"
'-':'-....-',
# '_':'.--.-', same as 'å' below
'"':'.-..-.',
'$':'...-..-',# SX-digraph (Stock-eXchange)
'@':'.--.-.', # AC-digraph


# selected non-english / national additions. 

chr(229):'.--.-', # à
chr(228):'.-.-',  # ä, æ, ¸a
'ć':'-.-..', # ĉ,ç
'é':'..-..', # ȩ, -d
'ð':'..--.', # Ð
'ĝ':'--.-.', #
'ĵ':'.---.', #
'ñ':'--.--', #
'ĥ':'----',  # ch (gerke), š
chr(246):'---.',  # ö, ó, ø
'ś':'...-...', # 
'ŝ':'...-.', # also: "Understood"
'þ':'.--..', # 
'ü':'..--',  # ǔ, originally gerke 
'ź':'--..-.', #
'ż':'--..-', #

# https://sv.wikipedia.org/wiki/Morsealfabetet
# = above -                                                   NU/DA?-digraph "separator"
# + above -                                                   AR-digraph "the end"
'½':'...-.-', # SK-digraph "End of work",      sv.wikipedia - @, "end of transmission"
'#':'.-..-',  # è, Ł, AU/RA?-digraph,          sv.wikipedia - #, "difference", used as separator before/after numbers
'§':'-.-.-',  # NK?-digraph "Starting Signal", sv.wikipedia - "attention", before new transmission?
'¼':'.-...',  # AS/RI?-digraph,                sv.wikipedia - ~, "wait" (char: altGr-4 in Ubuntu)

'':'' # accept empty string as input, return empty string
}

# more to look at -> https://sv.wikipedia.org/wiki/Specialtecken_i_morsealfabetet

# build the "reverse" dict, for decoding morse into alphas
mtoa={}
for a,m in atom.iteritems():
	mtoa[m]=a


def mEncode(s):
	""" Create a string of . (dit) and - (dah) that represents morse code for the string parameter """
	r=''
	for c in str(s).lower().decode('utf-8').encode('latin1'):
		try:
			r+=atom[c]+' '
		except:
			r+=' <def '+str(ord(c))+'> '
	return r


def mDecode(s):
	""" assume string with space, . (dit) and - (dah) in it; attempt decoding it as being morse into corresponding text """
	r=''
	s=s.split('  ') # double space, for words
	for ss in s:
		ss=ss.split(' ') # single space, for characters in words
		for c in ss:
			try:
				r+=mtoa[c]
			except: 
				r+=' <def?> '
		r+=' '
	return r.decode('latin1').encode('utf-8')


if __name__ != "__main__":
	pass ; # when used as a module, allow access to definitions and functions from other scripts
else:
	# main(sys.argv[1:])
	s=' '.join(sys.argv[1:])
	if len(s)==0 or s=='-h':
		s=((sys.argv[0]).split('/'))[-1]
		print('' \
		'{} <argument(s)>\n' \
		'> Convert to/from morse-code.\n' \
		'> Alphanumeric text arguments gets converted (encoded) to morse.\n' \
		'> Strings of . (dit), - (dah) and space; gets decoded, use double space for delimiting words (you need to quote args!)'.format(s))
	else:
		if len(s.strip('.- '))>0:
			# '--- text-> morse-code --- \n{}'.format(
			print(mEncode(s))
		else:
			# '--- dit/dah/space -> deciphered morse-code --- \n{}'.format(
			print(mDecode(s))
