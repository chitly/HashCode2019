def merge(pic_1, pic_2):
    return {
        'id': pic_1['id'] + pic_2['id'],
        'tags': pic_1['tags'] | pic_2['tags'],
    }

def get_score_table(pics):
    score_table = {}
    for i in range(len(pics)):
        for j in range(i + 1, len(pics)):
            r = len(pics[i]['tags'] & pics[j]['tags'])
            p = len(pics[i]['tags']) - r
            q = len(pics[j]['tags']) - r
            score = min([r, p, q])
            if i not in score_table:
                score_table[i] = []
            if j not in score_table:
                score_table[j] = []
            score_table[i].append((score, j))
            score_table[j].append((score, i))
    for idx in score_table:
        score_table[idx].sort(key=lambda x: -x[0])
    return score_table

def get_slides(h_pics, v_pics):
    get_num_tags = lambda pic: len(pic['tags'])
    sorted_v_pics = sorted(v_pics, key=get_num_tags)
    v_slides = [merge(sorted_v_pics[2 * i], sorted_v_pics[2 * i + 1]) for i in range(len(sorted_v_pics) // 2)]
    slides = sorted(h_pics + v_slides, key=get_num_tags)

    partition = 20
    top_tier = slides[-len(slides) // partition:]
    score_table = get_score_table(top_tier)
        
    seen_table = {top_tier_idx: 0 for top_tier_idx in score_table}
    selected_id = set([0])
    sorted_top_tier = [top_tier[0]]
    last_idx = 0
    for i in range(len(top_tier) - 1):
        for j in range(seen_table[last_idx], len(top_tier) - 1):
            next_idx = score_table[last_idx][j][1]
            if next_idx not in selected_id:
                sorted_top_tier.append(top_tier[next_idx])
                seen_table[last_idx] = j
                selected_id.add(next_idx)
                last_idx = next_idx
                break

    return slides[:-len(slides) // partition] + sorted_top_tier

def get_score(slides):
    score = 0
    for i in range(len(slides) - 1):
        r = len(slides[i]['tags'] & slides[i + 1]['tags'])
        p = len(slides[i]['tags']) - r
        q = len(slides[i + 1]['tags']) - r
        score += min([p, q, r])
    return score

sol_folder = 'top_tier'
datasets = ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']
# datasets = ['d_pet_pictures']

max_score = {dataset: 0 for dataset in datasets}
ref_ans = {dataset: [] for dataset in datasets}
random_round = 1

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

    for a in range(random_round):
        slides = get_slides(h_pics, v_pics)
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

# for i in range(len(slides)):
#     print(slides[i]['tags'])
#     if(i!=len(slides)-1):
#         middle = len(slides[i]['tags'].intersection(slides[i+1]['tags']))
#         left = len(slides[i]['tags']) - middle
#         right = len(slides[i+1]['tags']) - middle
#         print(left, middle, right, min(left,middle,right))
