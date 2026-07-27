def parse_markdown(text):
    lines = text.split('\n')
    html_blocks = []
    paragraph_lines = []

    def flush_paragraph():
        if paragraph_lines:
            joined = ' '.join(paragraph_lines)
            html_blocks.append(f'<p>{joined}</p>')
            paragraph_lines.clear()

    for line in lines:
        if line.startswith('## '):
            flush_paragraph()
            html_blocks.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('# '):
            flush_paragraph()
            html_blocks.append(f'<h1>{line[2:]}</h1>')
        elif line.strip() == '':
            flush_paragraph()
        else:
            paragraph_lines.append(line)

    flush_paragraph()
    return '\n'.join(html_blocks)
