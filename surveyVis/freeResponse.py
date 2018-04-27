from barPreventing import barchartPrev
from barReporting import barchartRep
from barStackReporting import barStackRep
from barStackPreventing import barStackPrev
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.font_manager import FontProperties


df = pd.read_csv('improvementsOptionsGroup.csv',header=None,index_col=None,encoding='utf8',dtype='str');
columns = ['group','gender','improvementsOption'];
df.columns = np.ravel(columns);

t_auth = t_mod = t_disc = t_acctpriv = t_admin = t_report = t_know = t_privconc = t_victim = t_none = t_idc = 0;
m_auth = m_mod = m_disc = m_acctpriv = m_admin = m_report = m_know = m_privconc = m_victim = m_none = m_idc = 0;
f_auth = f_mod = f_disc = f_acctpriv = f_admin = f_report = f_know = f_privconc = f_victim = f_none = f_idc = 0;


for i, row in df.iterrows():

    t_auth = t_auth+1 if '1' in row.group else t_auth;
    t_disc = t_disc+1 if '2' in row.group else t_disc;
    t_acctpriv = t_acctpriv+1 if '3' in row.group else t_acctpriv;
    t_admin = t_admin+1 if '4' in row.group else t_admin;
    t_report = t_report+1 if '5' in row.group else t_report;
    t_know = t_know+1 if '6' in row.group else t_know;
    t_privconc = t_privconc+1 if '7' in row.group else t_privconc;
    t_victim = t_victim+1 if '8' in row.group else t_victim;
    t_none = t_none+1 if '9' in row.group else t_none;
    t_idc = t_idc+1 if '10' in row.group else t_idc;

    if row.gender == '1':
        m_auth = m_auth+1 if '1' in row.group else m_auth;
        m_disc = m_disc+1 if '2' in row.group else m_disc;
        m_acctpriv = m_acctpriv+1 if '3' in row.group else m_acctpriv;
        m_admin = m_admin+1 if '4' in row.group else m_admin;
        m_report = m_report+1 if '5' in row.group else m_report;
        m_know = m_know+1 if '6' in row.group else m_know;
        m_privconc = m_privconc+1 if '7' in row.group else m_privconc;
        m_victim = m_victim+1 if '8' in row.group else m_victim;
        m_none = m_none+1 if '9' in row.group else m_none;
        m_idc = m_idc+1 if '10' in row.group else m_idc;

    if row.gender == '2':
        f_auth = f_auth+1 if '1' in row.group else f_auth;
        f_disc = f_disc+1 if '2' in row.group else f_disc;
        f_acctpriv = f_acctpriv+1 if '3' in row.group else f_acctpriv;
        f_admin = f_admin+1 if '4' in row.group else f_admin;
        f_report = f_report+1 if '5' in row.group else f_report;
        f_know = f_know+1 if '6' in row.group else f_know;
        f_privconc = f_privconc+1 if '7' in row.group else f_privconc;
        f_victim = f_victim+1 if '8' in row.group else f_victim;
        f_none = f_none+1 if '9' in row.group else f_none;
        f_idc = f_idc+1 if '10' in row.group else f_idc;

totals = np.array([t_auth, t_disc,t_acctpriv,t_admin,t_report,t_know,t_privconc,t_victim,t_none,t_idc]);
menTotals = np.array([m_auth,m_disc,m_acctpriv,m_admin,m_report,m_know,m_privconc,m_victim,m_none,m_idc]);
womenTotals = np.array([f_auth,f_disc,f_acctpriv,f_admin,f_report,f_know,f_privconc,f_victim,f_none,f_idc]);

print(totals);
print(sum(totals));
print(menTotals);
print(sum(menTotals));
print(womenTotals);
print(sum(womenTotals));

groups = ['Do Not Care','None','Victim','Privacy Conerns','Knowledge','Reporting','Administrative','Account Privacy','Discpline','Authority'];
#groups = ['Authority','Discipline','Account Privacy','Administrative','Reporting','Knowledge','Privacy Conerns','Victim','None','Do Not Care'];

N=10;
ind = np.arange(N);
bar_width = 0.8;
bar1 = plt.bar(ind,totals,bar_width,color='#450a5cff',label='Total Responses');

plt.ylabel('Number of Responses');
plt.title('Addressing Sexual Harassment on Social Media');
plt.xlabel('Solution Type');
plt.xticks(ind,groups,rotation=45, horizontalalignment='right');
plt.legend(loc='best');
plt.tight_layout();

plt.savefig("pdfs/FRtotals.pdf", bbox_inches="tight");
plt.savefig("pngs/FRtotals.png", bbox_inches="tight");
plt.show();

twobar_width = 0.35;
bar2 = plt.bar(ind,menTotals,twobar_width,color='#2d6e8eff',label='Male Responses');
bar3 = plt.bar(ind+twobar_width,womenTotals,twobar_width,color='#49be6eff',label='Female Responses');

plt.ylabel('Number of Responses per Gender Identity');
plt.title('Addressing Sexual Harassment on Social Media');
plt.xlabel('Solution Type');
plt.xticks(ind+twobar_width/2,groups,rotation=45, horizontalalignment='right');
plt.legend(loc='best');
plt.tight_layout();

plt.savefig("pdfs/FRtotalsgender.pdf", bbox_inches="tight");
plt.savefig("pngs/FRtotalsgender.png", bbox_inches="tight");
plt.show();
