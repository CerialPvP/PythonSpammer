## PythonSpammer

This is a Python program which can be used to spam text.

It works in almost every popular social media app (WhatsApp, Instagram, Discord, Telegram, Facebook) and probably in some games.

The reason why I said "some games" is because some games block the `SendInput()` function from Win32API. People have found alternatives to this, but we won't be using those.

### How to start spamming?

1. Make sure you have Python installed on your computer. To check that, open your command prompt / terminal and type `py` (or `python3` if you're on Mac/Linux). If no errors show up then you are good to go.
2. Download the Python file by clicking on `Code -> Download ZIP`
3. Extract the downloaded ZIP
4. Go to the extracted folder and make a new file named `input.txt`, and put any text you want to spam.
5. Open your command prompt / terminal in the extracted folder, and type `py main.py` (or `python3 main.py` if you're on Mac/Linux).
6. After you ran your program, go to the chat box quickly, and let the program do its magic.

### Custom arguments

For more control over the spammer, we have arguments built in to the `py main.py` command.

In PythonSpammer, command arguments with the value are taken like this:

`--argumentName:Value`

Now, here are all arguments available:

#### --pressBeforeSpam

This argument makes the program press a key before executing.

If you are trying to spam in a game where it's required to press a key to open the chat box, this is useful.

If you want to spam in Roblox, this is what you should use:

`py main.py --pressBeforeSpam:/`

This will make the program press `/` (the key to open chat) before spamming.

**Currently, the program does not support key combinations (example: Ctrl+T, not a real key to open chat in a game I know of). This may be added in the future though.**
