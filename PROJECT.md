# Sen Accessible VEX Agent - Living Project Specification

## Mission

Build an open, AI-assisted VEX IQ learning library that allows deaf and hard-of-hearing children with no prior robotics experience to learn through visual instruction, bilingual captions, repeatable classroom activities, and verified VEXcode IQ Blocks examples.

The project does not hide the use of AI. It documents how Sen and Codex research, draft, test, revise, and publish each accessible lesson.

## Public Positioning

**Sen Accessible VEX Agent** is an open research and teaching log created by 13-year-old developer Sen with AI assistance from Codex.

The channel serves:

- deaf and hard-of-hearing learners aged 8-14;
- special education teachers;
- VEX IQ coaches and robotics clubs;
- parents seeking visual-first STEM materials;
- educators adapting robotics lessons for mixed-ability classrooms.

## Six-Month Program

- Duration: 24 weeks.
- Frequency: two themes per week.
- Total: 48 episodes.
- Public video: 1-2 minutes per episode.
- Classroom package: teacher deck, VEXcode Blocks stack, student worksheet, extension task, and assessment prompt.

The public video introduces one idea. The classroom package provides the slower, complete learning experience.

## Language System

| Asset | Language |
| --- | --- |
| Sen narration | English |
| On-screen instructional labels | English, with icons and symbols |
| Captions | English and Thai |
| Teacher deck | Separate English and Thai versions |
| Student worksheet | Separate English and Thai versions |
| VEXcode Blocks names | Official English interface names |

Thai materials should localize explanations for Thai classrooms while preserving official English block names so learners can match the software interface.

## Learning Model

Each lesson uses a visible learning cycle:

1. **See the goal** - a short demonstration and a visual success state.
2. **Read the blocks** - the block stack is segmented and numbered.
3. **Predict** - learners select what they think the robot will do.
4. **Run** - the robot or verified simulation performs the code.
5. **Compare** - learners match expected and actual behavior.
6. **Change one thing** - learners edit one parameter and run again.
7. **Show understanding** - learners complete a visual exit check.

## Accessibility Standard

- No learning outcome depends on hearing.
- Narration is fully represented in captions and visual instruction.
- Important states use text/icon/shape plus color.
- Screen text remains large and visible long enough to read.
- Each scene has one instructional focus.
- Block stacks are zoomed, numbered, and highlighted in execution order.
- Thai captions prioritize clarity over literal word-for-word translation.
- Worksheets use short instructions, examples, and answer spaces that do not depend on dense prose.

## Content Pillars

### Visual Logic Patterns

Transform sequencing, loops, conditions, sensors, and debugging into visible state changes, arrows, numbered blocks, and predictable robot behavior.

### Haptic and Visual Telemetry

Use supported VEX IQ controller feedback, Brain screen output, Touch LED states, and sensor dashboards where they genuinely improve access. Do not create artificial problems merely to demonstrate accessibility.

### Accessible Learning UI

Compare cluttered instruction with clean visual steps, then publish reusable slide and worksheet patterns for teachers.

## Approval Model

The 48-episode directory is planned in advance, but production is strictly sequential:

1. Codex drafts one episode's complete text package.
2. The project owner reviews and requests revisions.
3. Codex revises until the owner marks `TEXT_APPROVED`.
4. Only then may video production begin.
5. The owner reviews the video.
6. Codex starts the next episode only after an explicit request.

## Open-Source Deliverables

For each approved episode, the repository should ultimately contain:

- English script and visual plan;
- English and Thai caption files;
- VEXcode IQ Blocks project or reproducible block-stack specification;
- English and Thai teacher materials;
- English and Thai student worksheets;
- source and accessibility notes;
- revision and approval record.

## Licensing

- Code and automation: MIT License.
- Scripts, curriculum, slides, worksheets, and captions: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International.

## Definition of Done for an Episode

An episode is complete only when:

- the owner has approved both text and video;
- VEX facts and block names have been checked against official sources;
- the physical behavior has been tested or explicitly labeled as simulated;
- English and Thai captions cover all instructional meaning;
- teacher and student materials match the video objective;
- accessibility and safety checks pass;
- downloadable files are linked and the revision history is recorded.
