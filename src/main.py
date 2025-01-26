import os

def main():
    from JellyJam.JellyJam import JellyJam

    # Create an instance of JellyJam
    directories_to_watch = os.getenv('DIRECTORIES_TO_WATCH', 'path/to/your/directory').split(',')
    jellyJam = JellyJam(directories_to_watch)
    jellyJam.run()

if __name__ == "__main__":
    main()