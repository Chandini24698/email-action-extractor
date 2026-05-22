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