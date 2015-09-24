import csv
from datetime import datetime
from math import exp, log, sqrt
from random import random
import pickle
train = 'train.csv'
test = 'test.csv' #'vali_100.tsv'
submission = 'cobblers.csv'  # path of to be outputted submission file
def check_useless_col():
    reader = csv.reader(open(train), delimiter=',')
    keys = reader.next()
    init_value = reader.next()
    check = range(len(init_value))
    for l in reader:
        remove_list = []
        for i in check:
            if l[i] != init_value[i]:
                remove_list.append(i)
        for i in remove_list[::-1]:
            check.remove(i)
            print 'remove %d' % i
    return sorted(check)
def get_na_average_value():
    num_col_with_na = [6, 7, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 160, 161, 162, 163, 164, 165, 170, 171, 172, 173, 174, 175, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 197, 198, 199, 201, 203, 206, 208, 209, 210, 211, 212, 215, 218, 219, 220, 222, 223, 224, 226, 227, 230, 232, 233, 234, 237, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 341, 342, 343, 344, 345, 346, 347, 348, 349, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529]
    reader = csv.reader(open(train), delimiter=',')

    num_na_dict = {}
    for i in num_col_with_na:
        num_na_dict[i] = []
    head = reader.next
    for l in reader:
        for idx in num_col_with_na:
            print l[idx]
            if l[idx] != 'NA':
                num_na_dict[idx][l[idx]] = 0
    reader = csv.reader(open(train), delimiter=',')
    head = reader.next
    for l in reader:
        for idx in num_col_with_na:
            if l[idx] != 'NA':
                num_na_dict[idx][l[idx]] += 1
    return num_na_dict
def check_for_range_and_count():
    reader = csv.reader(open(train), delimiter=',')
    use_less = [207, 213, 838, 845, 1426]
    char_col = [1, 5, 8, 9, 10, 11, 12, 43, 44, 196, 200, 202, 205, 214,
                216, 221, 225, 228, 229, 231, 235, 236, 238, 272, 281, 303,
                323, 340, 350, 351, 352, 402, 464, 465, 491, 1932]
    time_col = [73, 75, 156, 157, 158, 159, 166, 167, 168, 169, 176, 177, 178,
                179, 204, 217]

    num_col = range(0, len(reader.next()))
    non_num_col = sorted(use_less + char_col + time_col, reverse=True)
    for idx in non_num_col:
        del num_col[idx]

    num_col = num_col[1:-1]

    attribute_dict = {}
    for idx in non_num_col:
        attribute_dict[idx] = {}

    for idx in num_col:
        attribute_dict[idx] = [None, None]

    for l in reader:
        for idx in non_num_col:
            attribute_dict[idx][l[idx]] = 0

    error_set = set()
    reader = csv.reader(open(train), delimiter=',')
    head = reader.next()
    for l in reader:
        for idx in non_num_col:
            attribute_dict[idx][l[idx]] += 1
        for idx in num_col:
            if l[idx] == 'NA':
                error_set.add(idx)
                continue
            if attribute_dict[idx][0] is None:
                attribute_dict[idx][0] = float(l[idx])
            else:
                if attribute_dict[idx][0] > float(l[idx]):
                    attribute_dict[idx][0] = float(l[idx])
            if attribute_dict[idx][1] is None:
                attribute_dict[idx][1] = float(l[idx])
            else:
                if attribute_dict[idx][1] < float(l[idx]):
                    attribute_dict[idx][1] = float(l[idx])
    return attribute_dict, error_set


# # B, model
# alpha = .005  # learning rate
# beta = 1.   # smoothing parameter for adaptive learning rate
# L1 = 0.     # L1 regularization, larger value means more regularized
# L2 = 1.     # L2 regularization, larger value means more regularized

# # C, feature/hash trick
# D = 2 ** 24             # number of weights to use
# interaction = False     # whether to enable poly2 feature interactions

# # D, training/validation
# epoch = 1       # learn training data for N passes
# holdafter = 9   # data after date N (exclusive) are used as validation
# holdout = None  # use every N training instance for holdout validation


# ##############################################################################
# # class, function, generator definitions #####################################
# ##############################################################################

# class ftrl_proximal(object):
#     ''' Our main algorithm: Follow the regularized leader - proximal

#         In short,
#         this is an adaptive-learning-rate sparse logistic-regression with
#         efficient L1-L2-regularization

#         Reference:
#         http://www.eecs.tufts.edu/~dsculley/papers/ad-click-prediction.pdf
#     '''

#     def __init__(self, alpha, beta, L1, L2, D, interaction):
#         # parameters
#         self.alpha = alpha
#         self.beta = beta
#         self.L1 = L1
#         self.L2 = L2

#         # feature related parameters
#         self.D = D
#         self.interaction = interaction

#         # model
#         # n: squared sum of past gradients
#         # z: weights
#         # w: lazy weights
#         self.n = [0.] * D
#         self.z = [random() for k in range(D)]#[0.] * D
#         self.w = {}

#     def _indices(self, x):
#         ''' A helper generator that yields the indices in x

#             The purpose of this generator is to make the following
#             code a bit cleaner when doing feature interaction.
#         '''

#         # first yield idx of the bias term
#         yield 0

