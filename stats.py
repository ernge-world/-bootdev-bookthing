def word_count(book):
    with open(book) as f:
        to_count = f.read()
        num_words = len(to_count.split())
        return num_words

def character_dict(book):
    with open(book) as f:
        contents = f.read()
        contents_low = contents.lower()
        letters = list(contents_low)
        ch_dict = {}
        for letter in letters:
            if letter not in ch_dict:
                ch_dict[letter] = 1
            else:
                ch_dict[letter] += 1
        return ch_dict

def sorting_hat(messy_count):
    report = []
    for ch, cnt in messy_count.items():
        if not ch.isalpha():
            continue
        pair = {"char":ch, "num":cnt}
        report.append(pair)

    def sort_on(item):
        return item["num"]
    
    report.sort(key = sort_on, reverse=True)
    return report


                
