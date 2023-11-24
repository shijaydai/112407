from ckip_transformers import __version__
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker


print(__version__)

print("Initializing drivers ... WS")
ws_driver = CkipWordSegmenter(model="albert-base", device=0)
print("Initializing drivers ... POS")
pos_driver = CkipPosTagger(model="albert-base", device=0)
print("Initializing drivers ... NER")
ner_driver = CkipNerChunker(model="albert-base", device=0)
print("Initializing drivers ... all done")
print()
def clean(sentence_ws, sentence_pos):
  short_with_pos = []
  short_sentence = []
  stop_pos = set(['Nep', 'Nh', 'Nb'])
  for word_ws, word_pos in zip(sentence_ws, sentence_pos):
    is_N_or_V = word_pos.startswith("V") or word_pos.startswith("N")
    is_not_stop_pos = word_pos not in stop_pos
    is_not_one_charactor = not (len(word_ws) == 1)
    if is_N_or_V and is_not_stop_pos and is_not_one_charactor:
      short_with_pos.append(f"{word_ws}({word_pos})")
      short_sentence.append(f"{word_ws}")
  return (" ".join(short_sentence), " ".join(short_with_pos))
def main():
    text = [
        ''
    ]
    ws = ws_driver(text)
    pos = pos_driver(ws)
    ner = ner_driver(text)
    print()
    print('=====')
    for sentence, sentence_ws, sentence_pos, sentence_ner in zip(text, ws, pos, ner):
        print("原文：")
        print(sentence)
        (short, res) = clean(sentence_ws, sentence_pos)
        print("斷詞後：")
        print(short)
        print("斷詞後+詞性標注：")
        print(res)
        print('=====')
if __name__ == "__main__":
    main()