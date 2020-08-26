!#/usr/bin/python

import spotipy
import spotipy.util as util
import sys
import nfc


scope = 'streaming'
username = ''

def touched(tag):
	if tag.ndef:
		for record in tag.ndef.records:
			receivedtext = record.text

			print("Read from NFC tag: ", receivedtext)
			sp.start_playback(context_uri=receivedtext)
		return True

token = util.prompt_for_user_token(username, scope, client_id='', client_secret='', redirect_uri='http://example.com')

if token:
	sp = spotipy.Spotify(auth=token)

	reader - nfc.ContactlessFrontend('usb')

	while true:
		config = {'interval': 0.35, 'on-connect': touched}

		reader.connect(rdwr=config)
