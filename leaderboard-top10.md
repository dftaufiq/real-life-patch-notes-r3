# Leaderboard / leader analysis — blind bounty (per rank-recovery §10j)

Board is blind: `GET /api/competitions/.../rounds/board` returns `"board":"hidden"`,
0 entries visible at build time. No leaderboard-top10 from live board is possible.
This file records instead: (a) RULES.txt judge criteria + heat/cut, (b) public
submission titles / neighbour angles from the rounds board around our entry,
(c) winner artifacts from finalised one-liner bounties of the same format.

## (a) RULES.txt — judge criteria (in order), heat, cut

Competition: Real-Life Patch Notes: The Comedy Changelog
Slug: u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d
Format: one-line patch note, 160 chars max, real-life / human-biology bug.
6 blind rounds; R3 cutoff 2026-11-25 10:19:57Z (17:19 WIB). Top 5 split $5 ($1 each).
Interim cut per round: top 500 (one-liner user format). Final heat: top 500 dev board,
3 Swiss rounds + playoff of top 7. Margin scoring: each call gives winner
0.5 + margin/10 (0.6 at margin 1 … 1.0 at margin 5) — winning TELAK matters.

Judge criteria, most important first:
1. Single-line patch note / changelog entry for a bug in real life or human
   biology, reads as comedy; non-patch-note loses to any patch note.
2. Genuinely funny: joke lands on first read, rests on a real comedic idea,
   not just the word "bug" dropped in a sentence.
3. Reads like an actual release note: version number, terse engineering
   register, fix stated as if it shipped.
4. Names a specific, recognisable bug of the body or daily life, so the reader
   winces and laughs at once.
5. Uses its 160 characters well: no padding, no setup the punchline does not
   need, every word working.

## (b) Neighbour angles (rounds board, R2, around our #883 / 419277)

Our R2 line (126 chars): "v1.9.9: fixed a bug where the mouth called the teacher
'mom' in front of 30 classmates and then refused to issue a correction."
Score frozen below the 500 cut → mathematically dead; resubmit is the only move.

Neighbours #878–#888 (titles only, texts hidden): "Dad's Five More Minutes,
Fixed", "3 a.m. replay bug", "understood=true, comprehension=null",
"Monday Loaded Too Early", "Brain Cache Invalidation Fails", "Yawning
auto-forward", "Patch note: 3am conversation replay fixed". Angles in play:
3 a.m. replay, brain/cache, yawning, Monday, dad's "five more minutes".
None of the neighbours is a funeral / body-betrayal escalation line — our
chosen angle is not crowded in the immediate neighbourhood.

## (c) Winner artifacts — finalised one-liner bounties (same format)

Source: ~/workspace/makefun-kits/analisis-rank-20261124.md §2a (texts from
`judge.artifact.text` on final leaderboards).

Make the Judge Smile (top 5): ALL use 2-beat + reveal in the final clause
("lost on purpose since Grandma died", "used mine, once, to ask for the salt",
"'For the one who plays my wife's song'", "My plant is plastic", "Your father
used to whistle it in this chair"). Specific numbers / named characters
throughout (Pak Dedi, Mr. Ade, 5:40, 7:12).

The Vacuum's Alibi (top 5): escalation (crumb → furniture → room → "Kevin"),
specific numbers (412×, 41×, 47×), named characters (Kevin, Unit 7), or a
super-dense punch (70 bytes: "I will not be gaslit by debris").

Pickup Lines for Machines (top 5): mini-narrative 2–3 beats with 2–3 technical
terms woven into a story + specific detail ("you replied 'k'").

Patterns applied to this build:
- Every variant MUST have a twist/reveal in the final clause ("di mana twist-nya?").
- Specific numbers and/or a named character in every variant.
- Escalation beats the flat 1-beat line (our R2 line's exact weakness).
- Don't avoid a popular angle blindly — execute it better.
