from mycroft import MycroftSkill, intent_file_handler


class MopidyMusic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('music.mopidy.intent')
    def handle_music_mopidy(self, message):
        self.speak_dialog('music.mopidy')


def create_skill():
    return MopidyMusic()

