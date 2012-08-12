#!/usr/bin/python
import plistlib, os
from operator import itemgetter

# Assuming that your TextExpander config file is in Dropbox...
plist = plistlib.readPlist(os.path.expanduser('~/Dropbox/TextExpander/Settings.textexpander'))
# In my config file, groups and snippets were in the config as noted below...ymmv
groups = plist.get('groupsTE2')
snippets = plist.get('snippetsTE2')

entries = []
uuids = []

for i in groups:
	# replace XXXXXXX with the snippets group you're interested in
	if i['name'] == 'XXXXXXXX':
		uuids = i['snippetUUIDs']

for i in snippets:
	if i['uuidString'] in uuids:
		try:
			entries.append((i['abbreviation'], i['label'], i['lastUsed']))
		except:
			None

sortedsnips = sorted(entries, key=itemgetter(2), reverse=True)
for i in sortedsnips:
	print '%-20s    %-30s' % i[:2]
