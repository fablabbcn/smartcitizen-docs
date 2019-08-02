Analyse your sensor data
====================================================

In this section, we will work on the development of two models for the MOS sensors in the Smart Smart Citizen Kit. In the Sensor Analysis Framework, we have implemented two different approaches for model calibration:

- **Ordinary Least Squares (OLS)**: based on the [statsmodels package](http://www.statsmodels.org/stable), the model is able to input whichever expression referring to the kit's available data and perform OLS regression over the defined training and test data
- **Machine Learning (MLP or LSTM)**: based on the [keras package](https://keras.io/) using [tensorflow](https://www.tensorflow.org/) in the backend. This framework can be used to train larger collections of data, where we want to be, among others:
	- Robust to noise
	- Learn non-linear relationships
	- Aware of temporal dependence

## Ordinary Least Squares example

Let's delve first into an OLS example. The framework comes with a very simple interface to develop and interact with the models. By running these two cells we will generate the preliminary tweaks for the dataframes:


```python
from test_utils import combine_data

name_combined_data = 'COMBINED_DEVICES'

for reading in readings:
    ## Since we don't know if there are more or less channels than last time
    ## (and tbh, I don't feel like checking), remove the key
    readings[reading]['devices'].pop('COMBINED_DEVICES', None)
    ## And then add it again
    dataframe = combine_data(readings[reading]['devices'], True)
    readings[reading]['devices'][name_combined_data] = dict()
    readings[reading]['devices'][name_combined_data]['data'] = dict()
    readings[reading]['devices'][name_combined_data]['data'] = dataframe
```

Output:

```python
Dataframe has been combined for model preparation
```

Here we can list all the available channels for our test:

```python
test_linear_regression = '2018-08_INT_STATION_TEST_SUMMER_HOLIDAYS'

for channel in readings[test_linear_regression]['devices'][name_combined_data]['data'].columns:
    print channel
```

Output:

```python
BATT_4748
CO_AD_BASE_4748
CO_AD_BASE_filter_4748
CO_MICS_RAW_4748
EXT_HUM_4748
EXT_TEMP_4748
GB_1A_4748
GB_1W_4748
(...)
PM_1_4748
PM_10_4748
PM_25_4748
PM_DALLAS_TEMP_4748
PRESS_4748
TEMP_4748
O3_AD_BASE_filter_4748
```

And now, it's time to set up our model. In the cell below we can define the channel and features for the regression. 

```python
from linear_regression_utils import prepData, fit_model

## Select data
# Always have an item called 'REF', the rest can be anything
tuple_features = (['REF', 'CO_AD_BASE_4748'],
                 ['A', 'CO_MICS_RAW_4748'],
                 ['B', 'TEMP_4748'],
                 ['C', 'HUM_4748'],
                 ['D', 'PM_25_4748'])

formula_expression = 'REF ~ A + np.power(A,2) + B + np.power(B,2) + C + D'

min_date = '2018-08-31 00:00:00'
max_date = '2018-09-06 00:00:00'

ratio_train = 2./3 # Important that this is a float, don't forget the .

filter_data = True
alpha_filter = 0.1

dataframeModel = readings[test_linear_regression]['devices'][name_combined_data]['data']

dataTrain, dataTest = prepData(dataframeModel, tuple_features, min_date, max_date, ratio_train, filter_data, alpha_filter)
model, train_rmse, test_rmse = fit_model(formula_expression, dataTrain, dataTest
```

We have to keep at least the key `'REF '` within the `tuple_features`, but the rest can be renamed at will. We can also input whichever `formula_expression` for the model regression in the following format:

```python
formula_expression = 'REF ~ A + np.power(A,2) + B + np.power(B,2) + C + D'
```

Which converts to:

$$
REF = A + A^2 + B + B^2 + C + D + Intercept
$$

We can also define the ratio between the train and test dataset and the minimum dates to use within the datasets (globally):

```python
min_date = '2018-08-31 00:00:00'
max_date = '2018-09-06 00:00:00'

ratio_train = 2./3 # Important that this is a float, don't forget the .
```

Finally, if our data is too noisy, we can apply an `exponential smoothing` function, by setting `filter_data = True` and the alpha coefficient (0.1, 0.2 is already very filtered:

```python
filter_data = True
alpha_filter = 0.1
```

If we run this cell, we will perform model calibration, with the following output:

```python
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    REF   R-squared:                       0.676
Model:                            OLS   Adj. R-squared:                  0.673
Method:                 Least Squares   F-statistic:                     197.5
Date:                Thu, 06 Sep 2018   Prob (F-statistic):          1.87e-135
Time:                        12:25:17   Log-Likelihood:                 1142.9
No. Observations:                 575   AIC:                            -2272.
Df Residuals:                     568   BIC:                            -2241.
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
Intercept         -3.7042      0.406     -9.133      0.000      -4.501      -2.908
A                  0.0011      0.000      2.953      0.003       0.000       0.002
np.power(A, 2) -3.863e-05   7.03e-06     -5.496      0.000   -5.24e-05   -2.48e-05
B                  0.2336      0.024      9.863      0.000       0.187       0.280
np.power(B, 2)    -0.0032      0.000     -9.267      0.000      -0.004      -0.003
C                 -0.0014      0.001     -2.755      0.006      -0.002      -0.000
D                  0.0127      0.001     24.378      0.000       0.012       0.014
==============================================================================
Omnibus:                        7.316   Durbin-Watson:                   0.026
Prob(Omnibus):                  0.026   Jarque-Bera (JB):               10.245
Skew:                          -0.076   Prob(JB):                      0.00596
Kurtosis:                       3.636   Cond. No.                     4.29e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 4.29e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

```

This output brings a lot of information. First, we find what the dependent variable is, in our case always `'REF'`. The type of model used and some general information is shown below that.

More statistically important information is found in the rest of the output. Some key data:

- *R-squared and adjusted R-squared*: this is our classic correlation coefficient or R<sup>2</sup>. The adjusted one aims to correct the model overfitting by the inclusion of too many variables, and for that introduces a penalty on the number of variables included
- Below, we can find a summary of the *model coefficients* applied to all the variables and the P>|t| term, which indicates the significance of the term introduced in the model
- *Model quality diagnostics* are also indicated. Kurtosis and skewness are metrics for determining the distribution of the residuals. They indicate how the residuals of the model resemble a normal distribution. Below, we will review more on diagnosis plots. The [Jarque Bera test](https://en.wikipedia.org/wiki/Jarque–Bera_test) indicates if the residuals are normally distributed (the null hypothesis is a joint hypothesis of the skewness being zero and the excess kurtosis being zero), and a value of zero indicates that the data is normally distributed. If the Jarque Bera test is valid (in the case above it isn't), the Durbin Watson is applicable in order to check for autocorrelation of the residuals (meaning that the residuals of our model are related among themselves and that we haven't captured some characteristics of our data with the tested model).

Finally, there is a warning at the bottom indicating that the condition number is large. It suggests we might have multicollinearity problems in our model, which means that some of the independent variables might be correlated among themselves and that they are probably not necessary.

Our function also depicts the results in a graphical way for us to see the model itself. It will show the training and test datasets (as `Reference Train` and `Reference Test` respectively), and the prediction results. The mean and absolute confidence intervals for 95% confidence are also shown:

![](https://i.imgur.com/M9TBeBT.png)

Now we can look at some other model quality plots. If we run the cell below, we will obtain an adaptation of the summary plots from **R**:

```python
from linear_regression_utils import modelRplots
%matplotlib inline

modelRplots(model, dataTrain, dataTest)
```

Let's review the output step by step:

- **Residual vs Fitted** and **Scale Location plot**: these plots represents the model [heteroscedasticity ](https://en.wikipedia.org/wiki/Heteroscedasticity), which is a representation of the residuals versus the fitted values. This polot is helpful to check if the errors are distributed homogeneously and that we are not penalising high, low, or other values. There is also a red line which represents the average trend of this distribution which, we want it to be horizontal. For more information visit [here](https://stats.stackexchange.com/questions/76226/interpreting-the-residuals-vs-fitted-values-plot-for-verifying-the-assumptions) and [here](https://stats.stackexchange.com/questions/52089/what-does-having-constant-variance-in-a-linear-regression-model-mean/52107#52107). Clearly, in this model we are missing something:

![](https://i.imgur.com/QR2Ya4r.png)

- **Normal QQ**: the qq-plot is a representation of the kurtosis and skewness of the residuals distribution. If the data were well described by a normal distribution, the values should be about the same, i.e.: on the diagonal (red line). For example, in our case the model presents a deviation on both tails, indicating skewness. In general, a simple rubric to interpret a qq-plot is that if a given tail twists off counterclockwise from the reference line, there is more data in that tail of your distribution than in a theoretical normal, and if a tail twists off clockwise there is less data in that tail of your distribution than in a theoretical normal. In other words:

    - if both tails twist counterclockwise we have heavy tails (leptokurtosis),
    - if both tails twist clockwise, we have light tails (platykurtosis),
    - if the right tail twists counterclockwise and the left tail twists clockwise, we have right skew
    - if the left tail twists counterclockwise and the right tail twists clockwise, we have left skew

<div style="text-align:center">
<img src ="https://i.imgur.com/4ldXI80.png" alt="QQ-plot" class="cover"/>
</div>

- **Residuals vs Leverage**: this plot is probably the most complex of them all. It shows how much leverage one single point has on the whole regression. It can be interpreted as how the average line that passes through all the data (that we are calculating with the OLS) can be modified by 'far' points in the distribution, for example, outliers. This leverage can be seen as how much a single point is able to pull down or up the average line. One way to think about whether or not the results are driven by a given data point is to calculate how far the predicted values for your data would move if your model were fit without the data point in question. This calculated total distance is called Cook's distance. We can have four cases (more information from source, [here](https://stats.stackexchange.com/questions/58141/interpreting-plot-lm#65864))

    - everything is fine (the best)
    - high-leverage, but low-standardized residual point
    - low-leverage, but high-standardized residual point
    - high-leverage, high-standardized residual point (the worst)

<div style="text-align:center">
<img src ="https://i.imgur.com/BXsS6tE.png" alt="Cook Distance Plot" class="cover"/>
</div>

In this case, we see that our model has some points with higher leverage but low residuals (probably not too bad) and that the higher residuals are found with low leverage, which means that our model is safe to outliers. If we run this function without the filtering, some outliers will be present and the plot turns into:

<div style="text-align:center">
<img src ="https://i.imgur.com/NQLA4lw.png" alt="Cook Distance Plot" class="cover"/>
</div>

## Machine learning example

As we have seen in the [the calibration section](https://docs.iscape.smartcitizen.me/Sensor%20Analysis%20Framework/Low%20Cost%20Sensors%20Calibration/), machine learning algorithms promise a better representation of the sensor's data, being able to learn robust non-linear models and sequential dependencies. For that reason, we have implemented an easy to use interface based on [keras](https://keras.io/) with [Tensorflow](https://www.tensorflow.org/) backend, in order to train sequential models [^third].

The workflow for a supervised learning algorithm reads as follows:

- Reframe the data as a supervised learning algorithm and split into training and test dataframe. More information can be found [here](https://machinelearningmastery.com/convert-time-series-supervised-learning-problem-python/)
- Define Model and fit for training dataset
- Evaluate test dataframe and extract metrics

Let's go step by step. In order to reframe the data as a supervised learning algorithm, we have created a function called `prep_dataframe_ML` which is the only one function we'll have to interact with:

```python
# Combine all data in one dataframe
from ml_utils import prep_dataframe_ML

# Always have an item called 'REF', the rest can be anything
tuple_features = (['REF', 'CO_AD_BASE_STATION_CASE'],
                 ['A', 'CO_MICS_RAW_STATION_CASE'],
                 ['B', 'TEMP_STATION_CASE'],
                 ['C', 'HUM_STATION_CASE'],
                 ['D', 'PM_25_STATION_CASE'])

model_name = 'LSTM NO2'

ratio_train = 3./4 # Important that this is a float, don't forget the .
alpha_filter = 0.9 # 1 means no filtering

# Number of lags for the model
n_lags = 1

dataframeModel = readings[test_model]['devices'][name_combined_data]['data']

index, train_X, train_y, test_X, test_y, scaler, n_train_periods = prep_dataframe_ML(dataframeModel, min_date, max_date, tuple_features, n_lags, ratio_train, alpha_filter)
```

Output:

```python
DataFrame has been reframed and prepared for supervised learning
Reference is: CO_AD_BASE_STATION_CASE
Features are: ['CO_MICS_RAW_STATION_CASE', 'TEMP_STATION_CASE', 'HUM_STATION_CASE', 'PM_25_STATION_CASE']
Traning X Shape (1508, 1, 4), Training Y Shape (1508,), Test X Shape (501, 1, 4), Test Y Shape (501,)
```

Now, we can fit our model. The main function is `fit_model_ML` and currently implements a simple LSTM network. This network can be redefined easily by modifying the underlying function.

```python
model = fit_model_ML(train_X, train_y, test_X, test_y, epochs = 50, batch_size = 72, verbose = 2)
```

```python
def fit_model_ML(train_X, train_y, test_X, test_y, epochs = 50, batch_size = 72, verbose = 2):
    
    model = Sequential()
    layers = [50, 100, 1]
    model.add(LSTM(layers[0], return_sequences=True, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dropout(0.2))
    model.add(LSTM(layers[1], return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(output_dim=layers[2]))
    model.add(Activation("linear"))
    model.compile(loss='mse', optimizer='rmsprop')

    # fit network
    history = model.fit(train_X, train_y, epochs=epochs, batch_size=batch_size, validation_data=(test_X, test_y), verbose=verbose, shuffle=False)
    # plot history
    fig = plot.figure(figsize=(10,8))
    plot.plot(history.history['loss'], label='train')
    plot.plot(history.history['val_loss'], label='test')
    plot.xlabel('Epochs (-)')
    plot.ylabel('Loss (-)')
    plot.title('Model Convergence')
    plot.legend(loc='best')
    plot.show()
    
    return model
```

This function will return the model and it's learning outcomes:

```python
Train on 1508 samples, validate on 501 samples
Epoch 1/50
 - 1s - loss: 0.0500 - val_loss: 0.0051
Epoch 2/50
 - 0s - loss: 0.0200 - val_loss: 0.0058
Epoch 3/50
 - 0s - loss: 0.0158 - val_loss: 0.0052
...
```

![](https://i.imgur.com/5QoPq3n.png)

Then, we can evaluate the model and plot it's results:

```python
from ml_utils import predict_ML
from signal_utils import metrics
import matplotlib.pyplot as plot
%matplotlib inline

inv_y_train, inv_yhat_train = predict_ML(model, train_X, train_y, n_lags, scaler)
inv_y_test, inv_yhat_test = predict_ML(model, test_X, test_y, n_lags, scaler)
```

![](https://i.imgur.com/v1drQ74.png)

## Model comparison

Here is a visual comparison of both models:

```python
fig = plot.figure(figsize=(15,10))
# Actual data
plot.plot(index[:n_train_periods], inv_y_train,'r', label = 'Reference Train', alpha = 0.3)
plot.plot(index[n_train_periods+n_lags:], inv_y_test, 'b', label = 'Reference Test', alpha = 0.3)

# Fitted Values for Training
plot.plot(index[:n_train_periods], inv_yhat_train, 'r', label = 'ML Prediction Train')
plot.plot(index[n_train_periods+n_lags:], inv_yhat_test, 'b', label = 'ML Prediction Test')

# OLS
plot.plot(dataTrain['index'], predictionTrain, 'g', label = 'OLS Prediction Train')
plot.plot(dataTest['index'], predictionTest, 'k', label = 'OLS Prediction Test')

plot.legend(loc = 'best')
plot.ylabel('CO (ppm)')
plot.xlabel('Date (-)')
```

Output:

![](https://i.imgur.com/56eVx5P.png)

It is very difficult though, to know which one is performing better. Let's then evaluate and compare our models. In order to evaluate it's metrics, we will be using the following principles[^first][^second]:

!!! info
	In all of the expressions below, the letter *m* indicates the model field, *r* indicates the reference field. Overbar is average and $\sigma$ is the standard deviation.

**Linear correlation Coefficient**
A measure of the agreement between two signals:

$$
R = {{1 \over N} \sum_{i=0}^n (m_n-\overline m)( r_n-\overline r ) \over \sigma_m\sigma_r}
$$

The correlation coefficient is bounded by the range $-1 \le R \le 1$. However, it is difficult to discern information about the differences in amplitude between two signals from R alone.

**Normalized standard deviation**
A measure of the differences in amplitude between two signals:
$$
\sigma * = {\sigma_m \over \sigma_r}
$$

**_unbiased_ Root-Mean-Square Difference**
A measure of how close the modelled points fall to teach other:

$$
RMSD' = \Bigl( {1 \over N} \sum_{n=1}^N [(m_n - \overline m)-(r_n - \overline r)]^2  \Bigr)^{0.5}
$$

**Potential Bias**
Difference between the means of two fields:
$$
B = \overline m - \overline r
$$
**Total RMSD**
A measure of the average magnitude of difference:
$$
RMSD = \Bigl( {1 \over N} \sum_{n=1}^N (m_n - r_n)^2  \Bigr)^{0.5}
$$

In other words, the unbiased RMSD (RMSD') is equal to the total RMSD if there is no bias between the model and the reference fields (i.e. B = 0). The relationship between both reads:

$$
RMSD^2 = B^2 + RMSD'^2
$$

In contrast, the unbiased RMSD may be conceptualized as an overall measure of the agreement between the aplitude ($\sigma$) and phase ($\phi$) of two temporal patterns. For this reason, the correlation coefficient ($R$), normalised standard deviation ($\sigma*$), and unbiased RMSD are all referred to as **patern statistics**, related to one another by:

$$
RMSD'^2 = \sigma_r^2 + \sigma_m^2 - 2\sigma_r\sigma_mR
$$


**Normalized and unbiased RMSD**
If we recast in standard deviation normalized units (indicated by the asterisk) it becomes:

$$
RMSD'^* = \sqrt { 1 + \sigma*^2 - 2\sigma*R}
$$

**NB**: the minimum of this function occurrs when $\sigma* = R$.

**Normalized bias**
Gives information about the mean difference but normalized by the $\sigma*$
$$
B* = {\overline m - \overline r \over \sigma_r}
$$

**Target diagrams**
The target diagram is a plot that provides summary information about the **pattern statistics as well as the bias** thus yielding an overview of their respective contributions to the total RMSD. In a simple Cartesian coordinate system, the unbiased RMSD may serve as the X-axis and the bias may serve as the Y-axis. The distance between the origin and the model versus observation statistics (any point, s, within the X,Y Cartesian space) is then equal to the total RMSD. If all is normalized by the $\sigma_r$, the distance from the origin is again the _standard deviation normalized total RMSD_:[^first]

$$
RMSD^{*2} = B^{*2}+RMSD^{*'2}
$$

The resulting target diagram then provides information about:

- whether the $\sigma_m$ is larger or smaller thann the $\sigma_r$
- whether there is a positive or negative bias

<div style="text-align:center">
<img src ="https://i.imgur.com/x8NY4kD.png">
</div>

_Image Source: Jolliff et al. [^first]_

Any point greater than RMSD*=1 is to be considered a poor performer since it doesn't offer improvement over the time series average.

Interestingly, the target diagram has no information about the correlation coefficient R, but some can be inferred, knowing that all the points within the RMSD* <1 are positively correlated (R>0), although, in [^first] it is shown that a circle marker with radius $M_{R1}$, means that all the points between that marker and the origin have a R coefficient larger than R1, where:

$$
M_{R1} = min(RMSD*') = \sqrt {1+R1^2-2R1^2}
$$

## Results

Let's now compare both models. If we execute this line, we will retrieve all model metrics:

```python
metrics_model_train = metrics(inv_y_train, inv_yhat_train)
metrics_model_test = metrics(inv_y_test, inv_yhat_test)

## Metrics Train
print('\t\t Train \t\t Test')
for item in metrics_model_train.keys():
    print ('% s: \t %.5f \t %.5f ' % (item, metrics_model_train[item], metrics_model_test[item]))
```

Output:

```python
		  	 Train 		 Test
avg_ref: 	  	 0.65426 	 0.53583 
sig_est: 	  	 0.08412 	 0.03160 
RMSD: 	  	  	 0.08439 	 0.05511 
avg_est: 	  	 0.61639 	 0.53135 
sigma_norm: 	  	 0.67749 	 0.50032 
sign_sigma: 	  	 -1.00000 	 -1.00000 
sig_ref: 	  	 0.12416 	 0.06317 
bias: 	  	  	 -0.03787 	 -0.00448 
RMSD_norm_unb: 	  	 0.68200 	 0.87258 
rsquared: 	  	 0.53801 	 0.23874 
normalised_bias: 	 -0.30502 	 -0.07093
```

And finally, we can compare both models, training and test dataframe with the function:

```python
targetDiagram(_dataframe, _plot_train)
```

Output:

![](https://i.imgur.com/PBuBOpw.png)

Here, every point that falls inside the yellow circle, will have an R<sup>2</sup> over 0.7, and so will be the red and green for R<sup>2</sup> over 0.5 and 0.9 respectively. We see that only one of our models performs well in that sense, which is the training dataset of the OLS. However, this dataset performs pretty badly in the test dataset, being the LSTM options much better. This target diagram offers information about how the hyperparameters affect our networks. For instance, increasing the training epochs from 100 to 200 does not affect greatly on model performance, but the effect of filtering the data beforehand to reduce the noise shows a much better model performance in both, training and test dataframe.

## Export the models

Let's now assume that we are happy with our models. Depending on the model we have developed (OLS or ML ), we follow different approaches for the export:

***Machine Learning Model***

We will use `joblib` to save the model metrics and parameters. The `keras` model will be saved with the `to_json` property of the `model` and the weights in an `h5` format with the `save_weights`ght:

```python
from os.path import join
from sklearn.externals import joblib

modelDirML = '/path/to/modelDir'
filenameML = join(modelDirML, model_name_ML)

# Save everything
joblib.dump(dictModel[model_name_ML]['metrics'], filenameML + '_metrics.sav')
joblib.dump(dictModel[model_name_ML]['parameters'], filenameML + '_parameters.sav')
model_json = model.to_json()
with open(filenameML + "_model.json", "w") as json_file:
    json_file.write(model_json)
    
model.save_weights(filenameML + "_model.h5")
print("Model " + model_name_ML + " saved in: " + modelDir)
```

Output:

```python
Model LSTM CO 200 epochs Filter 0.9 saved in: /path/to/modelDir
```

And in our directory:

```shell
➜  models ls -l
-rw-r--r-- Sep 11 12:54 LSTM CO 200 epochs Filter 0.9_metrics.sav
-rw-r--r-- Sep 11 12:54 LSTM CO 200 epochs Filter 0.9_model.h5
-rw-r--r-- Sep 11 12:54 LSTM CO 200 epochs Filter 0.9_model.json
-rw-r--r-- Sep 11 12:54 LSTM CO 200 epochs Filter 0.9_parameters.sav
```

***OLS model***

We will use `joblib` for all the objects serialisation in this case:

```python
from os.path import join
from sklearn.externals import joblib

modelDir_OLS = '/path/to/model'
filename_OLS = join(modelDir_OLS, model_name_OLS)

# Save everything
joblib.dump(dictModel[model_name_OLS]['metrics'], filename_OLS + '_metrics.sav')
joblib.dump(dictModel[model_name_OLS]['parameters'], filename_OLS + '_parameters.sav')
joblib.dump(dictModel[model_name_OLS]['model'], filename_OLS + '_model.sav')
print("Model saved in: " + modelDir_OLS)
```

Output:

```python
Model saved in: /path/to/model
```

And in the terminal:

```shell
➜  models ls -l
total 1928
-rw-r--r-- Sep 11 12:53 CO_MICS + Log(CO_MICS) + Poly(T) + PM25_metrics.sav
-rw-r--r-- Sep 11 12:53 CO_MICS + Log(CO_MICS) + Poly(T) + PM25_model.sav
-rw-r--r-- Sep 11 12:53 CO_MICS + Log(CO_MICS) + Poly(T) + PM25_parameters.sav
```

## Load Models from Disk

Now, sometime after having exported our model, let's assume we need to get it back:

***Machine Learning Model***

We will use the symmetric functions from `joblib` and `keras`:

```python
from os.path import join
from sklearn.externals import joblib
from keras.models import model_from_json

modelDirML = '/path/to/model'
filenameML = join(modelDirML, model_name_ML)

# Load Model and weights
json_file = open(filenameML + "_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(filenameML + "_model.h5")
print("Loaded " + model_name_ML + " from disk")

# Load params and metrics
loaded_params = joblib.load(filenameML + '_parameters.sav')
loaded_metrics = joblib.load(filenameML + '_metrics.sav')

display(loaded_params)
display(loaded_metrics)
```

Output:

```python
Loaded LSTM CO 200 epochs Filter 0.9 from disk

{'features': (['REF', 'CO_AD_BASE_STATION_CASE'],
  ['A', 'CO_MICS_RAW_STATION_CASE'],
  ['B', 'TEMP_STATION_CASE'],
  ['C', 'HUM_STATION_CASE'],
  ['D', 'PM_25_STATION_CASE'])}

{'test': {'RMSD': 0.055340715974325445,
  'RMSD_norm_unb': 0.8761932784857427,
  'avg_est': 0.5344016428091338,
  'avg_ref': 0.5358268506805136,
  'bias': -0.0014252078713797856,
  'normalised_bias': -0.022562028100955915,
  'rsquared': 0.23248054249786632,
  'sig_est': 0.03133999875370688,
  'sig_ref': 0.06316842905267908,
  'sigma_norm': 0.4961338951071746,
  'sign_sigma': -1.0},
 'train': {'RMSD': 0.08111001248781997,
  'RMSD_norm_unb': 0.6549199203336652,
  'avg_est': 0.6204429297293235,
  'avg_ref': 0.6542569775479774,
  'bias': -0.033814047818653936,
  'normalised_bias': -0.27234526337748927,
  'rsquared': 0.573229625070228,
  'sig_est': 0.08824634698454116,
  'sig_ref': 0.12415875128250474,
  'sigma_norm': 0.7107541439729025,
  'sign_sigma': -1.0}}
```

***OLS Model***

Similarly, we will use the `joblib.load` function:

```python
from os.path import join
from sklearn.externals import joblib

modelDir_OLS = '/path/to/model'
filename_OLS = join(modelDir_OLS, model_name_OLS)

# Load everything
loaded_metrics = joblib.load(filename_OLS + '_metrics.sav')
loaded_params = joblib.load(filename_OLS + '_parameters.sav')
loaded_model = joblib.load(filename_OLS + '_model.sav')
print("Loaded " + model_name_OLS + " from disk")

display(loaded_params)
display(loaded_metrics)
```

Output:
```python
Loaded CO_MICS + Log(CO_MICS) + Poly(T) + PM25 from disk

{'features': (['REF', 'CO_AD_BASE_STATION_CASE'],
  ['A', 'CO_MICS_RAW_STATION_CASE'],
  ['B', 'TEMP_STATION_CASE'],
  ['C', 'HUM_STATION_CASE'],
  ['D', 'PM_25_STATION_CASE']),
 'formula': 'REF ~ np.log10(A) + A + B + np.power(B,2) + D'}

{'test': {'RMSD': 0.0440714230263565,
  'RMSD_norm_unb': 0.8723428704290845,
  'avg_est': 0.550690169722107,
  'avg_ref': 0.5351888829750784,
  'bias': 0.015501286747028664,
  'normalised_bias': 0.30432821283315176,
  'rsquared': 0.2513771504173782,
  'sig_est': 0.031200761981503004,
  'sig_ref': 0.05093608181350988,
  'sigma_norm': 0.6125473509277183,
  'sign_sigma': -1.0},
 'train': {'RMSD': 0.062207196964372664,
  'RMSD_norm_unb': 0.5279216759963998,
  'avg_est': 0.6559505800446772,
  'avg_ref': 0.6559505800448995,
  'bias': -2.2226664952995634e-13,
  'normalised_bias': -1.8862669894154184e-12,
  'rsquared': 0.721298704013152,
  'sig_est': 0.10007571794915669,
  'sig_ref': 0.11783414054170561,
  'sigma_norm': 0.849293061324077,
  'sign_sigma': -1.0}}
```

And that's it! Now it is time to iterate and compare our models.

## References

[^first]:[Engineering statistics handbook](http://www.itl.nist.gov/div898/handbook/mpc/section5/mpc52.htm)
[^second]:[Summary diagrams for coupled hydrodynamic-ecosystem model skill assessment (Jolliff et al.)](https://www.sciencedirect.com/science/article/pii/S0924796308001140)
[^third]:[Machine learning mastery](https://machinelearningmastery.com)
