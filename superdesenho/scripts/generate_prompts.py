import sys

def format_prompt(description):
    suffix = "1990s traditional hand-drawn animation style, 3D retro cartoon aesthetic, solid colors, bold outlines, cel shading, nostalgic TV animation vibe, organic texture"
    return f"{description.strip()}, {suffix}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_prompts.py \"visual description in English\"")
        sys.exit(1)
    
    desc = sys.argv[1]
    print(format_prompt(desc))
