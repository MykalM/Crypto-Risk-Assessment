from pathlib import Path
import questionary
import fire
import import_ipynb
#import apps


answers = questionary.form(
    first = questionary.confirm("Would you like the next question?", default=True),
    second = questionary.select("Select item", choices=["item1", "item2", "item3"])
).ask()

print(answers)