# Copyright 2017, Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
        if self.lang[:-3]=='eu':
            self.speak_dialog("joke")
        else:
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

    def stop(self):
        pass


def create_skill():
    return JokingSkill()
