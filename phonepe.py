import os
import json
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import pymysql
import plotly.express as px
from git.repo.base import Repo


#Get Data from Phonepe (6 tables)
#aggregated transaction 
path_1 ="C:/Users/santh/Desktop/Capstone Projects/New folder/PROJECTS/PhonePe/pulse/data/aggregated/transaction/country/india/state/"
aggr_trans_list = os.listdir(path_1)
data1 = {'state':[],'year':[],'quarter':[],'transaction_type':[],'transaction_count':[],'transaction_amount':[]}

for state in aggr_trans_list:
    current_state = path_1+state+"/"
    aggr_year_list = os.listdir(current_state)
    
    for year in aggr_year_list:
        current_year = current_state+year+"/"
        aggr_file_list = os.listdir(current_year)
        
        for file in aggr_file_list:
            current_file = current_year+file
            aggr_data = open(current_file,"r")

            S = json.load(aggr_data)
    
            for i in S['data']['transactionData']:
                name = i["name"]
                count = i['paymentInstruments'][0]['count']
                amount = i['paymentInstruments'][0]['amount']
                data1["transaction_type"].append(name)
                data1["transaction_count"].append(count)
                data1['transaction_amount'].append(amount)
                data1['state'].append(state)
                data1['year'].append(year)
                data1['quarter'].append(int(file.strip(".json")))

aggr_trans_df = pd.DataFrame(data1)
aggr_trans_df['state'] = aggr_trans_df['state'].str.replace("-"," ")
aggr_trans_df['state'] = aggr_trans_df['state'].str.title()



#aggregated user
path_2 = "C:/Users/santh/Desktop/Capstone Projects/New folder/PROJECTS/PhonePe/pulse/data/aggregated/user/country/india/state/"
aggr_user_list = os.listdir(path_2)
data2 = {'state':[],'year':[],'quarter':[],'brand':[],'transaction_count':[],'percentage':[]}

for state in aggr_trans_list:
    current_state = path_2+state+"/"
    aggr_year_list = os.listdir(current_state)
    
    for year in aggr_year_list:
        current_year = current_state+year+"/"
        aggr_file_list = os.listdir(current_year)
        
        for file in aggr_file_list:
            current_file = current_year+file
            aggr_data = open(current_file,"r")

            T = json.load(aggr_data)
            
            try:
                for i in T['data']['usersByDevice']:
                        brand = i['brand']
                        count = i['count']
                        percentage= i['percentage']
                        data2["brand"].append(brand)
                        data2["transaction_count"].append(count)
                        data2['percentage'].append(percentage)
                        data2['state'].append(state)
                        data2['year'].append(year)
                        data2['quarter'].append(int(file.strip(".json")))
            except:
                 pass
            
aggr_user_df = pd.DataFrame(data2)
aggr_user_df['state'] = aggr_user_df['state'].str.replace("-"," ")
aggr_user_df['state'] = aggr_user_df['state'].str.title()


#aggregated insurance
path_3 = "C:/Users/santh/Desktop/Capstone Projects/New folder/PROJECTS/PhonePe/pulse/data/aggregated/insurance/country/india/state/"
aggr_ins_list = os.listdir(path_3)
data3 = {'state':[],'year':[],'quarter':[],'insurance_type':[],'insurance_count':[],'insurance_amount':[]}

for state in aggr_ins_list:
    current_state = path_3+state+"/"
    aggr_year_list = os.listdir(current_state)
    
    for year in aggr_year_list:
        current_year = current_state+year+"/"
        aggr_file_list = os.listdir(current_year)
        
        for file in aggr_file_list:
            current_file = current_year+file
            aggr_data = open(current_file,"r")

            U = json.load(aggr_data)
            
            for i in U['data']['transactionData']:
                    name = i['name']
                    count = i['paymentInstruments'][0]['count']
                    amount= i['paymentInstruments'][0]['amount']
                    data3["insurance_type"].append(name)
                    data3["insurance_count"].append(count)
                    data3['insurance_amount'].append(amount)
                    data3['state'].append(state)
                    data3['year'].append(year)
                    data3['quarter'].append(int(file.strip(".json")))

aggr_ins_df = pd.DataFrame(data3)
aggr_ins_df['state'] = aggr_ins_df['state'].str.replace("-"," ")
aggr_ins_df['state'] = aggr_ins_df['state'].str.title()




