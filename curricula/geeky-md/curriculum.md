---
title: Python Basics for a Geeky Doctor — Interactive Curriculum
tags: [python, beginner, healthcare, medical, automation, data-processing]
updated: 2025-10-15
---

# Python Basics for a Geeky Doctor — Interactive Curriculum

> Work in **20–30 minute** sessions. For each phase: **Read Core Ideas → Ask the AI Teacher → Do the Activity → Reflect.**

## How to Use This Curriculum

1. **Set up your environment:** Install Python 3.12+ and a text editor (VS Code recommended)
2. **Work sequentially:** Complete phases 1-5 in order—each builds on previous concepts
3. **Use the AI Teacher prompts:** Copy the provided prompts to ChatGPT, Claude, or your preferred AI assistant
4. **Do the activities:** These are planning exercises (no coding required) to solidify understanding
5. **Reflect after each phase:** Answer the reflection question and log it using the GitHub issue template
6. **Take breaks:** Each phase is 20-30 minutes—don't rush through multiple phases at once

## Overview

This curriculum teaches Python fundamentals through a healthcare lens. You'll learn to automate medical data tasks, organize patient information, and build foundational coding skills—all without prior programming experience. Perfect for doctors, nurses, and healthcare researchers.

## Learning Outcomes

- Write and execute basic Python scripts to automate simple medical data tasks
- Apply Python data structures (lists, dictionaries) to organize patient information and medical records
- Use conditional logic and loops to process and filter healthcare datasets
- Read and manipulate CSV files containing medical data using Python's built-in libraries
- Debug common Python errors and use print statements to troubleshoot code issues

---

## Phase 1 — Python Fundamentals: Your First Medical Script

**Estimated time:** 25 minutes  
**Goal:** Successfully run your first Python script and understand basic syntax, variables, and print statements in a medical context.

### Phase 1 Core Ideas

- Python uses simple, readable syntax similar to writing instructions in plain English
- Variables store information (like patient names, ages, vital signs) for later use
- The `print()` function displays output to help you see what your code is doing
- Indentation and syntax matter—Python is precise about formatting
- Comments (using `#`) help document your code for future reference

### Phase 1 Ask the AI Teacher

**Copy these prompts to your AI assistant:**

> You are an expert in Python programming. I'm a healthcare professional learning Python basics as part of a structured curriculum.
>
> Please help me understand: What are variables in Python? Can you explain using a medical example like storing a patient's temperature?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm a healthcare professional learning Python basics as part of a structured curriculum.
>
> Please help me understand: How do I write my first Python script that prints a welcome message for a medical clinic? Walk me through each line.
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm a healthcare professional learning Python basics as part of a structured curriculum.
>
> Please help me understand: What's the difference between strings, integers, and floats? Give me examples using medical data like patient age and blood pressure.
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

### Phase 1 Activity (no code)

Describe a simple Python script that would store and display a patient's basic information (name, age, blood pressure, temperature). Write out in plain English what each line would do, what variables you'd need, and what the output should look like.

**What Good Looks Like:**

Your description should include:

- Variable names (e.g., `patient_name`, `age`, `blood_pressure`)
- Data types for each variable (string, integer, float)
- What the print statements would display
- Example output format

**Success Criteria:**

- You can explain what a variable does
- You understand the difference between strings and numbers
- You can describe the flow of a simple script from top to bottom

### Phase 1 Reflect

What medical task in your daily work could benefit from storing and displaying information automatically?

**Reflection Template:**

- Task description:
- Information that would be stored:
- How automation would save time:

---

## Phase 2 — Data Structures for Healthcare Information

**Estimated time:** 25 minutes  
**Goal:** Organize complex medical information using lists and dictionaries to represent patients, medications, and test results.

### Phase 2 Core Ideas

