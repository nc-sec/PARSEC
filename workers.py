
def process_page_content(page):
    # Use a temporary list to hold new or modified content to avoid frequent list modifications
    new_content = []
    for k, sect in enumerate(page.page_content):
        sect = sect.strip().replace('\n', ' ')
        if len(sect) > 1000:
            # Efficiently split by sentences and divide
            split = sect.split('. ')
            half = len(split) // 2
            sect1 = '. '.join(split[:half])
            sect2 = '. '.join(split[half:])
            new_content.append(sect1)
            new_content.append(sect2)
        elif len(sect) < 75 and k > 0:
            # Instead of removing, just append to the previous section if possible
            new_content[-1] += ' ' + sect
        else:
            new_content.append(sect)
    return new_content

def process_book(book):
    for j, page in enumerate(book):
        book[j].page_content = process_page_content(page)
    return book