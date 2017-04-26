## Emotion format

Enclosed in () at the beginning of the message. TODO

## Character announcement

Clients will announce `# Appears as CHARACTER` when changing their character, joining a comic channel, or switching to comic mode for the first time on a channel. After announcing it, Comic Chat clients seeing this message will supress it and then proceed to PRIVMSG the user who sent it their `# Appears as` block.

## Away announcement

An away message in comic channels will be send as a to-channel CTCP `AWAY` message, and the client will also use the normal IRC away message.

## Sending character without message

A <Chr> message with an emotion block will be send. Clients will filter this out and place the character without a message.

## Sounds

It sends a `CTCP SOUND` message, but since the message is prefixed by an emotion block, it doesn't show as such. Parameters are the sound's file name, then a message. Sounds will be looked for in the media search path, and played if they are WAV or MIDI. (An MP3 patch [exists](http://www.mermeliz.com/xpmp3help.htm).)
