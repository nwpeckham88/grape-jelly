def main():
    from GrapeJelly.GrapeJelly import GrapeJelly

    # Create an instance of GrapeJelly
    directories_to_watch = ["path/to/your/directory"]
    grapeJelly = GrapeJelly(directories_to_watch)
    grapeJelly.run()

if __name__ == "__main__":
    main()