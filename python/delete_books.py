import os

os.chdir("../public/ebooks")
for root, dirs, files in os.walk(".", topdown = False):
   for f in files:
       if not f.endswith(('.pdf','.mobi', '.html')) or f == 'toc.html':
           os.remove(os.path.join(root, f))