# map_transaction 
path_4 ="C:/Users/santh/Desktop/Capstone Projects/New folder/PROJECTS/PhonePe/pulse/data/map/transaction/hover/country/india/state/"
map_trans_list = os.listdir(path_4)
data4 = {'state':[],'year':[],'quarter':[],'district':[],'transaction_count':[],'transaction_amount':[]}

for state in map_trans_list:
    current_state = path_4+state+"/"
    map_year_list = os.listdir(current_state)
    
    for year in map_year_list:
        current_year = current_state+year+"/"
        map_file_list = os.listdir(current_year)
        
        for file in map_file_list:
            current_file = current_year+file
            map_data = open(current_file,"r")

            V = json.load(map_data)
    
            for i in V['data']['hoverDataList']:
                name = i["name"]
                count = i['metric'][0]['count']
                amount = i['metric'][0]['amount']
                data4["district"].append(name)
                data4["transaction_count"].append(count)
                data4['transaction_amount'].append(amount)
                data4['state'].append(state)
                data4['year'].append(year)
                data4['quarter'].append(int(file.strip(".json")))

map_trans_df = pd.DataFrame(data4)
map_trans_df['state'] = map_trans_df['state'].str.replace("-"," ")
map_trans_df['state'] = map_trans_df['state'].str.title()




#map_user
path_5 = "C:/Users/santh/Desktop/Capstone Projects/New folder/PROJECTS/PhonePe/pulse/data/map/user/hover/country/india/state/"
map_user_list = os.listdir(path_5)
data5 = {'state':[],'year':[],'quarter':[],'district':[],'registeredusers':[],'appopens':[]}

for state in map_user_list:
    current_state = path_5+state+"/"
    map_year_list = os.listdir(current_state)
    
    for year in map_year_list:
        current_year = current_state+year+"/"
        map_file_list = os.listdir(current_year)
        
        for file in map_file_list:
            current_file = current_year+file
            map_data = open(current_file,"r")

            W = json.load(map_data)
            
        
            for i in W['data']['hoverData'].items():
                    district = i[0]
                    registeredusers= i[1]['registeredUsers']
                    appopens= i[1]['appOpens']
                    data5["district"].append(district)
                    data5['registeredusers'].append(registeredusers)
                    data5['appopens'].append(appopens)
                    data5['state'].append(state)
                    data5['year'].append(year)
                    data5['quarter'].append(int(file.strip(".json")))

map_user_df = pd.DataFrame(data5)
map_user_df['state'] = map_user_df['state'].str.replace("-"," ")
map_user_df['state'] = map_user_df['state'].str.title()



#map insurance
path_6 = "C:/Users/santh/Desktop/Capstone Projects/New folder/PROJECTS/PhonePe/pulse/data/map/insurance/hover/country/india/state/"
map_ins_list = os.listdir(path_6)
data6 = {'state':[],'year':[],'quarter':[],'district':[],'insurance_count':[],'insurance_amount':[]}

for state in map_ins_list:
    current_state = path_6+state+"/"
    map_year_list = os.listdir(current_state)
    
    for year in map_year_list:
        current_year = current_state+year+"/"
        map_file_list = os.listdir(current_year)
        
        for file in map_file_list:
            current_file = current_year+file
            map_data = open(current_file,"r")

            X = json.load(map_data)
            
            for i in X['data']['hoverDataList']:
                    name = i['name']
                    count = i['metric'][0]['count']
                    amount= i['metric'][0]['amount']
                    data6["district"].append(name)
                    data6["insurance_count"].append(count)
                    data6['insurance_amount'].append(amount)
                    data6['state'].append(state)
                    data6['year'].append(year)
                    data6['quarter'].append(int(file.strip(".json")))

map_ins_df= pd.DataFrame(data6)
map_ins_df['state'] = map_ins_df['state'].str.replace("-"," ")
map_ins_df['state'] = map_ins_df['state'].str.title()



# top_transaction 
path_7 ="C:/Users/santh/Desktop/Capstone Projects/New folder/PROJECTS/PhonePe/pulse/data/top/transaction/country/india/state/"
top_trans_list = os.listdir(path_7)
data7 = {'state':[],'year':[],'quarter':[],'pincodes':[],'transaction_count':[],'transaction_amount':[]}

