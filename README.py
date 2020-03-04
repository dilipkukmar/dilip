# dilip
#AUTO TAG GENERATOR
import tag_gen2
import manava
from flask import *
from flask import Flask,redirect,url_for,request,render_template
app = Flask(__name__)
@app.route("/login",methods=['POST','GET'])
def login():
    resultant_tag=[]
    if(request.method=='POST'):
        the_title_you_have_entered=request.form.get('title')
        print(the_title_you_have_entered)
        resultant_tag=tag_gen2.tag_gen(the_title_you_have_entered)
        manava.donee(the_title_you_have_entered,resultant_tag)
        print(resultant_tag[1])
        c='background-image: url("/static/images/abb.jpeg");background-size:100% 100%;background-position:fixed;'
        return render_template('login.html',img=c,resultant_tag=resultant_tag,the_title_you_have_entered=the_title_you_have_entered)
    else:
        the_title_you_have_entered=request.form.get('title')
        print(the_title_you_have_entered)
        resultant_tag=tag_gen2.tag_gen(the_title_you_have_entered)
        manava.donee(the_title_you_have_entered,resultant_tag)
        print(resultant_tag[1])
        c='background-image: url("/static/images/abb.jpeg");background-size:100% 100%;background-position:fixed;'
        #return render_template('login.html',
        return render_template('login.html',img=c, resultant_tag=resultant_tag,the_title_you_have_entered=the_title_you_have_entered)
if __name__=='__main__':
    app.run(debug = True)
'''<div>
<br><input  type="submit"  size="45"  class="lo" id="subb" onclick="callthatpage()" value="Filter search"/><br>
</div>
'''

