#%%
import os
from pathlib import Path

import arrow
import click
from arrow import Arrow
from load_dotenv import load_dotenv

load_dotenv()
#%%
# WIP area

#%%
def format_date_with_ordinal(d: Arrow.datetime, format_string: str = "MMM DD{pp}, YYYY"):
    """add th, st, nd or rd based on last number in day."""
    ordinal = {"1": "st", "2": "nd", "3": "rd"}.get(str(d.day)[-1:], "th")
    return d.format(format_string).replace("{pp}", ordinal)


def next_monday(now: Arrow.datetime):
    # weekday (0-6), monday is 0
    weekday = now.weekday()
    offset_to_next_monday = 7 - weekday
    next = now.shift(days=offset_to_next_monday)
    return next


def format_week_to_md_day(week):
    for day in week.keys():
        week[day] = f"- ## {day} [[{week[day]}]]\n"
    return week


def next_week(monday: Arrow.datetime):
    week = {}
    week["Monday"] = format_date_with_ordinal(monday)
    week["Tuesday"] = format_date_with_ordinal(monday.shift(days=1))
    week["Wednesday"] = format_date_with_ordinal(monday.shift(days=2))
    week["Thursday"] = format_date_with_ordinal(monday.shift(days=3))
    week["Friday"] = format_date_with_ordinal(monday.shift(days=4))

    click.echo("\nUpdating to week ahead:")
    for day, date in week.items():
        click.echo(day + " - " + date)

    return format_week_to_md_day(week)


def update_week_ahead_md(fpath, week):
    """
    Read 'Week Ahead.md' in Logseq pages and update
    dates to the next week ahead.
    """
    with open(Path(fpath), "r") as f:
        week_md = f.readlines()

    with open(Path(fpath), "w") as f:
        for line in week_md:
            overwritten = False
            for day in week.keys():
                if day in line:
                    f.write(week[day])
                    overwritten = True
            if not overwritten:
                f.write(line)

DEFAULT_FILE_PATH = os.environ.get("WEEK_AHEAD_MD_FILE_PATH")

@click.command()
@click.option("--monday-date", "-f", default=None, type=str)
@click.option("--path", "-f", default=DEFAULT_FILE_PATH, type=str)
def update_week_ahead(path: str = DEFAULT_FILE_PATH, monday_date: str = None):
    """
    Update dates in logseq to week ahead based on the current date

    :param path: Path of the `Week Ahead.md` file in logseq
    :param monday_date: Overwrites the date of next monday with format YYYY-MM-DD
    :type path: str
    :param monday_date: str = None
    :type monday_date: str

    To run try:
       > poetry run week
    """

    now = arrow.now()

    if monday_date:
        try:
            monday = arrow.get(monday_date)
        except Exception:
            click.echo("Parsing monday date failed please use format YYYY-MM-DD")
            raise
    else:
        monday = next_monday(now)

    click.echo(f"Monday of the week ahead is {monday.format('YYYY-MM-DD')}")
    week = next_week(monday)

    update_week_ahead_md(path, week)

    click.echo("\nUpdate done!")
    click.echo(f"Check your week here: {path}")
    click.echo(f"Check your week here: {path}")
