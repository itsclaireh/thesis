import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

def numResponses(df, responseNo):
    return len(df.loc[df['preventingSH']==responseNo,['preventingSH']]);

def barchartPrev(face,yout,insta,twit,snap,redd,tumbl,other):
    objects = ('Facebook','YouTube','Instagram','Twitter','Snapchat','Reddit');
    #objects = ('Facebook','YouTube','Instagram','Twitter','Snapchat','Reddit','Tumblr','Other');
    #objects = ('Other','Tumblr','Reddit','Snapchat','Twitter','Instagram','YouTube','Facebook');
    n_groups = len(objects);
    index = np.arange(len(objects));
    bar_width = 0.18;
    opacity=0.8;
    #notadequate=(numResponses(face,'1'), numResponses(yout,'1'),numResponses(insta,'1'),numResponses(twit,'1'),numResponses(snap,'1'),numResponses(redd,'1'),numResponses(tumbl,'1'), numResponses(other,'1'));
    #some=(numResponses(face,'2'), numResponses(yout,'2'),numResponses(insta,'2'),numResponses(twit,'2'),numResponses(snap,'2'),numResponses(redd,'2'),numResponses(tumbl,'2'), numResponses(other,'2'));
    #adequate=(numResponses(face,'3'), numResponses(yout,'3'),numResponses(insta,'3'),numResponses(twit,'3'),numResponses(snap,'3'),numResponses(redd,'3'),numResponses(tumbl,'3'), numResponses(other,'3'));
    #idk=(numResponses(face,'4'), numResponses(yout,'4'),numResponses(insta,'4'),numResponses(twit,'4'),numResponses(snap,'4'),numResponses(redd,'4'),numResponses(tumbl,'4'), numResponses(other,'4'));

    notadequate=(numResponses(face,'1'), numResponses(yout,'1'),numResponses(insta,'1'),numResponses(twit,'1'),numResponses(snap,'1'),numResponses(redd,'1'));
    some=(numResponses(face,'2'), numResponses(yout,'2'),numResponses(insta,'2'),numResponses(twit,'2'),numResponses(snap,'2'),numResponses(redd,'2'));
    adequate=(numResponses(face,'3'), numResponses(yout,'3'),numResponses(insta,'3'),numResponses(twit,'3'),numResponses(snap,'3'),numResponses(redd,'3'));
    idk=(numResponses(face,'4'), numResponses(yout,'4'),numResponses(insta,'4'),numResponses(twit,'4'),numResponses(snap,'4'),numResponses(redd,'4'));

    rects1=plt.bar(index, notadequate, bar_width,alpha=opacity,color='#450a5cff',label='Not Adequate');
    rects2=plt.bar(index+bar_width, some, bar_width,alpha=opacity,color='#2d6e8eff',label='Somewhat');
    rects3=plt.bar(index+bar_width*2, adequate, bar_width,alpha=opacity,color='#49be6eff',label='Adequate');
    rects4=plt.bar(index+bar_width*3, idk, bar_width,alpha=opacity,color='#e1e329ff',label='I don\'t know');


    plt.xlabel('Social Media Platform');
    plt.ylabel('Number of Responses');
    plt.title('Ability to Prevent Sexual Harassment')
    plt.xticks(index+bar_width*1.5, objects,rotation=45, horizontalalignment='right');
    plt.legend();
    plt.tight_layout();

    plt.savefig("pdfs/barPreventing.pdf", bbox_inches="tight");
    plt.savefig("pngs/barPreventing.png", bbox_inches="tight");
    plt.show();

    ind = [x for x, _ in enumerate(objects)];

    notadequate=np.array([numResponses(face,'1'), numResponses(yout,'1'),numResponses(insta,'1'),numResponses(twit,'1'),numResponses(snap,'1'),numResponses(redd,'1')],dtype=float);
    some=np.array([numResponses(face,'2'), numResponses(yout,'2'),numResponses(insta,'2'),numResponses(twit,'2'),numResponses(snap,'2'),numResponses(redd,'2')],dtype=float);
    adequate=np.array([numResponses(face,'3'), numResponses(yout,'3'),numResponses(insta,'3'),numResponses(twit,'3'),numResponses(snap,'3'),numResponses(redd,'3')],dtype=float);
    idk=np.array([numResponses(face,'4'), numResponses(yout,'4'),numResponses(insta,'4'),numResponses(twit,'4'),numResponses(snap,'4'),numResponses(redd,'4')],dtype=float);

    total = adequate+some+notadequate+idk;
    proportion_nota = np.true_divide(notadequate,total, out=np.zeros_like(notadequate), where=total!=0)*100;
    proportion_some = np.true_divide(some,total, out=np.zeros_like(some), where=total!=0)*100;
    proportion_adeq = np.true_divide(adequate,total, out=np.zeros_like(adequate), where=total!=0)*100;
    proportion_idk = np.true_divide(idk,total, out=np.zeros_like(idk), where=total!=0)*100;

    plt.bar(ind, proportion_nota, width=0.8, label='Not Adequate',color='#450a5cff',bottom=proportion_some+proportion_adeq+proportion_idk);
    plt.bar(ind, proportion_some, width=0.8, label='Somewhat',color='#2d6e8eff',bottom=proportion_adeq+proportion_idk);
    plt.bar(ind, proportion_adeq, width=0.8, label='Adequate',color='#49be6eff',bottom=proportion_idk);
    plt.bar(ind, proportion_idk, width=0.8, label='I don\'t know',color='#e1e329ff');

    plt.xticks(ind, objects)
    plt.ylabel("Percentage of Responses")
    plt.xlabel("Social Media Platforms")
    plt.title('Ability to Prevent Sexual Harassment')
    plt.ylim=1.0;
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.legend(loc='lower center', ncol=2);
    plt.tight_layout();


    #plt.tight_layout();
    plt.savefig("pdfs/stackPreventing.pdf", bbox_inches="tight");
    plt.savefig("pngs/stackPreventing.png", bbox_inches="tight");
    plt.show();
