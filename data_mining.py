from math import sqrt
import math
import random
from sklearn.model_selection import KFold
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def read_data_input(file):
  datas = open(file, "r").readlines()
  lists = []
  for data in datas :
    rawLine = data.split(',')
    line = []
    for r in rawLine:
      line.append(float(r))
    lists.append(line)
  return lists


def read_data_output(file):
  datas = open(file, "r").readlines()[0].split(',')
  line = []
  for data in datas:
    line.append(float(data))
  return line

def split_lines(input, seed, output1, output2):
  random.seed(seed)
  out1 = open(output1, 'w')
  out2 = open(output2, 'w')
  for line in open(input, 'r').readlines():
    if random.randint(0, 1):
      out1.write(line)
    else:
      out2.write(line)

      
def split_lines_output(input, seed, output1, output2):
  random.seed(seed)
  out1 = open(output1, 'w')
  out2 = open(output2, 'w')
  list1 = []
  list2 = []
  for line in open(input, 'r').readlines()[0].split(','):
    if random.randint(0, 1):
      list1.append(float(line))
    else:
      list2.append(float(line))
  out1.write(str(list1))
  out1.close()
  out2.write(str(list2))
  out2.close()


def simple_distance(data1, data2):
  data_length = len(data1)
  summ_power = 0.0
  for i in range(0, data_length) :
    summ_power = summ_power + pow((data1[i]-data2[i]),2)
  return sqrt(summ_power)


def k_nearest_neighbors(x, points, dist_function, k):
  
  distances = []
  i = 0
  for point in points :
    d = dist_function(x, point)
    distances.append((i, d))
    i = i+1
  distances.sort(key=lambda tup: tup[1])
  indexes = []
  for pt in distances[0:k] :
    indexes.append(pt[0])
  return indexes


def get_value_knn(x, train_x, train_y, dist_function, k):
  class1 = 0
  class2 = 0
  class3 = 0
  class4 = 0
  class5 = 0
  tab1 = []
  tab2 = []
  tab3 = []
  tab4 = []
  tab5 = []
  maxValue = 0
  max = 0
  nearests = k_nearest_neighbors(x, train_x, dist_function, k)
  verdict_nearest = train_y[nearests[0]]
  for near in nearests:
    if(train_y[near] < 1.0):
      class1 = class1 + 1
      tab1.append(train_y[near])
      if(maxValue < class1):
        maxValue = class1
        max = np.mean(tab1)
    if(train_y[near] >= 1.0 and train_y[near] < 10.0):
      class2 = class2 + 1
      tab2.append(train_y[near])
      if(maxValue < class2):
        maxValue = class2
        max = np.mean(tab2)
    if(train_y[near] >= 10.0 and train_y[near] < 40.0):
      class3 = class3 + 1
      tab3.append(train_y[near])
      if(maxValue < class3):
        maxValue = class3
        max = np.mean(tab3)
    if(train_y[near] >= 40.0 and train_y[near] < 100.0):
      class4 = class4 + 1
      tab4.append(train_y[near])
      if(maxValue < class4):
        maxValue = class4
        max = np.mean(tab4)
    if(train_y[near] > 100.0):
      class5 = class5 + 1
      tab5.append(train_y[near])
      if(maxValue < class5):
        maxValue = class5
        max = np.mean(tab5)
    
  if(class1 == class2 == class3 == class4 == class5):
    return verdict_nearest
  else:
    return max


def compare_values(v1, v2):
  if v1 < 1 and v2 < 1:
    return True
  if 1 <= v1 <= 10 and 1 <= v2 <= 10:
    return True
  if 10 <= v1 <= 40 and 10 <= v2 <= 40:
    return True
  if 40 <= v1 <= 100 and 40 <= v2 <= 100:
    return True
  if v1 > 100 and v2 > 100 :
    return True
  else : 
    return False


