import argparse
import os
import jinja2
from dotenv import load_dotenv

class Config:
  CTX = {}

  def parse():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Nginx jinja2 template renderer.')
    parser.add_argument('--listen', type=str, required=False, action='store',
      dest='LISTEN', default=os.getenv('LISTEN'), help='Listen port.')
    parser.add_argument('--server-name', type=str, required=False, action='store',
      dest='SERVER_NAME', default=os.getenv('SERVER_NAME'), help='Server name.')
    parser.add_argument('--location', type=str, required=False, action='store',
      dest='LOCATION', default=os.getenv('LOCATION'), help='Location path.')
    parser.add_argument('--root', type=str, required=False, action='store',
      dest='ROOT', default=os.getenv('ROOT'), help='Static root directory.')
    parser.add_argument('--index', type=str, required=False, action='store',
      dest='INDEX', default=os.getenv('INDEX'), help='Index filename.')
    args = parser.parse_args()

    # TODO: None and "" checks
    Config.CTX = args.__dict__


def main():
  Config.parse()

  with open('nginx.conf.j2', 'r') as f:
    template = jinja2.Template(f.read())
  
  rendered: str = template.render(Config.CTX)
  clean_rendered = []
  for line in rendered.split('\n'):
    if line.strip():
      clean_rendered += [line]

  with open('nginx.conf', 'w') as f:
    f.write('\n'.join(clean_rendered))


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    exit(0)
