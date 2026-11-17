from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
df=pd.read_csv(BASE/'movie_scores.csv')
out=BASE/'images';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(10,5),layout='constrained')
x=list(range(len(df)));w=.36
ax.bar([i-w/2 for i in x],df.Tomatometer,w,label='Critics',color='#214f45')
ax.bar([i+w/2 for i in x],df.AudienceScore,w,label='Audience',color='#bd6351')
ax.set(xticks=x,xticklabels=['The Shape\nof Water','Black\nPanther','Dunkirk','The Martian','The Hobbit'],ylim=(0,105),ylabel='Positive-rating score (%)',title='Critics and audiences: five-film snapshot')
ax.legend(frameon=False);fig.savefig(out/'movie_comparison.png',dpi=160);plt.close(fig)
df['gap']=df.Tomatometer-df.AudienceScore
fig,ax=plt.subplots(figsize=(10,5),layout='constrained')
ax.barh(df.MovieTitle,df.gap,color=['#214f45' if v>=0 else '#bd6351' for v in df.gap])
ax.axvline(0,color='#65736e',lw=1);ax.set(xlabel='Critics minus audience (percentage points)',title='The direction of disagreement differs by film',xlim=(-25,25))
for i,v in enumerate(df.gap):ax.text(v+(0.6 if v>=0 else -.6),i,f'{v:+.0f}',va='center',ha='left' if v>=0 else 'right')
fig.savefig(out/'movie_gap.png',dpi=160);plt.close(fig)
df[['MovieTitle','Tomatometer','AudienceScore','gap']].to_csv(out/'movie_results.csv',index=False)
print('Movie charts and results generated from five supplied rows.')
