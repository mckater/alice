import json

data = open('log_from_glitch.txt')
ff = data.read()
if ff.startswith('INFO:root:Request:'):
    with open('request.json', 'w') as wr:
        json.dump(ff.split(None, 1)[1], wr, ensure_ascii=False, indent=4)
elif ff.startswith('INFO:root:Response:'):
    with open('response.json', 'w') as wr:
        json.dump(ff.split(None, 1)[1], wr, ensure_ascii=False, indent=4)
data.close()
