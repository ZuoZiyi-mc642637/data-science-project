from pathlib import Path
import json
import pandas as pd
from scipy.stats import pearsonr,spearmanr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
df=pd.read_csv(BASE/'zone_indicators.csv');df=df[df.analysis_scope=='land'].copy()
assert len(df)==23 and df.zone_id.is_unique
assert (df.area_km2>0).all()
assert int(df.four_categories_count.sum())==977
assert abs((df.elderly_65plus/df.total_population*100-df.elderly_share_pct)).max()<1e-8
assert abs((df.four_categories_count/df.area_km2-df.four_categories_density)).max()<1e-7
x=df.elderly_share_pct;y=df.four_categories_density
r,p=pearsonr(x,y);rho,sp=spearmanr(x,y)
out=BASE/'results';out.mkdir(exist_ok=True)
results={'zones':len(df),'core_records':int(df.four_categories_count.sum()),'extended_records':int(df.extended_all_count.sum()),'pearson_r':float(r),'pearson_p_two_sided':float(p),'spearman_rho':float(rho),'spearman_p_two_sided':float(sp),'population_year':2021,'facility_snapshot_year':2026}
(out/'statistics.json').write_text(json.dumps(results,indent=2)+'\n')
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(9,5.6),layout='constrained')
ax.scatter(x,y,s=65,color='#214f45',alpha=.85)
for _,row in df.iterrows():ax.annotate(str(int(row.zone_id)),(row.elderly_share_pct,row.four_categories_density),xytext=(4,4),textcoords='offset points',fontsize=8)
ax.set(xlabel='Residents aged 65+ (%), 2021',ylabel='Core-four facility records per km², 2026',title='Macao: an exploratory association across 23 land zones')
ax.text(.02,.97,f'Pearson r = {r:.3f}, p = {p:.3f}\nSpearman ρ = {rho:.3f}, p = {sp:.3f}',transform=ax.transAxes,va='top',bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
fig.savefig(out/'macao_scatter.png',dpi=160);plt.close(fig)
cols=['elderly_count','pharmacy_count','clinic_count','park_count'];counts=df[cols].sum()
fig,ax=plt.subplots(figsize=(9,5),layout='constrained')
bars=ax.barh(['Older-person service centres','Pharmacies','Clinics','Parks / gardens'],counts,color='#214f45')
ax.bar_label(bars,padding=5);ax.set(xlabel='Matched facility records (count)',title='Core four: 977 records, with an uneven category mix',xlim=(0,max(counts)*1.2));ax.invert_yaxis()
fig.savefig(out/'macao_categories.png',dpi=160);plt.close(fig)
print(json.dumps(results))
