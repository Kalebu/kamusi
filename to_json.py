import pandas as pd


def convert_to_json():
    kamusi = pd.read_csv(
        "words.csv", usecols=["Index", "Word", "Meaning", "Synonyms", "Conjugation"]
    )
    kamusi = kamusi.set_index("Index")
    kamusi.to_json("kamusi.json", orient="index")


if __name__ == "__main__":
    convert_to_json()
