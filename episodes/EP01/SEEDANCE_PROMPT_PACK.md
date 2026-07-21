# EP01 Seedance Prompt Pack

## Production Decision

Generate this 70-second episode as seven independent 10-second clips. Seedance
currently works best with short clips, while exact educational text, VEXcode
block names, and bilingual captions should be added as deterministic overlay
layers after generation.

- Ratio: `9:16`
- Resolution: `720p`
- Clip duration: `10 seconds` each
- Spoken language: English
- Captions: large Thai primary line, smaller English line
- Proof scene label: `SIMULATION`
- Do not ask Seedance to render readable captions or exact VEXcode text.

## Reference Setup

Upload the approved visual reference as `@Video1` and reuse it for every clip.
It is a style reference only: soft white background, thick black stick figure,
clean 2D motion, restrained particles, and neon focus glows.

After Clip 1 is approved, also use the latest approved clip as a continuity
reference for the next generation when the Seedance interface supports it.

## Shared Style Anchor

Append this direction to every prompt:

```text
Vertical 9:16 accessible educational motion graphic. Soft white-to-light-gray background, thick expressive black stick-figure teacher, clean industrial UI, generous empty space, stable layout, smooth readable motion. INPUT uses neon blue #00D2FF with a label shape, BRAIN uses cyber yellow #FFD700 with a label shape, OUTPUT uses vivid purple #BD00FF with a label shape. Meaning never depends on color alone. Match @Video1 only for animation rhythm, line weight, and visual simplicity. No photorealism, no real child, no logos, no watermark, no generated captions, no garbled letters, no malformed robot, no duplicated limbs, no camera shake, no clutter. Keep the lowest 20 percent visually quiet for later subtitles. Crisp vector-like edges, high contrast, stable objects.
```

## Clip 1 - Silent Hook

**Timing:** `00:00-00:10`

```text
10-second vertical 9:16 animation. A friendly black stick-figure teacher stands on the left and points toward three large empty labeled-card shapes arranged left to right: a blue input card, a yellow brain card, and a purple output card, connected by bold arrows. Hold the complete diagram still for the first two seconds for reading time. Then a pulse travels from the blue card through the yellow card to the purple card; each card gains a restrained glow and a matching icon: button, logic stack, moving robot. Fixed eye-level camera, no zoom. Subtle futuristic educational music and soft UI pulses, no speech. No generated text. Keep bottom subtitle safe area empty. Apply the shared style anchor.
```

**Overlay text:** `HOW A ROBOT THINKS` / `INPUT -> BRAIN -> OUTPUT`

**English narration:** “Every robot program begins with one pattern: input, Brain, output.”

## Clip 2 - The Check Button Is Input

**Timing:** `00:10-00:20`

```text
10-second vertical 9:16 animation. The same stick-figure teacher walks to a simplified VEX IQ Brain-shaped device without logos. A large blue circular Check button appears on the device. The teacher presses it once; concentric blue rings expand, a blue signal particle follows a clean cable-like line toward a waiting logic-block shape, and a small INPUT icon card locks into place. Medium-wide fixed camera, one clear action at a time, readable pauses between actions. Subtle futuristic educational music and one soft button click, no speech, no generated text. Keep bottom subtitle safe area empty. Apply the shared style anchor.
```

**Overlay text:** `INPUT: PRESS CHECK`

**English narration:** “The Check button is our input. It tells the robot that something has happened.”

## Clip 3 - The Brain Reads Top to Bottom

**Timing:** `00:20-00:30`

```text
10-second vertical 9:16 animation. The same stick-figure teacher holds a yellow magnifying glass beside a vertical stack of five clean colored programming-block shapes. A bright yellow scanner moves from the top block to the bottom block, pausing briefly at each one. Number badges 1 through 5 appear beside the blocks as simple geometric badges, while a small Brain icon remains fixed above the stack. Fixed camera, smooth downward scan, sparse particles only around the active block. No logos, no generated code text, no speech. Keep bottom subtitle safe area empty. Apply the shared style anchor.
```

**Overlay text:** `BRAIN: FOLLOW THE BLOCKS` and the exact VEXcode stack from the approved EP01 text package.

**English narration:** “The VEX IQ Brain reads the input and follows these blocks from top to bottom. First, the screen says PRESS CHECK.”

