# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`Group 10 TarotVulture`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `[Raavee Uttekar]` | `Fabrication / Mechanics` |  `Electronics` | `Material knowledge, physical assembly, mechanism problem-solving`
| `[Aditi Rathod]` | `Electronics / Coding` | `[Mechanics]` | `System integration, audio logic, interaction design` 

## 1.3 Project Title
`Tarot Fortune Telling Machine`

## 1.4 One-Line Pitch
`A theatrical interactive vulture puppet that gives RFID-based tarot fortunes or random magic 8 ball style yes/no/maybe answers using motion, sound, and physical character performance.`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`Our project is a playful fortune-telling machine built around a vulture puppet character. The system uses an ESP32 with MicroPython, RFID tarot cards, multiple servo motors, a limit switch, and laptop-based audio playback to create the illusion of a living creature that wakes up, reacts, speaks, and delivers fortunes.`

`The experience is designed to feel strange, dramatic, and memorable rather than practical. A participant can either choose tarot mode, where they present a tarot card and receive a random fortune linked to that card, or a yes/no/maybe mode, where they ask the bird a question and receive a mysterious spoken response. The project combines electronics, mechanics, coding, and sound design to create a playful interactive object with strong personality.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`We are creating a playful fortune-telling experience that feels theatrical, eerie, funny, and magical. The user interacts with the bird almost like it is a character rather than a machine.`

`We want the participant to feel curiosity, suspense, and delight. They should want to try it again because the outcome changes each time: different tarot fortunes can play for the same card, and the yes/no/maybe mode gives random answers that make the interaction feel unpredictable and alive.`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`We are designing this project as if we are a small creative studio making an interactive experience for  teens, adults, classmates, exhibition visitors, and a mixed audience.`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Toy / Object / Game]` | `Magic 8 Ball` | `Inspired the core interaction of asking a question and receiving a randomized, ambiguous answer that feels personally meaningful to the user.` |
| `[Practice / System]` | `Tarot Card Reading` | `Inspired the idea of symbolic cards and projection, where users interpret vague responses based on their own situation, making the experience feel personal.` |
| `[Toy / Machine / Installation]` | `Fortune telling machines and animatronic arcade characters` | `Inspired the physical interaction of a machine that “comes alive” and delivers spoken fortunes, and the importance of having a strong character.` |
| `[Video Game]` | `The Stanley Parable` | `Inspired the voice tone of a narrator that feels aware of the user and slightly comments on them, creating a psychological and humorous effect.` |
| `[Film]` | `Harry Potter and the Prisoner of Azkaban (Divination scenes)` | `Inspired the mystical, slightly dramatic tone and theatrical delivery of fortune-telling dialogue.` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`Our project combines physical interaction, character design, and psychological illusion. Unlike traditional fortune-telling systems, the vulture (Rune) acts as a character that observes and “reads” the user, making the interaction feel personal.`

`The original twist is combining a physical vulture puppet, RFID-triggered tarot card fortunes, and a second yes/no/maybe oracle mode in one character-driven system. Instead of a screen-based fortune app, the experience happens through a kinetic puppet that appears to wake up and speak to the user.`

`The use of RFID tarot cards creates a tangible ritual, while randomized audio responses make each interaction feel unique. The addition of movement synced with voice (beak, head, and eyes) enhances the illusion of life.`

`The project explores how vague, generalized statements can feel deeply personal when paired with performance, sound, and physical presence.`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`Short press → bird wakes up → question prompt plays → user asks a question → second press confirms → random yes/no/maybe answer plays → bird goes back to sleep`

`Long press -> bird wakes up -> tarot intro plays -> user places RFID card -> system reads card -> mapped random fortune plays -> bird goes back to sleep`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `Teens, young adults, and exhibition visitors` |
| Age range | `all ages above 13` |
| Solo or multiplayer | `Solo` |
| Expected duration of one round | `2 to 3 minutes` |
| What should the player feel? | `Curious, amused, slightly unsettled, and entertained` |
| Is explanation required before use? | `Very little explanation is needed if the interaction is labeled clearly` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

### Tarot Mode

1. **Approach:** `The player sees the vulture puppet in its idle resting state.`
2. **Start:** `The player presses and holds the switch to choose tarot mode.`
3. **First Action:** `The bird wakes up and plays an intro prompt.`
4. **Main Interaction:** `The player places one RFID tarot card on the reader.`
5. **System Response:** `The system reads the card UID, selects one mapped audio file at random, and the bird performs while the fortune plays.`
6. **Win / Lose / End Condition:** `The round ends when the fortune audio finishes.`
7. **Reset:** `The bird returns to its idle state and waits for the next player.`

