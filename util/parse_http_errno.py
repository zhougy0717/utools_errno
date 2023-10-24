import json
if __name__ == '__main__':
    items = []
    with open('http_errno.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split('\t')
            desc = ' '.join(words[2:])
            item = {
                'title': words[1],
                'errno': words[0],
                'description': 'errno = {}, {}'.format(words[0], desc.strip()),
                'icon': 'icons/http.png'
            }
            items.append(item)

    with open('../http_errno.json', 'w', encoding='utf-8') as out:
        json.dump(items, out, ensure_ascii=False, indent=4)
