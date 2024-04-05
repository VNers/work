from main_code import Link


def main():
    """How to work with customer"""
    links_filename = "links.db"
    links = Link(links_filename)

    asks= True

    while True:
        if asks:
            ask = input("\n\tHi! This is 'Link Maker'! \nDo yo want to make a link? yes/no: ")
            if ask == "no":
                print("So.. I can't help you today!")
                break
            elif ask == "yes":
                print("Let's start! ")
            else:
                print("Wrong option, try again!")
                continue
        asks = False

        print("\nWhat can you do:"),
        print("1. Make a short link."),
        print("2. Make expand link."),
        print("3. Stop using 'Link Maker'.")

        choice = input("Choose an option: ")

        if choice == "1":
            start_link = input("Enter the start link: ")
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
