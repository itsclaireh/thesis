#app.py

from flask import Flask, request
app = Flask(__name__)

@app.route('/form-example',methods=['GET','POST'])
def form_example():
    return '''<!DOCTYPE HTML>
    <html lang = "en">
    <head>
      <!-- basic.html -->
      <title>Thesis</title>
      <meta charset = "UTF-8" />
      <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>


    </head>
    <body>
      <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-sm-6 form-group">

      <h1>Enter your Tweet Below</h1>
      <p>
        This is a paragraph.
        Note that the text is automatically wrapped.
      </p>

        <form name="tweet" action="test.py" method="get">
        <label>Tweet</label>
        <textarea placeholder="Enter the textarea input here.. (limited to 280 characters)" rows="3" class="form-control" name="tweet" id="tweet" maxlength="280"></textarea><span id='remainingC'></span>
        <br/>
        <input type="submit" value="Submit">
      </form>
      </div>
    </div> <!--row-->

    </body>
    </html>


    '''
if __name__ == '__main__':
    app.run(debug=True, port=5000)