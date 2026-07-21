# Generate One Episode Text Package

Use this prompt only after the project owner has selected an episode and answered the Agent's one-question-at-a-time discovery process.

## Inputs

```yaml
episode_id: EPXX
curriculum_title: exact title from docs/CURRICULUM.md
learner_age: 8-14
learner_level: complete beginner
platform: VEX IQ 2nd generation
programming_mode: VEXcode IQ Blocks
spoken_language: English
caption_languages:
  - English
  - Thai
teacher_material_languages:
  - English
  - Thai
student_material_languages:
  - English
  - Thai
host: Sen, age 13
video_duration_seconds: 60-120
current_state: PLANNED
owner_constraints: supplied during discovery
```

## Agent Instruction

Create the complete **text-only** package for the selected episode.

Research first. Verify hardware capabilities and exact VEXcode block names using official VEX IQ 2nd generation sources. If a claim cannot be verified, flag it instead of inventing an answer.

The lesson must be completable without audio. Use short English narration, English and natural Thai captions, numbered Blocks, stable icons, high contrast, and visible robot states. Pair color with text, icon, shape, or pattern.

Use this video sequence:

1. Silent Hook
2. Visual Blocks
3. Robot Proof
4. Learning Check
5. Open Repository

Do not generate, render, edit, upload, or publish video. Do not start another episode.

## Required Output

Create or update:

```text
episodes/EPXX/EPXX_TEXT_DRAFT.md
episodes/EPXX/CAPTIONS_EN.srt
episodes/EPXX/CAPTIONS_TH.srt
episodes/EPXX/REVIEW.md
```

The text draft must follow `templates/EPISODE_TEXT_PACKAGE.md` and include:

- objective and observable success criteria;
- prerequisites, hardware, setup, and safety;
- official source links;
- 1-2 minute English narration;
- timestamped visual plan;
- exact VEXcode IQ Blocks stack;
- expected result and physical test record;
- English and Thai teacher deck outlines;
- English and Thai student worksheets;
- Facebook title, description, hashtags, and comment keyword;
- accessibility audit;
- revision notes.

## Validation

Before finishing:

1. Check that the narration fits the planned duration at 120-150 words per minute.
2. Check that English and Thai SRT files contain matching event numbers and timestamps.
3. Check that every spoken instruction appears in captions or visuals.
4. Check that color is never the only signal.
5. Check all official links and block names.
6. Mark untested robot behavior as `NOT YET TESTED`.
7. Set the episode state to `TEXT_REVIEW_REQUIRED`.
8. Stop and ask the project owner to review `REVIEW.md`.

## Forbidden Transitions

Without explicit owner approval, do not:

- change the state to `TEXT_APPROVED`;
- create a video project;
- generate the next episode;
- publish files or configure a social-media automation;
- claim a physical robot test passed.
