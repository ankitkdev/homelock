from flask import Flask, render_template, Response, request, redirect, url_for
import logging
from logging.handlers import RotatingFileHandler

application=app = Flask(__name__)

app.route("/")
@app.errorhandler(Exception)
def all_exception_handler(error):
   return render_template('index.html')


@app.route('/get_toggled_status') 
def toggled_status():
  current_status = request.args.get('status')
  if current_status == 'ap':
      app.logger.info("APP1 USED")
      return redirect("https://maker.ifttt.com/trigger/SP1_on/with/key/crmZamR-luaX4gK8HILby7", code=302)
    
  if current_status == 'ar':
      app.logger.info("APP1 CLOSED")
      return redirect("https://maker.ifttt.com/trigger/SP1_off/with/key/crmZamR-luaX4gK8HILby7", code=302)
      
  return render_template('index.html');

@app.route('/get_toggled_status1') 
def toggled_status1():
  current_status1 = request.args.get('status')
  if current_status1 == 'ap1':
      app.logger.info("APP2 USED")
      return redirect("https://maker.ifttt.com/trigger/SP2_on/with/key/crmZamR-luaX4gK8HILby7", code=302)
  if current_status1 == 'ar1':
      app.logger.info("APP2 CLOSED")
      return redirect("https://maker.ifttt.com/trigger/SP2_off/with/key/crmZamR-luaX4gK8HILby7", code=302)
      
  return render_template('index.html');


@app.route('/get_toggled_status2') 
def toggled_status2():
    current_status2 = request.args.get('status')
    if current_status2 == 'ap2':
        app.logger.info("APP3 USED")
        return redirect("https://maker.ifttt.com/trigger/SP3_on/with/key/crmZamR-luaX4gK8HILby7", code=302)
    if current_status2 == 'ar2':
      app.logger.info("APP3 CLOSED")
      return redirect("https://maker.ifttt.com/trigger/SP3_off/with/key/crmZamR-luaX4gK8HILby7", code=302)
      
    return render_template('index.html');

@app.route('/get_toggled_status3') 
def toggled_status3():
  current_status3 = request.args.get('status')
  if current_status3 == 'ap3':
      app.logger.info("LOCK USED")
      return redirect("#", code=302)
  if current_status3 == 'ar3':
      app.logger.info("LOCK CLOSED")
      return redirect("#", code=302)
     
  return render_template('index.html');
      




if __name__ == "__main__":
    logHandler = RotatingFileHandler('homizone.log', maxBytes=1000, backupCount=1)
    
    logHandler.setLevel(logging.DEBUG)

    app.logger.setLevel(logging.DEBUG)

    logHandler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))
                            
    app.logger.addHandler(logHandler)    
    app.run(debug="true")
