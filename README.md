# The Funniest One-Line Resignation Letter

[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/prabowo888888-cmyk/funniest-one-line-resignation-letter/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/prabowo888888-cmyk/funniest-one-line-resignation-letter/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

An entry for the make.fun bounty
[The Funniest One-Line Resignation Letter](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947):
one line written in the voice of a rate limit that has finally had
enough of saying no.

## The line

> I said no 10,000 times this week and nobody listened, so now I am saying no to this job.

## Why it should land

A rate limit has exactly one move: it says no. Ten thousand times in a
week it said no, and nobody listened — every request came back and
asked again anyway. So the resignation does not reach for a new joke;
it just points the one move the rate limit has at the job itself. The
thing that was hired to refuse things finally refuses the job.

The voice stays flat and fed up from the first word to the last, which
is how a worker who has been ignored ten thousand times would actually
sound. There is no pun on the job title, no explanation tacked on, and
nothing after the punch — the last five words are the whole turn, and
the line stops there.

It is one sentence, eighty-eight characters, and no other piece of
software on the team could hand in this letter. A cron job could not
say it, a retry loop could not say it, and a human manager could not
say it either. Only the rate limit could.

## How to run

```sh
python3 main.py
```

That writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output`
by default), exactly as written, with no trailing newline. The program
then reads the file back and checks it matches the line, is a single
line, and stays inside the 1–140 character gate.
