# main.py

wiki_base_url = "https://oldschool.runescape.wiki/"
grand_exchange_base_url = "https://prices.runescape.wiki/api/v1/osrs/"
highscores_base_url = "https://secure.runescape.com/m=hiscore_oldschool/"
quest_list_from_wiki = "https://oldschool.runescape.wiki/w/Quests/List"
achievement_diary_from_wiki = "https://oldschool.runescape.wiki/w/Achievement_Diary"
collection_log_from_wiki = "https://oldschool.runescape.wiki/w/Collection_log"
money_making_guide_skilling_from_wiki = "https://oldschool.runescape.wiki/w/Money_making_guide/Skilling"

class Application:
    """Main application class."""

    def __init__(self):
        """Initialize the application with default settings or attributes."""
        self.running = True

    def start(self):
        """Start the application."""
        print("Application started.")
        self.run()

    def run(self):
        """Main loop of the application."""
        while self.running:
            try:
                self.process()
            except KeyboardInterrupt:
                self.stop()

    def process(self):
        """Core logic of the application."""
        print("Processing...")
        user_input = input("Type 'quit' to exit: ").strip().lower()
        if user_input == 'quit':
            self.stop()

    def stop(self):
        """Stop the application."""
        print("Stopping the application...")
        self.running = False


if __name__ == "__main__":
    app = Application()
    app.start()