for state in top_trans_list:
    current_state = path_7+state+"/"
    top_year_list = os.listdir(current_state)
    
    for year in top_year_list:
        current_year = current_state+year+"/"
        top_file_list = os.listdir(current_year)
        
        for file in top_file_list:
            current_file = current_year+file
            top_data = open(current_file,"r")

            Y = json.load(top_data)
             
            for i in Y['data']['pincodes']:
                name = i['entityName']
                count = i['metric']['count']
                amount = i['metric']['amount']
                data7["pincodes"].append(name)
                data7["transaction_count"].append(count)
                data7['transaction_amount'].append(amount)
                data7['state'].append(state)
                data7['year'].append(year)
                data7['quarter'].append(int(file.strip(".json")))

top_trans_df = pd.DataFrame(data7)
top_trans_df['state'] = top_trans_df['state'].str.replace("-"," ")
top_trans_df['state'] = top_trans_df['state'].str.title()
        



#top insurance
path_8 = "C:/Users/santh/Desktop/Capstone Projects/New folder/PROJECTS/PhonePe/pulse/data/top/insurance/country/india/state/"
top_ins_list = os.listdir(path_8)
data8 = {'state':[],'year':[],'quarter':[],'pincode':[],'insurance_count':[],'insurance_amount':[]}

for state in top_ins_list:
    current_state = path_8+state+"/"
    top_year_list = os.listdir(current_state)
    
    for year in top_year_list:
        current_year = current_state+year+"/"
        top_file_list = os.listdir(current_year)
        
        for file in top_file_list:
            current_file = current_year+file
            top_data = open(current_file,"r")

            Z = json.load(top_data)
            
            for i in Z['data']['pincodes']:
                    name = i['entityName']
                    count = i['metric']['count']
                    amount= i['metric']['amount']
                    data8["pincode"].append(name)
                    data8["insurance_count"].append(count)
                    data8['insurance_amount'].append(amount)
                    data8['state'].append(state)
                    data8['year'].append(year)
                    data8['quarter'].append(int(file.strip(".json")))

top_ins_df = pd.DataFrame(data8)
top_ins_df['state'] = top_ins_df['state'].str.replace("-"," ")
top_ins_df['state'] = top_ins_df['state'].str.title()


#top_user
path_9 = "C:/Users/santh/Desktop/Capstone Projects/New folder/PROJECTS/PhonePe/pulse/data/top/user/country/india/state/"
top_user_list = os.listdir(path_5)
data9 = {'state':[],'year':[],'quarter':[],'pincode':[],'registeredusers':[]}

for state in top_user_list:
    current_state = path_9+state+"/"
    top_year_list = os.listdir(current_state)
    
    for year in top_year_list:
        current_year = current_state+year+"/"
        top_file_list = os.listdir(current_year)
        
        for file in top_file_list:
            current_file = current_year+file
            top_data = open(current_file,"r")

            A = json.load(top_data)
            
        
            for i in A['data']['pincodes']:
                    name = i['name']
                    registeredusers= i['registeredUsers']
                    data9["pincode"].append(name)
                    data9['registeredusers'].append(registeredusers)
                    data9['state'].append(state)
                    data9['year'].append(year)
                    data9['quarter'].append(int(file.strip(".json")))


top_user_df = pd.DataFrame(data9)
top_user_df['state'] = top_user_df['state'].str.replace("-"," ")
top_user_df['state'] = top_user_df['state'].str.title()


# convert the df into csv files ------ df.to_csv('filename.csv',index=False)

aggr_trans_df.to_csv('aggr_trans_df',index=False)
aggr_user_df.to_csv('aggr_user_df',index=False)
aggr_ins_df.to_csv('aggr_ins.df',index=False)
map_trans_df.to_csv('map_trans_df',index=False)
map_user_df.to_csv('map_user_df',index=False)
map_ins_df.to_csv('map_ins_df',index=False)
top_trans_df.to_csv('top_trans_df',index=False)
top_user_df.to_csv('top_user_df',index=False)
top_ins_df.to_csv('top_ins_df',index=False)


#sql connection
my_conn = pymysql.connect(host='localhost',
        user='root', 
        password = 'santhi@98#31$$05',
        database='phonpe',
        )
my_cursor = my_conn.cursor()

#state column 
state = aggr_trans_df['state'].unique()
df = pd.DataFrame(state)
df.to_csv('Statenames.csv',index =False)

#streamlit 
st.set_page_config(page_title= "PhonePe Pulse Data Visualisation",
                   page_icon="🧊",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items = None)

st.title("PHONEPE PULSE DATA VISUALIZATION")

with st.sidebar:
     st.title("PhonePe Pulse")
     select = option_menu("Menu",["Home","Data Exploration","Top Charts","About"])

#menu 1 -  home 

