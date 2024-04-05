from main_code import Link


def main():
    """How to work with customer"""
    links_filename = "links.db"
    links = Link(links_filename)

    while True:
        print("\nMenu:")
        print("1. Shorten link.")
        print("2. Expand link.")
        print("3. Exit.")

        choice = input("Choose an option: ")

        if choice == "1":
            start_link = input("Enter the starting link: ")
            short_link = input("Enter the name of the short link: ")
            links.shorten_link(start_link, short_link)
        elif choice == "2":
            short_link = input("Enter the name to expand the link: ")
            links.expand_link(short_link)
        elif choice == "3":
            print("Thank you for using our service!")
            break
        else:
            print("Wrong choice. Please select an option again.")


if __name__ == "__main__":
    main()
