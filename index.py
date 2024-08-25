import numpy as np
import pandas as pd

# sectors = np.arange(1,50).tolist()
# sectors_dict = {}
# for k in sectors:
#     g = k
#     while len(str(k)) > 1:
#         cop = str(k)
#         upd = 0
#         for c in cop:
#             upd+=int(c)
#         k = upd
#         sectors_dict.update({g:upd})
#     else:
#         sectors_dict.update({k:k})
# sectors_array = [[],[],[],[],[],[],[],[],[]]
# for o in range(len(sectors_array)):
#     h = []
#     for k,v in sectors_dict.items():
#         if v == o+1:
#             h.append({v:k})
#     sectors_array[o]=h

# oneone=[1,10,19,28,37,46]
# twotwo=[2,11,20,29,38,47]
# threethree=[3,12,21,30,39,48]
# fourfour=[4,13,22,31,40,49]
# fivefive=[5,14,23,32,41]
# sixsix=[6,15,24,33,42]
# sevenseven=[7,16,25,34,43]
# eighteight=[8,17,26,35,44]
# ninenine=[9,18,27,36,45]
# within=[oneone,twotwo,threethree,fourfour,fivefive,
#         sixsix,sevenseven,eighteight,ninenine]

# def reduce(n):
#     while len(str(n))>1:
#         f = str(n)
#         g = 0
#         for h in f:
#             g+=int(h)
#         n=g
#     return n

# former_analysiss_categories=[['11211', 83], ['21111', 70], ['12111', 55], ['11121', 54], ['11112', 44], 
# ['02211', 41], ['21210', 36], ['20112', 36], ['11022', 35], ['22110', 33], ['10221', 32], ['12210', 32], 
# ['20121', 31], ['12201', 31], ['11220', 31], ['21102', 30], ['21021', 30], ['22101', 30], ['12120', 29], 
# ['21120', 28], ['01221', 28], ['11202', 28], ['20211', 28], ['22011', 27], ['11130', 27], ['21201', 26], 
# ['02121', 26], ['12012', 26], ['01212', 25], ['12102', 25], ['02112', 25], ['12021', 24], ['10122', 24], 
# ['13110', 23], ['11031', 20], ['10212', 19], ['03111', 19], ['01122', 18], ['02202', 18], ['21012', 18], 
# ['13011', 17], ['02022', 17], ['31110', 16], ['11013', 16], ['30111', 15], ['20220', 14], ['11103', 14], 
# ['20022', 14], ['20130', 14], ['01131', 14], ['30210', 13], ['00321', 13], ['00222', 13], ['00231', 13], 
# ['31020', 13], ['22002', 13], ['31011', 12], ['00312', 12], ['10230', 12], ['30120', 12], ['13101', 12], 
# ['02220', 12], ['01311', 12], ['10311', 11], ['23010', 11], ['11301', 11], ['02013', 11], ['23100', 11], 
# ['13200', 11], ['10320', 10], ['20202', 10], ['10113', 10], ['10131', 10], ['31101', 10], ['11310', 10], 
# ['32010', 10], ['21300', 9], ['03012', 9], ['31200', 9], ['10302', 8], ['03120', 8], ['13002', 8], ['20103', 8], 
# ['03021', 8], ['12300', 8], ['01230', 8], ['22200', 8], ['02031', 8], ['32100', 7], ['20301', 7], ['21003', 7], 
# ['01113', 7], ['13020', 7], ['22020', 7], ['32001', 7], ['03201', 7], ['30102', 7], ['10140', 7], ['01320', 7], 
# ['03210', 7], ['30201', 7], ['02310', 7], ['03102', 6], ['01302', 6], ['12003', 6], ['20310', 6], ['02301', 6], 
# ['00213', 5], ['04011', 5], ['01401', 5], ['20013', 5], ['04110', 5], ['31002', 5], ['10023', 5], ['04200', 5], 
# ['10032', 5], ['30021', 5], ['00132', 5], ['00411', 5], ['40020', 5], ['12030', 5], ['10203', 5], ['23001', 5], 
# ['41001', 5], ['41100', 4], ['21030', 4], ['02130', 4], ['00123', 4], ['01410', 4], ['02103', 4], ['04101', 4], 
# ['00330', 4], ['20031', 4], ['01203', 4], ['14010', 4], ['14001', 4], ['40200', 4], ['11040', 4], ['30300', 3], 
# ['40110', 3], ['30012', 3], ['20400', 3], ['03003', 3], ['11400', 3], ['10401', 3], ['01023', 3], ['14100', 3], 
# ['02400', 3], ['03300', 3], ['00141', 2], ['40101', 2], ['40011', 2], ['01032', 2], ['01041', 2], ['01140', 2], 
# ['02040', 2], ['03030', 2], ['10041', 2], ['30030', 2], ['04020', 1], ['04002', 1], ['00402', 1], ['00303', 1], 
# ['41010', 1]]

