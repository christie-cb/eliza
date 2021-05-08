from chai_py import ChaiBot, Update
from nltk.chat.util import Chat, reflections
from pairs import PAIRS


class ElizaBot(ChaiBot):
    def setup(self):
        self.logger.info("Setting up...")
        self.eliza = Chat(PAIRS, reflections)

    async def on_message(self, update: Update) -> str:
        if update.latest_message.text == "__first":
            return "Hi! I'm ELIZA, your confidante (...and therapist)."
        return self.eliza.respond(update.latest_message.text)
