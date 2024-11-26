# Model Card

## Model Details

This model was created as a project for Udacity as part of Western Governors University
Data Analytics program. The model utilizes the RandomForestClassifier, produced by Scikit-Learn.

## Intended Use Cases

This model is used to predict if an individual makes more or less than $50,000 a year based on several idenfying attributes, which are included in the census data set. Although this model was created for the specific use of my degree program, it can be applied in other setting.

## Training Data

The trainig data was obtained from the 1994 US Census Database, with the raw file downloadable at this [link](https://archive.ics.uci.edu/dataset/20/census+income). The data contains individuals demographic information as well as income information.

## Evaluation Data

The data was evaluated at 20% of the population of the dataset. This was based on the best practice recomendation from this [resource](https://medium.com/@aaryanohekar277/what-happens-if-we-do-not-mention-test-size-in-the-train-test-split-b0043b16db27)

## Metrics

The model, with a randome_sate of 42 as the only parameter passed, received a precision score of 0.7391, recall at 0.6384, and F1 at 0.6851

## Ethical Considerations

The census.csv model is a based on a subset of the complete census and therefore does not represent the entire population. Making assumption based on demographic factors such as race and sex can also be unethical as this would not represent an entire population of the demographic.

## Caveats and Recommendations

The data set used for this model was created in 1994 and is 30 years behind current. Although the model gives us valuable insight, many of the demographic attributes have likely changed, along with the average income. We can assume that with inflation and real wages rising over the last 30 years, the wages from the census.csv would likely be signifigantly different than what is current, biased towards those who make less than $50,000.