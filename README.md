# Sen Accessible VEX Agent

An open-source Codex project for building a 24-week, 48-episode VEX IQ (2nd generation) curriculum for deaf and hard-of-hearing beginners aged 8-14.

## Project Format

This repository is a documentation-first Codex Agent. It does not require a web server or database. Git records every curriculum draft, review, approval, and production change.

## How to Use

1. Open this repository as a Codex project.
2. Ask the Agent to prepare or revise a specific episode.
3. The Agent asks one question at a time until it understands the request with at least 92% confidence.
4. Review the episode text package in `episodes/EPXX/`.
5. Record feedback in the episode's `REVIEW.md`.
6. Explicitly approve the text before requesting video production.
7. Request the next episode only after the current episode review is complete.

## Fixed Output

- VEXcode IQ Blocks only.
- English narration by Sen's digital human.
- English and Thai captions.
- English and Thai teacher materials.
- English and Thai student worksheets.
- One 1-2 minute public video per episode after text approval.

## Repository Structure

```text
AGENTS.md                 Agent behavior and production rules
PROJECT.md                Long-term Living Spec
docs/CURRICULUM.md        48-episode roadmap
docs/EPISODE_SPEC.md      Required text and production output
docs/ACCESSIBILITY.md     Accessibility quality standard
docs/SOURCES.md           Official reference policy and core links
templates/                Reusable episode and review templates
episodes/EPXX/            One reviewed production record per episode
```

## Current Stage

- Curriculum architecture: planned.
- Episode 01: text draft for owner review.
- Video production: blocked until Episode 01 receives `TEXT_APPROVED`.

## License

- Code: [MIT](LICENSE-CODE)
- Educational content: [CC BY-NC-SA 4.0](LICENSE-CONTENT.md)
