"""

# PROJETO VIDA

---
https://www.kaggle.com/kumarajarshi/life-expectancy-who<br>
Expectativa de vida global

# Aquisição dos Dados
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv('https://raw.githubusercontent.com/qodatecnologia/projeto-vida/master/data.csv')

df

df.shape

df.columns

df.info()

df.describe()

df.describe(include = ['object'])

df.describe(include = ['float'])

"""# Pré-processamento dos dados(explorar,limpar,preparar)

## Dados duplicados

---
"""

df.duplicated().sum()

# Poderiamos removar as duplicatas com drop_duplicates
df.drop_duplicates(inplace=True)

"""## Dados faltantes e preenchimento dos mesmos com mediana"""

df.isna().sum()

df.columns=['Country','Year','Status','Life_Expectancy','Adult_Mortality','Infant_death','Alcohol','Percentage_Expenditure','Hepatitis_B','Measles','BMI','Under_Five_Death','Polio','Total_Expenditure','Diphtheria','Hiv_Aids','GDP','Population','Thin_1_19_Years','Thin_5_9_Year','Income_Comp_Resource','Schooling']

df.info()

df[['Infant_death']].isna().sum()

df.Life_Expectancy=df.Life_Expectancy.fillna(df.Life_Expectancy.median())
df.Life_Expectancy.isna().sum()

df.info()

df.isna().sum()

df.Adult_Mortality=df.Adult_Mortality.fillna(df.Adult_Mortality.median())
df.Adult_Mortality.isna().sum()

df.Alcohol=df.Alcohol.fillna(df.Alcohol.median())
df.Alcohol.isna().sum()

df.Hepatitis_B=df.Hepatitis_B.fillna(df.Hepatitis_B.median())
df.Hepatitis_B.isna().sum()

df.BMI=df.BMI.fillna(df.BMI.median())
df.BMI.isna().sum()

df.Polio=df.Polio.fillna(df.Polio.median())
df.Polio.isna().sum()

df.Total_Expenditure = df.Total_Expenditure.fillna(df.Total_Expenditure.median())
df.Total_Expenditure.isna().sum()

df.isna().sum()

df.Diphtheria=df.Diphtheria.fillna(df.Diphtheria.median())
df.Diphtheria.isna().sum()

df.GDP=df.GDP.fillna(df.GDP.median())
df.GDP.isna().sum()

df.Population=df.Population.fillna(df.Population.median())
df.Population.isna().sum()

df.Thin_1_19_Years=df.Thin_1_19_Years.fillna(df.Thin_1_19_Years.median())
df.Thin_1_19_Years.isna().sum()

df.Thin_5_9_Year =df.Thin_5_9_Year.fillna(df.Thin_5_9_Year.median())
df.Thin_5_9_Year.isna().sum()

df.Income_Comp_Resource=df.Income_Comp_Resource.fillna(df.Income_Comp_Resource.median())
df.Income_Comp_Resource.isna().sum()

df.Schooling=df.Schooling.fillna(df.Schooling.median())
df.Schooling.isna().sum()

df.info()

"""## Outliers"""

# AMPLITUDE INTERQUARTIL PARA DETECTAR OUTLIERS
def find_outliers_tukey(x):
    q1 = x.quantile(.25)
    q3 = x.quantile(.75)
    iqr = q3 - q1 #INTER QUARTILE RANGE
    floor = q1 - 1.5*iqr
    ceiling = q3 + 1.5*iqr
    outlier_indices = list(x.index[(x < floor) | (x > ceiling)])
    outlier_values = list(x[outlier_indices])
    return outlier_indices, outlier_values

df.columns

print("Outliers for Year")
Year_indices, Year_values = find_outliers_tukey(df['Year'])
print(np.sort(Year_values))

print("Outliers for Life Expectancy")
Life_Expectancy_indices,Life_Expectancy_values = find_outliers_tukey(df['Life_Expectancy'])
print(np.sort(Life_Expectancy_values))

print("Outliers for Infant death")
Infant_death_indices,Infant_death_values = find_outliers_tukey(df['Infant_death'])
print(np.sort(Infant_death_values))

# Substituindo outlier por mediana
df["Infant_death"] = np.where(df["Infant_death"] >3, 3,df['Infant_death'])

df.Infant_death.median()

df.describe()

print("Outliers for Alcohol")
Alcohol_indices, Alcohol_values = find_outliers_tukey(df['Alcohol'])
print(np.sort(Alcohol_values))

print("Outliers for Percentage Expenditure")
Percentage_Expenditure_indices, Percentage_Expenditure_values = find_outliers_tukey(df['Percentage_Expenditure'])
print(np.sort(Percentage_Expenditure_values))

##Replacing the outlier with Median for Percentage Expenditure
df["Percentage_Expenditure"] = np.where(df["Percentage_Expenditure"] >100,64.8845366125,df['Percentage_Expenditure'])

