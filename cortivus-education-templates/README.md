# Cortivus Education — Templates Guide
_Use these templates to create a complete, three-layer curriculum in ~30 minutes._

**Three layers per topic**
1) **Landing Page** — orientation + progress tracker (`README.md` in the topic folder)
2) **Core Curriculum** — step‑by‑step phases with prompts and activities (`curriculum.md`)
3) **Companion Checklist** — one‑page quick prompts (`companion-checklist.md`)

**Extras**
- GitHub Issue template for reflections
- Consistent front matter (title, tags, updated date)
- Release checklist to package a ZIP like the GCP IaC example

---

## 1) Naming & folders (5 min)
Create a folder: `curricula/<topic-slug>/`  
Examples: `terraform-foundations`, `ai-learning-framework`

Inside it, you’ll add:
```
curricula/<topic-slug>/
├─ README.md                # Landing Page (use LANDING_README_TEMPLATE.md)
├─ curriculum.md            # Core Curriculum (use CURRICULUM_TEMPLATE.md)
├─ companion-checklist.md   # Companion Checklist (use COMPANION_CHECKLIST_TEMPLATE.md)
└─ assets/                  # (optional) images/diagrams
```
Also copy `.github/ISSUE_TEMPLATE/phase-reflection.md` to your repo root (if not present).

---

## 2) Fill the Landing Page (7 min)
Open **LANDING_README_TEMPLATE.md** and replace:
- `<Topic Title>`
- Update bullets under **Learning Outcomes**
- Keep the links to `curriculum.md` and `companion-checklist.md`
- Today’s date in `updated:` field

Goal: A skimmable entry point + progress tracker.

---

## 3) Build the Core Curriculum (12–15 min)
Open **CURRICULUM_TEMPLATE.md** and:
- Add a 1–2 sentence **Overview**
- Define **3–5 Learning Outcomes**
- Complete **Phases 1–5** using this structure per phase:
  - **Estimated time** (20–30 minutes)
  - **Goal** (outcome for the phase)
  - **Core Ideas** (3–5 bullets)
  - **Ask the AI Teacher** (2–3 prompts)
  - **Activity (no code)** (one small task learners can plan/describe)
  - **Reflect** (one question; point to reflection issue template)
- Add a **Final Project** with concrete deliverables

Keep language action‑oriented and tool‑agnostic unless essential.

---

## 4) Add the Companion Checklist (3–5 min)
Open **COMPANION_CHECKLIST_TEMPLATE.md** and condense each phase to three bullets:
- **Ask** (the prompts)
- **Activity** (short task)
- **Reflect** (one question)

This is the learner’s “quick view.”

---

## 5) Enable Reflections (2 min)
If not already present in your repo, copy `.github/ISSUE_TEMPLATE/phase-reflection.md`.  
Learners will click **New Issue → Phase Reflection** to journal insights.

---

## 6) Release checklist (3–5 min)
- [ ] All files have updated front matter with today’s date
- [ ] Internal links work (`README.md` → `curriculum.md` → back links)
- [ ] Phases fit in ~1 screen each (≤250 words/phase)
- [ ] Final Project deliverables are clear
- [ ] Commit your changes

**Optional ZIP:** If you want a downloadable bundle like our GCP IaC example, create a ZIP from the `curricula/<topic-slug>/` folder plus `.github/ISSUE_TEMPLATE/phase-reflection.md`.

---

## 7) Promoting your curriculum
Use `COMPANION_POST_TEMPLATE.md` as a short LinkedIn post. Put the repo (or site) link in the first comment.
