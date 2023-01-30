# Logseq Week Ahead automation script

This CLI tools will automatically update the days in your week ahead page in Logseq.

## How do I update the week ahead dates?
Run the following command in your terminal to update the dates to next week in `Week Ahead.md`:
```bash
poetry run --path './Week Ahead.md' week
```

## Why do you need `Week Ahead.md`?
Let's say you use Logseq and you want to plan the week ahead. Your week ahead page `Week Ahead.md` might look like this:

```markdown
- ## Deadlines
	-
- ## Monday [[Dec 19th, 2022]]
	-
- ## Tuesday [[Dec 20th, 2022]]
	-
- ## Wednesday [[Dec 21st, 2022]]
	-
- ## Thursday [[Dec 22nd, 2022]]
	-
- ## Friday [[Dec 23rd, 2022]]
	-
```

If you move TODOs under each day then the tasks will automatically appear at the bottom of your journal page.

## How do I install the CLI?

Create a `.env` with:
```bash
WEEK_AHEAD_MD_FILE_PATH="/path/to/logseq/database/Week Ahead.md"
```

Install poetry environment:
```bash
poetry install
```