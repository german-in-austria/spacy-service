# It’s probably a good idea to rewrite this with *flask.* 
# That’s the closest http framework to node’s express.

import http.server
import spacy
import socketserver
import json

# init with german news corpus
nlpDe = spacy.load('de_core_news_sm')

PORT = 2222
Handler = http.server.BaseHTTPRequestHandler

def tag_sentence(s: str):
  doc = nlpDe(s)
  return list(map(lambda x: {
    'spacy_orth': doc[x].orth_,
    'spacy_text': doc[x].text,
    'spacy_pos': doc[x].pos_,
    'spacy_tag': doc[x].tag_,
    'spacy_lemma': doc[x].lemma_, 
    'spacy_dep': doc[x].dep_,
    'spacy_entity_type': doc[x].ent_type_
  }, range(len(doc))))

class HttpController(http.server.BaseHTTPRequestHandler):
  def do_POST(self):
    print(self.path)
    length = int(self.headers.get('content-length'))
    i = self.rfile.read(length).decode()
    result = tag_sentence(i)
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(result).encode('utf-8'))

with socketserver.TCPServer(("", PORT), HttpController) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

