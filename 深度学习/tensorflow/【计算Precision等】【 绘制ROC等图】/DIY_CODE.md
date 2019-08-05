#### 计算Precion, Recall等度量值，并绘制ROC、P-R曲线
> - **说明**：有些时候想评估自己搭建的模型性能，但直接调包可能会出现一些问题；也可能会出现自己无法理解的情况，譬如：Precision是怎么计算得来的；为了对这些概念有更加深刻的理解，现DIY相关代码
> - **功能实现**：
> - 计算Precion, Recall等度量值，并绘制ROC、P-R曲线
> - 在给定阈值情况下，计算precision、recall、tpr、fpr值
> - 在不同阈值情况下，获取多组precision、recall、tpr、fpr值，用以绘制P-R、ROC曲线
```python
import numpy as np
import matplotlib.pyplot as plt


def calculate_metrics(labels, predictions, threshold=0.5):
    """
    :param labels: 样本数据的真实标签值，形如[[0], [1], [1], [0], [0], ...]
    :param predictions: 模型预测的概率值，形如[[0.08], [0.96], [0.66], [0.32], [0.88], ...]
    :param threshold:阈值，默认0.5，即预测模型的概率值>=0.5时，将模型预测值标记为正样本 1
    :return:返回该阈值下的 Precision, Recall, Tpr, Fpr
    """
    pos_label_index = np.where(labels == 1)[0]                      # 样本数据中，正样本的index列表
    # pos_label_count = sum(labels == 1)[0]
    pos_label_count = len(np.where(labels == 1)[0])                 # 样本数据中，正样本的个数

    predict_label_index = np.where(predictions >= threshold)[0]     # 预测为正样本的索引列表
    index_scores = []                                               # 降序的 (预测为正样本的概率值, 及对应的索引值)
    for pred_score, index in sorted(zip(predictions[predict_label_index], predict_label_index), reverse=True):
        index_scores.append((index, pred_score))

    # 分析 top-k 结果
    top_k = len(predict_label_index)
    top_index_score = index_scores[:top_k]
    correct_predict = 0
    for item in top_index_score:
        if item[0] in pos_label_index:
            correct_predict += 1

    try:
        TP = correct_predict
        FN = pos_label_count - TP
        FP = len(top_index_score) - TP
        TN = len(labels) - pos_label_count - FP

        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        tpr = recall
        fpr = FP / (TN + FP)

        print("当前阈值: {:.3f}".format(threshold))
        print("Precision: {:.4f} ===> {:.2f}% ===> {:}/{:}".format(precision, precision * 100, TP, TP + FP))
        print("Recall: {:.4f} ===> {:.2f}% ===> {:}/{:}".format(recall, recall * 100, TP, TP + FN))
        print("Tpr: {:.4f} ===> {:.2f}% ===> {:}/{:}".format(tpr, tpr * 100, TP, TP + FN))
        print("Fpr: {:.4f} ===> {:.2f}% ===> {:}/{:}\n".format(fpr, fpr * 100, FP, TN + FP))
    except ZeroDivisionError:
        precision, recall, tpr, fpr = 1, 0, 0, 0

    return precision, recall, tpr, fpr


# 计算fpr, tpr值
def get_metrics_values_list(labels, predictions, num_thresholds=100):
    start = 0
    step = 1.0 / num_thresholds
    end = 1 + step
    pre_ls = []
    rec_ls = []
    tpr_ls = []
    fpr_ls = []
    while start <= end:
        pre, rec, tpr, fpr = calculate_metrics(labels=labels, predictions=predictions, threshold=start)
        pre_ls.append(pre)
        rec_ls.append(rec)
        tpr_ls.append(tpr)
        fpr_ls.append(fpr)
        start = start + step

    # 转换fpr, tpr坐标，以便用于计算AUROC
    fpr_tpr_coordinate = []
    for fpr, tpr in sorted(zip(fpr_ls, tpr_ls), reverse=True):
        fpr_tpr_coordinate.append((fpr, tpr))

    fpr_tpr_coordinate_unique = list(set(fpr_tpr_coordinate))
    fpr_tpr_coordinate_unique.sort(key=fpr_tpr_coordinate.index)
    fpr_ls = [point[0] for point in fpr_tpr_coordinate_unique]
    tpr_ls = [point[1] for point in fpr_tpr_coordinate_unique]

    # added for 转换 rec, pre坐标，以便用于计算AUPR
    rec_pre_coordinate = []
    for rec, pre in sorted(zip(rec_ls, pre_ls), reverse=True):
        rec_pre_coordinate.append((rec, pre))

    rec_pre_coordinate_unique = list(set(rec_pre_coordinate))
    rec_pre_coordinate_unique.sort(key=rec_pre_coordinate.index)
    rec_ls = [point[0] for point in rec_pre_coordinate_unique]
    pre_ls = [point[1] for point in rec_pre_coordinate_unique]

    return rec_ls, pre_ls, fpr_ls, tpr_ls


# 计算AUROC值
def get_auroc(fpr_ls, tpr_ls):
    auc_value = 0.0
    for ix in range(len(fpr_ls[:-1])):
        x_right, x_left = fpr_ls[ix], fpr_ls[ix+1]
        y_top, y_bottom = tpr_ls[ix], tpr_ls[ix+1]
        temp_area = abs(x_right-x_left) * (y_top + y_bottom) * 0.5
        auc_value += temp_area
    return auc_value


# 计算AUPR值
def get_aupr(rec_ls, pre_ls):
    pr_value = 0.0
    for ix in range(len(rec_ls[:-1])):
        x_right, x_left = rec_ls[ix], rec_ls[ix + 1]
        y_top, y_bottom = pre_ls[ix], pre_ls[ix + 1]
        temp_area = abs(x_right-x_left) * (y_top + y_bottom) * 0.5
        pr_value += temp_area
    return pr_value


# 绘制ROC曲线
def plot_roc_curve(fpr_ls, tpr_ls, auc_value=None, title=None):
    label = "AUROC: " + str(auc_value)
    plt.plot(fpr_ls, tpr_ls, 'r-',)
    plt.plot([0, 1], [0, 1], 'k--', linewidth=0.8, label=label)
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")  # 若需显示label,必须在show之前加这一句
    plt.show()


# 绘制P-R曲线
def plot_pr_curve(rec_ls, pre_ls, pr_value=None, title=None):
    label = "AUPR: " + str(pr_value)
    plt.plot(rec_ls, pre_ls, 'r-', )
    plt.plot([0, 1], [1, 0], 'k--', linewidth=0.8, label=label)
    plt.axis([0, 1, 0, 1])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(title)
    plt.legend(loc="lower left")  # 若需显示label,必须在show之前加这一句
    plt.show()


def plot_curves(labels, predictions):
    rec_ls, pre_ls, fpr_ls, tpr_ls = get_metrics_values_list(labels=labels, predictions=predictions)
    auc_roc = np.around(get_auroc(fpr_ls, tpr_ls), 4)
    auc_pr = np.around(get_aupr(rec_ls, pre_ls), 4)
    print("AUROC: ", auc_roc)
    print("AUPR: ", auc_pr)
    plot_roc_curve(fpr_ls, tpr_ls, auc_value=auc_roc, title="ROC Curve")
    plot_pr_curve(rec_ls, pre_ls, pr_value=auc_pr, title="P-R Curve")

```
