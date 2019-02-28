from random import shuffle

def merge(pic_1, pic_2):
    return {
        'id': pic_1['id'] + pic_2['id'],
        'tags': pic_1['tags'] | pic_2['tags'],
    }

def get_score(slides):
    score = 0
    for i in range(len(slides) - 1):
        r = slides[i]['tags'] & slides[i + 1]['tags']
        p = slides[i]['tags'] - r
        q = slides[i + 1]['tags'] - r
        score += min([len(p), len(q), len(r)])
    return score

sol_folder = 'random_sol2'
datasets = ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']

max_score = {dataset: 0 for dataset in datasets}
ref_ans = {dataset: [] for dataset in datasets}

for a in range(10):
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

        score = get_score(slides)
        if score > max_score[dataset]:
            max_score[dataset] = score
            ref_ans[dataset] = slides

for dataset in datasets:
    wf = open('QualificationRound/{}/{}.txt'.format(sol_folder, dataset), 'w')
    wf.write('{}\n'.format(len(ref_ans[dataset])))
    for slide in ref_ans[dataset]:
        wf.write('{}\n'.format(' '.join(slide['id'])))
    wf.close()