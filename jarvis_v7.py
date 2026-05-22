#!/usr/bin/env python3
import os
import re
import json
import subprocess

MODEL = os.path.expanduser("~/model.gguf")
MEMORY_FILE = os.path.expanduser("~/jarvis_memory.json")
TTS = "/data/data/com.termux/files/usr/bin/termux-tts-speak"
STT = "/data/data/com.termux/files/usr/bin/termux-speech-to-text"
CALL = "/data/data/com.termux/files/usr/bin/termux-telephony-call"
CONTACTS = "/data/data/com.termux/files/usr/bin/termux-contact-list"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict) and "facts" in data and isinstance(data["facts"], list):
                return data
        except:
            pass
    return {"facts": []}

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def add_memory(memory, fact):
    fact = fact.strip()
    if fact and fact not in memory["facts"]:
        memory["facts"].append(fact)
        save_memory(memory)
        return True
    return False

def memory_text(memory):
    if not memory["facts"]:
        return "No memories stored yet."
    return "
".join(f"- {f}" for f in memory["facts"])

def is_remember_command(text):
    triggers = [
        "remember that", "remember,", "don't forget", "note that",
        "my name is", "i am ", "i wake", "i sleep", "i work",
        "i like", "i hate", "i prefer", "i always", "my friend",
        "my wife", "my husband", "my mom", "my dad", "my boss"
    ]
    t = text.lower()
    return any(x in t for x in triggers)

def extract_fact(text):
    text = text.strip()
    prefixes = [
        "please remember that", "remember that", "remember,",
        "don't forget that", "don't forget,", "note that",
        "please remember", "remember"
    ]
    lower = text.lower()
    for prefix in prefixes:
        if lower.startswith(prefix):
            text = text[len(prefix):].strip()
            break
    if text:
        return text[0].upper() + text[1:]
    return text

def speak(text):
    text = text.strip() if text else ""
    if not text:
        text = "Sorry, I have no response."
    try:
        subprocess.run([TTS, text], check=False)
    except:
        pass

def listen():
    try:
        result = subprocess.run([STT], capture_output=True, text=True, check=False)
        return result.stdout.strip()
    except:
        return ""

def get_contacts():
    try:
        result = subprocess.run([CONTACTS], capture_output=True, text=True, check=False)
        if result.stdout.strip():
            return json.loads(result.stdout)
    except:
        pass
    return []

def handle_call(name):
    name = name.strip()
    if not name:
        speak("Who should I call?")
        return

    num = name.replace("+", "").replace(" ", "")
    if num.isdigit():
        speak(f"Calling {name}")
        subprocess.run([CALL, name], check=False)
        return

    contacts = get_contacts()
    match = next((c for c in contacts if name.lower() in c.get("name", "").lower()), None)

    if match:
        number = match.get("number", "").replace(" ", "")
        if number:
            speak(f"Calling {match['name']}")
            subprocess.run([CALL, number], check=False)
        else:
            speak(f"I found {match['name']} but no number was available.")
    else:
        speak(f"I could not find {name} in your contacts.")

def clean_output(raw):
    text = re.sub(r'\u001B[[0-9;]*[mGKHFJA]', '', raw)
    text = text.replace('
', '
')
    lines = [line.strip() for line in text.split('
')]
    lines = [line for line in lines if line and not line.startswith('[') and not line.startswith('>')]
    joined = " ".join(lines)
    joined = re.sub(r's+', ' ', joined).strip()
    return joined

def get_response(question, memory, history):
    mem = memory_text(memory)
    system_prompt = (
        "You are Jarvis, a concise voice assistant. "
        "Answer directly and briefly. "
        "Use plain short sentences only. "
        "No markdown. No introductions. "
        "If the user asks for steps, give numbered steps. "
        f"User facts, only if relevant: {mem}"
    )

    if history:
        last = history[-1]
        user_prompt = (
            f"System: {system_prompt}
"
            f"Previous reply: {last['jarvis']}
"
            f"User: {question}
"
            f"Assistant:"
        )
    else:
        user_prompt = (
            f"System: {system_prompt}
"
            f"User: {question}
"
            f"Assistant:"
        )

    try:
        cmd = [
            "llama-cli",
            "-m", MODEL,
            "-t", "4",
            "-n", "128",
            "--temp", "0.7",
            "--no-display-prompt"
        ]
        child = subprocess.run(
            cmd,
            input=user_prompt,
            text=True,
            capture_output=True,
            check=False
        )
        raw = child.stdout if child.stdout else child.stderr
        response = clean_output(raw)
        return response if response else "I could not generate a response."
    except Exception:
        return "I could not generate a response."

def main():
    memory = load_memory()
    history = []
    MAX_HISTORY = 6

    print("=" * 40)
    print(" JARVIS - Personal AI Assistant")
    print("=" * 40)
    print(f"Memory: {len(memory['facts'])} facts loaded")
    print("Enter → type a message")
    print("Blank line → speak via mic")
    print("'memory' → show what Jarvis knows")
    print("'forget' → clear all memory")
    print("'history' → show chat history")
    print("'clear' → clear chat history")
    print("'call John' → call a contact")
    print("'quit' → exit")
    print("=" * 40)

    while True:
        try:
            user_input = input("
You: ").strip()

            if user_input.lower() in ["quit", "exit"]:
                speak("Goodbye.")
                break

            if user_input.lower() == "memory":
                print("
--- Jarvis Memory ---")
                print(memory_text(memory))
                continue

            if user_input.lower() == "forget":
                memory = {"facts": []}
                save_memory(memory)
                speak("Memory cleared.")
                continue

            if user_input.lower() == "history":
                print("
--- Chat History ---")
                if not history:
                    print("No history yet.")
                for h in history:
                    print(f"You: {h['user']}")
                    print(f"Jarvis: {h['jarvis']}")
                continue

            if user_input.lower() == "clear":
                history = []
                speak("Chat history cleared.")
                continue

            if not user_input:
                print("Listening...")
                user_input = listen()
                if not user_input:
                    continue
                print(f"You said: {user_input}")

            if user_input.lower().startswith("call "):
                handle_call(user_input[5:])
                continue

            if is_remember_command(user_input):
                fact = extract_fact(user_input)
                if add_memory(memory, fact):
                    speak("Got it. I will remember that.")
                else:
                    speak("I already know that.")
                continue

            print("Thinking...")
            response = get_response(user_input, memory, history)
            print(f"Jarvis: {response}")
            speak(response)

            history.append({"user": user_input, "jarvis": response})
            if len(history) > MAX_HISTORY:
                history.pop(0)

        except KeyboardInterrupt:
            speak("Goodbye.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
