#!/usr/bin/env python3

import os

def modify_file():
    file_path = '/app/libs/kotaemon/kotaemon/llms/chats/langchain_based.py'
    with open(file_path, 'r') as f:
        content = f.read()

    # Replace the Ollama imports with OpenAI
    old_code = '''    def _get_lc_class(self):
        try:
            from langchain_ollama import ChatOllama
            return ChatOllama
        except ImportError:
            raise ImportError("Please install langchain-ollama")'''

    new_code = '''    def _get_lc_class(self):
        try:
            from langchain_openai import ChatOpenAI
            return ChatOpenAI
        except ImportError:
            try:
                from langchain.chat_models import ChatOpenAI
                return ChatOpenAI
            except ImportError:
                raise ImportError("Please install langchain-openai")'''

    modified_content = content.replace(old_code, new_code)

    with open(file_path, 'w') as f:
        f.write(modified_content)

if __name__ == '__main__':
    modify_file()
