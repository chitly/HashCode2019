from random import shuffle

def merge(pic_1, pic_2):
    return {
        'id': pic_1['id'] + pic_2['id'],
        'tags': pic_1['tags'] | pic_2['tags'],
    }

sol_folder = 'random_sol2'
datasets = ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']

for dataset in datasets:
    f = open('QualificationRound/{}.txt'.format(dataset))
    n = int(f.readline())
    h_pics, v_pics = [], []
    for i in range(n):
        tags = f.readline().strip().split()
        pic_type, num_tags, tags = tags[0], int(tags[1]), set(tags[2:])
        if pic_type == 'H':
            h_pics.append({
                'id': [str(i)],
                'tags': tags,
            })
        elif pic_type == 'V':
            v_pics.append({
                'id': [str(i)], 
                'tags': tags
            })

    shuffle(v_pics)
    v_pics = [merge(v_pics[2 * i], v_pics[2 * i + 1]) for i in range(len(v_pics) // 2)]

    slides = h_pics + v_pics
    # shuffle(slides)

    wf = open('QualificationRound/{}/{}.txt'.format(sol_folder, dataset), 'w')
    wf.write('{}\n'.format(len(slides)))
    for slide in slides:
        wf.write('{}\n'.format(' '.join(slide['id'])))
    wf.close()