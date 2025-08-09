
# Contributing Guide

Thanks for your interest in improving Cortivus Education!

## What belongs here
- Concise, **interactive curricula** in Markdown
- Small, 20–30 minute phases with **Ask the AI Teacher** prompts
- **Activities without code** (describe steps; implementation can be added later)

## How to contribute
1. Create a new folder under `curricula/<topic-slug>/`.
2. Start from `templates/CURRICULUM_TEMPLATE.md` and copy it to `curricula/<topic-slug>/curriculum.md`.
3. (Optional) Add a short `companion-post.md` using the template.
4. Include any images in `curricula/<topic-slug>/assets/` (SVG/PNG) and reference them relatively.
5. Open a Pull Request with a clear title and summary of changes.

## Style guide
- Audience: self-learners and teams
- Tone: practical, encouraging, concise
- Keep each phase to **one screen** (approx. 150–250 words)
- Use action verbs and natural-language prompts
- Avoid tool-specific code unless strictly necessary (link out instead)

## Front matter
Each curriculum begins with YAML front matter:
```
---
title: <Topic Title> — Interactive Curriculum
tags: [<tag1>, <tag2>, <tag3>]
updated: YYYY-MM-DD
---
```

## PR checklist
- [ ] Clear learning outcomes
- [ ] Each phase has: Goal, Core Ideas, Ask the AI Teacher, Activity, Reflect
- [ ] Final Project defined with deliverables
- [ ] Spelling/grammar checked
