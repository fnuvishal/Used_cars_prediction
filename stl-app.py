import streamlit as st
import pickle
import numpy as np

st.title('Predicting Car Price')

st.write('Year Of Registration')
yearOfRegistration = st.text_input(label = 'Enter year between 1990 - 2014 ',  value = 0,key = '2')

st.write('Choose Vehicle GearBox ')
gearbox=st.radio('select',('gearbox_automatik', 'gearbox_manuell'))
if gearbox == 'gearbox_automatik':
    gearbox_automatik = 1
    gearbox_manuell  = 0

if gearbox == 'gearbox_manuell':
    gearbox_manuell = 1
    gearbox_automatik = 0

st.write('What is Vehicle type')
vehicleType = st.radio( 'Select ',('vehicleType_bus',
       'vehicleType_cabrio', 'vehicleType_coupe', 'vehicleType_kleinwagen',
       'vehicleType_kombi', 'vehicleType_limousine', 'vehicleType_others',
       'vehicleType_suv'))
vehicleType_bus   = 0
vehicleType_cabrio = 0
vehicleType_coupe = 0
vehicleType_kleinwagen = 0
vehicleType_kombi = 0
vehicleType_limousine = 0
vehicleType_others = 0
vehicleType_suv  = 0
if vehicleType == 'vehicleType_bus':
    vehicleType_bus   = 1
if vehicleType == 'vehicleType_cabrio':
    vehicleType_cabrio   = 1
if vehicleType == 'vehicleType_coupe':
    vehicleType_coupe   = 1
if vehicleType == 'vehicleType_kleinwagen':
    vehicleType_kleinwagen   = 1
if vehicleType == 'vehicleType_kombi':
    vehicleType_kombi   = 1
if vehicleType == 'vehicleType_limousine':
    vehicleType_limousine   = 1
if vehicleType == 'vehicleType_others':
    vehicleType_others   = 1

#st.write('What is the car Model')
#model = st.text_input(label = 'Enter ',  value = 0,key = '3')
#list=['model_3er', 'model_5er', 'model_a3', 'model_a4','model_a6', 'model_a_klasse', 'model_andere', 'model_astra','model_c_klasse', 'model_corsa', 'model_e_klasse', 'model_fiesta','model_focus', 'model_fortwo', 'model_golf', 'model_others','model_passat', 'model_polo', 'model_transporter', 'model_twingo']
st.write('What is the car Model')
model = st.radio( 'Select ',('model_1er', 'model_2_reihe', 'model_3er',
       'model_5er', 'model_a3', 'model_a4', 'model_a6', 'model_a_klasse',
       'model_andere', 'model_astra', 'model_c_klasse', 'model_corsa',
       'model_e_klasse', 'model_fiesta', 'model_focus', 'model_fortwo',
       'model_golf', 'model_others', 'model_passat', 'model_polo',
       'model_transporter', 'model_twingo',))
model_3er   = 0
model_5er  = 0
model_a3  = 0
model_a4  = 0
model_a6  = 0
model_a_klasse = 0
model_andere  = 0
model_astra  = 0
model_c_klasse = 0
model_corsa  = 0
model_e_klasse = 0
model_fiesta = 0
model_focus  = 0
model_fortwo = 0
model_golf  = 0
model_others = 0
model_passat = 0
model_polo  = 0
model_transporter = 0
model_twingo = 0
model_1er = 0
model_2_reihe = 0
if model == 'model_1er':
    model_1er = 1
if model == 'model_3er':
    model_3er = 1
if model == 'model_5er':
    model_5er = 1
if model == 'model_a3':
    model_a3 = 1
if model == 'model_a4':
    model_a4 = 1
if model == 'model_a6':
    model_a6 = 1
if model == 'model_a_klasse':
    model_a_klasse = 1
if model == 'model_andere':
    model_andere = 1
if model == 'model_astra':
    model_astra = 1
if model == 'model_c_klasse':
    model_c_klasse = 1
if model == 'model_fiesta':
    model_fiesta = 1
if model == 'model_focus':
    model_focus = 1
if model == 'model_fortwo':
    model_fortwo = 1
if model == 'model_golf':
    model_golf = 1
if model == 'model_others':
    model_others = 1
if model == 'model_passat':
    model_passat = 1
if model == 'model_polo':
    model_polo = 1
if model == 'model_transporter':
    model_transporter = 1
if model == 'model_twingo':
    model_twingo = 1
if model == 'model_corsa':
    model_corsa = 1
if model == 'model_e_klasse':
    model_e_klasse = 1
if model == 'model_2_reihe':
    model_2_reihe = 1


#for i in list:
#    if i == model:
#        i = 1
#    else:
#        i = 0



st.write('Miles on Car')
kilometer = st.text_input(label = 'Enter 10,000-150,000',  value = 0,key = '4')


click = st.button('Predict')
if click:
    with open('Random_Forest_cars.pkl', mode = 'rb') as pickle_in:
        pipe = pickle.load(pickle_in)
        input_val = [yearOfRegistration,vehicleType_bus,
        vehicleType_cabrio, vehicleType_coupe, vehicleType_kleinwagen,
        vehicleType_kombi, vehicleType_limousine, vehicleType_others,
        vehicleType_suv,

        model_1er, model_2_reihe, model_3er,
       model_5er, model_a3, model_a4, model_a6, model_a_klasse,
       model_andere, model_astra, model_c_klasse, model_corsa,
       model_e_klasse, model_fiesta, model_focus, model_fortwo,
       model_golf, model_others, model_passat, model_polo,
       model_transporter, model_twingo,

        kilometer,gearbox_automatik, gearbox_manuell]
        input_val = np.reshape(input_val,(1,-1))
        input_val = np.asarray(input_val,dtype='float64')
        predict = pipe.predict(input_val)

    st.write(f'Cost of the Car is $: {predict[0]}')
    #dict = {0:'low cost',
            #1:'medium cost',
           # 2:'high cost',
          #  3:'very high cost'}
   # st.write(f'The phone you picked will be {dict[predict[0]]}.')
