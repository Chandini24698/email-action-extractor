#!/usr/bin/env python3
"""
Email Action Items Extractor - Simple Version
Extracts action items from email text using Claude API
"""

import json
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Get API key
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    print("❌ Error: ANTHROPIC_API_KEY not found in .env file")
    print("Make sure your .env file contains: ANTHROPIC_API_KEY=sk-ant-...")
    exit(1)

# Try importing Anthropic
try:
    from anthropic import Anthropic
    client = Anthropic(api_key=api_key)
except Exception as e:
    print(f"❌ Error initializing Anthropic client: {e}")
    print("\nTrying alternative approach...")
    
    # Fallback: use requests to call API directly
    import requests
    
    def extract_action_items_direct(email_text: str) -> dict:
        """Call Claude API directly using requests library"""
        
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        
        system_prompt = """You are an expert at extracting action items from emails.

Given an email, extract ALL action items that need to be completed.

For each action item, provide:
- action: The specific task to complete
- assignee: Who should do it (if mentioned, otherwise "Unassigned")
- deadline: When it's due (if mentioned, otherwise "Not specified")
- priority: "High", "Medium", or "Low" based on context
- details: Any additional context or notes

Return ONLY valid JSON with this structure:
{
  "email_summary": "1-2 sentence summary of the email",
  "action_items": [
    {
      "action": "task description",
      "assignee": "person or team",
      "deadline": "date or timeframe",
      "priority": "High/Medium/Low",
      "details": "additional notes"
    }
  ],
  "total_items": number
}

If no action items found, return an empty action_items array."""

        data = {
            "model": "claude-opus-4-1",
            "max_tokens": 1024,
            "system": system_prompt,
            "messages": [
                {
                    "role": "user",
                    "content": f"Please extract action items from this email:\n\n{email_text}"
                }
            ]
        }
        
        print("📧 Processing email with Claude API...")
        print("-" * 50)
        
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data
        )
        
        if response.status_code != 200:
            raise Exception(f"API Error {response.status_code}: {response.text}")
        
        result = response.json()
        response_text = result["content"][0]["text"]
        
        # Parse JSON
        try:
            action_items = json.loads(response_text)
        except json.JSONDecodeError:
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0].strip()
                action_items = json.loads(json_str)
            elif "```" in response_text:
                json_str = response_text.split("```")[1].split("```")[0].strip()
                action_items = json.loads(json_str)
            else:
                raise ValueError("Could not parse Claude's response as JSON")
        
        return action_items
    
    # Use the direct version
    extract_action_items = extract_action_items_direct


# Standard version (if Anthropic library works)
try:
    def extract_action_items(email_text: str) -> dict:
        """Extract action items using Anthropic client"""
        
        system_prompt = """You are an expert at extracting action items from emails.

Given an email, extract ALL action items that need to be completed.

For each action item, provide:
- action: The specific task to complete
- assignee: Who should do it (if mentioned, otherwise "Unassigned")
- deadline: When it's due (if mentioned, otherwise "Not specified")
- priority: "High", "Medium", or "Low" based on context
- details: Any additional context or notes

Return ONLY valid JSON with this structure:
{
  "email_summary": "1-2 sentence summary of the email",
  "action_items": [
    {
      "action": "task description",
      "assignee": "person or team",
      "deadline": "date or timeframe",
      "priority": "High/Medium/Low",
      "details": "additional notes"
    }
  ],
  "total_items": number
}

If no action items found, return an empty action_items array."""

        print("📧 Processing email with Claude API...")
        print("-" * 50)
        
        message = client.messages.create(
            model="claude-opus-4-1",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"Please extract action items from this email:\n\n{email_text}"
                }
            ],
            system=system_prompt
        )
        
        response_text = message.content[0].text
        
        # Parse JSON
        try:
            action_items = json.loads(response_text)
        except json.JSONDecodeError:
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0].strip()
                action_items = json.loads(json_str)
            elif "```" in response_text:
                json_str = response_text.split("```")[1].split("```")[0].strip()
                action_items = json.loads(json_str)
            else:
                raise ValueError("Could not parse Claude's response as JSON")
        
        return action_items

except:
    pass


def display_results(action_items: dict):
    """Pretty print the extracted action items."""
    
    print("\n✅ EXTRACTION COMPLETE")
    print("=" * 50)
    
    print(f"\n📝 Email Summary:")
    print(f"   {action_items['email_summary']}")
    
    print(f"\n📋 Action Items: {action_items['total_items']}")
    print("-" * 50)
    
    if action_items['total_items'] > 0:
        for idx, item in enumerate(action_items['action_items'], 1):
            print(f"\n{idx}. {item['action']}")
            print(f"   👤 Assignee: {item['assignee']}")
            print(f"   📅 Deadline: {item['deadline']}")
            print(f"   🎯 Priority: {item['priority']}")
            if item.get('details'):
                print(f"   📌 Details: {item['details']}")
    else:
        print("   (No action items found)")


def save_results(action_items: dict, filename: str = "action_items.json"):
    """Save extracted action items to a JSON file."""
    
    import pathlib
    output_path = pathlib.Path(filename)
    with open(output_path, 'w') as f:
        json.dump(action_items, f, indent=2)
    
    print(f"\n💾 Results saved to: {output_path.absolute()}")


def main():
    """Main function - demo with sample email."""
    
    print("\n" + "=" * 50)
    print("📧 EMAIL ACTION ITEMS EXTRACTOR")
    print("Powered by Claude API")
    print("=" * 50)
    
    sample_email = """
Subject: Q2 Planning Meeting - Action Items Needed

Hi Team,

Thanks for attending the Q2 planning meeting yesterday. Here's what we discussed:

1. Sarah needs to finalize the budget spreadsheet by Friday (May 24th). This is HIGH priority since we need it for the board meeting.

2. The marketing team (Jessica, Mike, and team) should prepare the product roadmap slides. Medium priority, due by next Wednesday.

3. I'll handle the investor presentations, but I need the financial data from accounting. Can someone check with them? Not urgent, due by end of next week.

4. Dev team - please update the API documentation. This is blocking the partner integrations. High priority, ASAP.

5. HR mentioned we need to update the hiring process. Someone should schedule a meeting with them to discuss. Low priority.

Please confirm receipt and let me know if you have any blockers.

Thanks,
John
Product Manager
"""
    
    print("\n📥 Sample Email:")
    print("-" * 50)
    print(sample_email)
    print("-" * 50)
    
    try:
        action_items = extract_action_items(sample_email)
        display_results(action_items)
        save_results(action_items)
        
        print("\n✨ Done! You can now:")
        print("   1. Modify the email text and run again")
        print("   2. Check action_items.json for full results")
        print("   3. Integrate this into a workflow/API")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