# ffgff = []
# for i in former_analysiss_categories:
#     ffgff.append(i[1])

# we=[]
# for i in former_analysiss_categories:
#     we.append(i[0])

# section=int(input("section:"))

number89 = [ 
    [6,16,23,26,27,37],
    [3,6,15,20,28,31],
    [5,16,31,34,43,48],
    [1,12,19,27,35,37]
]
number90 = [ 
    [17,24,30,33,37,48],
    [1,11,16,33,40,48],
    [2,6,17,28,41,42],
    [1,2,3,11,27,34]
]
number95 = [ 
    [7,11,14,15,29,30],
    [7,17,23,35,37,42],
    [5,11,14,16,45,46],
    [8,14,18,25,46,47]
]
number96 = [ 
    [9,13,19,21,30,41],
    [3,4,6,23,30,48],
    [6,9,22,42,43,45],
    [10,12,21,36,37,45]
]
number97 = [
    [5,18,24,42,44,46],
    [2,20,34,38,47,48],
    [2,5,12,25,40,42],
    [3,5,28,38,39,44]
]
number98 = [
    [1,3,22,32,37,48],
    [7,18,20,25,45,46],
    [17,24,30,36,40,46],
    [7,27,30,40,41,47]
]
number99 = [ 
    [5,8,23,39,40,45],
    [2,6,7,11,23,26],
    [19,29,32,38,39,46],
    [9,10,13,14,26,48]
]
number101 = [ 
    [9,26,27,38,39,49],
    [18,19,21,28,45,49],
    [14,18,24,36,37,46],
    [18,21,27,30,37,41]
]
number102 = [ 
    [2,23,26,38,42,47],
    [25,29,30,31,45,47],
    [3,32,33,35,45,46],
    [3,15,37,40,43,49]
]
number103 = [
    [1,4,5,19,27,36],
    [24,25,30,31,38,42],
    [19,21,23,30,38,39],
    [4,10,15,16,42,47]
]
number104 = [
    [1,19,21,43,47,49],
    [7,19,27,32,44,49],
    [3,13,20,33,35,36],
    [5,12,30,31,40,49]
]
number105 = [
    [8,13,17,26,31,44],
    [1,13,18,19,22,46],
    [14,15,23,33,42,46],
    [9,10,13,20,39,43]
]
number106 = [
    [4,12,16,42,45,49],
    [10,22,26,29,33,38],
    [1,12,23,28,31,32],
    [12,25,36,39,45,48]
]
number107 = [
    [6,11,17,21,37,41],
    [7,11,18,26,46,49],
    [1,3,8,33,44,47],
    [2,6,17,25,32,40]
]
number108 = [
    [8,10,22,25,34,35],
    [11,17,26,32,34,40],
    [7,25,34,37,43,44],
    [2,5,25,30,32,34]
]
number109 = [
    [2,5,15,23,29,40],
    [2,4,14,24,38,41],
    [3,5,10,26,31,43],
    [7,9,13,14,32,40]
]
number110 = [
    [8,17,30,40,44,49],
    [5,18,25,38,45,46],
    [8,10,14,23,30,34],
    [11,25,28,32,36,45]
]
number111 = [
    [20,22,23,31,47,48],
    [4,10,19,30,35,41],
    [13,19,37,44,47,48],
    [3,5,19,33,35,49]
]
number112 = [
    [8,13,23,24,29,33],
    [8,10,13,31,33,37],
    [4,14,18,27,41,45],
    [4,11,12,13,39,44]
]
number113 = [
    [7,10,13,24,40,49],
    [4,13,15,29,40,43],
    [5,9,16,22,31,49],
    [1,13,19,36,40,42]
]
number114 = [
    [9,10,21,26,43,47],
    [8,29,30,37,46,47],
    [7,8,15,20,25,30],
    [7,8,17,35,45,46]
]
number115 = [
    [7,12,20,25,34,43],
    [5,13,14,15,36,47],
    [1,3,4,9,34,43],
    [3,5,19,27,31,35]
]
number116 = [
    [3,6,9,39,43,45],
    [7,15,25,29,30,38],
    [1,6,7,8,23,29],
    [11,14,18,21,26,30]
]
number117 = [
    [14,28,37,38,42,46],
    [2,8,18,29,37,38],
    [7,8,17,22,26,45],
    [22,24,34,36,44,46]
]
number118 = [
    [9,25,36,37,46,47],
    [3,27,36,37,41,45],
    [1,6,9,16,18,42],
    [1,11,15,20,25,43]
]
number119 = [
    [2,8,9,21,38,42],
    [2,13,14,25,41,45],
    [4,5,8,11,28,36],
    [6,21,23,29,37,39]
]
number120 = [
    [6,16,30,39,45,46],
    [3,14,17,35,39,47],
    [16,18,19,20,28,31],
    [25,31,33,34,39,40]
]
number121 = [
    [3,10,23,32,40,41],
    [6,13,28,34,45,46],
    [10,20,21,23,32,37],
    [1,27,35,36,42,44]
]
number123 = [
    [13,20,29,41,43,47],
    [5,17,34,37,39,43],
    [18,23,24,27,29,39],
    [4,6,15,18,23,44]
]
number125= [
    [3,9,25,35,38,42],
    [9,18,21,24,32,48],
    [1,2,3,14,18,28],
    [6,7,36,40,45,46]
]
number128 = [
    [7,14,18,25,43,49],
    [1,7,23,26,28,49],
    [5,9,14,23,29,39],
    [9,13,16,21,33,40]
]
number130 = [
    [4,20,24,33,39,47],
    [9,12,13,28,30,36],
    [3,28,29,37,42,48],
    [3,9,14,17,33,40]
]
number134 = [
    [7,14,22,37,41,42],
    [4,11,13,16,20,30],
    [10,15,25,32,33,35],
    [4,9,15,23,43,46]
]
number138 = [
    [8,16,17,19,33,49],
    [15,20,22,25,33,44],
    [9,14,31,37,39,41],
    [7,12,21,30,32,43]
]
number141 = [
    [2,7,13,20,32,43],
    [3,4,21,26,32,35],
    [17,18,23,26,38,39],
    [11,17,20,34,35,38]
]
number142 = [
    [9,17,24,25,40,44],
    [9,14,39,40,45,46],
    [3,6,16,42,47,49],
    [1,15,27,34,40,43]
]
number143 = [
    [2,5,6,33,38,48],
    [14,22,24,29,34,35],
    [1,18,26,30,39,44],
    [12,13,19,29,43,48]
]
number24_002 = [
    [3,8,14,21,26,48],
    [2,7,11,23,33,37],
    [1,2,3,6,16,34],
    [1,5,6,24,27,28]
]
number24_003 = [
    [3,11,17,26,47,48],
    [8,9,15,26,31,37],
    [2,10,28,35,43,45],
    [1,2,15,22,26,42]
]
number24_007 = [
    [4,9,18,23,33,47],
    [13,15,16,18,23,48],
    [4,17,21,23,42,45],
    [1,2,15,32,35,38]
]
number24_014 = [
    [12,14,25,30,39,48],
    [1,10,13,25,32,38],
    [5,12,19,22,26,34],
    [5,8,16,18,24,37]
]
number24_064 = [
    [2,12,16,20,25,26],
    [13,22,27,28,34,48],
    [6,8,11,39,40,49],
    [13,18,24,35,40,49]
]
number24_065 = [
    [14,32,37,38,42,49],
    [1,3,5,14,20,41],
    [13,16,27,29,35,44],
    [7,25,36,38,45,46]
]
locker=[
    number89,number90,number95,number96,number97,number98,number99,number101,number102,
    number103,number104,number105,number106,number107,number108,number109,number110,number111,
    number112,number113,number114,number115,number116,number117,number118,number119,number120,
    number121,number123,number125,number128,number130,number134,number138,number141,number142,
    number143,number24_002,number24_003,number24_007,number24_014,number24_064,number24_065
]
# number=locker[section]

