import fitz  # PyMuPDF
import os
import argparse

TEMPLATE = '''
<div class="paper">
    <div class="img_default">
        <img 
            src="{img_static}" 
            onmouseover="this.src='{img_hover}'; this.style.width='75%';" 
            onmouseout="this.src='{img_static}'; this.style.width='100%';" 
            width="100%"
        >
    </div>
    <div class="description">
        <p class="pub-descr">
            <a href="{paper_link}" class="title" target="_blank"><papertitle>{title}</papertitle></a>
        </p>
        <p class="pub-descr">
            {authors}
        </p>
        <p class="pub-descr">
            <em>{venue}</em> - <strong style="color: green">{type}</strong>
        </p>
        <p class="pub-descr">
            {links}
        </p>                             
        <p align="justify">{abstract}</p>
    </div>
</div>
'''

def extract_title_authors(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        meta = doc.metadata
        title = meta.get("title", "").strip()
        author = meta.get("author", "").strip()
        return title, author
    except Exception as e:
        print(f"Error reading PDF metadata: {e}")
        return "", ""

def generate_links(project_url, hf_url, github_url, arxiv_url, bibtex_url):
    return f'''
        <a href="{project_url}" target="_blank">🔗 Project Page</a> &nbsp|&nbsp
        <a href="{hf_url}" target="_blank">🤗 Hugging Face</a> &nbsp|&nbsp
        <a href="{github_url}" target="_blank">🐙 GitHub</a> &nbsp|&nbsp
        <a href="{arxiv_url}" target="_blank">📝 arXiv</a> &nbsp|&nbsp
        <a href="{bibtex_url}" target="_blank">📄 bibtex</a>
    '''

def format_authors(authors_list):
    formatted = []
    for name, url, is_strong in authors_list:
        tag_open = "<strong>" if is_strong else ""
        tag_close = "</strong>" if is_strong else ""
        formatted.append(f'{tag_open}<a href="{url}" target="_blank">{name}</a>{tag_close}')
    return ", ".join(formatted)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path", help="Path to the paper PDF")
    args = parser.parse_args()

    title, author = extract_title_authors(args.pdf_path)

    print("📝 Enter metadata (press Enter to keep default):")
    title = input(f"Title [{title}]: ") or title
    paper_link = input("Paper link (e.g., arXiv or DOI): ")
    img_static = input("Static image path: ")
    img_hover = input("Hover GIF path: ")
    abstract = input("Abstract: ")
    venue = input("Conference/journal venue: ")
    type_ = input("Type (Poster, Oral, etc): ")

    # List of authors
    print("Add authors (name, URL, is_strong). Type 'done' when finished.")
    authors = []
    while True:
        entry = input("Author (format: Name,URL,is_strong): ")
        if entry.lower() == "done":
            break
        try:
            name, url, is_strong = [x.strip() for x in entry.split(",")]
            authors.append((name, url, is_strong.lower() == "true"))
        except:
            print("⚠️ Invalid format. Please use: Name,URL,is_strong")

    project_url = input("Project page URL: ")
    hf_url = input("Hugging Face URL: ")
    github_url = input("GitHub URL: ")
    arxiv_url = input("arXiv or publication link: ")
    bibtex_url = input("BibTeX file URL: ")

    html = TEMPLATE.format(
        img_static=img_static,
        img_hover=img_hover,
        title=title,
        paper_link=paper_link,
        authors=format_authors(authors),
        venue=venue,
        type=type_,
        links=generate_links(project_url, hf_url, github_url, arxiv_url, bibtex_url),
        abstract=abstract
    )

    output_file = os.path.splitext(os.path.basename(args.pdf_path))[0] + "_paper_window.html"
    with open(output_file, "w") as f:
        f.write(html)

    print(f"✅ HTML saved to {output_file}")

if __name__ == "__main__":
    main()
