#this is scartch code for hw 5 to brute force runs and extract by no means is this complete needs total overhaul and refactor to match design pattern this is a todo
#not part of the assignment or class but just needed something to brute force run and extract 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib

def reading_confusion_matrix(filepath):
    s = open(filepath, 'r').read()
    s = s.replace("\n", " ")
    s = s.split(" ")
    s = [int(i) for i in s if i.isnumeric()]
    s = s[-4:]
    return s

def reading_test_confusion_matrix(filepath):
    s = open(filepath, 'r').read()
    s = s.replace("\n", " ")
    s = s.split(" ")
    s = [int(i) for i in s if i.isnumeric()]
    s = s[-4:]
    return s

def run():
    #list_of_costs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #for cost in list_of_costs:
       # file_object = open("FIT" + str(cost) + ".arff", "w")
        #file_object.close()
        #os.system('java -cp ../weka-3-9-5/weka.jar  weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 {0}; 1.0 0.0]" -S 1 -W weka.classifiers.functions.Logistic -num-decimal-places 4 -t C:\\Users\\A_mah\\PycharmProjects\\pythonProject\\assignment5\\FITclassification.arff > C:\\Users\\A_mah\\PycharmProjects\\pythonProject\\assignment5\\FIT{1}.arff'.format(cost,cost))
    for i in np.arange(0.10, 15.10, 0.10):
        #os.system('java -cp ../weka-3-9-5/weka.jar  weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 {0}; 1.0 0.0]" -S 1 -W weka.classifiers.functions.Logistic -num-decimal-places 4 -t C:\\Users\\A_mah\\PycharmProjects\\pythonProject\\assignment5\\FITclassification.arff > C:\\Users\\A_mah\\PycharmProjects\\pythonProject\\assignment5\\FIT{1}.arff'.format(cost,cost))
        os.system('java -cp ../weka-3-9-5/weka.jar  weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 {0}; 1.0 0.0]" -S 1 -W weka.classifiers.functions.Logistic -num-decimal-places 4 -t C:\\Users\\A_mah\\PycharmProjects\\pythonProject\\assignment5\\fit.arff > fit_{0}.txt'.format(i))

    file_paths = [i for i in os.listdir() if i[-3:] == "txt" and i[:3] == 'fit']

    cost = [float(i.split("_")[1].replace(".txt", "")) for i in file_paths]

    all_matrices = [reading_confusion_matrix(i) for i in file_paths]
    all_metrics = pd.DataFrame(all_matrices, columns=['tp', 'fn', 'fp', 'tn'])
    all_metrics['c'] = cost
    all_metrics['TPR'] = all_metrics.tp / (all_metrics.tp + all_metrics.fn)
    all_metrics['TNR'] = all_metrics.tn / (all_metrics.fp + all_metrics.tn)
    all_metrics['Type I Error'] = all_metrics.fp / (all_metrics.fp + all_metrics.tn)
    all_metrics['Type II Error'] = all_metrics.fn / (all_metrics.fn + all_metrics.tp)
    all_metrics = all_metrics[['c', 'tp', 'fn', 'fp', 'tn', "TPR", "TNR", 'Type I Error', 'Type II Error']]
    all_metrics = all_metrics.sort_values(by='c', ascending=True)
    writer3 = pd.ExcelWriter('fit' + '.xlsx', engine='xlsxwriter')
    all_metrics.to_excel(writer3, sheet_name='output', index=False)
    writer3.save()
    plt.figure(figsize=(20, 10))
    plt.plot(all_metrics.c, all_metrics["Type I Error"], marker = 'o')
    plt.plot(all_metrics.c, all_metrics["Type II Error"], marker = 'o')
    plt.show()

def test():
    for i in np.arange(1, 15, 1):
        os.system('java -cp ../weka-3-9-5/weka.jar  weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 {0}; 1.0 0.0]" -S 1 -W weka.classifiers.functions.Logistic -num-decimal-places 4 -t C:\\Users\\A_mah\\PycharmProjects\\pythonProject\\assignment5\\fit.arff -T C:\\Users\\A_mah\\PycharmProjects\\pythonProject\\assignment5\\test.arff > test_{0}.txt'.format(i))
    file_path_test = [i for i in os.listdir() if i[-3:] == "txt" and i[:4] == 'test']
    file_path_test
    cost_test = [float(i.split("_")[1].replace(".txt", "")) for i in file_path_test]
    cost_test
    all_matrices = [reading_confusion_matrix(i) for i in file_path_test]
    all_metrics_test = pd.DataFrame(all_matrices, columns=['tp', 'fn', 'fp', 'tn'])
    all_metrics_test['c'] = cost_test
    all_metrics_test['TPR'] = all_metrics_test.tp / (all_metrics_test.tp + all_metrics_test.fn)
    all_metrics_test['TNR'] = all_metrics_test.tn / (all_metrics_test.fp + all_metrics_test.tn)
    all_metrics_test['Type I Error'] = all_metrics_test.fp / (all_metrics_test.fp + all_metrics_test.tn)
    all_metrics_test['Type II Error'] = all_metrics_test.fn / (all_metrics_test.fn + all_metrics_test.tp)
    all_metrics_test = all_metrics_test[['c', 'tp', 'fn', 'fp', 'tn', "TPR", "TNR", 'Type I Error', 'Type II Error']]
    all_metrics_test = all_metrics_test.sort_values(by='c', ascending=True)
    print(all_metrics_test)
    writer3 = pd.ExcelWriter('test2' + '.xlsx', engine='xlsxwriter')
    all_metrics_test.to_excel(writer3, sheet_name='output', index=False)
    writer3.save()
    plt.figure(figsize=(20, 10))
    plt.plot(all_metrics_test.c, all_metrics_test["Type I Error"], marker = 'o')
    plt.plot(all_metrics_test.c, all_metrics_test["Type II Error"], marker = 'o')
    plt.show()

def fitmlp():
    file_path_test = [i for i in os.listdir() if i[-3:] == "txt" and i[:3] == 'mlp']

    all_matrices = [reading_confusion_matrix(i) for i in file_path_test]
    all_metrics_test = pd.DataFrame(all_matrices, columns=['tp', 'fn', 'fp', 'tn'])
    all_metrics_test['TPR'] = all_metrics_test.tp / (all_metrics_test.tp + all_metrics_test.fn)
    all_metrics_test['TNR'] = all_metrics_test.tn / (all_metrics_test.fp + all_metrics_test.tn)
    all_metrics_test['Type I Error'] = all_metrics_test.fp / (all_metrics_test.fp + all_metrics_test.tn)
    all_metrics_test['Type II Error'] = all_metrics_test.fn / (all_metrics_test.fn + all_metrics_test.tp)
    all_metrics_test = all_metrics_test[[ 'tp', 'fn', 'fp', 'tn', "TPR", "TNR", 'Type I Error', 'Type II Error']]
    print(all_metrics_test)
    writer3 = pd.ExcelWriter('mlpfit' + '.xlsx', engine='xlsxwriter')
    all_metrics_test.to_excel(writer3, sheet_name='output', index=False)
    writer3.save()

if __name__ == '__main__':
    #run()
    #test()
    fitmlp()