# t_name = [key for key, value in locals().items() if value == locker[section]][0]

# print("2023 issue: "+t_name.split("number")[1])

# recycle=[]
# duplicate = []
# for k in range(len(number)):
#     j = np.arange(0,4).tolist()
#     els = [r for r in j if r != k]
#     for g in number[k]:
#         if g in number[els[0]] or g in number[els[1]] or g in number[els[2]]:
#             duplicate.append(g)
# duplicate=sorted(list(set(duplicate)))
# remain = []
# for h in range(len(number)):
#     for f in number[h]:
#         if f not in duplicate:
#             remain.append(f)
# remain=sorted(remain)

# number_set = duplicate+remain
# print("number set:\n",number_set)

# safe = [reduce(i) for i in duplicate]
# print("duplicate:\n",duplicate)

# leadd = []
# for i in duplicate:
#     leadd.append(reduce(i))
# leadd=sorted(leadd)
# lead=[]
# for i in leadd:
#     if i not in lead:
#         lead.append(i)

# plural_set = []
# singular_set = []
# for i in range(len(sectors_array)):
#     if sectors_array[i][0][i+1] in lead:
#         if i+1 in [1,2,3,4]:
#             plural_set.append(sectors_array[i])
#         else:
#             singular_set.append(sectors_array[i])

