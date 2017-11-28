# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


from os.path import dirname, join

import pyjokes

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from random import choice


joke_types = ['chuck', 'neutral']


class JokingSkill(MycroftSkill):
    def __init__(self):
        super(JokingSkill, self).__init__(name="JokingSkill")

    def speak_joke(self, lang, category):
        self.speak(pyjokes.get_joke(language=lang, category=category))

    @intent_handler(IntentBuilder("JokingIntent").require("Joke"))
    def handle_general_joke(self, message):
        selected = choice(joke_types)
        self.speak_joke(self.lang[:-3], selected)

    @intent_handler(IntentBuilder("ChuckJokeIntent").require("Joke")
        .require("Chuck"))
    def handle_chuck_joke(self, message):
        self.speak_joke(self.lang[:-3], 'chuck')

    @intent_handler(IntentBuilder("NeutralJokeIntent").require("Joke")
        .require("Neutral"))
    def handle_neutral_joke(self, message):
        self.speak_joke(self.lang[:-3], 'neutral')

    @intent_handler(IntentBuilder("AdultJokeIntent").require("Joke")
        .require("Adult"))
    def handle_adult_joke(self, message):
        self.speak_joke(self.lang[:-3], 'adult')

    def stop(self):
        pass


def create_skill():
    return JokingSkill()
