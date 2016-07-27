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
  6. this shoudl fix thisngsijflasjfdlas;dkfj
