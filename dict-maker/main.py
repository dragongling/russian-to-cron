import re

# from pymorphy2.opencorpora_dict import convert_to_pymorphy2


def extract_cron_words(corpora_path, outfile):
    needed_words_path = "words-we-need.txt"
    needed_words = read_words_file(needed_words_path)
    needed_words_regex = f"<l t=\"(?:" + "|".join(needed_words) + ")\">"
    # needed_grammemes = ["Anum", "NUMR"]
    common_regex = "(?:<g v=\"(Anum|NUMR)\"/>|" + needed_words_regex + ")"
    with (open(corpora_path, 'r', encoding='utf-8') as file,
          open(outfile, 'w', encoding='utf-8') as outfile):
        for line in file:
            if "<lemma " in line:
                if re.search(common_regex, line):
                    outfile.write(line)
            elif "<link " not in line:
                outfile.write(line)


def read_words_file(needed_words_path):
    needed_words = []
    with open(needed_words_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.replace("\n", "")
            if line != "":
                needed_words.append(line)
    return needed_words


if __name__ == '__main__':
    needed_path = 'needed_corpora.xml'
    dawg_path = 'dawg'
    extract_cron_words('dict.opcorpora.xml', needed_path)
    # convert_to_pymorphy2(needed_path, dawg_path, "hz", "ru")
