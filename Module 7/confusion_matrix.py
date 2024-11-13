from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


def main():
    # 0 = dog, 1 = cat, 2 = bird
    data_labels = ['dog', 'cat', 'bird']
    # "Run" four images of dogs, 4 of cats, 4 of birds
    prediction = [2,2,0,1,1,1,1,1,2,2,0,2]
    actual_results = [0,0,0,0,1,1,1,1,2,2,2,2]
    ideal_results = [0,0,0,0,1,1,1,1,2,2,2,2]
    print(f'Accuracy = {(accuracy_score(actual_results, prediction))*100:.2f}%')
    print(f'Confusion Matrix:\n{confusion_matrix(actual_results, prediction)}')
    print(f'Classification Report:\n{classification_report()}')

if __name__ == '__main__':
    main()