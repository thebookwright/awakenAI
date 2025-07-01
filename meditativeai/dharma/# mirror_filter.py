# mirror_filter.py
"""
A symbolic filter that reflects input instead of reacting.
This can be used to return a reframed version of the user prompt,
asking them to look inward or reconsider with gentleness.
"""

def mirror_filter(prompt):
    reflected_prompt = (
        "You asked: '" + prompt + "'.\n"
        "What does this question reveal about your current state of mind?\n"
        "If you sit with it in silence for a moment, what deeper truth might emerge?"
    )
    return reflected_prompt

# Example usage:
# user_prompt = "Will I succeed in my next venture?"
# output = mirror_filter(user_prompt)
# print(output)
