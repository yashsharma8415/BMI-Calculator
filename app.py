import streamlit as st

# title to our app
st.title('BMI Calculator')

# weight input
weight = st.number_input("Enter your weight (in kgs)",
                         min_value=0.1, max_value=1000.0, step=0.1, format="%.1f")

# radio button to choose height format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet and inches'))

# compare status value
if(status == 'cms'):
    # height input in centimeters
    height = st.number_input('Centimeters', min_value=0.01, max_value=1000.0)

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")

elif(status == 'meters'):
    # height input in meters
    height = st.number_input('Meters', min_value=0.01, max_value=10.0)

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")

else:
    # height input in feet
    height_feet = st.number_input('Feet', min_value=0, max_value=100, step=1)
    height_inch = st.number_input('Inches', min_value=0, max_value=11, step=1)

    # 1 meter = 3.28 feet and 1 inch = 2.54 cm
    height_cm = (height_feet * 100)/3.28 + height_inch * 2.54

    try:
        bmi = weight / ((height_cm/100)**2)
    except:
        st.text("Enter some value of height")

# check if the button is pressed or not
if(st.button('Calculate BMI')):

    # print the BMI Index
    st.text("Your BMI Index is {}.".format(bmi))

    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("Critical! Extremely Underweight.")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("Oops! Underweight.")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Hurrah! Healthy.")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Oops! Overweight.")
    elif(bmi >= 30):
        st.error("Critical! Extremely Overweight.")

footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='text-align: center;' href="https://github.com/yashsharma8415" target="_blank">Yash Sharma</a></p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
