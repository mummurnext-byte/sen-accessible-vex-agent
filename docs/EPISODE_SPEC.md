# Episode Text and Production Specification

## Text Draft Package

Every episode begins as a complete text package with these sections:

1. Episode metadata and current workflow state.
2. One learner-facing objective.
3. Two or three observable success criteria.
4. Prerequisites, hardware, and preparation.
5. Verified official sources.
6. English narration script for a 1-2 minute video.
7. Timestamped visual plan.
8. Exact VEXcode IQ Blocks stack specification.
9. English caption file.
10. Thai caption file.
11. English teacher deck outline.
12. Thai teacher deck outline.
13. English student worksheet.
14. Thai student worksheet.
15. Facebook publishing copy and comment keyword.
16. Accessibility and safety audit.
17. Owner review record.

## Public Video Timing

The target duration is 60-120 seconds. Use the shortest duration that teaches the objective clearly.

| Segment | Target | Required purpose |
| --- | --- | --- |
| Silent Hook | 0-5 seconds | Show the learning problem without depending on narration |
| Visual Blocks | 5-25 seconds | Show numbered blocks and execution order |
| Robot Proof | 25-50 seconds | Show real hardware behavior or a labeled simulation |
| Learning Check | 50-75 seconds | Ask one visual prediction or comparison question |
| Open Repository | Final 10-15 seconds | Identify the downloadable classroom material |

## Script Style

- Sen speaks in short, confident English sentences.
- Target 120-150 spoken words per minute.
- Define one new technical term at a time.
- Never say “simple” or “obvious” about a task that may be new to the learner.
- Describe visible evidence: what changes, where it changes, and when it changes.
- Do not narrate decorative visuals.
- The standard ending must be complete and uncut.

## VEXcode Blocks Specification

For each stack:

- use the exact official English block name;
- state the category and configured device;
- list parameter values and units;
- show the block order with indentation for nested blocks;
- state the expected physical or screen result;
- include a verification source;
- flag any behavior that still needs physical testing.

The specification is not a substitute for an `.iqblocks` project in the final approved classroom package. It is the reproducible source for building and checking that project.

## Caption Standard

- English captions follow the spoken meaning and preserve technical terms.
- Thai captions are natural classroom Thai, not phonetic transliteration.
- Official English block names remain in English and may be followed by a short Thai explanation.
- Use no more than two lines per caption event.
- Avoid placing essential captions in the lowest 20% of vertical video.
- Captions should remain on screen long enough for beginner readers.

## Teacher Deck Standard

Each language version contains 8-10 slides:

1. Visual objective
2. Vocabulary with icons
3. Hardware and setup
4. Predict
5. Build the block stack
6. Run and observe
7. Change one parameter
8. Check understanding
9. Extension, when appropriate
10. Source and license

## Student Worksheet Standard

Limit the core worksheet to two pages:

- match icons and terms;
- trace or number the block sequence;
- predict one output;
- record one observation;
- change one parameter;
- complete one visual exit check.

## Review Gate

The owner must write an explicit approval in `REVIEW.md` before state changes from `TEXT_REVIEW_REQUIRED` to `TEXT_APPROVED`. A request for minor edits is not approval.
