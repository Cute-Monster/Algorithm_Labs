import wikipediaapi


if __name__ == "__main__":
    out = open("Result.txt", "w")

    wiki = wikipediaapi.Wikipedia(
        language="en",
        extract_format=wikipediaapi.ExtractFormat.WIKI)
    page = wiki.page("Moscow")
    print(page.summary)

    out.close()
