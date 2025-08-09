#!/usr/bin/env python3
import argparse, datetime, sys

def parse_args():
    p = argparse.ArgumentParser(description="Generate an AI prompt for a Cortivus Education curriculum package.")
    p.add_argument("--title", help="Topic title (e.g., 'Learning Google Cloud Infrastructure as Code')")
    p.add_argument("--slug", help="Kebab-case slug for folder/file naming (e.g., 'gcp-iac-fundamentals')")
    p.add_argument("--description", help="Description of the topic/subject to create curriculum for")
    p.add_argument("--expertise", help="Target expertise level", choices=["beginner", "intermediate", "advanced"])

    p.add_argument("--include_post", action="store_true", help="Include a companion social post in the prompt")
    p.add_argument("--out", help="Output .txt path", default="")
    args = p.parse_args()

    if not args.title:
        print("Enter the curriculum title (e.g., 'Learning Google Cloud Infrastructure as Code'):")
        args.title = input("> ").strip()
    
    if not args.slug:
        print("Enter kebab-case slug for folder/file naming (e.g., 'gcp-iac-fundamentals'):")
        args.slug = input("> ").strip()
    
    if not args.description:
        print("Enter a description of the topic/subject to create curriculum for:")
        args.description = input("> ").strip()
    
    if not args.expertise:
        print("Select target expertise level (beginner/intermediate/advanced):")
        args.expertise = input("> ").strip().lower()
        if args.expertise not in ["beginner", "intermediate", "advanced"]:
            args.expertise = "beginner"

    return args

def build_prompt(args):
    today = datetime.date.today().isoformat()
    return build_complete_prompt(args, today)

