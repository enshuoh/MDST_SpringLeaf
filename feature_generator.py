import csv
import pickle
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.feature_selection import RFE
from sklearn.svm import SVR


train = 'train.csv'
output_file = 'train_out.csv'
use_less = [8, 9, 10, 11, 12, 43, 44, 196, 202, 216, 221, 228, 238, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 38, 39, 40,
            41, 42, 188, 189, 190, 197, 199, 203,214,215, 220, 222, 244, 392, 436,
            444, 525, 526, 528, 207, 213, 838, 845, 1426]
time_col = [73, 75, 156, 157, 158, 159, 166, 167, 168, 169, 176, 177, 178,
            179, 204, 217]
char_col = [200, 205, 236, 272, 323, 340, 402, 491]
weird_int = [226, 227, 529]


hash_dict = pickle.load(open('hash_dict.pkl'))
num_mode = pickle.load(open('num_mode.pkl'))
num_col_with_na = [6, 7, 13, 14, 15, 16, 17, 33, 34, 35, 36, 37, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 160, 161, 162, 163, 164, 165, 170, 171, 172, 173, 174, 175, 180, 181, 182, 183, 184, 185, 186, 187, 191, 192, 193, 194, 195, 198, 201, 206, 208, 209, 210, 211, 212, 218, 219, 223, 224, 226, 227, 230, 232, 233, 234, 237, 239, 240, 241, 242, 243, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 341, 342, 343, 344, 345, 346, 347, 348, 349, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 393, 394, 395, 396, 397, 398, 399, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 437, 438, 439, 440, 441, 442, 443, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 527, 529]


def gen_data(input_file, output_file):
    reader = csv.reader(open(input_file), delimiter=',')
    writer = csv.writer(open(output_file,'w'), delimiter=',')
    delete_idx = sorted(use_less + char_col + time_col + weird_int+hash_dict.keys(), reverse=True)
    x = []
    y = []
    column = reader.next()
    for data in reader:
        for idx in hash_dict:
            if isinstance(hash_dict[idx][data[idx]], list):
                data += hash_dict[idx][data[idx]]
            else:
                data.append(hash_dict[idx][data[idx]])
        for idx in num_col_with_na:
            if data[idx] == 'NA':
                data[idx] = num_mode[idx]
        for idx in delete_idx:
            del data[idx]
        y.append(int(data[-1]))
        data = data[1:]
        #data = map(float, data)
        writer.writerow(data)
    #pickle.dump(x, 'all_x.pkl')
    #pickle.dump(y, 'all_y.pkl')
def feature_selection(input_file='train_out.csv'):
    reader = csv.reader(open(input_file), delimiter=',')
    count = 0
    x = []
    y = []
    for data in reader:
        yi = int(data[-1])
        xi = map(float, data[:-1])
        x.append(xi)
        y.append(yi)
        count += 1
        if count == 10000:
            break

    x = np.array(x)
    y = np.array(y)
    estimator = SVR(kernel="linear")
    selector = RFE(estimator,0.3, step=0.3,verbose=1)
    selector = selector.fit(x, y)
    return selector.support_