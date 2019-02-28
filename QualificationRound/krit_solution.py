# f=open("./a_example.txt", "r")
# n = int(f.readline())
# print(n)
# photos = []
# for i in range(0,n):
#   arr = [e.strip() for e in f.readline().split()]
#   photo_type = arr[0]
#   tags_count = arr[1]
#   for j in range(2,len(arr)):
#     photos[i][arr[j]] = 1

#   print(photo_type)
#   print(tags_count)
#   print(arr)
# # if f.mode == 'r':
# #   contents =f.read()
# #   print(contents)


from random import shuffle

def merge(pic_1, pic_2):
    return {
        'id': pic_1['id'] + pic_2['id'],
        'tags': pic_1['tags'] | pic_2['tags'],
    }

sol_folder = 'random_sol2'
# datasets = ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']
datasets = ['e_shiny_selfies']

for dataset in datasets:
    f = open('./{}.txt'.format(dataset))
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

    pics = v_pics + h_pics

    wf = open('./krit_test1.txt', 'w')
    print(dataset)
    print('=================')
    max_all = 0
    min_all = 9999
    sum_all = 0

    max_v = 0
    min_v = 9999
    sum_v = 0
    for i in range(len(v_pics)):
      # print(len(v_pics[i]['tags']))
      sum_v = sum_v + len(v_pics[i]['tags'])
      sum_all = sum_all + len(v_pics[i]['tags'])
      if(max_v < len(v_pics[i]['tags'])):
        max_v = len(v_pics[i]['tags'])
      if(min_v > len(v_pics[i]['tags'])):
        min_v = len(v_pics[i]['tags'])
      if(max_all < len(v_pics[i]['tags'])):
        max_all = len(v_pics[i]['tags'])
      if(min_all > len(v_pics[i]['tags'])):
        min_all = len(v_pics[i]['tags'])
    print('sum_v = ', sum_v)
    print('mean_v = ', sum_v/len(v_pics))
    print('max_v = ', max_v)
    print('min_v = ', min_v)
    print('=================')

    # max_h = 0
    # min_h = 9999
    # sum_h = 0
    # for i in range(len(h_pics)):
    #   # print(len(v_pics[i]['tags']))
    #   sum_h = sum_h + len(h_pics[i]['tags'])
    #   sum_all = sum_all + len(h_pics[i]['tags'])
    #   if(max_h < len(h_pics[i]['tags'])):
    #     max_h = len(h_pics[i]['tags'])
    #   if(min_h > len(h_pics[i]['tags'])):
    #     min_h = len(h_pics[i]['tags'])
    #   if(max_all < len(h_pics[i]['tags'])):
    #     max_all = len(h_pics[i]['tags'])
    #   if(min_all > len(h_pics[i]['tags'])):
    #     min_all = len(h_pics[i]['tags'])
    # print('sum_h = ', sum_h)
    # print('mean_h = ', sum_h/len(h_pics))
    # print('max_h = ', max_h)
    # print('min_h = ', min_h)
    # print('=================')

    print('sum_all = ', sum_all)
    print('mean_all = ', sum_all/(len(h_pics)+len(v_pics)))
    print('max_all = ', max_all)
    print('min_all = ', min_all)
    print('=================')

    # for i in range(len(pics)):
    #   for j in range(i+1,len(pics)):
    #     middle = len(pics[i]['tags'].intersection(pics[j]['tags']))
    #     left = len(pics[i]['tags']) - middle
    #     right = len(pics[j]['tags']) - middle
    #     # print(i,j,left,middle,right,min(left,middle,right))
    #     p = []
    #     p.append(str(i))
    #     p.append(str(j))
    #     p.append(str(left))
    #     p.append(str(middle))
    #     p.append(str(right))
    #     p.append(str(min(left,middle,right)))
    #     wf.write('{}\n'.format(' '.join(p)))
    wf.write('===')
    wf.close()

    # slides = h_pics + v_pics
    # # shuffle(slides)

    # wf = open('QualificationRound/{}/{}.txt'.format(sol_folder, dataset), 'w')
    # wf.write('{}\n'.format(len(slides)))
    # for slide in slides:
    #     wf.write('{}\n'.format(' '.join(slide['id'])))
    # wf.close()

    


