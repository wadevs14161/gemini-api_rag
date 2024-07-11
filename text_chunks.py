from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_text_chunks(data):
    text = ""
    # Convert list of dictionaries to a structured string
    for entry in data:
        formatted_entry = ' '.join(f"{key}: {value}" for key, value in entry.items())
        text += formatted_entry + "\n"  # Separate entries with triple newlines

    splitter = RecursiveCharacterTextSplitter(
        separators=['\n'],
        chunk_size=10000, chunk_overlap=1000)
    chunks = splitter.split_text(text)
    return chunks


if __name__ == "__main__":
    pass