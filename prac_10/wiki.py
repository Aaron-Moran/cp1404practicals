"""CP1404/CP5632 Practical - Wikipedia API demo."""

import wikipedia


def main():
    """Prompt for page titles and display Wikipedia information."""
    title = input("Enter page title: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError as exception:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(exception.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        else:
            print(page.title)
            print(page.summary)
            print(page.url)
        print()  # Blank line between interactions, like in the sample output
        title = input("Enter page title: ")
    print("Thank you.")


if __name__ == "__main__":
    main()
