import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

def numResponses(df, responseNo):
    return len(df.loc[df['reportingSH']==responseNo,['reportingSH']]);

def barchartRep(face,yout,insta,twit,snap,redd,tumbl,other):
    objects = ('Facebook','YouTube','Instagram','Twitter','Snapchat','Reddit','Tumblr','Other');
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



    rects1=plt.bar(index, notadequate, bar_width,alpha=opacity,color='#450a5cff',label='Not adequate');
    rects1=plt.bar(index+bar_width, some, bar_width,alpha=opacity,color='#2d6e8eff',label='Some');
    rects1=plt.bar(index+bar_width*2, adequate, bar_width,alpha=opacity,color='#49be6eff',label='Adequate');
    rects1=plt.bar(index+bar_width*3, idk, bar_width,alpha=opacity,color='#e1e329ff',label='I don\'t know');


    plt.xlabel('Social Media Platform');
    plt.ylabel('Number of Responses');
    plt.title('Evaluation of Social Media\'s Mechanisms \nFor Reporting Sexual Harassment')
    plt.xticks(index+bar_width*1.5, objects);
    plt.legend();
    plt.tight_layout();

    plt.savefig("barReporting.pdf", bbox_inches="tight");
    plt.savefig("barReporting.png", bbox_inches="tight");
    plt.show();
