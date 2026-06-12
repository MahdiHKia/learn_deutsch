# German A1 — my private course (run with Claude Code)

A self-contained, file-based system for learning German A1 one lesson at a time,
where each lesson is a fresh session and progress lives in version-controlled files.

## How to use

1. Open the **Claude Code** desktop app in this folder (`german-a1/`).
2. Pick the **Sonnet** model (faster, snappier for back-and-forth drilling).
3. Start a lesson by saying: **"Start Lesson 1"** (or just "let's do the next lesson").
   - Claude reads `CLAUDE.md`, `course-structure.md`, `progress.md`,
     `learner-profile.md`, and the one lesson file — nothing else.
4. Learn. Claude teaches, you produce German, it corrects you.
5. When you're done, say **"wrap up"**. Claude updates the progress/profile/log
   files, fills the lesson summary, and commits.

Next time, open a **new session** for the next lesson. Old conversations stay out
of context on purpose — what carries forward is the distilled state files.

## Files

| File | What it is |
|------|------------|
| `CLAUDE.md` | The rules Claude follows every session (the ritual). |
| `course-structure.md` | The full 16-lesson A1 syllabus (static). |
| `progress.md` | Where I am, per lesson. Updated each session. |
| `learner-profile.md` | Distilled memory about me as a learner. |
| `study-log.md` | Append-only record of every session. |
| `lessons/lesson-NN.md` | One plan per lesson + its post-session summary. |

## First step before Lesson 1
Open `learner-profile.md` and fill in the "About me" blanks (native language,
why you're learning, time per session). Or just tell Claude at the start of
Lesson 1 and let it write them in.

## Browsing past sessions
Sessions are saved per folder. Run `claude --resume` here to see and reopen any
past lesson conversation. Naming sessions per lesson keeps the picker clean.
Your durable progress, though, is the committed files + the git log.
