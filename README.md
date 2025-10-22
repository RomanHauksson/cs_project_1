I used [uv](https://docs.astral.sh/uv/), a really nice package manager for Python, to make this project. [To install it](https://docs.astral.sh/uv/getting-started/installation/) on MacOS or Linux, run this command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then, to execute my program, simply run:

```
uv run driver.py log.txt
```

And uv will automatically download the correct version of Python, install the dependencies (just one for this program), and run the script. I tested this on UTD's Linux server and it worked.
