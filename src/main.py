import os

def main():
    from GrapeJelly.GrapeJelly import GrapeJelly

    # Create an instance of GrapeJelly
    directories_to_watch = os.getenv('DIRECTORIES_TO_WATCH', 'path/to/your/directory').split(',')
    grapeJelly = GrapeJelly(directories_to_watch)
    grapeJelly.run()

if __name__ == "__main__":
    main()