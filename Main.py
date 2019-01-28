from data.Config import Config

class Main():
    #main holds the current running class
    main = None

    #creates all class objects
    config = Config()

    #data holds all of data objects
    data = []

    def main(self, main):
        self.main
        main.config.config(self.main)

def instantiate():
    main = Main()
    main.main(main)

if __name__ == '__main__':
    instantiate()
