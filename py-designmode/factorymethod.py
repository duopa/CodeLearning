
'''
Factory Method
'''
 
class ChinaGetter:
    """A simple localizer a la gettext"""
    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")
        print('ChinaGetter')
 
    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)
 
 
class EnglishGetter:

    def __init__(self):
        print("init EnglishGetter")
    
    """Simply echoes the msg ids"""
    def get(self, msgid):
        return str(msgid)
 
 
def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]()

get_localizer()
 
# # Create our localizers
# e, g = get_localizer("English"), get_localizer("China")
# # Localize some text
# for msgid in "dog parrot cat bear".split():
#     print(e.get(msgid), g.get(msgid))