### Magic 8 ball Mode

1. **Approach:** `The player sees the vulture puppet in its idle resting state.`
2. **Start:** `The player gives a short press on the switch to choose yes/no/maybe mode.`
3. **First Action:** `The bird wakes up and plays a question prompt.`
4. **Main Interaction:** `The player asks the bird a question out loud and then presses the switch again to confirm.`
5. **System Response:** `The system randomly selects and plays one answer audio such as yes, no, maybe, or idk while the bird performs.`
6. **Win / Lose / End Condition:** `The round ends when the answer audio finishes.`
7. **Reset:** `The bird immediately returns to idle without an outro.`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `Press and hold the switch for tarot mode.`
- `Press the switch briefly for yes/no/maybe mode.`
- `In tarot mode, place one RFID tarot card on the reader when prompted.`
- `In yes/no/maybe mode, ask a question and press the switch again for the answer.`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [x] `The bird begins in an idle state.`
- [x] `The switch reliably starts the interaction.`
- [x] `Tarot cards are detected and mapped to audio.`
- [x] `Audio plays reliably from the laptop.`
- [x] `The bird returns to idle after finishing a round.`
- [x] `The beak movement is more or less synced to the audio.`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`The minimum viable version is a working physical bird that wakes up on switch press, reads a tarot card UID, plays a mapped audio file, and returns to an idle state. Even without all movement fully refined, this still delivers the core experience of a speaking fortune-telling machine.`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `Dual interaction modes: tarot mode and yes/no/maybe mode`
- `Improved eye blinking and smoother character motion`
- `Stronger mechanical integration and cleaner final puppet finish`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [x] Mechanical
- [x] Sensor-based
- [ ] App-connected
- [x] Motorized
- [x] Sound-based
- [x] Light-based
- [ ] Screen/UI-based
- [x] Fabricated structure
- [x] Game logic based
- [x] Installation / tabletop experience
- [ ] Other: `Not applicable`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`The system takes input from a physical switch and an MFRC522 RFID reader. The ESP32 processes these inputs and controls the puppet’s motion using servo motors. Audio is handled by a laptop script connected over serial to the ESP32.`

`In tarot mode, the ESP32 waits for a card UID, sends a command to the laptop, and the laptop selects and plays one mapped audio file at random for that card. In yes/no/maybe mode, the ESP32 triggers a question prompt and later a random answer file. The outputs are head motion, eye motion, beak motion, and synchronized audio playback.`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `Limit switch` | Input | `Starts the interaction and is also used to confirm in yes/no mode` |
| `MFRC522 RFID reader` | Input | `Reads tarot card UID values` |
| `ESP32` | Processing | `Runs the interaction logic, motor control, and serial communication` |
| `Laptop Python script` | Processing / Output | `Plays audio files and sends amplitude values back for beak sync` |
| `Head servos` | Output | `Lift and lower the head` |
| `Beak servo` | Output | `Moves during speech` |
| `Eye servo` | Output | `Controls eye opening/closing and blinking` |
| `Puppet structure` | Physical Action | `Transforms servo motion into character performance` || `[Button / Sensor / Switch / App Input]` | Input | `[Describe]` |
| `[ESP32 / Controller]` | Processing | `[Describe]` |
| `LED` | Output | `Gives a visual signal during activation, mode feedback, or system state changes` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[Write here]` |
| Width | `[Write here]` |
| Height | `[Write here]` |
| Estimated weight | `[Write here]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [x] Linkages
- [x] Hinges
- [x] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [x] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`The project uses a puppet-like head assembly with moving eyes, beak, and head. Servo motors are attached to these moving parts through simple mechanical linkages. The head mechanism was later revised to use two servos instead of one because a single servo struggled under load.`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`The head moves up and down to create a wake-up and sleep effect. The beak opens and closes during audio playback to simulate speech. The eyes open when the bird wakes and can blink during speech. Problems encountered included servo load, mirrored movement requirements for dual head servos, hot servos under stress, and trial-and-error angle tuning once attached to the physical model.`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[Write here]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `ESP32` | `1` | `Main controller` |
| `MFRC522 RFID reader` | `1` | `Reads tarot cards` |
| `RFID cards` | `10` | `Trigger card-specific fortune audio` |
| `Servo motors` | `4` | `Head, beak, and eyes movement` |
| `Limit switch` | `1` | `Starts and confirms interaction` |
| `LM2596 buck converter` | `1` | `Provides regulated 5V to motors` |
| `Laptop speaker / Bluetooth speaker` | `1` | `Audio output` |
| `LED` | `1` | `Visual status indicator` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`The ESP32 is powered separately and communicates with the laptop over USB serial. The servo motors are powered from a 5V rail supplied by the LM2596 buck converter. The MFRC522 RFID reader is powered at 3.3V from the ESP32. All grounds are shared.`

