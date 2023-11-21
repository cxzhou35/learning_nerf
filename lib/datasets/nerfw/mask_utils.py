
def get_class_ids_from_labels(labels):
    ids = []
    for l in labels:
        ids.append(label_id_mapping_ade20k[l])
    return ids

def get_label_id_mapping():
    return label_id_mapping_ade20k

id_label_mapping_ade20k = {
  0: 'wall',
  1: 'building',
  2: 'sky',
  3: 'floor',
  4: 'tree',
  5: 'ceiling',
  6: 'road',
  7: 'bed ',
  8: 'windowpane',
  9: 'grass',
  10: 'cabinet',
  11: 'sidewalk',
  12: 'person',
  13: 'earth',
  14: 'door',
  15: 'table',
  16: 'mountain',
  17: 'plant',
  18: 'curtain',
  19: 'chair',
  20: 'car',
  21: 'water',
  22: 'painting',
  23: 'sofa',
  24: 'shelf',
  25: 'house',
  26: 'sea',
  27: 'mirror',
  28: 'rug',
  29: 'field',
  30: 'armchair',
  31: 'seat',
  32: 'fence',
  33: 'desk',
  34: 'rock',
  35: 'wardrobe',
  36: 'lamp',
  37: 'bathtub',
  38: 'railing',
  39: 'cushion',
  40: 'base',
  41: 'box',
  42: 'column',
  43: 'signboard',
  44: 'chest of drawers',
  45: 'counter',
  46: 'sand',
  47: 'sink',
  48: 'skyscraper',
  49: 'fireplace',
  50: 'refrigerator',
  51: 'grandstand',
  52: 'path',
  53: 'stairs',
  54: 'runway',
  55: 'case',
  56: 'pool table',
  57: 'pillow',
  58: 'screen door',
  59: 'stairway',
  60: 'river',
  61: 'bridge',
  62: 'bookcase',
  63: 'blind',
  64: 'coffee table',
  65: 'toilet',
  66: 'flower',
  67: 'book',
  68: 'hill',
  69: 'bench',
  70: 'countertop',
  71: 'stove',
  72: 'palm',
  73: 'kitchen island',
  74: 'computer',
  75: 'swivel chair',
  76: 'boat',
  77: 'bar',
  78: 'arcade machine',
  79: 'hovel',
  80: 'bus',
  81: 'towel',
  82: 'light',
  83: 'truck',
  84: 'tower',
  85: 'chandelier',
  86: 'awning',
  87: 'streetlight',
  88: 'booth',
  89: 'television receiver',
  90: 'airplane',
  91: 'dirt track',
  92: 'apparel',
  93: 'pole',
  94: 'land',
  95: 'bannister',
  96: 'escalator',
  97: 'ottoman',
  98: 'bottle',
  99: 'buffet',
  100: 'poster',
  101: 'stage',
  102: 'van',
  103: 'ship',
  104: 'fountain',
  105: 'conveyer belt',
  106: 'canopy',
  107: 'washer',
  108: 'plaything',
  109: 'swimming pool',
  110: 'stool',
  111: 'barrel',
  112: 'basket',
  113: 'waterfall',
  114: 'tent',
  115: 'bag',
  116: 'minibike',
  117: 'cradle',
  118: 'oven',
  119: 'ball',
  120: 'food',
  121: 'step',
  122: 'tank',
  123: 'trade name',
  124: 'microwave',
  125: 'pot',
  126: 'animal',
  127: 'bicycle',
  128: 'lake',
  129: 'dishwasher',
  130: 'screen',
  131: 'blanket',
  132: 'sculpture',
  133: 'hood',
  134: 'sconce',
  135: 'vase',
  136: 'traffic light',
  137: 'tray',
  138: 'ashcan',
  139: 'fan',
  140: 'pier',
  141: 'crt screen',
  142: 'plate',
  143: 'monitor',
  144: 'bulletin board',
  145: 'shower',
  146: 'radiator',
  147: 'glass',
  148: 'clock',
  149: 'flag'
}

label_id_mapping_ade20k = {
  'airplane': 90,
  'animal': 126,
  'apparel': 92,
  'arcade machine': 78,
  'armchair': 30,
  'ashcan': 138,
  'awning': 86,
  'bag': 115,
  'ball': 119,
  'bannister': 95,
  'bar': 77,
  'barrel': 111,
  'base': 40,
  'basket': 112,
  'bathtub': 37,
  'bed ': 7,
  'bench': 69,
  'bicycle': 127,
  'blanket': 131,
  'blind': 63,
  'boat': 76,
  'book': 67,
  'bookcase': 62,
  'booth': 88,
  'bottle': 98,
  'box': 41,
  'bridge': 61,
  'buffet': 99,
  'building': 1,
  'bulletin board': 144,
  'bus': 80,
  'cabinet': 10,
  'canopy': 106,
  'car': 20,
  'case': 55,
  'ceiling': 5,
  'chair': 19,
  'chandelier': 85,
  'chest of drawers': 44,
  'clock': 148,
  'coffee table': 64,
  'column': 42,
  'computer': 74,
  'conveyer belt': 105,
  'counter': 45,
  'countertop': 70,
  'cradle': 117,
  'crt screen': 141,
  'curtain': 18,
  'cushion': 39,
  'desk': 33,
  'dirt track': 91,
  'dishwasher': 129,
  'door': 14,
  'earth': 13,
  'escalator': 96,
  'fan': 139,
  'fence': 32,
  'field': 29,
  'fireplace': 49,
  'flag': 149,
  'floor': 3,
  'flower': 66,
  'food': 120,
  'fountain': 104,
  'glass': 147,
  'grandstand': 51,
  'grass': 9,
  'hill': 68,
  'hood': 133,
  'house': 25,
  'hovel': 79,
  'kitchen island': 73,
  'lake': 128,
  'lamp': 36,
  'land': 94,
  'light': 82,
  'microwave': 124,
  'minibike': 116,
  'mirror': 27,
  'monitor': 143,
  'mountain': 16,
  'ottoman': 97,
  'oven': 118,
  'painting': 22,
  'palm': 72,
  'path': 52,
  'person': 12,
  'pier': 140,
  'pillow': 57,
  'plant': 17,
  'plate': 142,
  'plaything': 108,
  'pole': 93,
  'pool table': 56,
  'poster': 100,
  'pot': 125,
  'radiator': 146,
  'railing': 38,
  'refrigerator': 50,
  'river': 60,
  'road': 6,
  'rock': 34,
  'rug': 28,
  'runway': 54,
  'sand': 46,
  'sconce': 134,
  'screen': 130,
  'screen door': 58,
  'sculpture': 132,
  'sea': 26,
  'seat': 31,
  'shelf': 24,
  'ship': 103,
  'shower': 145,
  'sidewalk': 11,
  'signboard': 43,
  'sink': 47,
  'sky': 2,
  'skyscraper': 48,
  'sofa': 23,
  'stage': 101,
  'stairs': 53,
  'stairway': 59,
  'step': 121,
  'stool': 110,
  'stove': 71,
  'streetlight': 87,
  'swimming pool': 109,
  'swivel chair': 75,
  'table': 15,
  'tank': 122,
  'television receiver': 89,
  'tent': 114,
  'toilet': 65,
  'towel': 81,
  'tower': 84,
  'trade name': 123,
  'traffic light': 136,
  'tray': 137,
  'tree': 4,
  'truck': 83,
  'van': 102,
  'vase': 135,
  'wall': 0,
  'wardrobe': 35,
  'washer': 107,
  'water': 21,
  'waterfall': 113,
  'windowpane': 8
}