if select == "Home":
     
     col1,col2 = st.columns([1,1],gap="large")
     
     with col1:
          
          st.title("Explore Pulse 2.0")
          st.header("Walkthrough Video")
          url = "https://www.youtube.com/watch?v=Yy03rjSUIB8&t=1s"
          st.write("Explore Now [link](%s)" % url)
     
     with col2:
            
            st.image('phonepeimage.png')

#menu2 - data exploration
elif select =="Data Exploration":
     
     type = st.selectbox("select the type",("INSURANCE","PAYMENTS"))
     if type == "INSURANCE":
         
         questions = st.selectbox("select question",("All India Policies Purchased","Total Premium Value"))
         if questions == "All India Policies Purchased":
                query_1 = "SELECT SUM(insurance_count) FROM phonpe.map_ins_df;"
                my_cursor.execute(query_1)
                result_1 = my_cursor.fetchone()[0]  
                st.header(result_1)
         elif questions == "Total Premium Value":
                query_2 = "SELECT SUM(insurance_amount) FROM phonpe.map_ins_df;"
                my_cursor.execute(query_2)
                result_2 = my_cursor.fetchone()[0]
                st.header(result_2)
                
         col1, col2, col3 = st.columns(3)
         with col1:
             if st.button("Top 10 States"):
                query = """SELECT state, SUM(insurance_count) AS Total_Insurance_Count FROM phonpe.map_ins_df GROUP BY state ORDER BY SUM(insurance_count) DESC LIMIT 10;"""
                my_cursor.execute(query)
                df = pd.DataFrame(my_cursor.fetchall(),columns= ['State','Total_Insurance_Count'])
                st.write(df)
                 
         with col2:
            if st.button("Top 10 Districts"):
                query = """SELECT district, SUM(insurance_count) AS Total_Insurance_Count FROM phonpe.map_ins_df GROUP BY district ORDER BY SUM(insurance_count) DESC LIMIT 10;"""
                my_cursor.execute(query)
                df = pd.DataFrame(my_cursor.fetchall(),columns= ['District','Total_Insurance_Count'])
                st.write(df)
           
         with col3:  
             if st.button("Top 10 Postal Codes"):
                  query = """SELECT pincode, SUM(insurance_count) AS Total_Insurance_Count FROM phonpe.top_ins_df GROUP BY pincode ORDER BY SUM(insurance_count) DESC LIMIT 10;"""
                  my_cursor.execute(query)
                  df = pd.DataFrame(my_cursor.fetchall(),columns= ['District','Total_Insurance_Count'])
                  st.write(df)
    
     elif type == "PAYMENTS":
            category = st.radio("select the category",["Transactions","User"])
            
            if category == "Transactions":

                questions = st.selectbox("select question",("All PhonePe Transactions","Average Transactions")) 
                
                # Query to get the sum of all PhonePe transactions
                if questions == "All PhonePe Transactions": 
                        query_1 = "SELECT SUM(transaction_count) FROM phonpe.map_trans_df;"
                        my_cursor.execute(query_1)
                        result_1 = my_cursor.fetchone()[0]
                        st.header(result_1)
                    # Query to get the average of all PhonePe transactions
                elif questions == "Average Transactions":
                        query_2 = "SELECT AVG(transaction_count) FROM phonpe.top_trans_df;"
                        my_cursor.execute(query_2)
                        result_2 = my_cursor.fetchone()[0]
                        st.header(result_2)
                    
                Year = st.slider("Year", min_value=2018, max_value=2024)
                Quarter = st.slider("Quarter", min_value=1, max_value=4)
            
                # Query to get the transactions data based on the selected year and quarter
                query_3 = f"""SELECT state, SUM(transaction_count) AS Total_Transactions, SUM(transaction_amount) AS Total_amount FROM aggr_trans_df WHERE year = {Year} and quarter = {Quarter} GROUP BY state ORDER BY state"""
                my_cursor.execute(query_3)
                df1 = pd.DataFrame(my_cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
                # Close the cursor
                my_cursor.close()
                # Load the state names from CSV
                df2 = pd.read_csv('Statenames.csv')
                # Merge state names to the dataframe
                df1.State = df2
                st.write(df1)
               
                # Plotting the choropleth map
                fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                      featureidkey='properties.ST_NM',
                      locations='State',
                      color='Total_amount',
                      color_continuous_scale='reds')   
                
                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
            
            elif category == "User":
                # Query to get the sum of all PhonePe transactions
                query_1 = "SELECT SUM(registeredusers) FROM phonpe.map_user_df;"
                my_cursor.execute(query_1)
                result_1 = my_cursor.fetchone()[0]
                
                # Query to get the average of all PhonePe transactions
                query_2 = "SELECT SUM(appopens) FROM phonpe.map_user_df;"
                my_cursor.execute(query_2)
                result_2 = my_cursor.fetchone()[0]
               
                # Display results with colored text
                st.write(":blue[Registered PhonePe users till 2024:]",result_1)
                st.write(":blue[PhonePe app opens till 2024]", result_2) 
                
                Year = st.slider("Year", min_value=2018, max_value=2024)
                Quarter = st.slider("Quarter", min_value=1, max_value=4)
            
                # Query to get the transactions data based on the selected year and quarter
                query_3 = f"""SELECT state, SUM(registeredusers) AS Total_Users, SUM(appopens) AS Total_AppOpens FROM map_user_df WHERE year = {Year} and quarter = {Quarter} GROUP BY state ORDER BY state"""
                my_cursor.execute(query_3)
                df1 = pd.DataFrame(my_cursor.fetchall(),columns= ['State', 'Total_Users', 'Total_AppOpens'])
                # Close the cursor
                my_cursor.close()
                # Load the state names from CSV
                df2 = pd.read_csv('Statenames.csv')
                df1.Total_AppOpens = df1.Total_AppOpens.astype(float)
                # Merge state names to the dataframe
                df1.State = df2
                st.write(df1)
               
                # Plotting the choropleth map
                fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                      featureidkey='properties.ST_NM',
                      locations='State',
                      color='Total_AppOpens',
                      color_continuous_scale='reds')   
                
                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)

