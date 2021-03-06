#!/usr/bin/env python
"""
scores.py - Slap Module
Author: Michael S. Yanovich http://opensource.cse.ohio-state.edu/
Jenni (About): http://inamidst.com/phenny/
"""

import random

def slap(jenni, input):
    """.slap <target> - Slaps <target>"""
    text = input.group().split()
    if len(text) < 2 or text[1].startswith('#'): return
    if text[1] == jenni.nick:
        if (input.nick not in jenni.config.admins):
            text[1] = input.nick
        else: text[1] = 'herself'
    if text[1] in jenni.config.admins:
        if (input.nick not in jenni.config.admins):
            text[1] = input.nick
    verb = random.choice(('slaps', 'kicks', 'destroys', 'annihilates', 'punches', 'teabags', 'roundhouse kicks', 'rusty hooks', 'pwns', 'owns'))
    jenni.write(['PRIVMSG', input.sender, ' :\x01ACTION', verb, text[1], '\x01'])
slap.commands = ['slap', 'slaps']
slap.priority = 'medium'

if __name__ == '__main__':
    print __doc__.strip()