df.Percentage_Expenditure.median()

df.describe()

print("Outliers for Hepatitis B")
Hepatitis_B_indices, Hepatitis_B_values = find_outliers_tukey(df['Hepatitis_B'])
print(np.sort(Hepatitis_B_values))

print("Outliers for Measles")
Measles_indices, Measles_values = find_outliers_tukey(df['Measles'])
print(np.sort(Measles_values))

##Replacing the outlier with Median for Percentage Expenditure
df["Measles"] = np.where(df["Measles"] >50,17,df['Measles'])

df.Measles.median()

df.describe()

print("Outliers for BMI")
BMI_indices, BMI_values = find_outliers_tukey(df['BMI'])
print(np.sort(BMI_values))

print("Outliers for Under Five Death")
Under_Five_Death_indices, Under_Five_Death_values = find_outliers_tukey(df['Under_Five_Death'])
print(np.sort(Under_Five_Death_values))

"""## Substituindo outlier com a mediana de "Under_Five_Death""""

df.Under_Five_Death.median()

df["Under_Five_Death"] = np.where(df["Measles"] >4,4,df['Under_Five_Death'])

df.describe()

print("Outliers Polio")
Polio_indices, Polio_values = find_outliers_tukey(df['Polio'])
print(np.sort(Polio_values))

print("Outliers Total Expenditure")
Total_Expenditure_indices, Total_Expenditure_values = find_outliers_tukey(df['Total_Expenditure'])
print(np.sort(Total_Expenditure_values))

print("Outliers Diphtheria")
Diphtheria_indices, Diphtheria_values = find_outliers_tukey(df['Diphtheria'])
print(np.sort(Diphtheria_values))

print("Outliers Hiv_Aids")
Hiv_Aids_indices, Hiv_Aids_values = find_outliers_tukey(df['Hiv_Aids'])
print(np.sort(Hiv_Aids_values))

print("Outliers GDP")
GDP_indices, GDP_values = find_outliers_tukey(df['GDP'])
print(np.sort(GDP_values))

"""## Substituindo outlier com mediana de "GDP""""

df.GDP.median()
df["GDP"] = np.where(df["GDP"] >2500,1766.947595,df['GDP'])

df.describe()

print("Outliers Population")
Population_indices, Population_values = find_outliers_tukey(df['Population'])
print(np.sort(Population_values))

print("Outliers Thin_1_19_Years")
Thin_1_19_Years_indices, Thin_1_19_Years_values = find_outliers_tukey(df['Thin_1_19_Years'])
print(np.sort(Thin_1_19_Years_values))

print("Outliers Thin_5_9_Year")
Thin_5_9_Year_indices, Thin_5_9_Year_values = find_outliers_tukey(df['Thin_5_9_Year'])
print(np.sort(Thin_5_9_Year_values))

print("Outliers Income Comp Resource")
Income_Comp_Resource_indices, Income_Comp_Resource_values = find_outliers_tukey(df['Income_Comp_Resource'])
print(np.sort(Income_Comp_Resource_values))

print("Outliers Schooling")
Schooling_indices, Schooling_values = find_outliers_tukey(df['Schooling'])
print(np.sort(Schooling_values))

df.columns

# UTILIZE AMPLITUDE INTERQUARTIL E ACABE COM TODOS OUTLIERS DESTE DATASET
# dica:
#q1 = x.quantile(.25)
#q3 = x.quantile(.75)
#iqr = q3 - q1 #INTER QUARTILE RANGE
#floor = q1 - 1.5*iqr # se menor, OUTLIER
#ceiling = q3 + 1.5*iqr # se maior, OUTLIER

"""## Dataviz"""

plt.figure(figsize=(20,15))
sns.heatmap(df.corr(),annot=True,linewidths=7)

"""## One hot Encoder para "Country"(str) ?!"""

pd.get_dummies(df.Country,prefix = "Country")

Country_dummies = pd.get_dummies(df.Country,prefix = "Country").iloc[:,0:]

df = pd.concat([df,Country_dummies],axis = 1)
df.head()

df=df.drop('Country',axis=1)
df.head()

"""## Lidando com a coluna "Status"(String) : One Hot encoder"""

pd.get_dummies(df.Status,prefix = "Status")

Status_dummies = pd.get_dummies(df.Status,prefix = "Status").iloc[:,0:]

df = pd.concat([df,Status_dummies],axis = 1)
df.head()

df=df.drop('Status',axis=1)
df.head()

"""##Feature Selection

---


Make a list of data frame column names
"""

l_column = list(df.columns) # Making a list out of column names
len_feature = len(l_column) # Length of column vector list
print(l_column)
print(len_feature)

"""## Features numericas em X e "Life Expectancy" em y"""

"""
colunas do df: 22
colunas removidas(status&Country): 2 
total: 20 colunas
"""
df.info()

X = df[l_column[0:len_feature-195]] 
X.columns

