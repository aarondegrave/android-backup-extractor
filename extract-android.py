__Author__ = "Aaron DeGrave"
import zlib
import tarfile
import argparse
import io
import json

parser = argparse.ArgumentParser()
parser.add_argument("file", help = "Point me to the file", type=str)
args = parser.parse_args()

with open(args.file, 'rb') as f:
    f.seek(24)
    data= f.read()
    stream = zlib.decompress(data)
    tar = tarfile.open(fileobj=io.BytesIO(stream))
    members = tar.getmembers()
    for member in members:
        try:
            a = tar.extractfile(member)
            data = a.read()
            with open('data.json', 'a') as f:
                datatest = json.dumps(str(data))
                f.write(datatest + "\n")
            with open('file.tar', 'a') as c:
                c.write(data.decode('utf-8'))
            print(data)
        except AttributeError as e:
            continue
        except UnicodeDecodeError as e:
            continue