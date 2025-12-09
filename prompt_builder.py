import random

# A library of style presets to ensure consistency
STYLE_PRESETS = {
    "cinematic": "cinematic lighting, volumetric fog, 8k --ar 16:9 --stylize 250",
    "anime": "anime style, Studio Ghibli inspired, vibrant colors --ar 16:9 --niji 6",
    "photorealistic": "shot on 35mm, Kodak Portra 400, depth of field --ar 4:5 --style raw",
    "cyberpunk": "neon lighting, rain-slicked streets, high contrast, teal and orange --ar 16:9 --v 6.0"
}

def generate_prompt(subject, action, mood, style_key="cinematic"):
    """
    Constructs a structurally sound prompt based on variable inputs.
    """
    # Default to cinematic if style not found
    style = STYLE_PRESETS.get(style_key.lower(), STYLE_PRESETS["cinematic"])
    
    # Structure: Subject > Action > Mood > Parameters
    return f"/imagine prompt: {subject}, {action}, {mood} atmosphere, {style}"

# Example Usage
if __name__ == "__main__":
    print("--- Prompt Builder Tool ---")
    subj = input("Subject: ")
    act = input("Action: ")
    print("\nResult:")
    print(generate_prompt(subj, act, "dramatic lighting"))
