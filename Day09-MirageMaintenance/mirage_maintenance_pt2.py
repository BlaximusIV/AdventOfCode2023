import time

def predict_next_steps(trend, predictions):
    if all([value == 0 for value in trend]):
        predictions.append(0)
        return
    
    new_trend = []
    for i in range(len(trend) - 1):
        new_trend.append(trend[i + 1] - trend[i])
    
    predict_next_steps(new_trend, predictions)
    predictions.append(trend[0] - predictions[-1])

    return 

def main():
    start = time.time()

    report_lines = []
    with open("input.txt", 'r') as f:
        lines = f.readlines()

        for line in lines:
            values = [int(value) for value in line.rstrip('\n').split(' ')]
            report_lines.append(values)

    predicted_next_steps = []
    for trend in report_lines:
        predictions = []
        predict_next_steps(trend, predictions)
        predicted_next_steps.append(predictions[-1])

    print(f'Sum of predicted values: {sum(predicted_next_steps)}')

    end = time.time()
    print(f'Time elapsed: {end - start}s')


main()