# keys = [j for i in singular_set for j in i[0].keys()];keys=sorted(keys)
# els = [i for i in lead if i not in keys];els=sorted(els)

# singular_filter = []
# plural_filter = []
# for i in els:
#     plural_filter.append([i,[]])
# for i in keys:
#     singular_filter.append([i,[]])
# for i in range(len(singular_set)):
#     for j in singular_set[i]:
#         if j[lead[i+len(plural_set)]] not in number_set:
#             re = reduce(j[lead[i+len(plural_set)]])
#             singular_filter[keys.index(re)][1].append(j[lead[i+len(plural_set)]])
#         else:
#             recycle.append(j[lead[i+len(plural_set)]])
# for i in range(len(plural_set)):
#     for h in plural_set[i]:
#         if h[lead[i]] not in number_set:
#             re = reduce(h[lead[i]])
#             plural_filter[els.index(re)][1].append(h[lead[i]])
#         else:
#             recycle.append(h[lead[i]])

# nextx = [k for k in np.arange(1,10).tolist() if k not in lead]
# print(lead,nextx)
# flow = []
# passage = []
# for i in range(len(sectors_array)):
#     if sectors_array[i][0][i+1] in nextx:
#         if i+1 in [1,2,3,4]:
#             flow.append(sectors_array[i])
#         else:
#             passage.append(sectors_array[i])

# next_f = [i for i in nextx if i not in [5,6,7,8,9]]
# next_p = [i for i in nextx if i not in next_f]

