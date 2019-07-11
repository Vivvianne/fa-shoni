from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View the home page (to be added from landing page syntax)
    '''
    return render_template('men.html')
@app.route('/designers',methods=['GET'])
def designers():
    
    return render_template('designers.html')
@app.route('/designers')
def search_designers(search):
    designers = []
    search_string = search.data['search']
    if search_string:
        if search.data['select'] == 'Artist':
            qry = db_session.query(User, Profile).filter(
                Profile.id==User.profile_id).filter(
                    Profile.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'User':
            qry = db_session.query(User).filter(
                User.title.contains(search_string))
            results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Profile(profile)
        table.border = True
        return render_template('designer.html', table=table)