def eval_classifier(test_x, test_y, classifier):
  
  length_data = len(test_y)
  nbr_error = 0
  i = 0
  for elem in test_x :
    verdict_classifier = classifier(elem, read_data_input('dataset/inputTrain'),  read_data_output('dataset/outputTrain'), simple_distance, 10)
    tolereanceRate = test_y[i] * 30 / 100
    #if(abs(verdict_classifier - test_y[i]) > tolereanceRate):
    if(compare_values(verdict_classifier, test_y[i]) == False):
      nbr_error = nbr_error + 1
    i = i + 1
  print('error rate knn : ', 100 * float(nbr_error) / float(length_data))
  return (100 * float(nbr_error) / float(length_data))


def linear_regression(Xtrain, Ytrain, Xtest, Ytest):
  length_data = len(Ytest)
  model = LinearRegression()
  model.fit(Xtrain,Ytrain)
  predictions = model.predict(Xtest)
  print('\nprediction score :', model.score(Xtest, Ytest))
  print('\nprediction coeff :\n', model.coef_)
  i = 0
  nbr_error = 0
  for elem in Xtest:
    tolereanceRate = Ytest[i] * 40 / 100
    if(abs(predictions[i] - Ytest[i]) > tolereanceRate):
      nbr_error = nbr_error + 1
    i = i + 1
  print('\nerror rate knn : ', 100 * float(nbr_error) / float(length_data))
  



def cross_validation(train_x, train_y, untrained_classifier, k):
  
  global_errors = []
  kf = KFold(n_splits=4)
  for train_index, test_index in kf.split(train_x):
    data_train_x = []
    data_train_y = []
    data_test_x = []
    data_test_y = []
    for dt in train_index :
      data_train_x.append(train_x[dt])
      data_train_y.append(train_y[dt])
    for dt in test_index :
      data_test_x.append(train_x[dt])
      data_test_y.append(train_y[dt])
    
    length_data = len(data_test_y)
    nbr_error = 0
    i = 0
    for elem in data_test_x :
      verdict_classifier = untrained_classifier(elem, data_train_x,  data_train_y, simple_distance, k)
      if(compare_values(verdict_classifier, data_test_y[i]) == False):
        nbr_error = nbr_error + 1
      i = i + 1
      
    error = 100 * float(nbr_error) / float(length_data)
    global_errors.append(error)
        
  print('For k = ', k)
  print('Global error = ', (sum(global_errors)/len(global_errors)))
  return (sum(global_errors)/len(global_errors))


def sampled_range(mini, maxi, num):
  if not num:
    return []
  lmini = math.log(mini)
  lmaxi = math.log(maxi)
  ldelta = (lmaxi - lmini) / (num - 1)
  out = [x for x in set([int(math.exp(lmini + i * ldelta)) for i in range(num)])]
  out.sort()
  return out


def find_best_k(train_x, train_y, untrained_classifier_for_k):
  
  k_tests = sampled_range(1, 1, 10)
  error_ratios = []
  for k in k_tests :
    error_ratios.append((k,cross_validation(train_x, train_y, untrained_classifier_for_k, k)))
  error_ratios.sort(key=lambda tup: tup[1])
  print("error ratios ", error_ratios)
  return error_ratios[0][0]



def main():
  #eval_classifier(read_data_input('dataset/inputTest'), read_data_output('dataset/outputTest'), get_value_knn)
  #cross_validation(read_data_input('dataset/inputTrain'), read_data_output('dataset/outputTrain'), get_value_knn, 12)
  find_best_k(read_data_input('dataset/inputTrain'), read_data_output('dataset/outputTrain'), get_value_knn)
  #linear_regression(read_data_input('dataset/inputTrain'), read_data_output('dataset/outputTrain'),read_data_input('dataset/inputTest'), read_data_output('dataset/outputTest'))

#split_lines("dataset/inputData", 1, "dataset/inputTrain", "dataset/inputTest")
#split_lines_output("dataset/outputData", 1, "dataset/outputTrain", "dataset/outputTest")
#read_data_input("dataset/inputTrain")
#read_data_output("dataset/outputTrain")
main()
