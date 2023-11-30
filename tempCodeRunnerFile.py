df['match']=matches['Match confidence']
        df1=df.sort_values('match')
        df2=df1[['Position', 'Company','Location']].head(10).reset_index()
        
        
        
        
        
    #return  'nothing' 
    return render_template('index.html',tables=[df2.to_html(classes='job')],titles=['na','Job'])