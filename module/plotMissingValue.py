import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def percentage(orders_df):
    missing = orders_df.isnull().sum()*100 / len(orders_df)

    percentage_missing = pd.DataFrame({'column':orders_df.columns,
                                       'missing_percentage %':missing.values})
    percentage_missing['missing_percentage %'] = percentage_missing['missing_percentage %'].round(2)
    percentage_missing = percentage_missing.sort_values('missing_percentage %', ascending=False)
    percentage_missing = percentage_missing.reset_index()
    percentage_missing = percentage_missing.drop('index', axis=1)

    # plot the missing value percentage
    plt.figure(figsize=(10,5))
    ax = sns.barplot(x='missing_percentage %', y='column', data=percentage_missing, color='#E1341E')
    for p in ax.patches:
        ax.annotate("%.2f" % p.get_width() + '%', xy=(p.get_width(), p.get_y()+p.get_height()/2),
                xytext=(8, 0), textcoords='offset points' ,ha="left", va="center", fontsize=10)
    plt.title('Missing values Percentage for Each Column', fontsize=17, fontweight='bold')
    plt.ylabel('Column', fontsize=12)
    plt.xlabel('Missing percentage %', fontsize=12)
    plt.xlim(0,50)
    plt.show()