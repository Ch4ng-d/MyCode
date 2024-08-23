import requests

url_login="http://127.0.0.1:60942/fanyalogin"
users=[ 2441976, 724380, 9684242, 5338200, 4483308, 2966088, 7441099, 9703737, 3039401, 9679912, 1939499, 5630732, 3298056, 2937240, 1233145, 1661213, 6773543, 6031939, 4483786, 8446419, 6273946, 7872819, 3769810, 5505908, 2571388, 2499743, 771234, 1023934, 7000436, 2765141, 9427207, 2035092, 2686643, 7913589, 8869147, 7889446, 2039375, 5413993, 9717940, 1115014, 8020487, 2723168, 15218, 5381428, 4247234, 6772515, 526226, 3958885, 8652486, 9796755, 2516345, 7328329, 8874721, 8682063, 5439535, 6331608, 5366679, 1414463, 1104202, 4535584, 1586223, 4926020, 6233386, 7032261, 5696765, 6959647, 4968259, 1360484, 332819, 7938620, 6656056, 4826696, 2342767, 2021257, 2652510, 4689221, 9341962, 5404553, 6911458, 9981079, 8623225, 3072508, 1787809, 8646844, 7156296, 2843331, 465578, 4249762, 6020902, 2190400, 9316455, 9041246, 732662, 1656334, 8284265, 5110976, 7495938, 9011765, 6200509, 1778478, 8170634, 4117430, 3663896, 2783838, 8208568, 3591515, 2424563, 9287513, 8869963, 3072351, 9705862, 9916810, 7261260, 1165763, 5851973, 4880464, 5638699, 5830504, 5479924, 752306, 5280937, 2483873, 6707231, 2581910, 2156945, 9524077, 3436473, 9802743, 7751839, 8281309, 1898709, 5860349, 2658792, 2833352, 2195140, 7499631, 4794401, 4381318, 8790743, 4539260, 1814301, 6464791, 4269525, 7244372, 7511917, 6064995, 9797953, 8643106, 7787839, 5929832, 3919073, 3022476, 9978972, 1207002, 7398576, 7013217, 321537, 1149317, 7479682, 8874729, 114316, 8940937, 7578712, 7948914, 878864, 2924334, 6613751, 9562714, 2258876, 640563, 2691108, 5317994, 1429154, 1934985, 3257362, 3560187, 126941, 1920381, 8347877, 1960535, 893962, 4679344, 5043102, 9550629, 5965844, 5015018, 5609729, 4006476, 5160161, 837938, 6190813, 7451296, 5350758, 9186639, 7804257, 8030599, 693010, 9447462, 8352345, 1283453, 7864824, 2439728, 7510708, 4873258, 5545429, 3885508, 8177929, 9768349, 3128920, 2864252, 7734814, 4586778, 3505714, 3605769, 380375, 6970830, 9126866, 6129694, 3617825, 57354, 7334602, 8749494, 9905590, 620745, 3166715, 4642193, 6474470, 6093478, 6226952, 1028320, 7312251, 6933342, 8082624, 8209919, 2634475, 719207, 4450186, 4821461, 7207837, 5694022, 8022491, 1046671, 7439756, 6656382, 8384499, 8431878, 5171784, 3146454, 4458185, 8637955, 8044112, 2250368, 7066894, 5264122, 6013009, 9099968, 4639535, 7678681, 3531433, 5728487, 7723507, 9272654, 8535406, 8596929, 4238267, 100860, 7422541, 6876996, 5051669, 7138073, 5775086, 5886629, 6311845, 9160616, 4221616, 1487010, 2430964, 7164820, 2591922, 3028266, 2254781, 2950258, 3223542, 5698547, 4194785, 8755630, 4614173, 7828954, 1106954, 8257715, 8089599, 6825233, 1331618, 6255154, 544948, 1543752, 5565900, 2074211, 7127021, 8770586, 376746, 484705, 3816368, 2741477, 2441701, 1154976, 5271907, 2255117, 578801, 5587696, 5990524, 1699271, 9393019, 1319001, 548591, 2125426, 4559573, 8269719, 8803058, 8686188, 9194275, 588557, 8664503, 8393335, 3455272, 6489899, 9479534, 7209500, 8730893, 7063847, 6834951, 5658813, 7757311, 6529625, 1162279, 1537631, 172722, 5593730, 1551633, 6101892, 9811699, 1471091, 8651187, 90288, 6754156, 9753128, 1062121, 210235, 7343602, 4579114, 7603791, 5354745, 2272645, 5735746, 4621439, 9436560, 5785276, 7352761, 243086, 9004792, 3617326, 3834110, 1403106, 8128072, 322737, 6650585, 9016702, 5819552, 5046190, 5842861, 4046270, 5461560, 6049251, 3287230, 3649221, 4495358, 6265774, 2851132, 460885, 4099517, 3652025, 7208855, 2144684, 3952911, 5347888, 16890, 132065, 4651006, 6486583, 2437792, 1499212, 9724425, 8101583, 2011847, 8664695, 5869005, 1177233, 4246626, 1321103, 7004214, 4594078, 188817, 3086110, 7279101, 8368606, 3028391, 14273, 6200353, 8541013, 1936814, 2021198, 7701966, 5718928, 8689758, 821369, 7844758, 3578754, 3340020, 9304009, 1251262, 2717172, 4673702, 7046947, 452862, 2927535, 2672686, 8118658, 972564, 6032450, 8730185, 6849631, 2794790, 7813837, 4949422, 5664355, 5994841, 1139754, 4857121, 3008309, 4701023, 7148212, 7122067, 3162737, 5443223, 8773015, 3615354, 4577825, 9236079, 1741865, 5560683, 2125859, 8498812, 8302333, 4870006, 2713976, 5613684, 7962689, 9209142, 4016416, 7941347, 3198007, 9966175, 2500377, 863937, 6006919, 5356489, 9320262, 9015471, 1491620, 2206994, 5374264, 5351961, 6132940, 9377907, 8611378, 3877075, 4006891, 9412685, 8269717, 9719486, 1237549, 696513, 7499257, 5152216, 7998063, 4853640, 3676318, 5488855, 8901623, 6295869, 7869162, 1378529, 4532018, 3193553, 4030435, 4584867, 3253660, 1484410, 2827923, 9045945, 4890307, 1103701, 9740645, 2580476, 5187005, 5677162, 3453520, 3975260, 4982549, 8272296, 5933897, 509700, 6759227, 3463209, 5440781, 5037500, 6995539, 6521261, 2578752, 9545679, 3081103, 1945492, 7904036, 8469292, 9832612, 9991227, 468267, 919620, 3240792, 9548651, 7712484, 4852542, 1888340, 2160923, 7069787, 8250471, 6034615, 8689689, 145581, 9186488, 3194513, 1676553, 4636796, 8801687, 133349, 1508200, 6944431, 4416558, 5268062, 417308, 4415501, 7271726, 1778646, 1743843, 8548318, 6473999, 9167964, 5378957, 5474362, 1885730, 4343944, 5944193, 9783482, 9628668, 9413489, 3610636, 3413588, 7176481, 1677439, 2381510, 2558267, 7092484, 7828502, 7410742, 9511704, 8417427, 3435714, 7390915, 2251620, 3619508, 9548634, 716657, 5914266, 7512161, 5531090, 3309134, 8673061, 1494751, 7100101, 9383498, 6501542, 5875503, 154149, 3902116, 9149762, 5689730, 666450, 9872536, 3890404, 5488629, 687271, 7390791, 2113149, 448628, 861387, 4463656, 5575020, 7463618, 3638526, 7270416, 4063068, 4379147, 6879397, 4702115, 7692677, 5551645, 4341144, 6809393, 7843101, 4628956]
for user in users:
    session=requests.session()
    data = {
        'uname': user,
        'password': user
    }
    session.post(url_login,data)
    print(session.post(url_login,data).text)
    url_qiandao="http://127.0.0.1:60942/widget/sign/e?id=4000000000000&c=3073382159311&enc=0B5D66FE0DD49CE8E1C3B3518721C092&DB_STRATEGY=PRIMARY_KEY&STRATEGY_PARA=id"
    session.get(url_qiandao)
    print(session.get(url_qiandao).text)