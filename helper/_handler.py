'''
Command handler module for AidenBot
'''

from functools import partial as pt
from . import (
    about, cat_wrap, convert, curx_wrap, combine, echo, shout,
    mock, space, aesthetic, bawl1, bawl2, is_palindrome, rng, rpick, emote,
    translate, isup, calc, ask,
    mirror_toggle, define, reddit_hot, slap, stalkig_wrap, stalktwt,
    ticket_add, ticket_rem, ticket_get, urban, wiki_get,
    wiki_lang, wolfram, wolfram_wrap, weather
)

HELP_MSG = ("Available commands:\n"
            "\n"
            "\U00100036 [meta]:\n"
            "about, bye, help, profile\n"
            "\n"
            "\U00100077 [knowledge]:\n"
            "define, kbbi, reddit, tl, urban, wiki, wolfram\n"
            "\n"
            "\U001000B4 [tools]:\n"
            "ask, cur, calc, isup, mirror, pick, rng, stalk, weather\n"
            "\n"
            "\U0010002D [chat enhancer]:\n"
            "cat, slap, text\n"
            "\n"
            "Use /help <command> for more information. Example: /help kbbi")

CMD_TEXT = ("Available text commands:\n"
            "aes, bawl1, bawl2, cmb, echo, lenny, me, mock, pal, ppal, shout, "
            "shrug, spc")

