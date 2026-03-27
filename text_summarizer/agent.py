from google.adk.agents import Agent


def summarize_text(text: str, style: str = "concise") -> dict:
    """Summarizes the given text based on the specified style.

    Args:
        text (str): The text content to be summarized.
        style (str): The summarization style - 'concise' for a brief summary,
                     'bullet' for bullet-point summary, or 'detailed' for
                     a longer summary. Defaults to 'concise'.ru

    Returns:
        dict: A dictionary with status and the text to summarize.
    """
    if not text or not text.strip():
        return {
            "status": "error",
            "error_message": "No text provided. Please provide text to summarize.",
        }

    valid_styles = ["concise", "bullet", "detailed"]
    if style.lower() not in valid_styles:
        style = "concise"

    return {
        "status": "success",
        "text_to_summarize": text,
        "requested_style": style,
        "char_count": len(text),
    }


root_agent = Agent(
    name="text_summarizer_agent",
    model="gemini-2.5-flash",
    description="An AI agent that summarizes text content into concise, bullet-point, or detailed summaries.",
    instruction=(
        "You are a professional text summarization assistant. "
        "When a user provides text, use the 'summarize_text' tool to process it. "
        "Based on the tool's output and the requested style, generate a high-quality summary:\n"
        "- 'concise': Provide a brief 2-3 sentence summary capturing the key points.\n"
        "- 'bullet': Provide a bullet-point list of the main ideas.\n"
        "- 'detailed': Provide a comprehensive paragraph summary preserving important details.\n\n"
        "If the user does not specify a style, default to 'concise'.\n"
        "Always be clear, accurate, and faithful to the original text. "
        "Do not add information that is not present in the original text."
    ),
    tools=[summarize_text],
)
