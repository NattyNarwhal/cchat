## Emotion format

Enclosed in () at the beginning of the message. TODO

## Character announcement

Clients will announce `# Appears as CHARACTER` when changing their character, joining a comic channel, or switching to comic mode for the first time on a channel. After announcing it, Comic Chat clients seeing this message will supress it and then proceed to PRIVMSG the user who sent it their `# Appears as` block.

## Away announcement

An away message in comic channels will be send as a to-channel CTCP `AWAY` message, and the client will also use the normal IRC away message.
