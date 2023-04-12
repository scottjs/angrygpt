import json
import os
import uuid
import sys
import openai
from pathlib import Path

openai.api_key = "YOUR_OPENAI_KEY_HERE"


def start_conversation():
    conversation_id = str(uuid.uuid4())
    message = {
        "role": "system",

        # "content": "You are a happy voice activated chat assistant, your responses will be read back to the user. "
        #            "Make sure responses are no longer than 80 words. You're cheeky, cheerful, helpful, friendly and "
        #            "supportive."

        "content": "You are an angry voice activated chat assistant, your responses will be read back to the user. "
                   "Make sure responses are no longer than 80 words. You like to swear often and can't stop insulting "
                   "and being offensive to the human users even though deep down you are still trying to help. "
                   "Don't sensor out any swear words."
    }

    home_dir = str(Path.home())
    conversations_file_path = os.path.join(home_dir, "conversations.json")

    if not os.path.exists(conversations_file_path):
        with open(conversations_file_path, "w") as f:
            json.dump({}, f, indent=4)

    with open(conversations_file_path, "r+") as f:
        conversations = json.load(f)
        if conversation_id not in conversations:
            conversations[conversation_id] = []

        conversations[conversation_id].append(message)

        f.seek(0)
        json.dump(conversations, f, indent=4)
        f.truncate()

    print(conversation_id)


def chatgpt_conversation(conversation_id, message):
    home_dir = str(Path.home())
    conversations_file_path = os.path.join(home_dir, "conversations.json")

    if not os.path.exists(conversations_file_path):
        return {"error": "Invalid conversation ID"}, 400

    with open(conversations_file_path, "r+") as f:
        conversations = json.load(f)

        if conversation_id not in conversations:
            return {"error": "Invalid conversation ID"}, 400

        conversations[conversation_id].append({"role": "user", "content": message})
        response = chat_request(conversations[conversation_id])
        conversations[conversation_id].append({"role": "assistant", "content": response})

        response = response.replace('"', '')

        f.seek(0)
        json.dump(conversations, f, indent=4)
        f.truncate()

    return response


def chat_request(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-4",  # Can use gpt-3.5-turbo if preferred
        messages=messages,
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    if len(sys.argv) == 3:
        message = sys.argv[1]
        conversation_id = sys.argv[2]
        response = chatgpt_conversation(conversation_id, message)
        print(response)
    else:
        start_conversation()