## Clip 4 - Input Becomes True

**Timing:** `00:30-00:40`

```text
10-second vertical 9:16 split-screen educational animation. Left side: a large blue Check button and a waiting logic-block shape. A simple fingertip presses the button; the waiting block changes from an outlined hourglass state to a green check-mark state. Right side: a simplified robot Brain screen changes through three clearly different icon states: waiting dots, forward arrow, completion check mark. A signal pulse crosses the center divider from left to right. Fixed camera, synchronized cause-and-effect timing, high contrast, no generated words, no speech. Keep bottom subtitle safe area empty. Apply the shared style anchor.
```

**Overlay text:** `PRESS CHECK -> TRUE -> GO`

**English narration:** “When I press Check, the waiting block becomes true. The Brain changes the screen to GO.”

## Clip 5 - Robot Output Simulation

**Timing:** `00:40-00:50`

```text
10-second vertical 9:16 top-down simulation. A simple two-wheel educational robot starts behind a blue tape line on a clean white practice lane. A yellow execution pulse reaches the robot, then the robot drives straight forward and stops exactly at a purple 300-millimeter target line. Show a fixed distance bracket between the start and target lines. When it stops, a large purple completion icon appears above it and emits one restrained pulse. Smooth physically plausible wheel motion, fixed overhead camera, no drifting, no collision, no real-world footage, no logos, no generated text, no speech. Keep bottom subtitle safe area empty. Apply the shared style anchor.
```

**Overlay text:** `SIMULATION` / `OUTPUT: DRIVE 300 mm` / `DONE`

**English narration:** “The drivetrain moves forward for 300 millimeters. When the movement finishes, the final output appears: DONE.”

## Clip 6 - Prediction Check

**Timing:** `00:50-01:00`

```text
10-second vertical 9:16 educational prediction animation. The same stick-figure teacher thinks beside a large question-mark icon. A green distance-parameter card visually changes from a short bar marked by three dots to a longer bar marked by five dots. Below it, the same simple robot first stops at the nearer blue marker, resets, then stops at the farther purple marker. The input button icon and Brain icon remain unchanged and locked in place, while only the output distance bracket stretches. Fixed camera, clear comparison, pause on the final answer for two seconds. No generated text, no speech. Keep bottom subtitle safe area empty. Apply the shared style anchor.
```

**Overlay text:** `300 mm -> 500 mm` / `INPUT: SAME` / `BRAIN ORDER: SAME` / `OUTPUT DISTANCE: CHANGES`

**English narration:** “Now predict: if we change 300 to 500 millimeters, which part stays the same, and which output changes?”

## Clip 7 - Open Repository

**Timing:** `01:00-01:10`

```text
10-second vertical 9:16 closing animation. The same black stick-figure teacher bows once, then points downward. Three clean resource cards slide into the center: a document icon, a colorful blocks icon, and a teacher-guide icon. A simple open-source branch symbol connects the cards. Hold the final composition for the last four seconds. Soft white background, restrained blue glow, gentle ending motion, subtle futuristic music resolves warmly. No generated URLs, no generated captions, no speech. Keep all essential elements above the lowest 20 percent. Apply the shared style anchor.
```

**Overlay text:** `OPEN-SOURCE LESSON PACKAGE` / `PDF · VEXCODE BLOCKS · TEACHER GUIDE`

**English narration:** “Download the English and Thai lesson materials from our open repository. Input your logic, spark their world. See you in the next log.”

## Subtitle Layer Standard

Add subtitles after combining the seven clips:

- Thai is the primary line, large and bold.
- English is the secondary line, smaller and medium gray.
- Use no more than two lines per language event.
- Position the subtitle panel above the lowest 20 percent platform overlay area.
- Use a solid or nearly opaque white panel with black Thai text.
- Preserve exact English terms: `INPUT`, `BRAIN`, `OUTPUT`, `PRESS CHECK`, `GO`, `DONE`, and `300 mm`.

## Assembly Check

- Total runtime: approximately 70 seconds.
- Use one continuous English voice track across all clips.
- Keep music below narration and avoid audio-only teaching cues.
- Label all generated robot behavior as `SIMULATION`.
- Do not publish until the block stack has been physically tested on the selected VEX IQ build.
