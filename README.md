# demonIRCBot
A mischievous IRC bot.

This bots goal is to be threaded and able to control an army of minibots called "Imps". Perhaps a stupid naming convention, but I like it.
The master bot, is called "demon" and it can create "Imps". Each bot individually have unique "abilities" and owners.
The owners are defaultly myself right now, and (I have yet to add) the bot "demon" who creates them. Although if a user has permissions
to request a bot from "demon" he will also become the owner of the bot that is created. Each bot is a unique thread as well.
Ideally I want to be able to create what I call worker bots which can perform individual small tasks to do larger tasks, like
mass ascii art drawing. Usually if you attempt to draw ascii art in IRC there is a flow control that will kick you. Having
multiple bots doing a unique line of ascii art prevents the kickage.

Generally speaking, I'm still working on the base functions of the bot. Right now I'm striving for flexibilty so that additional
features will not be a pain to add later.

TODO:
  1. Create abilities from which to use. The base is there now
  2. Touch up the initial connection so that the bot doesn't interpret unimportant data during connection
  3. Eventaully create a separate interpreter for data. One that can handle verbose commands
  4. Allow for saved states.
  5. Allow for either ability usage or response types based on the user.

FINAL THOUGHTS:
GOOD:
  1. The usage of the function 'performAbility' was very useful for implementing more complicated abilites.
    - The next iteration needs to have a strong base structure, in which core features are defined in the bot class
  2. The bots being threads was very useful and worked very easily
  3. I thought the implementation of giving abilities through the bit field was good. Made all bots potentially unique and easy to make
        with custom abilities.

BAD:
  1. The permissions need to be handled by a seperate class. All existing within the bot class was ugly.
  2. The passing of arguments that needed to be parsed by each ability could be better. It got worse as things got layered, such as "repeat 4 timedevent 2 echo hi"
    - This forced me to thread timedevents so that the bots didn't wait forever. Unfortunately it made it difficult to do repeat with it because, well they are threads.
  3. There was no way to save states or bots. Allowing it to save bots in files or other information would be great.

UGLY:
  1. Importing was really awkward. Entire program should run via python3 instead of being an abomination that it is now. Needs to be python3 style
  2. Coding style needs to be consistent, in terms of variable names and how variables are created.
  3. Everything should be python3 oriented, instead of the mixture that I had
  4. Needs a better way to handle incorrect types and bad arguments. That is ability dependent though.
  5. Probably should make a seperate class for an "Interpreter" which determines if it is a command or a general response. That way I can handle commands or
        look for random things said in IRC. Making a "talking" bot would be cool.
  6. Seriously need to improve importing. It was really problematic.

