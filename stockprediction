"""
Stock market prediction using Markov chains.
"""

import comp140_module3 as stocks
import random

### Model

def markov_chain(data, order):
    """
    Create a Markov chain with the given order from the given data.

    inputs:
        - data: a list of ints or floats representing previously collected data
        - order: an integer repesenting the desired order of the markov chain

    returns: a dictionary that represents the Markov chain
    """
    chain = {}
    #"count" keeps track of the number of times a unique state of length "order" occurs in "data"
    count = {}
    for index in range(len(data)-order):
        #"key" gets each state of length "order" in "data"
        key = []
        for num in range(order):
            key.append(data[index+num])
        key = tuple(key)
        next_bin = data[index+order]
        #Checking to see if "key" is unique and incrementing "count"
        if key in chain:
            count[key] += 1
            #"next_bin" keeps track of the number of times the next state is each of the 4 bins
            if next_bin in chain[key]:
                (chain[key])[next_bin] += 1
            else:
                (chain[key])[next_bin] = 1
        else:
            count[key] = 1
            chain[key] = {next_bin:1}
    #Changing the count of each next state into the probability of each next state
    for past in chain:
        for future in chain[past]:
            (chain[past])[future] = ((chain[past])[future])/count[past]
    return chain

    
### Predict

def predict(model, last, num):
    """
    Predict the next num values given the model and the last values.

    inputs:
        - model: a dictionary representing a Markov chain
        - last: a list (with length of the order of the Markov chain)
                representing the previous states
        - num: an integer representing the number of desired future states

    returns: a list of integers that are the next num states
    """
    prediction = []
    previous = tuple(last)
    #Checking if the previous state is in "model"
    for index in range(num):
        if previous in model:
            #If yes, randomly predict next state according to the probability values in "model"
            prob = random.random()
            percent = 0.0
            for key in model[previous]:
                if prob < (percent + (model[previous][key])):
                    prediction.append(key)
                    break
                percent += model[previous][key]
        else:
            #If not, randomly predict next state with equal probability
            prediction.append(random.randrange(0,4))
        #Update "previous"
        previous_list = list(previous)
        previous_list.append(prediction[index])
        previous_list.pop(0)
        previous = tuple(previous_list)
    return prediction


### Error

def mse(result, expected):
    """
    Calculate the mean squared error between two data sets.

    The length of the inputs, result and expected, must be the same.

    inputs:
        - result: a list of integers or floats representing the actual output
        - expected: a list of integers or floats representing the predicted output

    returns: a float that is the mean squared error between the two data sets
    """
    total = 0.0
    for index in range(len(result)):
        total += ((result[index]-expected[index])**2)
    error = total / len(result)
    return error


### Experiment

def run_experiment(train, order, test, future, actual, trials):
    """
    Run an experiment to predict the future of the test
    data given the training data.

    inputs:
        - train: a list of integers representing past stock price data
        - order: an integer representing the order of the markov chain
                 that will be used
        - test: a list of integers of length "order" representing past
                stock price data (different time period than "train")
        - future: an integer representing the number of future days to
                  predict
        - actual: a list representing the actual results for the next
                  "future" days
        - trials: an integer representing the number of trials to run

    returns: a float that is the mean squared error over the number of trials
    """
    total = 0.0
    model = markov_chain(train,order)
    for _ in range(trials):
        prediction = predict(model,test,future)
        total += mse(actual,prediction)
    error = total / trials
    return error


### Application

def run():
    """
    Run application.

    You do not need to modify any code in this function.  You should
    feel free to look it over and understand it, though.
    """
    # Get the supported stock symbols
    symbols = stocks.get_supported_symbols()

    # Get stock data and process it

    # Training data
    changes = {}
    bins = {}
    for symbol in symbols:
        prices = stocks.get_historical_prices(symbol)
        changes[symbol] = stocks.compute_daily_change(prices)
        bins[symbol] = stocks.bin_daily_changes(changes[symbol])

    # Test data
    testchanges = {}
    testbins = {}
    for symbol in symbols:
        testprices = stocks.get_test_prices(symbol)
        testchanges[symbol] = stocks.compute_daily_change(testprices)
        testbins[symbol] = stocks.bin_daily_changes(testchanges[symbol])

    # Display data
    #   Comment these 2 lines out if you don't want to see the plots
    stocks.plot_daily_change(changes)
    stocks.plot_bin_histogram(bins)

    # Run experiments
    orders = [1, 3, 5, 7, 9]
    ntrials = 500
    days = 5

    for symbol in symbols:
        print(symbol)
        print("====")
        print("Actual:", testbins[symbol][-days:])
        for order in orders:
            error = run_experiment(bins[symbol], order,
                                   testbins[symbol][-order-days:-days], days,
                                   testbins[symbol][-days:], ntrials)
            print("Order", order, ":", error)
        print()

# You might want to comment out the call to run while you are
# developing your code.  Uncomment it when you are ready to run your
# code on the provided data.

run()
