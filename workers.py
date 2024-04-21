<<<<<<< HEAD
#
=======
"""from langchain.docstore.document import Document

def process_book(book):
    for page in book:
        page.page_content = page.page_content.replace('\\n', ' ').replace('\n', ' ').strip()
        if len(page.page_content) > 600:
            # Efficiently split by sentences and divide
            split = page.page_content.split('. ')
            half = len(split) // 2
            sect1 = '. '.join(split[:half])
            sect2 = '. '.join(split[half:])
            book.append(Document(sect1, metadata=page.metadata.copy()))
            book.append(Document(sect2, metadata=page.metadata.copy()))
    return book
"""
from langchain.docstore.document import Document
import re

def process_book(book):
    """Split pages in a book into smaller pages if they are too long."""    
    processed_pages = []  # To store new and modified pages

    for page in book:
        print(page.metadata)
        cleaned_content = re.sub(r'\s+', ' ', page.page_content).strip()
        cleaned_content = cleaned_content.replace('\\n', ' ').replace('\n', ' ').strip()
        if len(cleaned_content) < 20:
            continue
        if len(cleaned_content) > 600:
            sentences = re.split(r'(?<=[.!?]) +', cleaned_content)
            half = len(sentences) // 2
            sect1 = ' '.join(sentences[:half])
            sect2 = ' '.join(sentences[half:])

            # Create new documents and add them to the temporary list
            processed_pages.append(Document(sect1, metadata=page.metadata.copy()))
            processed_pages.append(Document(sect2, metadata=page.metadata.copy()))
        else:
            # For shorter content, just create a single document
            processed_pages.append(Document(cleaned_content, metadata=page.metadata.copy()))

    # Extend the original book with all processed pages at once
    book.extend(processed_pages)
    return book
>>>>>>> eda2e4c (hihi)
