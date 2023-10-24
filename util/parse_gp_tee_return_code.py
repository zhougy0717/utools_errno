import json
if __name__ == '__main__':
    items = []
    with open('./gp_tee_return_code', 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(' ')
            desc = ' '.join(words[2:])
            item = {
                'title': words[0],
                'errno': words[-1].strip(),
                'icon': 'icons/tee.png'
            }
            items.append(item)

    with open('../gp_tee.json', 'w', encoding='utf-8') as out:
        json.dump(items, out, ensure_ascii=False, indent=4)