def build_complete_prompt(args, today):
    prompt = (
f"""You are an expert curriculum designer working with the Cortivus Education framework. This is a PHASED approach to create a complete learning package.

TOPIC DESCRIPTION: {args.description}
TARGET EXPERTISE LEVEL: {args.expertise.title()}

REFERENCE TEMPLATES (study these structures carefully):
- Landing Page: C:\\Projects\\cortivus-education\\cortivus-education-templates\\LANDING_README_TEMPLATE.md
- Core Curriculum: C:\\Projects\\cortivus-education\\cortivus-education-templates\\CURRICULUM_TEMPLATE.md  
- Companion Checklist: C:\\Projects\\cortivus-education\\cortivus-education-templates\\COMPANION_CHECKLIST_TEMPLATE.md
- Social Post: C:\\Projects\\cortivus-education\\cortivus-education-templates\\COMPANION_POST_TEMPLATE.md

- Scaffold Guide: C:\\Projects\\cortivus-education\\cortivus-education-templates\\scaffold-guide.md

EXAMPLE REFERENCE: Study the existing GCP-IAC curriculum at C:\\Projects\\cortivus-education\\curricula\\gcp-iac\\ for quality standards.

PHASE 1: CURRICULUM PLANNING & STRUCTURE
Using the provided title and slug, create the remaining foundational elements that will work with the template structure:

**GIVEN INFORMATION:**
- **Topic Title**: {args.title}
- **Slug**: {args.slug}

**CREATE THESE ELEMENTS:**
1. **Learning Outcomes**: Develop 5 specific, measurable outcomes that learners can achieve
2. **Phase Titles**: Design 5 progressive phase titles that build logically (20-30 min each)
3. **Tags**: Choose 4-6 relevant tags (e.g., gcp, iac, cloud, terraform, beginner)
4. **Target Audience**: Define who this is for based on {args.expertise} level
5. **Capstone Options**: Suggest 2-3 hands-on project options (NO CODE required)

IMPORTANT PHASE STRUCTURE REQUIREMENTS:
Each phase must include:
- **Goal**: What success looks like for that phase
- **Core Ideas**: 3-5 bullet points of key concepts
- **Ask the AI Teacher**: 2-3 natural language prompts for learners to ask
- **Activity**: Hands-on task (planning/describing, NO CODE)
- **Reflect**: 1 question for self-assessment

OUTPUT FORMAT FOR PHASE 1:
```
## CURRICULUM STRUCTURE

**Topic Title:** {args.title}
**Slug:** {args.slug}
**Expertise Level:** {args.expertise.title()}
**Updated:** {today}

**Learning Outcomes:**
- [Specific, measurable outcome 1]
- [Specific, measurable outcome 2] 
- [Specific, measurable outcome 3]
- [Specific, measurable outcome 4]
- [Specific, measurable outcome 5]

**Phase Progression:**
1. Phase 1 — [Foundation/Basics title]
2. Phase 2 — [Building on Phase 1]
3. Phase 3 — [Intermediate concepts]
4. Phase 4 — [Advanced application]
5. Phase 5 — [Integration/Complex scenarios]

**Tags:** [tag1, tag2, tag3, tag4, tag5, tag6]
**Target Audience:** [Specific description for {args.expertise} level learners]

**Capstone Options:**
- Option 1: [Hands-on project description - no code]
- Option 2: [Alternative project description - no code]
- Option 3: [Third option description - no code]
```

EXPERTISE LEVEL GUIDANCE:
- **Beginner**: Start with fundamentals, use simple language, provide more context, assume no prior knowledge
- **Intermediate**: Assume basic knowledge, focus on practical application, bridge theory to practice
- **Advanced**: Dive deeper into complex concepts, assume strong foundation, focus on optimization and best practices

QUALITY STANDARDS:
- Learning outcomes must be specific and measurable (use action verbs)
- Phase titles should build progressively and logically
- Each phase should take 20-30 minutes to complete
- Capstone projects should synthesize knowledge from all phases
- Content appropriate for {args.expertise} level learners
- Activities must contain NO CODE - only descriptions, planning, or conceptual tasks
- All phases should include meaningful reflection questions

---

STOP HERE FOR PHASE 1. Wait for approval before proceeding to Phase 2 (file creation).

═══════════════════════════════════════════════════════════════════════════════

PHASE 2: CREATE CURRICULUM FILES
Using the approved structure from Phase 1, create the three main curriculum files using the templates as your foundation.

REFERENCE THE APPROVED STRUCTURE from Phase 1 and use these templates:
- Landing Page Template: C:\\Projects\\cortivus-education\\cortivus-education-templates\\LANDING_README_TEMPLATE.md
- Core Curriculum Template: C:\\Projects\\cortivus-education\\cortivus-education-templates\\CURRICULUM_TEMPLATE.md  
- Companion Checklist Template: C:\\Projects\\cortivus-education\\cortivus-education-templates\\COMPANION_CHECKLIST_TEMPLATE.md

CREATE THESE FILES (output as separate markdown code blocks):

1) **PATH: curricula/{args.slug}/README.md** (Landing Page)
   - Use LANDING_README_TEMPLATE.md as foundation
   - Replace all placeholders with your generated content from Phase 1
   - Title should be: "{args.title} — Learning Path (Landing Page)"
   - Include all 5 learning outcomes from Phase 1
   - Add progress tracker for all 5 phases
   - Ensure all links are correct

2) **PATH: curricula/{args.slug}/curriculum.md** (Core Curriculum)  
   - Use CURRICULUM_TEMPLATE.md as foundation
   - Title should be: "{args.title} — Interactive Curriculum"
   - Fill in all 5 phases with detailed content from Phase 1 structure
   - Each phase needs: Goal, Core Ideas (3-5 bullets), AI Teacher prompts (2-3), Activity (no code), Reflect
   - Add your capstone options to Final Project section
   - Keep each phase ≤250 words

USABILITY REQUIREMENTS FOR CURRICULUM.MD:
- Add clear "How to Use This Curriculum" section at the top with numbered steps
- Format AI Teacher prompts as copy-paste ready with full context setup
- Use this format for AI Teacher prompts:
  ```
  ### Phase X Ask the AI Teacher
  
  **Copy this prompt to your AI assistant:**
  
  > You are an expert in [topic]. I'm learning about [phase topic] as part of a structured curriculum. 
  > 
  > Please help me understand: [question]
  > 
  > Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.
  ```
- Add reflection templates users can fill out with specific prompts
- Include "What Good Looks Like" examples for activities
- Provide clear success criteria for each phase
- Add troubleshooting tips for common confusion points

3) **PATH: curricula/{args.slug}/companion-checklist.md** (Companion Checklist)
   - Use COMPANION_CHECKLIST_TEMPLATE.md as foundation  
   - Title should be: "{args.title} — Companion Checklist"
   - Create quick prompts for each of the 5 phases
   - Include capstone deliverables section

FORMAT REQUIREMENTS:
- Output each file as a separate markdown code block
- Prefix with exact PATH comment
- Example:
  <!-- PATH: curricula/{args.slug}/README.md -->
  ```markdown
  [file contents here]
  ```

MARKDOWN FORMATTING REQUIREMENTS (to prevent lint errors):
- Use only ONE H1 heading per file (the main title)
- Use H2 for major sections, H3 for subsections within phases
- Add blank lines before AND after all headings
- Add blank lines before AND after all lists
- Use proper H3 headings (###) instead of bold text (**text**) for subsections
- Make ALL headings unique - add phase numbers to subsection headings (e.g., "### Phase 1 Core Ideas", "### Phase 2 Core Ideas")
- Ensure consistent spacing throughout

QUALITY CHECKS:
- All internal links between files work correctly
- Front matter includes correct title, tags, and updated date
- Content is appropriate for {args.expertise} level
- Activities contain NO code - only descriptions/planning tasks
- Each phase builds logically on previous phases
- Markdown follows linting standards (no MD022, MD032, MD036, MD025 errors)

---

STOP HERE FOR PHASE 2. Wait for approval before proceeding to Phase 3 (companion post).

═══════════════════════════════════════════════════════════════════════════════

PHASE 3: CREATE COMPANION POST & FINALIZE
Create the optional social media companion post and provide final packaging instructions.

REFERENCE TEMPLATE:
- Social Post Template: C:\\Projects\\cortivus-education\\cortivus-education-templates\\COMPANION_POST_TEMPLATE.md
- Scaffold Guide: C:\\Projects\\cortivus-education\\cortivus-education-templates\\scaffold-guide.md

CREATE THIS FILE:

**PATH: curricula/{args.slug}/companion-post.md** (Social Media Post)
- Use COMPANION_POST_TEMPLATE.md as foundation
- Title should be: "{args.title} — What I'm Learning This Month"
- Write engaging 3-5 sentence description of the curriculum
- Highlight key phases and learning outcomes from Phase 1
- Target {args.expertise} level learners specifically
- Include relevant hashtags for the topic
- Make it shareable and encouraging

FORMAT:
<!-- PATH: curricula/{args.slug}/companion-post.md -->
```markdown
[file contents here]
```

FINAL PACKAGING INSTRUCTIONS:
Following the scaffold-guide.md approach, the complete curriculum package should include:

**File Structure:**
```
curricula/{args.slug}/
├─ README.md                # Landing page (from Phase 2)
├─ curriculum.md            # Core curriculum (from Phase 2)  
├─ companion-checklist.md   # Quick checklist (from Phase 2)
├─ companion-post.md        # Social post (from Phase 3)
└─ assets/                  # (empty folder for future resources)
```

**Additional Resources:**
- Empty `assets/` folder for future curriculum resources

**Release Checklist:**
- [ ] All internal links work correctly
- [ ] Each phase is ≤250 words
- [ ] Front matter updated dates are correct
- [ ] Activities contain no code
- [ ] Content appropriate for {args.expertise} level
- [ ] Learning outcomes are specific and measurable

CURRICULUM COMPLETE! Ready for learners to use with their AI Teacher.

The AI should create these files directly in the IDE with write access to the project folders.
"""
    )
    return prompt.strip()

def main():
    args = parse_args()
    prompt_text = build_prompt(args)
    # Use slug for filename and save to prompts folder
    out = args.out or f"prompts/{args.slug}_curriculum_prompt.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(prompt_text)
    print(f"Prompt saved to: {out}")

if __name__ == "__main__":
    main()
