import argparse
import datetime as dt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('in_file')
parser.add_argument('-o', '--out_file', required=False, default='report.pdf')
parser.add_argument('-a', '--author', required=False, default='N/A')

args = parser.parse_args()
input_file = args.in_file
output_file = args.out_file
author = args.author

df = pd.read_csv(input_file)
with PdfPages(output_file) as pdf:

    heading = 'Student Performance'
    date_text = f'Produced: {dt.date.today()}'
    author_text = f'By: {author}'
    cols_text = f'Columns:\n {'\n'.join(['- ' + col for col in df.columns])}'
    rows_text = f'Rows: {len(df)}'

    figure = plt.figure()
    figure.text(0.1, 0.85, heading, fontsize=24, fontweight='bold')
    figure.add_artist(plt.Line2D([0.1, 0.9], [0.83, 0.83], color='black', linewidth=1.5))
    figure.text(0.1, 0.75, date_text)
    figure.text(0.1, 0.7, author_text)
    figure.text(0.1, 0.35, cols_text)
    figure.text(0.1, 0.3, rows_text)
    pdf.savefig()
    plt.close(figure)

    READING = 'reading score'
    WRITING = 'writing score'
    MATHS = 'math score'

    axes = df.groupby(['gender', 'lunch'])[[READING, WRITING]].mean().plot(
        kind='bar',
        title='Mean Reading Score by Gender & Lunch',
        yticks=range(0, 110, 10),
        xlabel='gender (lunch)',
        rot=0
    )
    
    axes.set_xticklabels(['F (free)', 'F (std)', 'M (free)', 'M (std)'])
    pdf.savefig()
    plt.close()


    df.plot(
        kind='scatter',
        title='Reading and Maths Correlation',
        x=READING,
        y=MATHS,
        alpha=0.5
    )

    pdf.savefig()
    plt.close()


    df[[READING, WRITING, MATHS]].plot(
        kind='hist',
        title='Score Distribution',
        subplots=True,
        bins=50
    )

    pdf.savefig()
    plt.close()


    df['race/ethnicity'].value_counts().plot(
        kind='pie',
        title='Race/Ethnic Group Proportions',
        y='race/ethnicity',
        autopct='%1.1f%%'
    )

    pdf.savefig()
    plt.close()