"""## Dropar a coluna target"""

X=X.drop('Life_Expectancy',axis=1)
X.columns

X=X.drop('Year',axis=1)
X.columns

y = df[l_column[len_feature-214]]

X.shape

X.head()

"""## Remover features que não geram valor"""

X=X.drop('Hepatitis_B',axis=1)
X=X.drop('Percentage_Expenditure',axis=1)
X=X.drop('Measles',axis=1)
X=X.drop('Under_Five_Death',axis=1)
X=X.drop('Total_Expenditure',axis=1)
X=X.drop('Population',axis=1)

X.columns

X.shape

y.shape

y.head()

"""# Modelo Preditivo

## Criação de X e y, treino/teste
"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

print("Features Treino:",X_train.shape)
print("Features Teste:",X_test.shape)
print()
print("Target Treino:",y_train.shape)
print("Target Teste:",y_test.shape)

"""### Treinar modelo preditivo"""

from sklearn.linear_model import LinearRegression
from sklearn import metrics

lm = LinearRegression() # Creating a Linear Regression object 'lm'

lm.fit(X_train,y_train) # Fit the linear model on to the 'lm' object itself i.e. no need to set this to another variable

"""# Avaliação do modelo e métricas
https://scikit-learn.org/stable/modules/model_evaluation.html

## Intercepto/coeficiente linear em um DataFrame
"""

print("Intercepto:", lm.intercept_)

print("Coeficiente Linear:", lm.coef_)

train_pred = lm.predict(X_train)

"""* MAE: Média da diferença absoluta entre previsto/realizado
* MSE: Média dos quadrados dos erros
* RMSE: Desvio padrão da diferença entre previsto/realizado
"""

# MSE
metrics.mean_squared_error(y_train,train_pred)

# MAE
metrics.mean_absolute_error(y_train,train_pred)

"""## R² do modelo
O R-quadrado é uma medida estatística de quão próximos os dados estão da linha de regressão ajustada. O R-quadrado está sempre entre 0 e 100%:

* 0% indica que o modelo não explica nada da variabilidade dos dados de resposta ao redor de sua média.
* 100% indica que o modelo explica toda a variabilidade dos dados de resposta ao redor de sua média.

Em geral, quanto maior o R-quadrado, melhor o modelo se ajusta aos seus dados.
"""

print(f"R-quadrado: {round(metrics.r2_score(y_train,train_pred),2)}")

"""## Scatter plot das predições/valores reais: devemos encontrar uma linha reta"""

plt.figure(figsize=(10,7))
plt.title("Actual vs. predicted ",fontsize=25)
plt.xlabel("Actual test ",fontsize=18)
plt.ylabel("Predicted ", fontsize=18)
plt.scatter(x=y_test,y=predictions)

"""## Métricas de avaliação para regressão(treino)
* MAE: Média da diferença absoluta entre previsto/realizado
* MSE: Média dos quadrados dos erros
* RMSE: Desvio padrão da diferença entre previsto/realizado
"""

print(f"Mean absolute error (MAE): {metrics.mean_absolute_error(y_train,train_pred)}")
print(f"Mean square error (MSE): {metrics.mean_squared_error(y_train,train_pred)}")
print(f"Root mean square error (RMSE): {np.sqrt(metrics.mean_squared_error(y_train,train_pred))}")

"""## Métricas de avaliação para regressão(teste)
* MAE: Média da diferença absoluta entre previsto/realizado
* MSE: Média dos quadrados dos erros
* RMSE: Desvio padrão da diferença entre previsto/realizado
"""

print(f"Mean absolute error (MAE): {metrics.mean_absolute_error(y_test,predictions)}")
print(f"Mean square error (MSE): {metrics.mean_squared_error(y_test,predictions)}")
print(f"Root mean square error (RMSE): {np.sqrt(metrics.mean_squared_error(y_test,predictions))}")

"""## Mean Absolute Percentage error(y_train)
O MAPE (Erro Absoluto Médio Percentual) mede o erro em porcentagem. Este é calculado como a média do erro percentual
"""

def mean_absolute_percentage_error(y_train, train_pred):
    y_train,train_pred=np.array(y_train),np.array(train_pred)
    return np.mean(np.abs((y_train - train_pred)/y_train))*100

print(f"Mean absolute percentage error (MAPE): {mean_absolute_percentage_error(y_train,train_pred)}")

"""## Mean Absolute Percentage error(y_test)
O MAPE (Erro Absoluto Médio Percentual) mede o erro em porcentagem. Este é calculado como a média do erro percentual
"""

def mean_absolute_percentage_error(y_test, predictions):
    y_test,predictions=np.array(y_test),np.array(predictions)
    return np.mean(np.abs((y_test - predictions)/y_test))*100

print(f"Mean absolute percentage error (MAPE): {mean_absolute_percentage_error(y_test,predictions)}")
