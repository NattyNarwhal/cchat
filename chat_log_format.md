Comic Chat logs in comic mode are plain text files wrapped within an OLE2
container. The format of the logs are human readable, yet contain enough
information to recreate the comic view transcript, complete with emotions.

The beginning of the format begins with a magic `CHATCONVERSATION` string, followed by some commands to initialize the buffer.

Lines are seperated by Windows style CRLFs. If a message has multiple lines, then those lines are in LF format to simplify parsing.

Each line begins with a command, and parameters that are seperated by tabstops.

## Commands

### `starthistory`

Takes two nicknames as the parameter, and then a title for the log. Comic Chat picks a title at random when creating a transcript.

### `backdrop`

Takes the filename for a backdrop as a parameter, such as `DEN.bgb`.

### `ejoin`

Only seems to appear at the beginning, and takes a nickname of someone who was already in the room.

### `changeavatar`

Takes a nickname, then a character's name (without extension) as parameters. Can appear at the beginning to initialize the transcript, or further inside as people change their characters.

### `getinfo`

Creates a panel describing metadata about people, such as people's client versions or away status. Takes a username, then any message as parameters.

### `join`

Takes a nickname as parameter. Not shown in the transcript.

### `part`

Takes a nickname as parameter. Not shown in the transcript.

### `say`

An IRC message. Takes a nickname, then an format for emotion, then the IRC message.
