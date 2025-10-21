## 2025-10-19 22:54

- I can't believe I put off this project until now. I spent all day today debugging the resizing of a fallback font for a side project instead of starting this. I'll just accept the 15% penalty and turn it in by EOD tomorrow.
- For this session, I just want to get a handle on what exactly it is I'm supposed to accomplish, and set up the environment. Not sure whether I should use Python, Java, or C++. I'll try just using Python, but I'll want to set up types. I've heard good things about Mypy.
- Just looked online. Interesting to see Astral is making their own type checker now, but it's not ready for production yet. I'll just use Pyright.
- Now I'm going to read to figure out what the project should look like.
- The logger program seems simple enough. I just need to figure out to accept command line arguments to a Python file (simple, I know, but I really haven't used Python that much).
- Encryption: hm, interested to figure out how I can make a Python file that continuously listens to things via standard input. I bet one of the error cases will be if someone tries to encrypt/decrypt before having sett a passkey.

## 2025-10-20

- Plan: finish it!
- Alright, just gave the project description and example files another read over. This doesn't seem too difficult at all, just need to plug together some syntax. Excited to get into it.
- I guess I will be using a different command for running a python process: uv run.

2025-10-20:

- Just finished writing the first draft of the encryption program. I realized there are so many small things about Python that I'm rusty about.
- I decided to use a match statement, which they added in Python 3.10.
- I learned online that I don't need to flush stdout after I print, which makes sense.
- Time to write the logger. I'll copy over my code from the encryption algorithm as a starter.
- Oops, accidentally deleted the project instructions.
- I kinda want to experiment with using a terminal menu libary. I haven't used one of those before. Found one online called "simple-term-menu".
