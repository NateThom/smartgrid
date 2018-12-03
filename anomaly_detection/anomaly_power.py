import real_power

import numpy as np
import random
import graphviz
from sklearn import svm, tree, neural_network, ensemble

training_data_labels = []
training_data_features = []
testing_data_labels = []
testing_data_features = []

for data_iteration in range(0, 2):
    print(f'data_iteration: {data_iteration}')

    real_power_dict = {}
    real_power_dict = real_power.hourly_demmand(
                    real_power.annual_peak_demand_load_feeder,
                    real_power.weekly_load_factors,
                    real_power.daily_load_factors,
                    real_power.hourly_load_factors_weekday_1_8__44_52,
                    real_power.hourly_load_factors_weekend_1_8__44_52,
                    real_power.hourly_load_factors_weekday_18_30,
                    real_power.hourly_load_factors_weekend_18_30,
                    real_power.hourly_load_factors_weekday_9_17__31_43,
                    real_power.hourly_load_factors_weekend_9_17__31_43,
                    real_power_dict
                    )

    real_power_dict_features = {}
    real_power_dict_labels = {}

    for feed in range(1,len(real_power_dict)+1):
        real_power_dict_labels[feed] = []
        real_power_dict_features[feed] = []
        for week in range(1, len(real_power_dict[feed])+1):
            for day in range(1, len(real_power_dict[feed][week])+1):
                for hour in range(1, len(real_power_dict[feed][week][day])+1):
                    real_power_dict_labels[feed].append(real_power_dict[feed][week][day][hour][4])
                    real_power_dict_features[feed].append(real_power_dict[feed][week][day][hour][0:4])

    for feed in real_power_dict_features:
        anomaly_occurence = abs(np.random.normal(.1, .1))
        for count in range(0, int(anomaly_occurence * len(real_power_dict_features[feed]))):
            anomaly_duration = abs(np.random.normal(2, 12))
            anomaly_severity = np.random.normal(0, .2)

            hour_of_event = random.choice(range(0, len(real_power_dict_features[feed])))

            for index in range(0, int(anomaly_duration)):

                if hour_of_event + anomaly_duration > 8736:
                    real_power_dict_labels[feed][hour_of_event - index] = 1

                    real_power_dict_features[feed][hour_of_event - index][0] = \
                    real_power_dict_features[feed][hour_of_event - index][0] + (
                                real_power_dict_features[feed][hour_of_event - index][0] * anomaly_severity)

                    real_power_dict_features[feed][hour_of_event - index][1] = \
                        real_power_dict_features[feed][hour_of_event - index][1] + (
                                real_power_dict_features[feed][hour_of_event - index][1] * anomaly_severity)

                    real_power_dict_features[feed][hour_of_event - index][2] = \
                        real_power_dict_features[feed][hour_of_event - index][2] + (
                                real_power_dict_features[feed][hour_of_event - index][2] * anomaly_severity)
                else:
                    real_power_dict_labels[feed][hour_of_event + index] = 1

                    real_power_dict_features[feed][hour_of_event + index][0] = \
                    real_power_dict_features[feed][hour_of_event + index][0] + (
                                real_power_dict_features[feed][hour_of_event + index][0] * anomaly_severity)

                    real_power_dict_features[feed][hour_of_event + index][1] = \
                        real_power_dict_features[feed][hour_of_event + index][1] + (
                                real_power_dict_features[feed][hour_of_event + index][1] * anomaly_severity)

                    real_power_dict_features[feed][hour_of_event + index][2] = \
                        real_power_dict_features[feed][hour_of_event + index][2] + (
                                real_power_dict_features[feed][hour_of_event + index][2] * anomaly_severity)

        anomaly_count = 0
        for counter in range(0, len(real_power_dict_labels[feed])):
            if data_iteration == 1:
                if real_power_dict_labels[feed][counter] == 1:
                    anomaly_count = anomaly_count+1
                    print(anomaly_count)
                    print(real_power_dict_features[feed][counter])

                testing_data_features.append(real_power_dict_features[feed][counter])
                testing_data_labels.append(real_power_dict_labels[feed][counter])
                #print(f' testing label data length: {len(testing_data_labels)}')
                #print(f' testing feature data length: {len(testing_data_features)}')
            else:
                training_data_features.append(real_power_dict_features[feed][counter])
                training_data_labels.append(real_power_dict_labels[feed][counter])
                #print(f' training label data length: {len(training_data_labels)}')
                #print(f' training feature data length: {len(training_data_features)}')

print(len(training_data_features))
print(len(training_data_labels))

print(len(testing_data_features))
print(len(testing_data_labels))

#clf_svm = svm.svc()
#clf_dtree = tree.DecisionTreeClassifier()
#clf_mlp = neural_network.MLPClassifier()
#clf_rf = ensemble.RandomForestClassifier(n_estimators=100)


# clf_svm.fit(training_data_features, training_data_labels)
# clf_dtree.fit(training_data_features, training_data_labels)
# clf_mlp.fit(training_data_features, training_data_labels)
#clf_rf.fit(training_data_features, training_data_labels)

# print("here1")
# dot_data = tree.export_graphviz(clf_dtree, out_file=None)
# print(dot_data)
# print("here2")
# graph = graphviz.Source(dot_data)
# print("here3")
# graph.render("dtree")

# svm_acc = 0
# dtree_acc = 0
# mlp_acc = 0
#rf_acc = 0

for sample in range(0, len(testing_data_features)):
    print(f'Percent Finished: {sample/len(testing_data_features)}')
    # svm_prediction = clf_svm.predict([testing_data_features[sample]])
    #dtree_prediction = clf_dtree.predict([testing_data_features[sample]])
    #mlp_prediction = clf_mlp.predict([testing_data_features[sample]])
    #rf_prediction = clf_rf.predict([testing_data_features[sample]])

    # print(f'feature: {testing_data_features[sample]}')
    # print(f'label: {testing_data_labels[sample]}')
    # print(f'svm prediction: {svm_prediction}')
    # print(f'dtree prediction: {dtree_prediction}')

    # if svm_prediction == testing_data_labels[sample]:
    #     svm_acc = svm_acc + 1
    # if dtree_prediction == testing_data_labels[sample]:
    #     dtree_acc = dtree_acc + 1
    # if mlp_prediction == testing_data_labels[sample]:
    #     mlp_acc = mlp_acc + 1
    if rf_prediction == testing_data_labels[sample]:
        rf_acc = rf_acc + 1

# svm_acc = svm_acc / len(testing_data_labels)
# print(f'svm accuracy: {svm_acc}')
# dtree_acc = dtree_acc / len(testing_data_labels)
# print(f'dtree accuracy: {dtree_acc}')
# mlp_acc = mlp_acc / len(testing_data_labels)
#print(f'mlp accuracy: {mlp_acc}')
#rf_acc = rf_acc / len(testing_data_labels)
print(f'rf accuracy: {rf_acc}')