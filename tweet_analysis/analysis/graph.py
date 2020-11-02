from wordcloud import WordCloud
import matplotlib.pyplot as plt
from tweet_analysis.utils import save_plt_fig
from datetime import datetime

def generate_wordcloud(tweets=[], fig_id=str(datetime.now())):
    wordcloud = WordCloud(width=500, height=500).generate(' '.join(tweets))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    save_plt_fig(fig_id)


