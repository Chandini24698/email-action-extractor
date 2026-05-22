# 📧 Email Action Items Extractor

Extract structured action items from email text using Claude API.

## What This Does

Takes raw email text and uses Claude AI to:
- ✅ Identify all action items
- ✅ Extract assignees
- ✅ Determine deadlines
- ✅ Assess priority levels
- ✅ Return structured JSON output

**Example Input:**
```
Hi Team, Sarah needs to finalize the budget by Friday. Marketing should prepare slides by next Wednesday. Dev team, update API docs ASAP.
```

**Example Output:**
```json
{
  "email_summary": "Q2 planning meeting with action items for budget, marketing slides, and API documentation.",
  "action_items": [
    {
      "action": "Finalize budget spreadsheet",
      "assignee": "Sarah",
      "deadline": "Friday (May 24th)",
      "priority": "High",
      "details": "Needed for board meeting"
    },
    {
      "action": "Prepare product roadmap slides",
      "assignee": "Marketing team (Jessica, Mike)",
      "deadline": "Next Wednesday",
      "priority": "Medium",
      "details": ""
    },
    {
      "action": "Update API documentation",
      "assignee": "Dev team",
      "deadline": "ASAP",
      "priority": "High",
      "details": "Blocking partner integrations"
    }
  ],
  "total_items": 3
}
```

---

## Quick Start

### 1. Clone and Setup
```bash
git clone <your-repo-url>
cd email-action-extractor
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Add Your Claude API Key
Get your key from: https://console.anthropic.com/keys

Create `.env` file:
```
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

### 3. Run the Demo
```bash
python3 email_action_extractor.py
```

You'll see:
- Sample email processed
- Extracted action items displayed
- Results saved to `action_items.json`

---

## How It Works

### Architecture
```
Raw Email Text
    ↓
Send to Claude API with structured prompt
    ↓
Claude extracts action items in JSON format
    ↓
Python parses and displays results
    ↓
Save to file for further processing
```

### The Claude Prompt
The script uses a **system prompt** that tells Claude exactly:
- What information to extract
- How to structure the output (JSON format)
- What fields are required
- How to handle missing data

This is **prompt engineering** — the skill Eternity is hiring for.

### Error Handling
The code handles:
- Claude returning JSON in markdown code blocks
- Invalid responses
- API errors
- File I/O errors

---

## How To Use With Real Emails

### Option 1: Copy-Paste
Edit `email_action_extractor.py`, replace `sample_email` with your actual email:

```python
sample_email = """
Your actual email here...
"""
```

Then run:
```bash
python3 email_action_extractor.py
```

### Option 2: Command-Line Input (Advanced)
Modify the script to accept file input:

```python
# Instead of sample_email, read from file:
with open('email.txt', 'r') as f:
    email_text = f.read()
```

### Option 3: Extend as a Function
Import and use in other projects:

```python
from email_action_extractor import extract_action_items

result = extract_action_items("Your email text here")
print(result)
```

---

## What You're Learning

### 🔴 Claude API
- ✅ How to authenticate with API key
- ✅ How to send messages to Claude
- ✅ How to parse structured responses
- ✅ Error handling with API responses

### 🔴 Prompt Engineering
- ✅ System prompts (define behavior)
- ✅ Structured output (JSON format)
- ✅ Edge case handling (missing data)
- ✅ Iterative refinement (making prompts better)

### 🔴 Python Development
- ✅ Virtual environments and dependencies
- ✅ Working with APIs (requests/responses)
- ✅ JSON parsing and manipulation
- ✅ Error handling and debugging
- ✅ Code structure and functions

### 🔴 Real-World Patterns
- ✅ This is exactly how Eternity will ask you to work
- ✅ Identify a business problem → build automation
- ✅ Call Claude API to process data
- ✅ Extract structured output
- ✅ Trigger next action

---

## Why This Matters For Eternity

Eternity is hiring you to build automation like this:

> **Operations Manager:** "We get 100+ emails a day with action items. Someone has to manually read them and create tasks. Can we automate this?"

> **You (using this code):** "Yes. Build an email integration → call Claude to extract action items → create tasks in Slack/Asana automatically."

This project is that exact pattern. You're learning to **think in systems**:
1. Problem: Manual email parsing
2. Solution: Claude API extraction
3. Integration: Pipe results to next tool (Slack, Asana, etc.)
4. Scale: Automate 100+ emails daily

---

## Next Steps (To Extend This)

Once you understand the basics, you can:

### 1. Add Database Storage
```python
# Save results to database instead of JSON file
import sqlite3
db.execute("INSERT INTO action_items ...")
```

### 2. Build a REST API
```python
from flask import Flask
@app.route('/extract', methods=['POST'])
def extract_api():
    email = request.json['email']
    return extract_action_items(email)
```

### 3. Connect to n8n
```
Email arrives → Webhook to your Python API → 
Extract action items → Create Asana task automatically
```

### 4. Add More Features
- Extract dates more accurately
- Estimate effort/time required
- Auto-assign based on skills
- Generate status reports

---

## Troubleshooting

### Error: "API key not found"
**Fix:** Create `.env` file with your `ANTHROPIC_API_KEY`

### Error: "JSON parsing failed"
**Fix:** Claude sometimes wraps JSON in code blocks. The code handles this, but if it fails, print the raw response:
```python
print("Raw response:", response_text)
```

### Error: "Module 'anthropic' not found"
**Fix:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Claude returns poor results
**Fix:** The prompt is tunable. Edit the `system_prompt` to be more specific:
```python
system_prompt = """... Your improved prompt here ..."""
```

---

## Project Structure

```
email-action-extractor/
├── email_action_extractor.py    # Main script
├── requirements.txt              # Python dependencies
├── .env.example                  # Template for API key
├── .gitignore                    # Files to exclude from git
├── README.md                     # This file
└── action_items.json             # Output (generated)
```

---

## GitHub Setup

### 1. Initialize Git
```bash
git init
git add .
git commit -m "Initial commit: Email action items extractor using Claude API"
```

### 2. Create GitHub Repo
Go to github.com → Create new repository → `email-action-extractor`

### 3. Push Code
```bash
git remote add origin https://github.com/YOUR_USERNAME/email-action-extractor.git
git branch -M main
git push -u origin main
```

### 4. Share the Link
Your GitHub link is: `https://github.com/YOUR_USERNAME/email-action-extractor`

---

## Interview Talking Points

When Eternity asks, "Tell me about a project you've built":

> "I built an Email Action Items Extractor that uses Claude API to automatically extract structured action items from raw emails. 
> 
> **The problem:** Operations teams manually parse emails to create tasks. That's repetitive and slow.
> 
> **How I solved it:** I wrote a Python script that:
> - Takes email text as input
> - Calls Claude API with a structured prompt
> - Claude returns JSON with action items, assignees, deadlines, priorities
> - Results are saved for further processing
> 
> **What I learned:** 
> - How to authenticate and call Claude API
> - How to write prompts that return structured data (JSON)
> - Error handling for API responses
> - Python best practices (virtual environments, dependencies, error handling)
> 
> **Why it matters:** This is exactly the pattern you'll use at Eternity. Identify a business problem → build Claude integration → extract structured data → trigger next action. I'm not just familiar with Claude API — I've shipped code that uses it."

---

## License

MIT (feel free to use, modify, share)

## Questions?

If you get stuck:
1. Check the error message carefully
2. Read the code comments
3. Google the error
4. Ask in the code comments below

---

**Good luck building! 🚀**