#menu 3 - top charts 
elif select == "Top Charts":
      
       Year = st.slider("Year", min_value=2018, max_value=2024)
       Quarter = st.slider("Quarter", min_value=1, max_value=4)

       col1, col2, col3 = st.columns(3)
       with col1:
            if st.button("Top 10 States"):
                query = f"""SELECT state, SUM(transaction_amount) AS Total_Transaction_Amount FROM phonpe.aggr_trans_df WHERE year = {Year} and quarter = {Quarter} GROUP BY state ORDER BY SUM(transaction_amount) DESC LIMIT 10;"""
                my_cursor.execute(query)
                df = pd.DataFrame(my_cursor.fetchall(),columns= ['State','Total_Transaction_Amount'])
                st.write(df)
                
                fig = px.pie(df, values='Total_Transaction_Amount',
                             names='State',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                            labels={'Transactions_Count':'Transactions_Count'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)
                

       with col2:
           if st.button("Top 10 Districts"):
                query = f"""SELECT district, SUM(transaction_count) AS Total_Count, SUM(transaction_amount) AS Transaction_Amount FROM phonpe.map_trans_df WHERE year = {Year} and quarter = {Quarter} GROUP BY district ORDER BY Transaction_Amount DESC LIMIT 10;"""
                my_cursor.execute(query)
                df = pd.DataFrame(my_cursor.fetchall(),columns= ['District','Transaction_Count','Transaction_Amount'])
                st.write(df)
                

                fig = px.pie(df, values='Transaction_Amount',
                             names='District',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             labels={'Transactions_Count':'Transactions_Count'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)
      
       with col3:  
            if st.button("Top 10 Postal Codes"):
                query = f"""SELECT pincode, SUM(insurance_count) AS Total_Count, SUM(insurance_amount) AS Total_Amount FROM phonpe.top_ins_df WHERE year = {Year} and quarter = {Quarter} GROUP BY pincode ORDER BY Total_Amount DESC LIMIT 10;"""
                my_cursor.execute(query)
                df = pd.DataFrame(my_cursor.fetchall(),columns= ['Pincode','Total_Count','Total_Amount'])
                st.write(df)
                
                fig = px.pie(df, values='Total_Amount',
                             names='Pincode',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             labels={'Transactions_Count':'Transactions_Count'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)


#menu 4 - About 

elif select == "About":
     st.title("About Pulse")
     st.text("""The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages,
there is a payments revolution being driven by the penetration of mobile phones and data."
             
When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. 
Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top 
cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes? This year as we became India's 
largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments 
in India.
                
This year, as we crossed 2000 Cr. transactions and 30 Crore registered users, we thought as India's largest digital payments 
platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages and grows its money. 
So it was time to demystify and share the what, why and how of digital payments in India.

             
PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis 
based on our data put together by the PhonePe team.""")