CMD_HELP = {'about': "Usage: /about\n"
                     "Send a message about me.",

            'aes': "Usage: /aes <something>\n"
                   "{}\n"
                   "Can be combined with /bawl1, /bawl2, /mock, "
                   "/shout, and /spc using /cmb.\n"
                   "Example: /aes thetic"
                   .format(aesthetic('Repeat <something> aesthetically')),

            'ask': "Usage: /ask <question>\n"
                   "Simulator Kulit Kerang Ajaib.\n"
                   "Example: /ask Apa aku boleh makan?\n"
                   "Note: use /mcs to get the answers in English",

            'bawl1': "Usage: /bawl1 <something>\n"
                     "Repeat\n{}\n"
                     "Result will be boxed if the first letter in <something> "
                     "is same as the last letter.\n"
                     "Result will look best if <something> consists of "
                     "fullwidth characters (those generated by /aes).\n"
                     "Can be combined with /aes, /mock, "
                     "/shout, and /spc using /cmb.\n"
                     "Example: /bawl1 EDGY"
                     .format(bawl1('<something>')),

            'bawl2': "Usage: /bawl2 <something>\n"
                     "Repeat\n{}\n"
                     "Result will look best if <something> consists of "
                     "fullwidth characters (those generated by /aes).\n"
                     "Can be combined with /aes, /mock, "
                     "/shout, and /spc using /cmb.\n"
                     "Example: /bawl2 ARROW"
                     .format(bawl2('<something>')),

            'bye': "Usage: /bye\n"
                   "Instruct me to leave this chat room.",

            'bencoin': "Usage: /bencoin\n"
                       "[Fasilkom UI 2017 joke]\n"
                       "Send bencoin help message.\n"
                       "(note: the commands actually work!)",

            'calc': "Usage: /calc <expression>\n"
                    "Evaluate a mathematical <expression>, retrieved from "
                    "mathjs.org.\n"
                    "Example: /calc 4 + 8 + 15 + 16 + 23 + 42",

            'cat': "Usage: /cat\n"
                   "Get a random cat image, retrieved from thecatapi.com.\n"
                   "\n"
                   "psst, use /cats for a surprise!",

            'cats': "Usage: /cats\n"
                    "Like /cat, but with a twist.",

            'cmb': "Usage: /cmb <num> <cmd1> <cmd2> ... <cmdnum>\n"
                   "Combine <num> commands into one. Commands are executed "
                   "respectively.\n"
                   "Available commands to combine: "
                   "aes, bawl1, bawl2, mock, shout, spc\n"
                   "Note: each commands can only be used once and bawl1 can't "
                   "be used with bawl2.\n"
                   "Example: /cmb 3 bawl1 aes mock noble man",

            'cur': "Usage: /cur <currency_from> <currency_to>\n"
                   "Get the currency exchange rate from <currency_from> "
                   "to <currency_to>, "
                   "obtained from currencyconverterapi.com.\n"
                   "Example: /cur usd idr\n"
                   "Note: Use /curx to use a custom amount",

            'curx': "Usage: /curx <amount> <currency_from> <currency_to>\n"
                    "Convert <amount> <currency_from> into <currency_to>, "
                    "obtained from currencyconverterapi.com.\n"
                    "Example: /curx 42 eur idr",

            'define': "Usage: /define <something>\n"
                      "Define <something>, retrieved from "
                      "oxforddictionaries.com\n"
                      "Example: /define onomatopoeia",

            'echo': "Usage: /echo <something>\n"
                    "Repeat <something>.\n"
                    "Example: /echo Hello, world!",

            'getmemes': "Usage: /getmemes <keyword>\n"
                        "Find memes containing <keyword>.\n"
                        "If <keyword> is not specified, then a list of "
                        "all available memes will be returned.\n"
                        "Example: /getmemes saya kan",

            'help': "Usage: /help\n"
                    "Send a list of available commands.",

            'isup': "Usage: /isup <website>\n"
                    "Check <website>'s status, "
                    "retrieved from isitup.org.\n"
                    "Example: /isup google.com\n"
                    "Note: use /isupd for a more detailed result.",

            'isupd': "Usage: /isupd <website>\n"
                     "Check <website>'s status, along with its IP, "
                     "response code, and response time, "
                     "retrieved from isitup.org.\n"
                     "Example: /isupd google.com",

            'kbbi': "Usage: /kbbi <something>\n"
                    "Define <something>, retrieved from "
                    "kbbi.kemdikbud.go.id.\n"
                    "Example: /kbbi eufemisme\n"
                    "Note: use /kbbix to also get usage examples.",

            'kbbix': "Usage: /kbbix <something>\n"
                     "Define <something> and give usage examples (if any), "
                     "retrieved from kbbi.kemdikbud.go.id.\n"
                     "Example: /kbbix cinta",

            'lenny': "Usage: /lenny\n"
                     "Send ( ͡° ͜ʖ ͡°)",

            'mcs': "Usage: /mcs <question>\n"
                   "Magic Conch Shell simulator.\n"
                   "Example: /mcs Can I eat something?",

            'me': "Usage: /me <action>\n"
                  "Emote an <action>.\n"
                  "Example: /me is playing guitar.",

            'meme': "Usage: /meme <keyword1>;<keyword2;...;<keywordN>\n"
                    "Send a meme associated with each <keyword>.\n"
                    "If no <keyword> is specified, a random meme will "
                    "be sent.\n"
                    "A maximum of 5 memes can be sent at the same time.\n"
                    "Example: /meme ipk saya kan tinggi;saya kan maba\n"
                    "Note: use /getmemes to get the keywords.",

            'mirror': "Usage: /mirror\n"
                      "Toggle temporary file mirroring on or off.\n"
                      "If turned on, simply send a file (50 MB limit) and "
                      "a temporary mirror will be sent.",

            'mock': "Usage: /mock <something>\n"
                    "{}\n"
                    "Can be combined with /aes, /bawl1, /bawl2, "
                    "/shout, and /spc using /cmb.\n"
                    "Example: /mock Don't tell me what I can't do!"
                    .format(mock('Repeat <something> in a mocking manner.')),

            'pal': "Usage: /pal <something>\n"
                   "Check if <something> is a palindrome.\n"
                   "(only alphanumeric characters are checked, "
                   "case-insensitive)\n"
                   "Example: /pal Dammit, I'm mad!",

            'ppal': "Usage: /ppal <something>\n"
                    "Check if <something> is a perfect palindrome.\n"
                    "Example: /ppal kasur nababan rusak",

            'pick': "Usage: /pick <something1>;<something2>;...;<somethingN>\n"
                    "Pick a random item from a semicolon-separated list.\n"
                    "Example: /pick Dota;LoL;Mobile Legends",

            'profile': "Usage: /profile\n"
                       "Send your display name, profile picture URL, "
                       "and your status message (if any).\n"
                       "If used in a group/multi chat, I can't see your "
                       "status message unless you've added me.",

            'reddit': "Usage: /reddit <subreddit> <limit>\n"
                      "Get hot <limit> posts' titles in <subreddit>.\n"
                      "<limit> is optional, default is 5, maximum is 25.\n"
                      "Example: /reddit showerthoughts 7",

            'rng': "Usage: /rng <floor> <ceiling>\n"
                   "Random (integer) number generator in range "
                   "<floor>..<ceiling> (inclusive).\n"
                   "<floor> is optional, default is 1.\n"
                   "Example: /rng 4815 162342\n"
                   "Note: use /rngf to generate (real) numbers "
                   "with fractions.",

            'rngf': "Usage: /rngf <floor> <ceiling>\n"
                    "Random (float, 2 digit precision) number generator "
                    "in range <floor>..<ceiling> (inclusive).\n"
                    "<floor> is optional, default is 1.\n"
                    "Example: /rngf 2.19 4.2",

            'shout': "Usage: /shout <something>\n"
                     "REPEAT <SOMETHING> IN UPPERCASE.\n"
                     "Can be combined with /aes, /bawl1, /bawl2, "
                     "/mock, and /spc using /cmb.\n"
                     "Example: /shout how do you like them apples?",

            'shrug': "Usage: /shrug\n"
                     "Send ¯\\_(ツ)_/¯",

            'slap': "Usage: /slap <someone>\n"
                    "Slap <someone> with a random object.\n"
                    "Example: /slap Pak Dengklek",

            'spc': "Usage: /spc <something>\n"
                   "{}\n"
                   "Can be combined with /aes, /bawl1, /bawl2, "
                   "/mock, and /shout using /cmb.\n"
                   "Example: /spc aesthetic"
                   .format(space('Repeat <something> with extra spaces')),

            'stalk': "Use /stalkig to stalk an instagram account.\n"
                     "Use /stalktwt to stalk a twitter account.\n"
                     "See \"/help stalkig\" and \"/help stalktwt\" "
                     "for more information.",

            'stalkig': "Usage: /stalkig <username>\n"
                       "Get a random picture taken from <username>'s "
                       "Instagram account, along with the post's link.\n"
                       "Example: /stalkig tychomusic",

            'stalktwt': "Usage: /stalktwt <username>\n"
                        "Get a random Tweet taken from <username>'s "
                        "Twitter account, along with the Tweet's link.\n"
                        "Example: /stalktwt whattheffacts",

            'surprise': "Usage: /surprise\n"
                        "?",

            'text': "Usage: /text\n"
                    "Send a list of text-related commands.",

            'ticket': "Usage: /ticket <something>\n"
                      "Send <something> to my developer. "
                      "Don't worry, it's anonymous!\n"
                      "Example: /ticket this bot sucks",

            'tl': "Usage: /tl <src_lang> <dest_lang> <text>\n"
                  "Translate <text> from <src_lang> to <dest_lang>.\n"
                  "You can use auto as <src_lang> for auto-detection.\n"
                  "See cloud.google.com/translate/docs/languages for "
                  "a list of available languages.\n"
                  "Example: /tl auto id Sorry for my English",

            'urban': "Usage: /urban <something>\n"
                     "Define <something>, retrieved from "
                     "urbandictionary.com.\n"
                     "Example: /urban Mac DeMarco\n"
                     "Note: use /urbanx to also get usage examples.",

            'urbanx': "Usage: /urbanx <something>\n"
                      "Define <something>, and give usage examples (if any), "
                      "retrieved from urbandictionary.com.\n"
                      "Example: /urbanx Young the Giant",

            'weather': "Usage: /weather <location>\n"
                       "Obtain current weather data in <location>, retrieved "
                       "from wunderground.com.\n"
                       "Example: /weather Jakarta",

            'wiki': "Usage: /wiki <title>\n"
                    "Summarize a Wikipedia article titled <title>, or get "
                    "a list of titles in the disambiguation page.\n"
                    "Example: /wiki Vampire Weekend\n"
                    "Note: use /wikilang to change the language.",

            'wikilang': "Usage: /wikilang <language>\n"
                        "Change /wiki language to <language>\n"
                        "See meta.wikimedia.org/wiki/List_of_Wikipedias for "
                        "a list of available languages, and use the prefix "
                        "in the Wiki column to set the language.\n"
                        "Language settings will be reset to default (en) "
                        "every once in a while.\n"
                        "Example: /wikilang id",

            'wolfram': "Usage: /wolfram <something>\n"
                       "Ask wolframalpha.com about <something>.\n"
                       "Returns an image of the result summary.\n"
                       "Example: /wolfram Who are Cage the Elephant?\n"
                       "Note: use /wolframs to get a short text answer.",

            'wolframs': "Usage: /wolframs <something>\n"
                        "Ask wolframalpha.com about <something>.\n"
                        "Returns a short text answer (if available).\n"
                        "Example: /wolframs Tell me a computer science joke"}


