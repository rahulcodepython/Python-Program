import fitz  # PyMuPDF
import re


def convert_to_markdown(text):
    # Basic conversions
    # Replace multiple newlines with a single newline
    text = re.sub(r'\n+', '\n', text)

    # Convert headings (assuming they are in all caps or have a specific pattern)
    text = re.sub(r'\n([A-Z][A-Z0-9 ]+)\n', r'\n# \1\n', text)

    # Convert bullet points (assuming they start with a dash or asterisk)
    text = re.sub(r'\n•\s*', r'\n- ', text)

    # Convert numbered lists (assuming they start with a number followed by a dot)
    text = re.sub(r'\n(\d+)\.\s*', r'\n\1. ', text)

    # Convert bold text (assuming it is surrounded by asterisks or double underscores)
    text = re.sub(r'\*\*(.*?)\*\*', r'**\1**', text)
    text = re.sub(r'__(.*?)__', r'**\1**', text)

    # Convert italic text (assuming it is surrounded by single asterisks or underscores)
    text = re.sub(r'\*(.*?)\*', r'*\1*', text)
    text = re.sub(r'_(.*?)_', r'*\1*', text)

    # Convert links (assuming they are in the format [text](url))
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'[\1](\2)', text)

    return text


def pdf_to_markdown(pdf_path, md_path):
    doc = fitz.open(pdf_path)
    markdown_text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        markdown_text += convert_to_markdown(text)

    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_text)


# Example usage
pdf_to_markdown('1739268735090.pdf', 'output.md')
