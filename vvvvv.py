from flask import Flask
app =Flask(_name_)
@app.route('/api/data',method=['get'])
def get_data():
data ={"Name":['New York','New York','Los Angeles','Los Angeles','Chicago','Chicago','Houston','Houston','Phoenix','Phoenix','Philadelphia','Philadelphia'],
"gender":['male','female','male','female','male','female','male','female','male','female','male','female'],
"population":['6000000','4300000','1985000','2070000','1350000','1400000','1100000','1120000','800000','810000','750000','770000']
    }
return jsonify()
if name ='main'
app run()
