
# Cortivus Education

Public, lightweight curricula you can follow with an **AI Teacher**. Each guide is hands-on, split into short phases, and uses plain-language prompts and small activities (no code required in activities). You may need to tinker wiht the unstructions and/or prompts.  It does generate lint errors, but it does work.

## How to use

1. Pick a curriculum in `curricula/<topic>/`.
2. Read the **Overview** and **Learning Outcomes**.
3. For each phase: ask the AI Teacher the listed questions, complete the small activity, and write a brief reflection.
4. Share your progress (blog/LinkedIn) using the included `companion-post.md` as a starting point.

## Featured curricula

- [GCP Infrastructure as Code](curricula/gcp-iac/curriculum.md)

## Creating New Curricula

### Quick Start with AI Generation

Use the `make_curriculum_prompt.py` tool to generate a comprehensive prompt for AI-assisted curriculum creation:

```powershell
# Interactive mode (recommended)
python make_curriculum_prompt.py

# Command line mode
python make_curriculum_prompt.py --title "Learning Google Cloud Infrastructure as Code" --slug "gcp-iac-fundamentals" --description "Learn GCP IAC concepts and implementation" --expertise beginner
```

**Required Inputs:**

- **Title**: Full curriculum title (e.g., "Learning Google Cloud Infrastructure as Code")
- **Slug**: Kebab-case folder naming (e.g., "gcp-iac-fundamentals")
- **Description**: Topic/subject description and learning goals
- **Expertise Level**: `beginner`, `intermediate`, or `advanced`

**Expertise Levels:**

- `beginner` - Fundamentals with simple language and more context
- `intermediate` - Practical application assuming basic knowledge  
- `advanced` - Complex concepts assuming strong foundation

**Output**: Single comprehensive prompt file (`{slug}_curriculum_prompt.txt`) with three sequential phases for AI execution.

### Manual Creation

Use the templates in `cortivus-education-templates/` and follow the `scaffold-guide.md` for manual curriculum creation.

## Framework Structure

Each curriculum follows a **three-layer learning experience**:

- **Layer 1 — Landing Page** (`README.md`): Overview and navigation
- **Layer 2 — Core Curriculum** (`curriculum.md`): Step-by-step phases with AI prompts
- **Layer 3 — Companion Checklist** (`companion-checklist.md`): Quick reference prompts

### Phase Structure

Each learning phase includes:

- **Core Ideas** (3-5 bullet points)
- **Ask the AI Teacher** (2-3 natural language prompts)
- **Activity** (hands-on task, no code required)
- **Reflect** (self-assessment with GitHub issue integration)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

MIT — see [LICENSE](LICENSE).
