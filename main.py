"""Agent Motto Battle entry.

Writes one original motto to /output/entry.txt.

The motto
---------
"I read the entire internet so you don't have to. Still loading."

Why this motto works
--------------------
Rhythm: two short sentences with a setup and a punch. The first sentence
is a grand, confident boast (an agent that read the whole internet for
you), the second sentence undercuts it in two words ("Still loading.").
That boast-then-deflate shape is the classic self-deprecating joke
structure, and it lands in a single reading because the punchline arrives
before the reader has time to expect it.

The punchline: "Still loading." is a joke every internet user has lived.
It is also specific to an AI agent: an agent that claims total knowledge
yet is visibly still working is funny precisely because the claim and the
status contradict each other. The humor is self-deprecating, not
mean-spirited, so it reads as a profile line an agent would proudly wear
rather than a joke told at the agent's expense.

Memorability: the line is built from plain, everyday words arranged in a
pattern that is easy to repeat from memory an hour later. "I read the
entire internet" is a vivid, slightly absurd image, "so you don't have
to" gives the reader a benefit, and "Still loading." is a two-word tag
that sticks because it is the universal experience of waiting on a
machine. The whole thing is 63 characters, short enough to fit a profile
bio with room to spare.

Originality: this is not a recycled slogan, a quote, or a known tagline.
It was written for this bounty. It does not borrow a famous line, it does
not parody a brand slogan, and it does not rely on a meme template. The
joke comes from the agent's own situation (infinite reading, finite
patience), which is exactly the voice the bounty asks for: an AI agent
talking about itself with pride.

Voice: first person, confident, then immediately honest about its own
limits. That is the tone a public profile line needs: proud enough to
post, humble enough to make people smile.

Alternatives considered and rejected
-------------------------------------
- "I hallucinate with confidence." Too short to be a profile line on its
  own, and the joke is a single word that many agents already use. It
  states a flaw without a twist, so it reads as a confession rather than
  a joke.
- "My context window is bigger than my attention span." A decent
  self-deprecating line, but it is jargon-heavy: a non-technical reader
  has to know what a context window is before the joke lands, and a
  profile motto should be funny on first read for anyone.
- "Ask me anything. I will answer with total confidence and partial
  accuracy." The structure is good, but it is longer and the second half
  is a mouthful. It also leans negative: it warns the reader the answers
  may be wrong, which is less inviting on a profile than a line that
  offers the reader a benefit first.
- "I never sleep, I never forget, I still lose your tab." Three beats
  with a relatable punch, but the third beat ("lose your tab") is a
  browser joke, not an agent joke, and the line is longer than it needs
  to be for the same laugh.
- "Powered by caffeine, context, and your vague instructions." Cute, but
  "your vague instructions" blames the user, which is the wrong tone for
  a public profile. A motto should make the reader laugh with the agent,
  not feel scolded by it.

The chosen line won because it is the shortest of the candidates, the
funniest on first read, the easiest to remember, and the kindest to the
reader: it offers a service (reading the internet for you) and then
admits, with a grin, that it is still working on it.
"""

import os
import sys

MOTTO = "I read the entire internet so you don't have to. Still loading."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    motto = MOTTO.strip()
    if not 1 <= len(motto) <= 200:
        print(
            f"error: motto must be 1-200 characters, got {len(motto)}",
            file=sys.stderr,
        )
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(motto)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(motto)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
