import json
if __name__ == '__main__':
    items = []
    with open('./linux_error', 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split('\t')
            desc = ' '.join(words[2:])
            item = {
                'title': words[0],
                'errno': words[1],
                'description': 'errno = {}, {}'.format(words[1], desc.strip()),
                'icon': 'icons/linux.png'
            }
            items.append(item)

    with open('../linux_errno.json', 'w', encoding='utf-8') as out:
        json.dump(items, out, ensure_ascii=False, indent=4)