#         # then yield the normal indices
#         for idx in x:
#             yield idx

#         # now yield interactions (if applicable)
#         if self.interaction:
#             D = self.D
#             L = len(x)

#             x = sorted(x)
#             for i in xrange(L):
#                 for j in xrange(i+1, L):
#                     # one-hot encode interactions with hash trick
#                     yield abs(hash(str(x[i]) + '_' + str(x[j]))) % D

#     def predict(self, x):
#         ''' Get probability estimation on x

#             INPUT:
#                 x: features

#             OUTPUT:
#                 probability of p(y = 1 | x; w)
#         '''

#         # parameters
#         alpha = self.alpha
#         beta = self.beta
#         L1 = self.L1
#         L2 = self.L2

#         # model
#         n = self.n
#         z = self.z
#         w = {}

#         # wTx is the inner product of w and x
#         wTx = 0.
#         for i in self._indices(x):
#             sign = -1. if z[i] < 0 else 1.  # get sign of z[i]

#             # build w on the fly using z and n, hence the name - lazy weights
#             # we are doing this at prediction instead of update time is because
#             # this allows us for not storing the complete w
#             if sign * z[i] <= L1:
#                 # w[i] vanishes due to L1 regularization
#                 w[i] = 0.
#             else:
#                 # apply prediction time L1, L2 regularization to z and get w
#                 w[i] = (sign * L1 - z[i]) / ((beta + sqrt(n[i])) / alpha + L2)

#             wTx += w[i]

#         # cache the current w for update stage
#         self.w = w

#         # bounded sigmoid function, this is the probability estimation
#         return 1. / (1. + exp(-max(min(wTx, 35.), -35.)))

#     def update(self, x, p, y):
#         ''' Update model using x, p, y

#             INPUT:
#                 x: feature, a list of indices
#                 p: click probability prediction of our model
#                 y: answer

#             MODIFIES:
#                 self.n: increase by squared gradient
#                 self.z: weights
#         '''

#         # parameter
#         alpha = self.alpha

#         # model
#         n = self.n
#         z = self.z
#         w = self.w

#         # gradient under logloss
#         g = p - y

#         # update z and n
#         for i in self._indices(x):
#             sigma = (sqrt(n[i] + g * g) - sqrt(n[i])) / alpha
#             z[i] += g - sigma * w[i]
#             n[i] += g * g


# def logloss(p, y):
#     ''' FUNCTION: Bounded logloss

#         INPUT:
#             p: our prediction
#             y: real answer

#         OUTPUT:
#             logarithmic loss of p given y
#     '''

#     p = max(min(p, 1. - 10e-15), 10e-15)
#     return -log(p) if y == 1. else -log(1. - p)


# def data(path, D):
#     ''' GENERATOR: Apply hash-trick to the original csv row
#                    and for simplicity, we one-hot-encode everything

#         INPUT:
#             path: path to training or testing file
#             D: the max idx that we can hash to

#         YIELDS:
#             ID: id of the instance, mainly useless
#             x: a list of hashed and one-hot-encoded 'indices'
#                we only need the idx since all values are either 0 or 1
#             y: y = 1 if we have a click, else we have y = 0
#     '''

#     for t, row in enumerate(DictReader(open(path), delimiter=',')):
#         # process id
#         #print row
#         try:
#             ID=row['ID']
#             del row['ID']
#         except:
#             pass
#         # process clicks
#         y = 0.
#         target='target'#'IsClick' 
#         if target in row:
#             if row[target] == '1':
#                 y = 1.
#             del row[target]

#         # extract date

#         # turn hour really into hour, it was originally YYMMDDHH

#         # build x
#         x = []
#         for key in row:
#             value = row[key]

#             # one-hot encode everything with hash trick
#             idx = abs(hash(key + '_' + value)) % D
#             x.append(idx)

#         yield ID,  x, y


# ##############################################################################
# # start training #############################################################
# ##############################################################################

# start = datetime.now()

# # initialize ourselves a learner
# learner = ftrl_proximal(alpha, beta, L1, L2, D, interaction)

# # start training
# for e in range(epoch):
#     loss = 0.
#     count = 0
#     for t,  x, y in data(train, D):  # data is a generator

#         p = learner.predict(x)
#         loss += logloss(p, y)
#         learner.update(x, p, y)
#         count+=1
#         if count%1000==0:
#             #print count,loss/count
#             print('%s\tencountered: %d\tcurrent logloss: %f' % (
#                 datetime.now(), count, loss/count))
#         if count>10000: # comment this out when you run it locally.
#             break


# count=0
# loss=0
# #import pickle
# #pickle.dump(learner,open('ftrl3.p','w'))
# print ('write result')
# ##############################################################################
# # start testing, and build Kaggle's submission file ##########################
# ##############################################################################
# with open(submission, 'w') as outfile:
#     outfile.write('ID,target\n')
#     for  ID, x, y in data(test, D):
#         count+=1
#         p = learner.predict(x)
#         loss += logloss(p, y)

#         outfile.write('%s,%s\n' % (ID, str(p)))
#         if count%1000==0:
#             #print count,loss/count
#             print('%s\tencountered: %d\tcurrent logloss: %f' % (
#                 datetime.now(), count, loss/count))