def get_help(command=None):
    '''
    Return a command's help message.
    '''
    if not command:
        return HELP_MSG
    try:
        return CMD_HELP[command]
    except KeyError:
        return command + " is unavailable."


def predefined(key):
    '''
    Predefined strings.
    '''
    strings = {'about': "ShivaBot\nBeta 1.1",
               'lenny': '( ͡° ͜ʖ ͡°)',
               'shrug': '¯\\_(ツ)_/¯',
               'stalk': CMD_HELP['stalk'],
               'text': CMD_TEXT}
    return strings[key]


def command_handler(text, user, myself, set_id):
    '''
    Command handler for AidenBot.
    '''
    command = text.split(maxsplit=1)
    cmd = text.lower().split(maxsplit=1)
    result = None

    no_args = {'about': pt(predefined, 'about'),
               'lenny': pt(predefined, 'lenny'),
               'mirror': pt(mirror_toggle, set_id=set_id),
               'shrug': pt(predefined, 'shrug'),
               'stalk': pt(predefined, 'stalk'),
               'tix': pt(ticket_get, allowed=itsme),
               'text': pt(predefined, 'text')}

    single_args = {'ask': pt(ask, id_=False),
                   'aes': aesthetic,
                   'bawl1': bawl1,
                   'bawl2': bawl2,
                   'calc': calc,
                   'cmb': combine,
                   'define': define,
                   'echo': echo,
                   'isup': isup,
                   'isupd': pt(isup, detailed=True),
                   'mcs': ask,
                   'me': pt(emote, user.display_name),
                   'mock': mock,
                   'pal': is_palindrome,
                   'ppal': pt(is_palindrome, perfect=True),
                   'pick': rpick,
                   'rtix': pt(ticket_rem, allowed=itsme),
                   'shout': shout,
                   'slap': pt(slap, user, myself=myself),
                   'spc': space,
                   'stalktwt': stalktwt,
                   'ticket': ticket_add,
                   'tl': translate,
                   'urban': urban,
                   'urbanx': pt(urban, ex=True),
                   'weather': weather,
                   'wiki': pt(wiki_get, set_id=set_id),
                   'wikilang': pt(wiki_lang, set_id=set_id),
                   'wolframs': wolfram}

    double_args = {'cur': convert,
                   'reddit': pt(reddit_hot, splitted=True),
                   'rng': rng,
                   'rngf': pt(rng, frac=True)}

    distinct_commands = {'cat': cat_wrap,
                         'curx': pt(curx_wrap, *command[1:]),
                         'help': pt(get_help, *cmd[1:]),
                         'stalkig': pt(stalkig_wrap, *command[1:]),
                         'wolfram': pt(wolfram_wrap, *command[1:])}

    try:
        if cmd[0] in no_args:
            result = ('text', no_args[cmd[0]]())

        elif cmd[0] in single_args:
            result = ('text', single_args[cmd[0]](command[1]))

        elif cmd[0] in double_args:
            command = command[1].split()
            result = ('text', double_args[cmd[0]](command[0], command[-1]))

        elif cmd[0] in distinct_commands:
            result = distinct_commands[cmd[0]]()

    except (IndexError, TypeError, ValueError):
        result = ("Invalid format.\n"
                  "Please see /help {} for more info."
                  .format(cmd[0]))

    return result
