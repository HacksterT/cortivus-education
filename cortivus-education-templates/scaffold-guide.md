# Scaffold & Package Guide

## Create a new topic (manual copy/rename)
1. Duplicate the folder structure below:
```
curricula/<topic-slug>/
├─ README.md                # from templates/LANDING_README_TEMPLATE.md
├─ curriculum.md            # from templates/CURRICULUM_TEMPLATE.md
├─ companion-checklist.md   # from templates/COMPANION_CHECKLIST_TEMPLATE.md
└─ assets/
```
2. Replace placeholders in each file:
   - <Topic Title>, tags, updated date
   - Fill Outcomes and Phases
3. Ensure `.github/ISSUE_TEMPLATE/phase-reflection.md` exists at repo root.

## Package as a ZIP (like the GCP IaC example)
- Create a ZIP that includes:
  - `curricula/<topic-slug>/` (the three files + assets)
  - `.github/ISSUE_TEMPLATE/phase-reflection.md`
- Name it: `<topic-slug>-learning-bundle.zip`

## Release checklist
- [ ] Landing page links work
- [ ] Phases concise (≤250 words/phase)
- [ ] Final Project deliverables clear
- [ ] Front matter `updated:` is today