# next_plural_filter=[]
# next_singular_filter=[]
# for i in next_f:
#     next_plural_filter.append([i,[]])
# for i in next_p:
#     next_singular_filter.append([i,[]])
# for i in range(len(flow)):
#     for g in flow[i]:
#         if g[next_f[i]] not in number_set:
#             next_plural_filter[next_f.index(reduce(g[next_f[i]]))][1].append(g[next_f[i]])
#         else:
#             recycle.append(g[next_f[i]])
# for i in range(len(passage)):
#     for g in passage[i]:
#         if g[next_p[i]] in number_set:
#             next_singular_filter[next_p.index(reduce(g[next_p[i]]))][1].append(g[next_p[i]])
#         else:
#             recycle.append(g[next_p[i]])
# print("#%3 items:\n",singular_filter)
# print("#%2 items:\n",plural_filter)
# print("next #%3 items:\n",next_singular_filter)
# print("next #%2 items:\n",next_plural_filter)

# possible = []
# for i in plural_filter:
#     for j in i[1]:
#         possible.append(j)
# for i in singular_filter:
#     for j in i[1]:
#         possible.append(j)
# for i in next_singular_filter:
#     for j in i[1]:
#         possible.append(j)
# for i in next_plural_filter:
#     for j in i[1]:
#         possible.append(j)
# print("################################################################################\npossible list:\n",
# sorted(possible))
# print("possible len:",len(possible))
# print("left list:\n",sorted(list(set(recycle))))
# print("left len:",len(list(set(recycle))))

actual_answers=[
    [2,3,4,13,18,42],[3,12,13,17,24,36],[6,18,29,31,44,46],[16,26,31,35,39,46],
    [3,6,7,33,36,46],[10,15,17,21,40,44],[15,20,25,39,45,48],[20,22,24,25,29,49],[4,6,19,32,39,42],
    [4,10,12,16,30,32],[17,27,30,31,32,38],[10,24,34,40,41,45],[8,9,10,27,35,38],[1,10,22,28,33,46],
    [3,27,28,35,44,46],[9,12,30,31,45,48],[6,8,11,26,35,47],[8,16,32,39,40,43],[2,11,20,29,41,49],
    [4,9,12,36,43,47],[1,12,22,23,34,39],[2,13,23,28,30,31],[1,29,31,42,47,48],[8,18,24,34,41,42],
    [1,13,18,32,34,49],[6,8,12,31,32,46],[19,20,29,45,48,49],[11,16,27,32,33,37],[3,14,32,37,43,47],
    [7,16,26,31,47,49],[2,15,27,36,37,48],[6,25,29,30,34,35],[3,14,20,30,38,42],[27,28,37,38,43,45],
    [3,4,11,37,44,48],[4,9,13,33,35,46],[1,10,12,33,46,49],[1,4,24,31,33,34],[3,9,16,19,33,35],[2,10,17,46,47,49],
    [3,7,21,32,36,47],[6,11,19,21,27,43],[6,9,12,17,19,42]
]
# recorded_log=[]
# if section<=len(actual_answers)-1:
#     counter=0
#     print(actual_answers[section])
#     for i in possible:
#         if i in actual_answers[section]:
#             counter+=1
#     print("{} in possible".format(counter))
#     distr=[1 if i % 2 == 0 else 0 for i in actual_answers[section]]
# revised = [[i+1,[],0] for i in range(0,9)]
# for i in number_set:
#     revised[reduce(i)-1][1].append(i)
#     revised[reduce(i)-1][2]=len(revised[reduce(i)-1][1])
# print("revised of number_set counting:")
# for i in revised:
#     print("category: ",revised.index(i)+1,i[1])

r1,r2,r3,r4=[],[],[],[]
for i in locker:
    r1.append(i[0])
    r2.append(i[1])
    r3.append(i[2])
    r4.append(i[3])
ans=[]
for i in actual_answers:
    ans.append(i)
df = pd.DataFrame({
    "r1":r1,
    "r2":r2,
    "r3":r3,
    "r4":r4,
    "ans":ans,
})
df.to_csv("his.csv")