`The RFID reader uses SPI connections. The limit switch is wired with the ESP32 internal pull-up enabled, so the pressed state reads low. The final working setup used two separate GPIO pins for the mirrored head servos, one GPIO for the beak servo, one for the eye servo, and one for the switch. An LED is connected as a visual output indicator for system state and feedback alongside the moving puppet parts and audio.`
`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `USB for ESP32 and laptop audio, LM2596-regulated 5V rail for motors` |
| Voltage required | `3.3V for MFRC522, 5V for servos` |
| Current concerns | `Servo current draw caused instability during some tests, especially under mechanical load` |
| Safety concerns | `Servos can overheat or stall if driven beyond their safe range or under too much force` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `MicroPython` | `ESP32 logic and hardware control` |
| `Thonny` | `Uploading and testing MicroPython code` |
| `Python on laptop` | `Serial communication and audio playback` |
| `ElevenLabs` | `Voice generation` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`The ESP32 code initializes the motors, RFID reader, and switch, then waits in an idle state. Depending on the switch press duration, it enters tarot mode or yes/no/maybe mode.`

`In tarot mode, the ESP32 wakes the puppet, asks for a card through audio, waits for an RFID UID, and then sends a command to the laptop to play one random mapped fortune. In yes/no/maybe mode, the ESP32 wakes the puppet, plays a question prompt, waits for a second confirmation press, and then triggers a random answer file. During audio playback, the laptop script sends live amplitude values back to the ESP32 so the beak motion can roughly sync to the audio.`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode

```text
start
initialize switch, servos, RFID, serial
set puppet to idle pose

loop forever
    wait for switch press
    measure press length

    if long press
        wake up bird
        play tarot intro
        wait for RFID card
        read UID
        send UID to laptop
        play mapped random fortune audio
        play outro
        return to idle

    else if short press
        wake up bird
        play question prompt
        wait for second switch press
        play random yes/no/maybe/idk answer
        return to idle
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [x] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Write here]`

## 12.3 Items to Purchase Separately
`We selected an ESP32 because it is flexible, easy to work with in MicroPython, and has enough GPIO for the project. Servo motors were chosen because they are simple to control for puppet-style motion. The MFRC522 was chosen because it allows each tarot card to act as a physical trigger with a unique UID. The LM2596 was used because the servo motors required a more stable 5V supply than the ESP32 could safely provide.`

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[Cost]` |
| Mechanical parts | `[Cost]` |
| Fabrication materials | `[Cost]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `[Cost]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Write here]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`We divided work based on strengths but kept testing and problem-solving collaborative. Mechanical and fabrication decisions were led by the teammate working more closely with the physical model, while electronics and code integration were led by the teammate working more closely with MicroPython and laptop scripting. Major decisions were tested physically before being accepted, especially when hardware behavior was uncertain.`

`We regularly adjusted the plan when parts failed or behaved differently than expected. The README acts as process documentation, not only a final summary, so major changes, failures, and fixes should be added as evidence of iteration.`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Name]` | `2` | `[Date]` | `None` | `To Do` |
| T2 | `[Complete BOM]` | `[Name]` | `1` | `[Date]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Name]` | `2` | `[Date]` | `T1` | `To Do` |
| T4 | `[Build structure]` | `[Name]` | `4` | `[Date]` | `T1` | `To Do` |
| T5 | `[Write control code]` | `[Name]` | `4` | `[Date]` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `[Name]` | `4` | `[Date]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Name]` | `2` | `[Date]` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `[Name]` | `3` | `[Date]` | `T7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Name]` | `[Name]` |
| Electronics | `[Name]` | `[Name]` |
| Coding | `[Name]` | `[Name]` |
| App | `[Name]` | `[Name]` |
| Mechanical build | `[Name]` | `[Name]` |
| Testing | `[Name]` | `[Name]` |
| Documentation | `[Name]` | `[Name]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [x] Key uncertainty identified
- [x] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [x] Electronics tests completed
- [x] CAD / structure planning completed
- [ ] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [ ] App connected if required
- [x] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready


## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `Finalize concept and decide the interaction style` | `The project direction became a tarot fortune-telling vulture puppet with sound, motion, and RFID card input.` | `The project moved away from being only a fortune teller and later expanded into a second yes/no/maybe mode.` | `Test the main electronics and confirm the sensing and audio approach.` |
| Week 2 | `Test subsystems like RFID, switch, servos, and audio` | `RFID card reading, switch detection, and laptop-based audio playback were all tested separately and working.` | `Audio playback was moved to the laptop instead of trying to do all playback directly on the ESP32.` | `Integrate hardware and start building the full interaction flow.` |
| Week 3 | `Integrate the physical puppet with the code and audio system` | `The full tarot loop started working, including card scan, random fortune playback, and synchronized beak movement.` | `Several mechanical issues appeared once the servos were attached to the real puppet, especially with the head and beak under load.` | `Stabilize the motion system and simplify any parts that are too risky.` |
| Week 4 | `Refine the final experience and add additional features` | `A yes/no/maybe oracle mode was added, motion ranges were tuned, and the project was adjusted around real component limits.` | `The head system was revised, dual head servos were tested, and the README/documentation became more process-focused.` | `Finalize the build, polish presentation, and complete missing documentation sections.` |

---

# 15. Risks and Unknowns

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `Servo stalls or overheats under puppet load` | `Technical / Mechanical` | `High` | `High` | `Reduce movement range, test parts separately, use safer fallback behavior, and disable motion if necessary.` | `Both` |
| `Head mechanism becomes unreliable when attached to the final model` | `Mechanical` | `High` | `High` | `Use two head servos, reduce speed, and simplify motion if needed.` | `Raavee Uttekar` |
| `RFID card detection becomes inconsistent in the full build` | `Technical` | `Medium` | `High` | `Keep card reading logic simple, test UID mapping repeatedly, and isolate reader wiring from motor noise.` | `Aditi Rathod` |
| `Power instability from running multiple servos together` | `Technical` | `High` | `High` | `Use the LM2596 5V power rail for motors, keep common ground, and avoid powering motors from the ESP32.` | `Both` |
| `Audio-beak sync fails during some files` | `Technical` | `Medium` | `Medium` | `Use amplitude-based sync from the laptop and keep a simpler fake-motion fallback if required.` | `Aditi Rathod` |
| `The final interaction is confusing for first-time users` | `Gameplay / Experience` | `Medium` | `Medium` | `Make the switch behavior clear and use spoken prompts to guide the user.` | `Both` |


## 15.2 Biggest Unknown Right Now

**Response:**  
`The single biggest uncertainty is how reliable the full mechanical system will be during repeated public use. The electronics and logic work perfectly, but will it be able to take the load after repeated usage throughout the day`


---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

# 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `Observe whether they can start a mode and complete a round without much explanation.` |
| Is the interaction satisfying? | `Watch for emotional reaction, attention, laughter, surprise, or repeated use.` |
| Do players want another turn? | `See whether they try both modes or scan multiple cards again.` |
| Is the challenge balanced? | `Check whether the yes/no mode and tarot mode both feel easy to understand but still mysterious.` |
| Is the response clear and immediate? | `Observe whether users notice the bird's motion, speech, and output as part of one connected experience.` |


## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Add actual date]` | `RFID reader was not detecting cards at first` | `Technical` | `Rechecked wiring, added the correct MFRC522 library, and tested with a dedicated card-reading script.` | `Worked` | `Store all card UIDs and map them to audio files.` |
| `[Add actual date]` | `The same card kept retriggering multiple fortune files` | `Technical` | `Added card locking and delayed removal logic so one scan would only trigger once.` | `Worked` | `Use the more stable card-read approach in the final interaction loop.` |
| `[Add actual date]` | `Beak moved during intro but not during fortune playback` | `Technical` | `Fixed the playback event reset logic in the laptop script so amplitude data was sent during every audio playback.` | `Worked` | `Keep amplitude-sync playback for all spoken audio.` |
| `[Add actual date]` | `Single head servo could lift the head in testing but failed under real load` | `Mechanical` | `Tested smaller movement ranges, considered a stepper motor, and later tried dual head servos.` | `Partly worked` | `Use the most reliable head movement setup for the final version.` |
| `[Add actual date]` | `Beak servo overheated during testing` | `Technical / Mechanical` | `Reduced range, slowed movement, added delay before beak movement, and treated the beak as optional until stable.` | `Partly worked` | `Monitor the beak carefully and keep a fallback option.` |
| `[Add actual date]` | `Eye testing caused unexpected movement in other servos` | `Technical / Wiring` | `Ran isolated test files and disconnected unrelated servo signal wires during testing.` | `Worked` | `Keep tests isolated and only reconnect parts during integration.` |
| `[Add actual date]` | `Needed an additional mode beyond tarot` | `Design / Gameplay` | `Added a yes/no/maybe mode triggered by short press, with tarot mode using long press.` | `Worked` | `Refine the spoken prompts and make the two modes clear to users.` |


## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `Classmate / peer` | `Tried starting the bird and using tarot mode` | `Needed a little explanation about long press vs short press` | `Enjoyed the dramatic audio and physical performance of the bird and shocked how much the reading resonated with me` | `Make the two modes more clearly signposted with prompts or labels` |
| `Classmate / peer` | `Tried yes/no mode and asked a spoken question` | `Was unsure when to press the switch again to confirm` | `Liked the random answer and character-based response` | `Strengthen the spoken prompt so the confirm step is clearer` |


---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`The project was built through repeated cycles of subsystem testing and physical integration. We began by testing the electronics independently on a breadboard: the RFID reader, the limit switch, and the servos were all tested with simple scripts before being combined into the main puppet logic. Once those tests worked, we connected the ESP32 to a laptop so the laptop could handle audio playback while the ESP32 focused on motion and interaction control.`

`As the puppet body was assembled, the project became more mechanical and iterative. Some servo movements that worked in isolated tests became unreliable once attached to the real head, beak, and eye mechanisms. This led to multiple revisions, including reducing movement ranges, slowing motion, testing separate files for individual parts, trying alternate hardware ideas, and eventually moving toward a dual-servo head setup. The fabrication process therefore involved not only assembly, but also adaptation based on physical stress, alignment, and load.`

`Wiring was also refined over time. The servo power was separated from the ESP32 logic supply using an LM2596 5V rail, while the RFID module remained on 3.3V. Common grounding was necessary for stability. The final build process therefore combined breadboard prototyping, motion testing, serial communication setup, and repeated mechanical adjustment rather than a single fixed assembly path.`

## 17.2 Build Photos

Add photos throughout the project.

Suggested images:
- early sketch
- prototype
- electronics testing
- mechanism test
- app screenshot if applicable
- final build

Example:

```md
![Concept sketch](images/concept-sketch.jpg)
![RFID testing](images/rfid-test.jpg)
![Dual head servo test](images/head-servo-test.jpg)
![Full puppet build](images/final-build.jpg)
```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Add date]` | `Basic RFID scanning and random tarot audio playback worked` | `To prove the core fortune-telling interaction was possible` |
| `v2` | `[Add date]` | `Added intro/outro flow and coordinated puppet motion` | `To make the system feel like a character instead of only a sensor trigger` |
| `v3` | `[Add date]` | `Added amplitude-based beak sync from laptop audio` | `To make speech motion feel more convincing` |
| `v4` | `[Add date]` | `Added short-press yes/no/maybe mode and long-press tarot mode` | `To increase replay value and create two different experiences in one project` |
| `v5` | `[Add date]` | `Revised head mechanism and tested safer motion setups` | `Because the original mechanical setup was unreliable under load` |


---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
- `The project creates a memorable character-based interaction instead of a generic sensor demo.`
- `RFID tarot mode works well as a physical ritual because the player must present a real card to the bird.`
- `Laptop-based audio playback made it easier to use rich sound files and synchronize the beak with speech.`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `Mechanical reliability is still the biggest challenge, especially under real puppet load.`
- `The eye mechanism needs more refinement and safe range tuning.`
- `The final user guidance could be clearer so first-time users instantly understand the two modes.`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`Our team worked well when dividing responsibilities by strength while still solving problems together. Coding, testing, electronics, and mechanical integration all influenced one another, so collaboration was important whenever a problem crossed between software and hardware. We were able to keep making progress because we treated testing as part of the design process instead of waiting for a perfect final build.`

`What slowed us down most was integration under real physical load. Several things that worked during isolated testing behaved differently once attached to the puppet body. This meant we had to revisit movement ranges, servo choices, and even interaction details. Time management improved once we started using simpler test scripts for each subsystem before putting everything back into the full project.`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