- Lists store ordered collections (like a patient's medication list or vital sign readings over time)
- Dictionaries store key-value pairs (like patient_id: patient_details) for quick lookups
- You can nest data structures (a list of dictionaries) to represent complex medical records
- Accessing data uses bracket notation: `patient["name"]` or `medications[0]`
- Lists and dictionaries are mutable—you can add, remove, or update entries

### Phase 2 Ask the AI Teacher

**Copy these prompts to your AI assistant:**

> You are an expert in Python programming. I'm learning about data structures as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: How would I use a Python dictionary to represent a patient's complete medical record with multiple fields?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm learning about data structures as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: What's the best way to store a list of patients where each patient has multiple attributes? Should I use a list of dictionaries?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm learning about data structures as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: Can you show me how to access and update a specific patient's blood pressure reading in a nested data structure?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

### Phase 2 Activity (no code)

Design the data structure for a small clinic's patient database. Describe how you would organize information for 3 patients, each with: name, age, diagnosis, medications (list of 2-3), and last visit date. Write out what the structure would look like and how you would access specific information (e.g., "get the second medication for patient 1").

**What Good Looks Like:**

Your design should show:

- A list containing 3 patient dictionaries
- Each dictionary with keys: name, age, diagnosis, medications, last_visit
- The medications value as a list
- Clear notation for accessing nested data (e.g., `patients[0]["medications"][1]`)

**Success Criteria:**

- You understand when to use lists vs. dictionaries
- You can describe nested data structures
- You can explain how to access specific values in complex structures

**Common Confusion Points:**

- Lists use numeric indexes [0, 1, 2], dictionaries use keys ["name", "age"]
- Square brackets are used for both, but the content differs
- Nesting means "a structure inside a structure"

### Phase 2 Reflect

How could organizing data in dictionaries and lists make it easier to find and update patient information compared to paper records?

**Reflection Template:**

- Advantage 1:
- Advantage 2:
- One challenge I foresee:

---

## Phase 3 — Control Flow: Making Decisions with Patient Data

**Estimated time:** 25–30 minutes  
**Goal:** Use if/else statements and loops to process patient data, filter results, and make automated decisions based on medical criteria.

### Phase 3 Core Ideas

- `if/elif/else` statements let your code make decisions based on conditions (e.g., flag high blood pressure)
- Comparison operators (`>`, `<`, `==`, `!=`) check values against medical thresholds
- `for` loops iterate through lists of patients or test results to process each one
- `while` loops continue until a condition is met (useful for data validation)
- Combining conditions with `and`/`or` handles complex medical criteria

### Phase 3 Ask the AI Teacher

**Copy these prompts to your AI assistant:**

> You are an expert in Python programming. I'm learning about control flow (if statements and loops) as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: How do I write an if statement to check if a patient's temperature is above 100.4°F and flag them for fever?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm learning about control flow (if statements and loops) as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: Can you explain how to use a for loop to go through a list of 10 patients and print only those with high blood pressure?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm learning about control flow (if statements and loops) as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: What's the best way to validate user input, like making sure an age is a positive number?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

### Phase 3 Activity (no code)

Describe the logic for a triage system that processes a list of patients and categorizes them as "urgent," "moderate," or "routine" based on their vital signs (temperature, heart rate, blood pressure). Write out the decision criteria, how you'd loop through patients, and what the output would show.

**What Good Looks Like:**

Your description should include:

- Specific thresholds for each category (e.g., temp > 103°F = urgent)
- The loop structure (for each patient in the list...)
- The decision tree (if condition A, then urgent; elif condition B, then moderate; else routine)
- Expected output format

**Success Criteria:**

- You can define clear decision criteria using comparison operators
- You understand how loops process each item in a list
- You can describe nested conditions (checking multiple vital signs)

**Common Confusion Points:**

- `=` assigns a value, `==` checks equality
- Indentation matters—code inside if/for blocks must be indented
- `elif` is "else if"—it only runs if previous conditions were false

### Phase 3 Reflect

What repetitive decision-making task in your medical practice could be automated with conditional logic?

**Reflection Template:**

- Task description:
- Decision criteria:
- Expected time savings:

---

## Phase 4 — File Handling: Working with Medical Records

**Estimated time:** 25 minutes  
**Goal:** Read data from CSV files, process it with Python, and write results back to files—essential for working with exported medical records.

### Phase 4 Core Ideas

- CSV (Comma-Separated Values) files are common for exporting patient data from medical systems
- Python's `csv` module or `open()` function reads and writes files
- Always close files after use (or use `with` statement for automatic cleanup)
- File paths specify where to find or save data on your computer
- Error handling (`try/except`) prevents crashes when files are missing or corrupted

### Phase 4 Ask the AI Teacher

**Copy these prompts to your AI assistant:**

> You are an expert in Python programming. I'm learning about file handling as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: How do I read a CSV file containing patient data and convert it into a list of dictionaries in Python?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm learning about file handling as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: What's the safest way to write processed patient data back to a new CSV file without losing the original?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm learning about file handling as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: Can you explain how to handle errors when a file doesn't exist or has the wrong format?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

### Phase 4 Activity (no code)

Plan a script that reads a CSV file of patient lab results (columns: patient_id, test_name, result_value, normal_range), identifies abnormal results, and writes those to a new CSV file called "flagged_results.csv". Describe the steps: opening the file, reading each row, checking if results are abnormal, and writing output.

**What Good Looks Like:**

Your plan should include:

- Step 1: Open the input CSV file
- Step 2: Read each row and store in a data structure
- Step 3: For each result, compare result_value to normal_range
- Step 4: If abnormal, add to flagged list
- Step 5: Write flagged list to new CSV file
- Step 6: Close both files

**Success Criteria:**

- You understand the file open/read/write/close cycle
- You can describe how to iterate through CSV rows
- You know to create a new file rather than overwriting the original

**Common Confusion Points:**

- File paths: Use absolute paths (C:\...) or relative paths (./data/file.csv)
- The `with` statement automatically closes files—this is best practice
- CSV rows are read as strings—you may need to convert to numbers for comparisons

### Phase 4 Reflect

How would being able to process CSV files of medical data save you time compared to manual review?

**Reflection Template:**

- Current manual process:
- Automated process benefits:
- Data volume that would benefit most:

---

## Phase 5 — Putting It Together: A Mini Medical Data Pipeline

**Estimated time:** 30 minutes  
**Goal:** Combine all learned skills to build a complete workflow that reads, processes, filters, and outputs medical data.

### Phase 5 Core Ideas

- Real-world scripts combine file I/O, data structures, loops, and conditionals
- Breaking complex tasks into functions makes code reusable and organized
- Testing with small sample data helps catch errors before processing large datasets
- Documentation (comments and docstrings) helps others understand your medical logic
- Version control and backups protect your work and data

### Phase 5 Ask the AI Teacher

**Copy these prompts to your AI assistant:**

> You are an expert in Python programming. I'm learning about building complete workflows as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: How do I organize a Python script that reads patient data, filters it, and generates a summary report?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm learning about building complete workflows as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: What's the best way to test my medical data processing script with sample data before using real patient files?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

> You are an expert in Python programming. I'm learning about building complete workflows as part of a structured curriculum on Python for healthcare.
>
> Please help me understand: Can you help me understand how to break down a complex medical workflow into smaller, manageable functions?
>
> Provide a clear explanation with practical examples, and ask me a follow-up question to check my understanding.

### Phase 5 Activity (no code)

Design a complete workflow for a "Daily Patient Summary" system. It should: (1) read today's patient visit data from a CSV, (2) categorize patients by department, (3) count visits per department, (4) identify any patients with abnormal vitals, and (5) write a summary report. Describe each step, what data structures you'd use, and what the final output would contain.

**What Good Looks Like:**

Your workflow design should include:

- Input: CSV file structure (columns needed)
- Step-by-step process with data structures at each stage
- Functions you would create (e.g., `read_patient_data()`, `categorize_by_department()`, `check_vitals()`, `generate_report()`)
- Output: Summary report format (what information, how organized)
- Error handling considerations

**Success Criteria:**

- You can break a complex task into logical steps
- You understand how data flows through the pipeline
- You can identify where to use lists, dictionaries, loops, and conditionals
- You consider edge cases (missing data, file errors)

**Common Confusion Points:**

- Start with the end goal (report format) and work backwards
- Each function should do ONE thing well
- Test each function separately before combining
- Use descriptive variable and function names

### Phase 5 Reflect

Looking back at all five phases, what's one medical data task you feel confident you could now automate with Python?

**Reflection Template:**

- Task I want to automate:
- Skills from which phases I'll use:
- My next step to make this real:

---

## Final Project

Choose one capstone project that stitches all phases together. This is a planning exercise—describe your approach without writing code.

### Capstone Options

**Option 1: Patient Appointment Reminder System**

Design a system that reads a CSV of appointments and identifies which patients need reminders based on date criteria. Describe the logic flow, data structure, and output format.

**Option 2: Medication Inventory Tracker**

Plan a medication inventory tracker that processes a list of medications, tracks quantities, and flags items below reorder thresholds. Outline the data organization, filtering logic, and reporting approach.

**Option 3: Symptom Checker Data Processor**

Create a symptom checker data processor that takes patient symptom inputs and categorizes them by severity or system. Describe the categorization logic, data validation, and output structure.

### Deliverables

- **1-page write-up** describing your chosen project, including:
  - Problem statement: What medical task are you solving?
  - Data structure: How will you organize the information?
  - Logic flow: Step-by-step process (read → process → output)
  - Expected output: What does the final result look like?
- **List of resources/decisions** and why you made them:
  - What data structures (lists, dictionaries, nested structures)?
  - What control flow (if/else, loops)?
  - What file operations (read CSV, write results)?
- **Three lessons learned** from completing this curriculum:
  - One technical insight
  - One practical application to your medical work
  - One area you want to explore further

**Success Criteria:**

- Your design uses concepts from all 5 phases
- The workflow is logical and complete
- You can explain your decisions
- The project solves a real medical data problem
