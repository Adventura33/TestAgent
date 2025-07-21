def write_markdown_file(content, filename):
  """Writes the given content as a markdown file to the local directory.

  Args:
    content: The string content to write to the file.
    filename: The filename to save the file as.
  """
  with open(f"{filename}.md", "w", encoding="cp1251") as f: # utf-8
        f.write(content)

def write_text_file(content: str, filename: str) -> None:
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        f.write(content)