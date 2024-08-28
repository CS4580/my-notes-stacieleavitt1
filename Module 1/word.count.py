"""Read file from web and do analysis of data
"""


from urllib.request import urlopen

def count_words_from_file(url_address):
    words = 0
    # read file from web
    with urlopen(url_address) as data:
        for line in data:
            line = line.decode('utf-8')
            # print(line, type(line))
            line_words = line.split()
            for word in line_words:
                # count number of words
                words += 1
    return words
    

def main():
    """Driven Function
    """
    file_address = 'http://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    total_words = count_words_from_file(file_address)
    print(f'There are a total of {total_words} words in the file')

if __name__ == '__main__':
    main()