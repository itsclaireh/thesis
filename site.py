#app.py

from flask import Flask, request, render_template
from test import classify
app = Flask(__name__)

#@app.route('/')
#def runit():
#    return render_template('index.html');

@app.route('/main',methods=['GET','POST'])
def form_example():
    rel=''
    stance='';
    cat='';
    prob1='';
    prob2='';
    prob3='';


    if request.method == 'POST':
        tweet = request.form.get('tweet');

        if len(tweet) < 281:
            wowza = classify(tweet);
            relateed=wowza[0];
            stancey=wowza[1];
            categ=wowza[2];
            probby1=wowza[3];
            probby2=wowza[4];
            probby3=wowza[5];

            if wowza[0]=='1':
                rel='Related';
                prob1 = probby1[0];
            elif wowza[0]=='2':
                rel='Not Related';
                prob1 = probby[1];

            if wowza[1]=='1':
                stance='Support';
                prob2 = probby2[0];
            elif wowza[1]=='2':
                stance='Against';
                prob2 = probby2[1];
            elif wowza[1]=='3':
                stance='Neutral';
                prob2 = probby2[3];

            if wowza[2]=='1':
                cat='Patronizing';
                prob3 = probby3[0];
            elif wowza[2]=='2':
                cat='Unwanted Sexual Attention';
                prob3 = probby3[1];
            elif wowza[2]=='3':
                cat='Predatory';
                prob3 = probby3[2];
            elif wowza[2]=='4':
                cat='Not Enough Context';
                prob3 = probby3[3];

        else:
            return 'Tweet is too long';

    return '''<!DOCTYPE HTML>
    <html lang = "en">
    <head>
      <!-- basic.html -->
      <title>Thesis</title>
      <meta charset = "UTF-8" />
      <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="style.css">

    </head>
    <body>
      <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-sm-6 form-group">

      <h1>Enter your Tweet Below</h1>
      <p>
        Click submit to receive your classification.
      </p>

        <form name="tweet" method="POST">
        <label>Tweet</label>
        <textarea placeholder="Enter your tweet here... (limited to 280 characters)" rows="3" class="form-control" name="tweet" id="tweet" maxlength="280"></textarea><span id='remainingC'></span>
        <br/>
        <input type="submit" value="Submit">
      </form>
      </div>
    </div> <!--row-->
    <script src="scripty.js"></script>

  <div class="row">
  <div class="col-sm-3"></div>
  <div class="col-sm-6 form-group">
  <p>Your tweet was: {0}</p>
    <table>
    <col width="150">
    <col width="300">
    <col width="300">
    <col width="300">
    <tr>
        <th></th>
        <th>Relavance</th>
        <th>Stance</th>
        <th>Category</th>
    </tr>
    <tr>
        <th>Classification:</th>
        <th>{1}</th>
        <th>{2}</th>
        <th>{3}</th>
    </tr>
    <tr>
        <th>Probability:</th>
        <th>{4:.2f}%</th>
        <th>{5:.2f}%</th>
        <th>{6:.2f}%</th>
    </tr>
    </table>
    </div>
    </div><!--row-->
    </body>
    </html>'''.format(tweet,rel,stance,cat,prob1*100,prob2*100,prob3*100)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
