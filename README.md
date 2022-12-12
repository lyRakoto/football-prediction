# football-prediction

Code portion about the cross validation of the model , the best k = 20 gives an error rate of 19.98%




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
