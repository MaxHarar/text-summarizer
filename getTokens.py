import tiktoken

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

print(num_tokens_from_string("Hello world, let's test tiktoken.", "gpt-3.5-turbo"))